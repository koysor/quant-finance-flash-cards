# Variance Drag

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** variance drag, geometric mean, arithmetic mean, compounding, volatility, Kelly criterion
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

Variance drag (also called volatility drag or the Itô correction) is the systematic gap between a portfolio's arithmetic mean return and its realised geometric (compounded) mean return. Because compounding is multiplicative, losing 20% and then gaining 20% does not return to the starting value — the drag is approximately half the variance of returns per period.

## Key Formula

$$\mu_g \approx \mu_a - \tfrac{1}{2}\sigma^2$$

where $\mu_g$ is the geometric (compound) mean return, $\mu_a$ is the arithmetic mean return, and $\sigma^2$ is the variance of periodic returns. The exact relationship for log-normally distributed returns is:

$$\mu_g = \mu_a - \tfrac{1}{2}\sigma^2$$

Equivalently, in terms of log returns: if $r_t \sim N(\mu, \sigma^2)$ then the expected log return is $\mu - \tfrac{1}{2}\sigma^2$.

## Example

Two funds both report a 10% arithmetic mean annual return. Fund A has volatility 5%; Fund B has volatility 30%.

| Fund | $\mu_a$ | $\sigma$ | Drag $\tfrac{1}{2}\sigma^2$ | $\mu_g$ |
|------|--------|---------|--------------------------|--------|
| A | 10% | 5% | 0.13% | 9.87% |
| B | 10% | 30% | 4.50% | 5.50% |

Over 20 years, £1 invested in Fund A grows to $1.09875^{20} \approx £6.53$, while Fund B grows to only $1.055^{20} \approx £2.92$ — less than half, despite identical arithmetic means.

## Remember

Variance drag explains why the Kelly criterion prescribes betting a fraction of wealth rather than the full edge: maximising expected (arithmetic) return does not maximise compounded wealth. The optimal Kelly fraction $f^* = \mu/\sigma^2$ is precisely the ratio that eliminates the marginal variance drag relative to the marginal expected return gain. In quantitative finance, high-volatility strategies must clear a higher return hurdle than low-volatility ones to deliver the same compounded wealth — a 30%-vol strategy needs roughly 5% more arithmetic return just to match the geometric growth of a 5%-vol strategy with the same arithmetic mean.

