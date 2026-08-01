# Skill: Validate Links

Automate the verification of all external learning resources (websites and videos) in `resources.json`. This skill performs deep checks, including detecting unavailable YouTube videos that would otherwise return a standard `200 OK` status.

## Instructions

1.  **Run Validation:** Execute `uv run python scripts/validate_urls.py --force`.
2.  **Analyze Results:**
    *   If all URLs pass, inform the user that the knowledge graph's external links are healthy.
    *   If failures are found, list the specific cards and titles that have broken links.
3.  **Propose Fixes:**
    *   For broken links, offer to find alternative resources (e.g., via web search) or remove them from `resources.json`.
    *   If the user approves removal, use a targeted `replace` operation on `resources.json` to delete the failing entry.

## Integration

-   **Pre-commit Hook:** This validation runs automatically before every commit where `resources.json` is modified.
-   **Manual Check:** Use this skill whenever adding new cards or performing periodic maintenance on the library.

## Verification

After removing or replacing links, run the validation script again to ensure the file is now clean:
`uv run python scripts/validate_urls.py --force`
