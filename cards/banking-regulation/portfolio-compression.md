# Portfolio Compression

**Topic:** Banking Regulation
**Tags:** portfolio compression, notional reduction, leverage ratio, netting, otc derivatives
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Portfolio compression is a post-trade risk management technique in which multiple counterparties submit offsetting OTC derivative trades to a third-party service that identifies and tears up redundant positions, replacing them with a smaller set of trades that preserve the same net risk profile but reduce gross notional outstanding. It addresses the accumulation of economically offsetting trades that arise from continuous trading without position novation.

## Key Formula

Let a portfolio contain $N$ trades with notionals $n_1, n_2, \ldots, n_N$ and net risk $R_{\text{net}}$. After compression to $M < N$ trades:

$$R_{\text{net,after}} = R_{\text{net,before}} \quad \text{(risk preserved)}$$

$$\sum_{j=1}^{M} |n_j^{\prime}| \ll \sum_{i=1}^{N} |n_i| \quad \text{(gross notional reduced)}$$

Compression efficiency is measured as the **notional reduction ratio**:

$$\eta = 1 - \frac{\text{Gross notional after}}{\text{Gross notional before}}$$

Industry compression cycles for interest rate swaps regularly achieve $\eta > 90\%$.

## Example

Three banks hold a cycle of offsetting interest rate swaps: A pays fixed to B (£100 m), B pays fixed to C (£100 m), C pays fixed to A (£100 m). Net economic risk for each bank is zero. Compression tears up all three trades: gross notional falls from £300 m to £0, leverage ratio exposure falls from £300 m to £0, and all three banks free up balance-sheet capacity at zero net change in risk.

## Remember

Portfolio compression became commercially critical after Basel III's leverage ratio used gross notional (rather than net risk) as a key component of the total exposure measure. A bank running £10 tn in interest rate swaps — much of it offsetting — might face a leverage ratio breach purely from gross balance-sheet size, even though the net interest rate risk is small. Compression services (TriOptima, Tradeweb) run multilateral cycles where hundreds of counterparties contribute portfolios simultaneously, achieving far greater notional reduction than any bilateral cancellation could.
