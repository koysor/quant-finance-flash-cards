# Attention for Option Pricing

**Topic:** Machine Learning
**Tags:** attention mechanism, option pricing, volatility surface, multi-asset, transformer, cross-strike
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

Applying **self-attention** to option pricing treats the collection of strikes and maturities as a sequence of tokens, allowing each option's price to attend to information from all other strikes and maturities simultaneously. This captures global no-arbitrage constraints (butterfly spreads, calendar spreads) that local feedforward architectures miss, making it natural for pricing entire volatility surfaces or multi-asset baskets in one forward pass.

## Key Formula

For a set of $N$ options with feature vectors $\{\mathbf{x}_i\}$ (encoding strike, maturity, moneyness), the scaled dot-product attention for the $i$-th option is:

$$\text{Attn}(\mathbf{Q}, \mathbf{K}, \mathbf{V})_i = \sum_j \underbrace{\text{softmax}\!\left(\frac{\mathbf{q}_i \cdot \mathbf{k}_j}{\sqrt{d_k}}\right)}_{\text{attention weight}} \mathbf{v}_j$$

where queries $\mathbf{Q} = \mathbf{X}W^Q$, keys $\mathbf{K} = \mathbf{X}W^K$, and values $\mathbf{V} = \mathbf{X}W^V$ are learned linear projections. The $i$-th option's price estimate aggregates information from all other strikes and maturities weighted by their relevance.

## Example

A transformer pricer processes all 50 options on an index (5 maturities × 10 strikes) simultaneously. The 25-delta 1-month put attends strongly to the 10-delta 1-month put (same maturity, different strike → butterfly constraint) and to the 25-delta 3-month put (same moneyness, different maturity → calendar spread constraint). After 10,000 training surfaces, the model prices the full surface with mean absolute vol error of 0.3 vol points versus 0.8 vol points for independent per-option MLPs — the attention captures global arbitrage structure that independent networks ignore.

## Remember

The key advantage of attention over TDBP's per-option MLP is **consistency**: a collection of independent neural network pricers can produce butterfly-violated or calendar-violated surfaces because each network has no knowledge of the others. Self-attention resolves this by making each option's price a function of the entire strike-maturity surface — the attention weights effectively learn the no-arbitrage relationships (put-call parity, convexity in strike, monotonicity in maturity) from data rather than enforcing them as hard constraints. This makes attention-based pricers particularly valuable when the trading book contains many interdependent options that must be jointly consistent.
