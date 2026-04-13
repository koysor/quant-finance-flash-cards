# MLE for ARCH Models

**Topic:** Statistics
**Tags:** mle, garch, log-likelihood, conditional variance, parameter estimation
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

Maximum likelihood estimation for ARCH models adapts the general MLE principle to the time-series setting by evaluating the likelihood **conditionally** on the past: each observation's contribution uses the conditional variance $h_t$ computed recursively from the current parameter vector $\theta$. The conditional normality log-likelihood simplifies to a sum of two competing penalties — one that grows with $h_t$ (discouraging overestimation of variance) and one that grows with $z_t^2$ (discouraging underestimation) — so MLE finds the variance path that is just large enough to explain the observed shocks.

## Key Formula

Assuming conditional normality, the log-likelihood (dropping the constant $-\frac{T}{2}\ln(2\pi)$) is:

$$\ell(\theta) = -\frac{1}{2} \sum_{t=1}^{T} \left[\ln h_t + z_t^2\right], \qquad z_t = \frac{r_t - \mu_t}{\sqrt{h_t}}$$

$h_t$ is computed **recursively** for each trial $\theta$:

1. Initialise $h_1 = V = \omega/(1 - \alpha - \beta)$
2. For $t = 2, \ldots, T$: $h_t = \omega + \alpha(r_{t-1} - \mu)^2 + \beta h_{t-1}$

$$\hat\theta = \underset{\theta}{\arg\max}\; \ell(\theta) \quad \text{subject to } \omega, \alpha, \beta \geq 0,\; \alpha + \beta < 1$$

## Example

Suppose at iteration $k$ a trial parameter set gives $h_t = 0.0001$ (low variance) when the return shock was large: $r_t - \mu = 0.03$ (3% return). Then $z_t^2 = 0.03^2/0.0001 = 9$, contributing $-\frac{1}{2}({\ln 0.0001 + 9}) = -\frac{1}{2}(-9.21 + 9) = +0.105$ to $\ell$ — a modest reward despite the large penalty. If instead $h_t = 0.001$, then $z_t^2 = 0.9$, contributing $-\frac{1}{2}(-6.91 + 0.9) = +3.0$ — a much larger contribution. MLE naturally pushes $h_t$ up to absorb volatile days.

## Remember

ARCH MLE is not one-shot matrix inversion like OLS — it is an iterative optimisation where each evaluation of $\ell(\theta)$ requires a full forward pass through the data to compute the recursive $h_t$ sequence. Practitioners use quasi-Newton methods (BFGS) with analytic or numerical gradients; starting values matter and are typically set from the unconditional variance and small values of $\alpha, \beta$. Switching the innovation from normal to Student-$t$ simply replaces $z_t^2$ with the $t$-density log-contribution and adds $\nu$ to $\theta$ — the recursive structure is identical, making fat-tailed ARCH estimation almost as easy as Gaussian.
