# GARCH Variance Half-Life

**Topic:** Statistics
**Tags:** garch, half-life, variance persistence, mean reversion, volatility forecasting
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **half-life of a GARCH variance shock** is the number of periods it takes for the gap between the current conditional variance and its long-run level to halve. It measures how quickly a volatility spike dissipates — a long half-life means turbulent periods are sustained for months, not days. The half-life is determined entirely by the persistence parameter $\alpha + \beta$.

## Key Formula

The $n$-step-ahead GARCH(1,1) variance forecast mean-reverts to the long-run variance $V = \omega/(1-\alpha-\beta)$:

$$h_{t+n} = V + (\alpha + \beta)^n (h_t - V)$$

The **half-life** $H$ solves $(\alpha + \beta)^H = \tfrac{1}{2}$:

$$\boxed{H = \frac{-\ln 2}{\ln(\alpha + \beta)}}$$

Higher persistence $(\alpha + \beta \to 1)$ implies a longer half-life. At $\alpha + \beta = 1$ (IGARCH), the half-life is infinite — shocks never decay.

## Example

**DM/\$ 1991–2000:** $\hat\alpha = 0.035$, $\hat\beta = 0.955$, so $\alpha + \beta = 0.990$.

$$H = \frac{-\ln 2}{\ln 0.990} = \frac{0.693}{0.01005} \approx 69 \text{ days} \approx 3.3 \text{ months}$$

After a volatility spike (say daily vol jumping from 0.7% to 2.0%), the model predicts it will take over 3 months before vol falls back halfway towards the long-run level. By contrast, a model with $\alpha + \beta = 0.90$ would have $H \approx 6.6$ days — almost no memory.

## Remember

The half-life translates an abstract persistence parameter into a statement risk managers can act on. A half-life of 70 days means that elevated VaR limits, wider bid-ask spreads, and reduced position sizes after a shock should remain in place for **months**, not days. It also explains why volatility-targeting strategies (e.g., risk parity funds that scale positions inversely to estimated variance) are slow to restore normal position sizes after a market dislocation — they are responding to the same slow mean reversion that the GARCH half-life formalises.
