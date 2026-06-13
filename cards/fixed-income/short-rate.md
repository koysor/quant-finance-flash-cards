# Short Rate

**Topic:** Fixed Income
**Tags:** short rate, spot rate, yield curve, interest rate models, non-traded
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **short rate** $r(t)$ (also called the spot rate) is the continuously compounded yield on a bond of infinitesimal maturity — the instantaneous risk-free interest rate at time $t$. It is the single state variable driving the entire yield curve in one-factor interest rate models.

## Key Formula

The short rate is not directly observable but is approximated by the yield on very short-maturity instruments. In continuous-time models it defines the **money market account**:

$$B(t) = \exp\!\left(\int_0^t r(s)\,ds\right)$$

which grows at the instantaneous rate $r(t)$. The price of any zero-coupon bond with maturity $T$ then satisfies:

$$V(r, t; T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r(s)\,ds}\,\middle|\,\mathcal{F}_t\right]$$

| Quantity | How it depends on $r$ |
|---|---|
| Zero-coupon bond price | Directly via the pricing PDE |
| Entire yield curve | Determined by the dynamics of $r$ |
| Swap, cap, floor values | Functions of future $r$ values |

## Example

The Vasicek model specifies $dr = \kappa(\theta - r)\,dt + \sigma\,dW$ where $\kappa = 0.5$, $\theta = 4\%$, $\sigma = 1\%$. Starting from $r_0 = 6\%$, the short rate is pulled toward 4% with speed 0.5. A 5-year zero-coupon bond priced under this model produces a yield of roughly 4.3% — above $\theta$ because $r$ starts elevated.

## Remember

The short rate is **not a traded asset**: unlike a stock price $S$, you cannot buy or sell the short rate directly. This non-traded nature is what makes fixed-income modelling fundamentally different from equity modelling. In equity Black–Scholes, the stock hedges itself; in interest rate models, you must hedge one bond against another bond, which forces an additional term — the market price of interest rate risk — into the pricing PDE.
