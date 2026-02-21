"""Simple template rendering utilities."""

from pathlib import Path
from typing import Dict


def render_template(content: str, context: Dict[str, str]) -> str:
    """Render placeholders in the form `{{KEY}}` using a context map."""
    rendered = content
    for key, value in context.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", str(value))
    return rendered


def render_template_file(template_path: Path, output_path: Path, context: Dict[str, str]) -> Path:
    """Render a template file and write the output to disk."""
    template_content = template_path.read_text(encoding="utf-8")
    rendered = render_template(template_content, context)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered, encoding="utf-8")

    return output_path
