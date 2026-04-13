# Liquidity-Adjusted VaR

**Topic:** Banking Regulation
**Tags:** liquidity risk, var, bid-ask spread, market risk, stress testing
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Liquidity-Adjusted VaR (LVaR) extends standard VaR by adding the cost of exiting a position in the market — the bid-ask spread — to the pure price-move risk. Standard VaR assumes positions can be liquidated instantly at mid-price; LVaR recognises that the act of selling widens the spread and that in stress scenarios both price volatility and spreads increase simultaneously.

## Key Formula

The additive form separates market risk from liquidity cost:

$$LVaR = VaR + \text{Liquidity Cost}$$

where the liquidity cost for a portfolio of value $S$ is:

$$\text{Liquidity Cost} = \frac{S}{2}\left(\bar{s} + z_\alpha \sigma_s\right)$$

Here $\bar{s}$ is the mean relative bid-ask spread, $\sigma_s$ is its standard deviation, and $z_\alpha$ is the confidence level factor (e.g., 2.33 for 99%). The full expression is:

$$LVaR = S\left(-\mu + z_\alpha \sigma + \tfrac{1}{2}\bar{s} + \tfrac{1}{2}z_\alpha \sigma_s\right)$$

## Example

A trading desk holds £10 m of a corporate bond. The daily return has $\mu = 0$, $\sigma = 0.8\%$. The bond's bid-ask spread has mean $\bar{s} = 0.3\%$ and standard deviation $\sigma_s = 0.1\%$ (at 99%, $z_{0.99} = 2.33$).

$$\text{Standard VaR} = £10\text{m} \times 2.33 \times 0.008 = £186{,}400$$

$$\text{Liquidity Cost} = \frac{£10\text{m}}{2}(0.003 + 2.33 \times 0.001) = £5\text{m} \times 0.00533 = £26{,}650$$

$$LVaR = £186{,}400 + £26{,}650 = £213{,}050$$

The liquidity add-on is 14% of standard VaR — small in normal conditions but much larger in stressed markets.

## Remember

In the 2008 crisis, bid-ask spreads on investment-grade corporate bonds widened from a few basis points to over 100 bps, while simultaneously price volatility spiked — making LVaR a multiple of pre-crisis VaR estimates. Under FRTB, regulators address illiquidity through Liquidity Horizons (1–120 days depending on asset class) rather than a spread-based add-on, but the underlying insight is the same: holding an illiquid position forces you to bear the cost of the spread when you exit, and that cost is correlated with the very market dislocations that also trigger large VaR losses.
