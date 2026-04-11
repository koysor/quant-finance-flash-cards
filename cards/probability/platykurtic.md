# Platykurtic Distribution

**Topic:** Probability
**Tags:** platykurtic, thin tails, excess kurtosis, kurtosis, distribution shape
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

A **platykurtic** distribution has **excess kurtosis less than zero** ($\gamma_2 - 3 < 0$). Compared to the normal distribution, it has a flatter peak and **thinner tails** — extreme outcomes are less likely than a normal model predicts.

$$\gamma_2 - 3 < 0 \iff \text{platykurtic}$$

## Key Formula

$$\gamma_2 - 3 = \frac{E[(X-\mu)^4]}{\sigma^4} - 3 < 0$$

**Common platykurtic distributions:**

| Distribution | Excess kurtosis |
|---|---|
| Uniform$[a,b]$ | $-1.2$ |
| Beta$(\alpha, \beta)$ with $\alpha=\beta=2$ | $-0.86$ |
| Raised cosine | $-0.59$ |
| Normal | 0 (reference) |

The thinner the tails, the more negative the excess kurtosis.

## Example

Consider a scenario-based stress test using 1,000 equally weighted macro scenarios, each with a bounded P&L impact. The resulting loss distribution is approximately uniform — platykurtic with excess kurtosis $\approx -1.2$. Extreme outcomes are bounded by construction, making the distribution more spread-out and flat than a normal, not more peaked.

An asset whose daily return is bounded in $[-r_{\max}, +r_{\max}]$ (such as a circuit-breaker-protected instrument) will also exhibit platykurtic returns.

## Remember

Platykurtic means "broad hump, thin tails" — from Greek *platy* (flat, broad). It is the opposite of leptokurtic. Platykurtic distributions are rare in finance: real asset returns nearly always have fat (leptokurtic) tails. Encountering platykurtosis in financial data is often a sign of bounded or capped returns — circuit breakers, structured products with caps, or artificial data generation — rather than a genuine feature of the underlying asset.
