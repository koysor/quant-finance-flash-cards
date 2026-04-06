# Argmax, Argmin, Sup, and Inf Notation

**Topic:** Mathematical Notation
**Tags:** notation, argmax, argmin, supremum, infimum, optimisation, portfolio
**Created:** 2026-04-04
**Author:** Claude Sonnet 4.6

---

## Definition

These four operators return either the **value** of a function's optimum (sup, inf) or the **point** at which it is achieved (argmax, argmin):

| Symbol | Read as | Returns |
|---|---|---|
| $\max_{x} f(x)$ | "maximum of $f$" | The largest value $f$ attains |
| $\min_{x} f(x)$ | "minimum of $f$" | The smallest value $f$ attains |
| $\sup_{x} f(x)$ | "supremum of $f$" | Least upper bound (exists even if max is not attained) |
| $\inf_{x} f(x)$ | "infimum of $f$" | Greatest lower bound (exists even if min is not attained) |
| $\operatorname{argmax}_{x} f(x)$ | "argmax of $f$" | The input $x^*$ that maximises $f$ |
| $\operatorname{argmin}_{x} f(x)$ | "argmin of $f$" | The input $x^*$ that minimises $f$ |

The domain of optimisation is written as a subscript: $\max_{x \in \mathcal{X}}$, $\operatorname{argmin}_{\boldsymbol{w}: \mathbf{1}^\top\mathbf{w}=1}$.

## Key Formula

**Relationship:**

$$\max_x f(x) = f\!\left(\operatorname{argmax}_x f(x)\right)$$

**Minimum variance portfolio:**

$$\mathbf{w}^* = \operatorname{argmin}_{\mathbf{w}:\,\mathbf{1}^\top\mathbf{w}=1} \mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}$$

**Maximum likelihood estimator:**

$$\hat{\theta}_{\text{MLE}} = \operatorname{argmax}_{\theta} \sum_{i=1}^{n} \log f(x_i \mid \theta)$$

## Example

The Sharpe-ratio maximising portfolio solves:

$$\mathbf{w}^* = \operatorname{argmax}_{\mathbf{w}:\,\mathbf{1}^\top\mathbf{w}=1} \frac{\mathbf{w}^\top \boldsymbol{\mu} - r_f}{\sqrt{\mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}}}$$

The **sup** appears in option pricing when max is not attained: $\sup_{\tau} E^{\mathbb{Q}}[e^{-r\tau}(S_\tau - K)^+]$ over all stopping times $\tau$ gives the American option price — the supremum exists even though no single stopping rule is globally dominant at $t = 0$.

## Remember

The distinction between $\max$ and $\sup$ matters in finance whenever a bound is approached but never reached. The **American option price** as a supremum over stopping times is the canonical example: it is bounded above (by the stock price) but may not be attained by a single deterministic rule. The `argmin` over portfolio weights subject to constraints is the core computation of every portfolio optimiser — writing it in argmin notation immediately signals that you want the **optimal weights**, not just the **minimum variance value**, making the notation precise in a way that "find the minimum" is not.
