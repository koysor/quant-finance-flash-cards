# Extreme Value Theory

**Topic:** Risk
**Tags:** risk, tail risk, EVT, extreme events, loss distribution, GEV

---

## Definition

**Extreme Value Theory (EVT)** is a branch of statistics that models the behaviour of extreme (maximum or minimum) values in a dataset. Rather than fitting the entire distribution of returns, EVT focuses exclusively on the tails — the region where rare, large losses occur. The key result is the **Fisher–Tippett–Gnedenko theorem**, which states that the distribution of properly normalised block maxima converges to one of three types: Gumbel, Fréchet, or Weibull, unified as the **Generalised Extreme Value (GEV)** distribution.

## Key Formula

The **Generalised Extreme Value** CDF for the block maximum $M_n$ is:

$$G(x;\; \mu,\; \sigma,\; \xi) = \exp\left(-\left[1 + \xi\left(\frac{x - \mu}{\sigma}\right)\right]^{-1/\xi}\right)$$

where $\mu$ is the location parameter, $\sigma > 0$ is the scale parameter, and $\xi$ is the **shape parameter** (also called the tail index):

- $\xi > 0$: heavy tail (Fréchet) — the case relevant to financial returns
- $\xi = 0$: light tail (Gumbel) — exponentially decaying tails like the normal
- $\xi < 0$: bounded tail (Weibull) — finite upper endpoint

## Example

Suppose we collect the worst daily loss each month for 5 years (60 block maxima) and fit a GEV distribution, obtaining $\mu = 1.2\%$, $\sigma = 0.5\%$, $\xi = 0.25$.

**Estimate the loss exceeded only once every 100 months (99th percentile):**

$$x_{0.99} = \mu + \frac{\sigma}{\xi}\left[(-\ln 0.99)^{-\xi} - 1\right]$$

$$= 1.2 + \frac{0.5}{0.25}\left[(0.01005)^{-0.25} - 1\right]$$

$$= 1.2 + 2.0 \times (3.163 - 1) = 1.2 + 4.33 = 5.53\%$$

The model estimates a 5.53% loss is exceeded roughly once every 100 months — far larger than a normal-distribution estimate would suggest.

## Remember

Standard VaR models assume returns are normally distributed and therefore systematically underestimate the probability and severity of extreme losses. EVT provides a statistically rigorous framework for modelling just the tail, without imposing assumptions about the centre of the distribution. In practice, risk managers use EVT to compute **tail VaR** and **Expected Shortfall** at very high confidence levels (99.9%), where the normal approximation breaks down most severely — exactly the region that matters for regulatory capital calculations under Basel III.
