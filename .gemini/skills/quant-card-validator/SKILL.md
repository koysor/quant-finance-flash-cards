---
name: quant-card-validator
description: Validate quantitative finance flash card structure, metadata, British English spelling, and finance relevance. Use when creating or editing .md files in the cards/ directory.
---

# Quant Card Validator

This skill ensures all flash cards adhere to the project's strict "source of truth" architecture and stylistic requirements.

## Validation Checklist

### 1. Structure & Metadata
- **Title**: Must start with a single `# ` followed by the concept name.
- **Metadata Fields**: Must include exactly these fields in this order:
  - `**Topic:** <Topic Name>` (Must match `TOPIC_COLOURS` in `app/routes.py`)
  - `**Tags:** tag1, tag2` (Comma-separated)
  - `**Author:** <Name/Model>`
- **Separator**: A horizontal rule `---` must follow the metadata.
- **Required Sections**: Must contain these `## ` headers in order:
  - `## Definition`
  - `## Key Formula`
  - `## Example`
  - `## Remember`

### 2. Topic Consistency
The `**Topic:**` field must be one of these existing categories:
- Calculus
- Derivatives
- Financial Mathematics
- Linear Algebra
- Mathematical Notation
- Probability
- Risk
- Statistics
- Stochastic Processes

### 3. British English (Mandatory)
Flag and fix any American spellings. Common targets:
- `-ise` instead of `-ize` (e.g., *normalised*, *optimise*, *recognise*)
- `-our` instead of `-or` (e.g., *colour*, *behaviour*)
- `-ll-` in inflected forms (e.g., *modelling*, *labelled*)
- `-re` instead of `-er` (e.g., *centre*)

### 4. Maths Rendering (KaTeX)
- **Inline**: Use single dollar signs `$E = mc^2$`.
- **Display**: Use double dollar signs `$$...$$`.
- **Escaping**: If using backslashes in LaTeX (e.g. `\sigma`), ensure the loader's `_protect_math` logic isn't bypassed.

### 5. Finance Relevance (The "Remember" Test)
The `## Remember` section must not just summarise the maths. It **MUST** explicitly state the concept's application in quantitative finance (e.g., "Used to derive the Black-Scholes PDE", "Crucial for calculating CVA").

## Workflow
1. **Read**: Load the target `.md` file.
2. **Check**: Run through the checklist above.
3. **Report**: provide a concise list of violations or a "Pass" confirmation.
4. **Fix**: Propose the corrected Markdown content.
