---
name: quant-resource-manager
description: Manage external learning resources in resources.json and project statistics. Use when adding new cards or maintaining existing links.
---

# Quant Resource Manager

This skill manages the external learning resources and maintenance scripts for the Quantitative Finance Flash Cards project.

## Maintenance Tasks

### 1. Resources (`resources.json`)
Every card must have a corresponding entry in `resources.json` with at least 1-2 external links (websites and videos).
- **Format**:
```json
"category/slug": {
  "websites": [{ "title": "...", "url": "..." }],
  "videos": [{ "title": "...", "url": "..." }]
}
```
- **Verification**: Use `uv run python scripts/validate_urls.py --force` to check for broken links.

### 2. Project Statistics
After significant changes, update the global card and edge counts in `README.md`.
- **Action**: Run `uv run python scripts/update_readme_stats.py`.

### 3. Dependency Management
- **Action**: Use `uv sync` to ensure the environment matches the `pyproject.toml`.

## Resource Quality Guidelines
- **Websites**: Prefer **Paul's Online Math Notes**, **Wolfram MathWorld**, **Investopedia**, or academic lecture notes.
- **Videos**: Prefer **3Blue1Brown**, **Khan Academy**, **MIT OpenCourseWare**, or **Wilmott** channel content.
- **Titles**: Titles should be concise and mention the source (e.g., "Khan Academy — Chain Rule").

## Workflow
1. **Search**: Find resources for a new concept.
2. **Validate**: Ensure URLs are live and content is high-quality.
3. **Insert**: Append to `resources.json`.
4. **Update Stats**: Run the `update_readme_stats.py` script.
