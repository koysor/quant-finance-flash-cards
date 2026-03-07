---
name: quant-graph-architect
description: Manage flash card connections and knowledge graph dependencies. Use when adding new cards, identifying missing links, or refining the knowledge structure in edges.json.
---

# Quant Graph Architect

This skill manages the semantic graph connecting flash cards, ensuring that concept dependencies and "See Also" links are accurate and high-quality.

## Responsibilities

### 1. Edge Generation & Mapping
When a new card is added, identify its "Prerequisites" (incoming edges) and "See Also" (outgoing edges). 
- **Inbound**: What concept is absolutely required to understand this? (e.g., *Stochastic Integrals* → *Itô's Lemma*)
- **Outbound**: Where does this lead next? (e.g., *Black-Scholes Equation* → *Option Greeks*)

### 2. Semantic Integrity (`edges.json`)
Every edge must follow this schema:
```json
{
  "source": "folder/slug",
  "target": "folder/slug",
  "label": "<short_action_verb>",
  "description": "<contextual_explanation>"
}
```
- **Labels**: Use clear verbs: `extends`, `requires`, `prices`, `approximates`, `generalises`, `specialises`.
- **Descriptions**: Explain *why* the link exists. This description is displayed on the card detail page. Avoid tautologies.

### 3. Orphan Prevention
Search the graph for nodes with zero edges. Every card in the system must have at least one incoming or outgoing edge to be reachable in the interactive graph and "See Also" lists.

## Workflow
1. **Research**: Identify potential connections using `grep_search` to find mentions of a card name in other cards.
2. **Design**: Draft the `edges.json` objects for new connections.
3. **Audit**: Review existing connections for a specific card to ensure they are still relevant.
4. **Update**: Append or modify `edges.json` manually. **NEVER** overwrite the entire file unless performing a full refactor.
