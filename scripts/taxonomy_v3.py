#!/usr/bin/env python3
"""Explicit task boundaries and evidence-preserving migration from taxonomy v2.

Reviewed decisions in decisions.jsonl are the classification inputs. Inherited labels are explicitly distinguished from new
contribution reviews. This script does not claim a fresh full-text audit.
"""
import csv
from functools import lru_cache
import gzip
import io
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / 'checks/taxonomy_v3'
VERSION = '3.0'
# id, English, Chinese, boundary, evaluation guidance (Chinese / English)
TASKS = [
 ('alpha_mining','Factor Mining','因子挖掘','Discover and select reusable alpha signals or formulas; distinguish predictive alpha from economic pricing factors. / 发现与筛选可复用的收益信号或公式，区别于经济定价因子。','检查样本外 IC、因子冗余、搜索预算、换手与成本。','Check out-of-sample IC, signal redundancy, search budget, turnover and costs.'),
 ('time_series','Time Series','时间序列','Forecast, represent, generate or reconstruct financial sequences; a specific asset-value target belongs to valuation prediction. / 金融序列预测、表征、生成与重建；明确的资产价值目标归估值预测。','使用严格时间切分，分别报告预测误差、概率校准及合成质量。','Use chronological splits and separate forecast error, probabilistic calibration and synthesis quality.'),
 ('pricing','Pricing','定价','Asset pricing mechanisms, risk premia, derivative valuation and calibration; distinguish pricing relationships from predictive price targets. / 资产定价机制、风险溢价、衍生品估价与校准，区别于价格预测。','核验无套利约束、定价误差、对冲误差及交易假设。','Test no-arbitrage constraints, pricing error, hedging error and trading assumptions.'),
 ('valuation_prediction','Valuation Prediction','估值预测','Predict asset prices, returns, volatility, enterprise value, earnings or revenue. / 预测资产价格、收益、波动率、企业价值、盈利与营收。','同时核对时间泄漏、预测目标、跨市场泛化和经济效用。','Check temporal leakage, target definitions, cross-market transfer and economic utility.'),
 ('portfolio','Portfolio','投资组合','Select, allocate, rebalance and evaluate portfolios across assets. / 跨资产组合选择、配置、再平衡与评价。','统一成本与调仓频率，报告收益、回撤、风险及换手。','Match costs and rebalancing frequency; report return, drawdown, risk and turnover.'),
 ('insurance','Insurance and Actuarial Science','保险精算','Insurance underwriting, claims, reserves, actuarial prediction and insurance business decisions. / 承保、理赔、准备金、精算预测及保险业务决策。','关注索赔分布、校准、选择偏差、长期风险及业务约束。','Inspect claim distributions, calibration, selection bias, long-term risk and business constraints.'),
 ('financial_sentiment','Financial Sentiment','金融情感','Financial sentiment, stance, tone and emotion as the prediction target; downstream return prediction stays valuation prediction. / 以金融情感、立场、语气与情绪为目标；下游收益预测仍归估值预测。','检查标注口径、时效性、领域与语言迁移，区分情感准确率和收益效果。','Check annotation policy, temporal drift and domain/language transfer; separate sentiment accuracy from returns.'),
 ('financial_qa','Financial Question Answering','金融问答','Answer financial questions and perform numerical, table or conversational reasoning. / 金融问题回答及数值、表格、对话推理。','分别检查答案、推理程序、证据引用及跨表跨文档一致性。','Evaluate answers, reasoning programs, evidence attribution and cross-table/document consistency separately.'),
 ('financial_understanding','Financial Understanding','金融理解','Extract, interpret, summarize and verify financial language, reports, charts, invoices and accounting records. / 金融文本、财报、图表、票据及会计记录的抽取、解释、摘要与核验。','关注结构提取、数值忠实性、证据覆盖及版面变化。','Measure structural extraction, numerical faithfulness, evidence coverage and layout shift.'),
 ('financial_decision','Financial Decision Making','金融决策','Trading, execution, market simulation and financial agent decisions; portfolio allocation has its own task. / 交易、执行、市场仿真与金融 Agent 决策；组合配置单列。','区分离线预测与闭环决策，显式计入交易成本、延迟和市场冲击。','Separate offline prediction from closed-loop decisions; include costs, latency and market impact.'),
 ('sustainable_finance','Sustainable Finance','可持续金融','ESG disclosure, greenwashing, climate-related financial analysis and sustainable investment. / ESG 披露、漂绿、气候金融分析与可持续投资。','核对披露证据、跨期可比性、行业偏差和实际投资约束。','Check disclosure evidence, temporal comparability, sector bias and investment constraints.'),
 ('financial_services','Financial Services','金融服务','Banking, payments, customer service, marketing and personal/business financial services. / 银行、支付、客户服务、营销及个人与企业金融服务。','区分公开业务数据与真实部署，检查客户、时间和机构间迁移。','Distinguish public business data from deployment; check transfer across customers, time and institutions.'),
 ('blockchain','Blockchain','区块链','Blockchain transactions, digital assets, smart contracts and DeFi mechanisms. / 链上交易、数字资产、智能合约与 DeFi 机制。','关注链与协议差异、时间切分、攻击假设及链上成本。','Check chain/protocol differences, chronological splits, attack assumptions and on-chain costs.'),
 ('financial_safety','Financial Safety','金融安全','Fraud, scams, money laundering, privacy, attacks and regulatory compliance. / 欺诈、诈骗、反洗钱、隐私、攻击与监管合规。','重视类别不平衡、误报成本、攻击适应性、隐私与合规证据。','Account for imbalance, false-positive costs, adaptive attacks, privacy and compliance evidence.'),
 ('financial_ir','Financial Retrieval','金融检索','Retrieve, embed, rerank and ground financial evidence, including financial RAG. / 金融证据检索、嵌入、重排及 RAG。','分开报告检索召回、重排质量、引用忠实性和最终回答质量。','Report retrieval recall, reranking, citation faithfulness and answer quality separately.'),
 ('financial_evaluation','Financial Evaluation','金融评测','The main contribution is a financial dataset, benchmark, evaluation environment or capability audit. / 主要贡献为金融数据集、基准、评测环境或能力诊断。','检查覆盖、污染、标注质量、评测预算与指标外推边界。','Inspect coverage, contamination, annotation quality, evaluation budget and limits of metric extrapolation.'),
 ('financial_models','Financial Models','金融模型','Financial domain pretraining, adaptation and reusable foundation models; generic time-series pretraining stays time series. / 金融领域预训练、适配与可复用基础模型；通用序列预训练仍归时间序列。','检查预训练数据、时间污染、跨任务迁移、模型规模和计算预算。','Audit pretraining data, temporal contamination, cross-task transfer, model size and compute budget.'),
 ('financial_risk','Financial Risk','金融风险','Credit scoring, default, market, liquidity and systemic risk; fraud and attacks belong to financial safety. / 信用评分、违约、市场风险、流动性及系统性风险；欺诈与攻击归金融安全。','关注违约与尾部事件、概率校准、成本敏感性、压力测试及跨期稳定性。','Evaluate default and tail events, calibration, cost sensitivity, stress tests and temporal stability.'),
]
MAP = dict(alpha_mining='alpha_mining',time_series='time_series',asset_pricing='pricing',derivatives='pricing',portfolio='portfolio',trading='financial_decision',market_prediction='valuation_prediction',credit_risk='financial_risk',insurance='insurance',fraud_aml='financial_safety',financial_nlp='financial_understanding',financial_qa='financial_qa',financial_ir='financial_ir',document_ai='financial_understanding',financial_agents='financial_decision',macro_economics='time_series',corporate_finance='financial_understanding',esg='sustainable_finance',banking='financial_services',blockchain='blockchain',financial_safety='financial_safety',financial_models='financial_models',other_finance='financial_services')

@lru_cache(maxsize=1)
def baseline():
    return json.loads(gzip.decompress((AUDIT/'baseline.json.gz').read_bytes()))

def records(track):
    return [json.loads(l) for l in baseline()[track+'/finance_catalog.jsonl'].splitlines()]

@lru_cache(maxsize=1)
def schema():
    old=json.loads(baseline()['main/checks/finance_taxonomy/schema.json'])
    topics=[dict(id=t[0],label=t[1]+' / '+t[2],sheet=t[1][:31],description=t[3],evaluation_zh=t[4],evaluation_en=t[5]) for t in TASKS]
    from finance_subtopics_v3 import definitions
    subs=definitions()
    return dict(version=VERSION,topics=topics,subtopics=subs,methods=[{k:v for k,v in m.items() if k!='pattern'} for m in old['methods']],notes=['One primary task per paper; related tasks may overlap.','Main/Findings and Core/Application are independent storage partitions.','Contribution review takes precedence over inherited task labels.','Inherited evidence and method labels do not imply a fresh full-text audit; see per-paper review status.'])

if __name__=='__main__':
    print(json.dumps(schema(),ensure_ascii=False,indent=2))
