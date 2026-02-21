# Azure Data Engineering Utilities

This repository now includes lightweight **project utilities** and reusable **templates (`temps/`)** to speed up common setup tasks.

## What's included

- `project_utils/`: reusable Python helper functions for:
  - directory bootstrapping
  - normalized resource naming
  - simple token-based template rendering
- `temps/`: starter template files for common data engineering project configuration.
- `tests/`: unit tests for core utility behavior.

## Quick start

```bash
python -m unittest discover -s tests -v
```

## Example usage

```python
from pathlib import Path
from project_utils import ensure_project_dirs, make_resource_name, render_template_file

base = Path("demo_project")
ensure_project_dirs(base, ["src", "configs", "pipelines"])

name = make_resource_name("sales", "daily ingest", max_length=24)
print(name)  # sales-daily-ingest

result = render_template_file(
    template_path=Path("temps/pipeline_config.template.json"),
    output_path=base / "configs" / "pipeline_config.json",
    context={"PROJECT": "sales", "ENV": "dev", "OWNER": "data-team"},
)
print(result)
```
