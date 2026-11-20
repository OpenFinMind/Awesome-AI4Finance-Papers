"""Read curated task prose and adapt its relative links for an index page."""
import os
import re
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit, urlunsplit

START = '<!-- task-summary:start -->'
END = '<!-- task-summary:end -->'


def render_summary(root, task, page):
    root, page = Path(root), Path(page)
    source = root / 'summaries' / (task + '.md')
    text = source.read_text().strip()

    def adapt(match):
        target = urlsplit(match.group(1).strip('<>'))
        if target.scheme or target.netloc or not target.path:
            return match.group(0)
        resolved = (source.parent / unquote(target.path)).resolve()
        assert resolved.is_relative_to(root.resolve()) and resolved.exists(), (source, target.path)
        relative = quote(os.path.relpath(resolved, page.parent), safe='/._-')
        return '](' + urlunsplit(('', '', relative, target.query, target.fragment)) + ')'

    return START + '\n\n' + re.sub(r'\]\(([^)]+)\)', adapt, text) + '\n\n' + END
