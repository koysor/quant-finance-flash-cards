---
name: quant-topic-scanner
description: Scans a folder for mathematical, statistical, financial, trading, or quantitative finance topics and generates succinct flash cards in markdown format for learning. Use when you need to extract and summarise key concepts from a directory of files into a structured flash card format.
---

# Quant Topic Scanner

This skill enables Gemini CLI to act as a specialized agent for scanning directories and generating educational flash cards for quantitative finance topics.

## Workflow

1.  **Identify Target Directory:** The user will provide a directory path to scan.
2.  **Scan and Analyze:** Use `ls` or `glob` to find all files in the directory. Read relevant file contents (markdown, text, etc.) to identify distinct topics related to:
    -   Mathematics
    -   Statistics
    -   Finance
    -   Trading
    -   Quantitative Finance
3.  **Topic Extraction:** List all unique topics identified.
4.  **Flash Card Generation:** For each distinct topic, generate a succinct flash card in markdown format.
    -   **Target Audience:** A Level maths standard student.
    -   **Tone:** Clear, intuitive, and educational.
    -   **Reference Style:** Consult [references/style_guide.md](references/style_guide.md) for the exact structure and tone.
    -   **Mathematics:** Always use LaTeX for formulas.
5.  **Output:**
    -   Create a subdirectory named `flash_cards` within the scanned folder if it does not already exist.
    -   Save each topic as a separate markdown file within the `flash_cards` directory.
    -   Use hyphenated slugs for filenames (e.g., `black-scholes.md`).

## Best Practices

-   **De-duplication:** Ensure that if multiple files mention the same topic, only one consolidated flash card is generated.
-   **Clarity:** Prioritize intuitive explanations over complex jargon.
-   **Verification:** Ensure all LaTeX is correctly formatted and uses KaTeX-compatible syntax (e.g., `$$ ... $$` for blocks).
-   **Language:** Always use British English (e.g., "normalised", "optimisation", "favour").

## Example Usage

"Scan the current directory for quant topics and generate flash cards in a flash_cards folder."
