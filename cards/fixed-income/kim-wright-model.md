# Kim–Wright Model

**Topic:** Fixed Income
**Tags:** term premium, kim-wright, federal reserve, kalman filter, essentially affine, treasury yields
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The Kim–Wright (2005) model is a two-factor, continuous-time, essentially affine Gaussian term structure model that decomposes US Treasury yields into rate expectations and a time-varying term premium, estimated by the Federal Reserve Board using a Kalman filter applied directly to observed yields.

## Key Formula

**Latent state vector** $X_t = (x_{1t}, x_{2t})^\top$ evolves under the physical measure $\mathbb{P}$:

$$dX_t = K^{\mathbb{P}}\!\left(\theta^{\mathbb{P}} - X_t\right)dt + \Sigma\,dW_t^{\mathbb{P}}$$

**Essentially affine market price of risk:**

$$\lambda_t = \lambda_0 + \lambda_1 X_t$$

**Yields affine in state** (risk-neutral bond-pricing):

$$y_t(\tau) = A(\tau) + B(\tau)^\top X_t$$

where $A(\tau)$ and $B(\tau)$ satisfy the Riccati ODEs from the affine bond-pricing formula.

**Term premium decomposition** at horizon $\tau$:

$$y_t(\tau) = \underbrace{\frac{1}{\tau}\int_0^{\tau}\mathbb{E}_t^{\mathbb{P}}\!\left[r_{t+s}\right]ds}_{\text{rate expectations}} + \underbrace{tp_t(\tau)}_{\text{term premium}}$$

**Estimation:** state $X_t$ is unobserved; the Kalman filter jointly estimates the states and model parameters by maximising the likelihood of observed Treasury yields across maturities.

## Example

For a 10-year Treasury with yield $y_t(10) = 4.20\%$:

The Kim–Wright model might attribute:
- Rate expectations component: $3.60\%$ (average expected short rate over 10 years)
- Term premium: $+0.60\%$

In 2011–2015, during aggressive Fed QE, the Kim–Wright 10-year term premium was persistently negative (around $-0.50\%$ to $-1.00\%$), indicating that investors were accepting yields well below expected short rates — the opposite of the usual risk compensation. The two latent factors in Kim–Wright capture this primarily through the level factor, while ACM's five PC-based factors spread the signal across more dimensions.

## Remember

The Kim–Wright model and the ACM model both decompose the same Treasury yield into rate expectations and term premium, yet can give materially different estimates: ACM uses five observable principal components and OLS-style regression, while Kim–Wright uses two latent (unobserved) factors estimated by Kalman filter. The choice matters for monetary policy: a Fed researcher using Kim–Wright might conclude that 60% of a yield rise reflects expectations, while an ACM estimate might say 75%. Central bank communications about whether "bond yields reflect rate expectations or risk appetite" are implicitly model-dependent.
