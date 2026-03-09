# Probability Integral Transform

**Topic:** Probability
**Tags:** CDF, uniform distribution, model validation, copula, quantile
**Created:** 2026-03-08
**Author:** Claude Opus 4.6

---

## Definition

The **probability integral transform** (PIT) states that if $X$ is a continuous random variable with CDF $F$, then the transformed variable $U = F(X)$ follows a standard uniform distribution $U \sim \text{Uniform}(0, 1)$. Conversely, if $U \sim \text{Uniform}(0, 1)$, then $X = F^{-1}(U)$ has CDF $F$. This theorem is the theoretical foundation of both random number generation and model validation.

## Key Formula

**Forward transform:**

$$U = F(X) \sim \text{Uniform}(0, 1)$$

**Proof sketch:** $P(U \leq u) = P(F(X) \leq u) = P(X \leq F^{-1}(u)) = F(F^{-1}(u)) = u$

**Inverse transform:**

$$X = F^{-1}(U) \sim F$$

**Copula construction** — for a bivariate pair $(X_1, X_2)$ with marginal CDFs $F_1, F_2$:

$$C(u_1, u_2) = P(F_1(X_1) \leq u_1,\; F_2(X_2) \leq u_2)$$

The PIT strips away the marginal distributions, isolating the pure dependence structure in the copula $C$.

## Example

A risk model predicts that daily log-returns follow $X \sim N(0.001, 0.02^2)$. Over 5 days, the actual returns are:

| Day | Return $x$ | $u = \Phi\!\left(\frac{x - 0.001}{0.02}\right)$ |
|---|---|---|
| 1 | $-0.025$ | $\Phi(-1.30) = 0.097$ |
| 2 | $+0.015$ | $\Phi(0.70) = 0.758$ |
| 3 | $+0.031$ | $\Phi(1.50) = 0.933$ |
| 4 | $-0.008$ | $\Phi(-0.45) = 0.326$ |
| 5 | $+0.004$ | $\Phi(0.15) = 0.560$ |

If the model is correct, the $u$ values should be uniformly distributed on $(0, 1)$. Clustering near 0 or 1 would indicate the model underestimates or overestimates volatility.

## Remember

The probability integral transform is the theoretical engine behind three pillars of quantitative finance. First, **simulation**: inverse transform sampling generates draws from any distribution by passing uniforms through $F^{-1}$, and the Box–Muller transform is a clever application of the same principle. Second, **model validation**: the PIT histogram (Rosenblatt transform) tests whether a fitted distribution matches the data — if the transformed values are not uniform, the model is misspecified, and VaR estimates built on it will be unreliable. Third, **copulas**: the PIT separates marginal behaviour from joint dependence by mapping each variable to $U(0,1)$, enabling modellers to mix arbitrary marginal distributions with any dependence structure — the construction at the heart of portfolio credit risk models.
