# XVA

**Topic:** Derivatives
**Level:** A Level Mathematics
**Tags:** XVA, CVA, DVA, FVA, valuation adjustment, counterparty risk, funding
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

XVA is the collective term for the family of valuation adjustments applied to the theoretical (risk-free, frictionless) price of OTC derivatives to account for real-world costs and risks. The main components are: **CVA** (credit valuation adjustment — the cost of counterparty default risk), **DVA** (debit valuation adjustment — the benefit from one's own default risk), **FVA** (funding valuation adjustment — the cost of funding uncollateralised exposure), and **KVA** (capital valuation adjustment — the cost of regulatory capital). XVA desks at major banks actively manage these adjustments as a portfolio.

## Key Formula

The **risk-free price** is adjusted by:

$$V_{\text{traded}} = V_{\text{risk-free}} - \text{CVA} + \text{DVA} - \text{FVA} - \text{KVA}$$

**CVA** (cost of counterparty default):

$$\text{CVA} = (1 - R_C) \int_0^T \text{EE}(t) \, dP_C(t)$$

**DVA** (benefit of own default):

$$\text{DVA} = (1 - R_B) \int_0^T \text{NEE}(t) \, dP_B(t)$$

**FVA** (funding cost on uncollateralised exposure):

$$\text{FVA} = \int_0^T s_f(t) \cdot \text{EE}_{\text{uncoll}}(t) \, dt$$

where $\text{EE}$ is expected exposure, $\text{NEE}$ is negative expected exposure, $R$ is recovery rate, $P(t)$ is default probability, and $s_f$ is the funding spread.

## Example

A bank enters a 10-year uncollateralised interest rate swap with a corporate counterparty.

| Component | Value | Explanation |
|-----------|-------|-------------|
| Risk-free price | £0 | Par swap at inception |
| CVA | $-£320{,}000$ | Counterparty default probability 3%, avg EE £8m, recovery 40% |
| DVA | $+£85{,}000$ | Bank's own default probability 0.8%, avg NEE £6m |
| FVA | $-£180{,}000$ | Funding spread 50 bps on avg uncollateralised EE of £3.6m |
| KVA | $-£95{,}000$ | 13% cost of capital on £7.3m regulatory capital |

$$V_{\text{traded}} = 0 - 320{,}000 + 85{,}000 - 180{,}000 - 95{,}000 = -£510{,}000$$

The bank must charge the client at least £510,000 upfront (or adjust the fixed rate by ~5 bps) to break even on the true cost of the trade.

## Remember

XVA transformed derivatives pricing after the 2008 financial crisis. Before Lehman's collapse, banks priced OTC derivatives as if counterparties were default-free and funding was unlimited at LIBOR flat — neither assumption survived. Today, XVA desks are among the largest and most technically sophisticated teams at major banks, managing portfolios of valuation adjustments that can run into billions. For quant developers, XVA is computationally intensive: calculating CVA alone requires simulating the entire portfolio of trades across thousands of scenarios to compute the expected exposure profile, then integrating against counterparty default probabilities. This makes XVA one of the primary drivers of investment in Monte Carlo infrastructure, GPU computing, and adjoint algorithmic differentiation at banks. Understanding XVA is essential because it explains why the same derivative can have different prices at different banks — each bank's funding cost, credit quality, and capital requirements produce different adjustments.
