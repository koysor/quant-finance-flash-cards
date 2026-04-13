# General ARCH Framework

**Topic:** Statistics
**Tags:** arch, conditional variance, information set, heteroscedasticity, time series
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

The **General ARCH Framework** is the meta-structure shared by all ARCH-family models. Any ARCH model must specify six components: the observable return series, the information set, the conditional mean, the conditional variance (the key object), the conditional distributional form, and the parameter vector. The framework unifies GARCH, GJR-GARCH, EGARCH, FIGARCH, and ARCH-M as different choices within the same scaffold.

## Key Formula

The six components:

| Component | Symbol | Meaning |
|---|---|---|
| Returns | $r_t$ | Observable time series |
| Information set | $\mathcal{I}_{t-1} = \{r_{t-1}, r_{t-2}, \ldots\}$ | All past returns up to $t-1$ |
| Conditional mean | $\mu_t = E[r_t \mid \mathcal{I}_{t-1}]$ | Expected return given the past |
| Conditional variance | $h_t = \text{Var}(r_t \mid \mathcal{I}_{t-1})$ | The object ARCH models |
| Conditional distribution | $r_t \mid \mathcal{I}_{t-1} \sim D(\mu_t, h_t)$ | Normal, Student-$t$, GED, etc. |
| Parameter vector | $\theta$ | All parameters to be estimated by MLE |

The **standardised residual** must be i.i.d.:

$$z_t = \frac{r_t - \mu_t}{\sqrt{h_t}} \overset{\text{i.i.d.}}{\sim} D(0, 1)$$

## Example

For GARCH(1,1) with normal innovations the choices are:
- $\mu_t = \mu$ (constant mean)
- $h_t = \omega + \alpha(r_{t-1} - \mu)^2 + \beta h_{t-1}$
- $D = \mathcal{N}(0,1)$
- $\theta = (\mu, \omega, \alpha, \beta)$

Diagnostics check whether the $z_t$ are truly i.i.d. $\mathcal{N}(0,1)$: plot the ACF of $z_t^2$ (should be near zero), test kurtosis (should be 3), and apply the Jarque–Bera test. Significant ACF in $z_t^2$ signals a misspecified variance equation; excess kurtosis signals the wrong distributional choice.

## Remember

The ARCH framework separates three modelling decisions that practitioners often conflate: (1) the **variance equation** (GARCH vs GJR vs EGARCH — determines how past shocks enter $h_t$), (2) the **mean equation** (constant vs ARCH-M — determines whether volatility earns a risk premium), and (3) the **innovation distribution** (normal vs Student-$t$ vs GED — determines tail behaviour of $z_t$). Choosing poorly on any one dimension leads to systematic mispricing of tail risk: a normal GARCH underestimates VaR because the $z_t$ are fat-tailed, not because $h_t$ is misspecified.
