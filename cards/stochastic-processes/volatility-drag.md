# Volatility Drag

**Topic:** Stochastic Processes
**Tags:** volatility drag, GBM, Itô's lemma, log returns, Jensen's inequality, compounding
**Author:** Claude Opus 4.6

---

## Definition

**Volatility drag** is the reduction in compound (geometric) growth rate caused by volatility. When an asset follows geometric Brownian motion with drift $\mu$ and volatility $\sigma$, the log-price drifts at $\mu - \frac{1}{2}\sigma^2$, not $\mu$. The $-\frac{1}{2}\sigma^2$ correction arises directly from applying Itô's lemma to $\ln S$ and means that higher volatility lowers the realised compound return.

## Key Formula

Starting from GBM $dS = \mu S \, dt + \sigma S \, dW$, apply Itô's lemma to $V(S) = \ln S$:

$$d(\ln S) = \left(\mu - \tfrac{1}{2}\sigma^2\right) dt + \sigma \, dW$$

| Quantity | Value |
|---|---|
| Arithmetic mean return | $\mu$ |
| Geometric (compound) growth rate | $\mu - \frac{1}{2}\sigma^2$ |
| Volatility drag | $\frac{1}{2}\sigma^2$ |

The derivation uses $\frac{d}{dS}(\ln S) = \frac{1}{S}$ and $\frac{d^2}{dS^2}(\ln S) = -\frac{1}{S^2}$. The negative second derivative produces the downward correction via the Itô term $\frac{1}{2}\sigma^2 S^2 \cdot (-\frac{1}{S^2}) = -\frac{1}{2}\sigma^2$.

## Example

A stock has arithmetic mean return $\mu = 10\%$ and volatility $\sigma = 30\%$. The compound growth rate of the log-price is:

$$\mu - \tfrac{1}{2}\sigma^2 = 0.10 - \tfrac{1}{2}(0.09) = 0.055 = 5.5\%$$

The volatility drag is $\frac{1}{2}(0.09) = 4.5\%$. Despite an arithmetic mean of 10%, the median outcome grows at only 5.5% per year. Doubling the volatility to 60% would give a drag of 18%, turning the compound growth rate negative.

## Remember

Volatility drag explains why two assets with the same arithmetic mean return but different volatilities produce different wealth outcomes over time. The more volatile asset has a lower median terminal value. This is the mathematical basis for the common advice that volatility is costly for long-term compounding, and it is a direct consequence of Itô's lemma — the same $-\frac{1}{2}\sigma^2$ correction that appears in the Black-Scholes framework.
