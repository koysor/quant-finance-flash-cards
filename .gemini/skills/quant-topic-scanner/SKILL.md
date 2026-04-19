---
name: quant-topic-scanner
description: Scans a folder for mathematical, statistical, financial, trading, or quantitative finance topics and generates succinct flash cards in markdown format for learning. Use when you need to extract and summarise key concepts from a directory of files into a structured flash card format.
---

# Quant Topic Scanner

This skill enables Gemini CLI to act as a specialized agent for scanning directories and generating educational flash cards for quantitative finance topics that integrate directly into the project's card system.

## Workflow

1.  **Identify Target Directory:** The user will provide a directory path to scan.
2.  **Scan and Analyze:** Use `ls` or `glob` to find all files in the directory. Read relevant file contents (markdown, text, etc.) to identify distinct topics related to Quantitative Finance.
3.  **Topic Extraction:** List all unique topics identified.
4.  **Categorisation:** Map each identified concept to one of the following mandatory project topics:
    -   `Banking Regulation`
    -   `Calculus`
    -   `Computational Finance`
    -   `Derivatives`
    -   `Financial Mathematics`
    -   `Fixed Income`
    -   `Linear Algebra`
    -   `Mathematical Notation`
    -   `Portfolio Theory & Asset Pricing`
    -   `Probability`
    -   `Risk`
    -   `Short Selling`
    -   `Statistics`
    -   `Stochastic Processes`
    -   `Volatility`
5.  **Flash Card Generation:** For each distinct concept, generate a succinct flash card in markdown format.
    -   **Structure:** Follow the strict structure defined in [references/style_guide.md](references/style_guide.md).
    -   **Metadata:** Include `**Topic:**`, `**Tags:**`, `**Created:**`, and `**Author:**`.
    -   **Target Audience:** A Level maths standard student.
    -   **Tone:** Clear, intuitive, and educational.
    -   **Mathematics:** Always use LaTeX for formulas ($...$ for inline, $$...$$ for blocks).
6.  **Output:**
    -   Save each concept as a separate markdown file within the `cards/<topic>/` directory of the project root.
    -   Create the topic subdirectory if it does not already exist.
    -   Use hyphenated slugs for filenames (e.g., `black-scholes-formula.md`).

## Best Practices

-   **De-duplication:** Ensure that if multiple files mention the same concept, only one consolidated flash card is generated.
-   **Topic Accuracy:** Only use topics from the allowed list. If a concept fits multiple, pick the most specific one.
- **Consistency:** Consult `notation.json` for standardized LaTeX symbols and `key-terms.json` for common variable definitions used across the project to maintain mathematical consistency.
- **Verification:** Ensure all LaTeX is correctly formatted and uses KaTeX-compatible syntax.

-   **Language:** Always use British English (e.g., "normalised", "optimisation", "favour").

## Example Usage

"Scan the current directory for quant topics and generate cards for the project."

