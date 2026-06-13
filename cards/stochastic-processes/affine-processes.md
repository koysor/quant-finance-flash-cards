# Affine Processes

**Topic:** Stochastic Processes
**Tags:** affine process, characteristic function, Riccati ODE, Heston, CIR, Fourier pricing, tractability
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

An affine process is a Markov process $X_t$ on $\mathbb{R}^n$ whose log-characteristic function (log-Laplace transform) is affine in the initial state $x$:

$$\mathbb{E}_x\!\left[e^{\langle u,\, X_t\rangle}\right] = \exp\!\bigl(\phi(t,u) + \langle\psi(t,u),\, x\rangle\bigr)$$

This holds if and only if the drift and diffusion matrix of $X_t$ are themselves affine in $x$.

## Key Formula

**Affine coefficients** (necessary and sufficient for the above):

$$\text{Drift: } \alpha(x) = a + Bx \quad \text{(linear in }x\text{)}$$

$$\text{Diffusion: } (\sigma\sigma^\top)(x) = A + \textstyle\sum_i x_i\, C_i \quad \text{(linear in }x\text{)}$$

The scalar functions $\phi(t,u)$ and vector $\psi(t,u)$ satisfy **generalised Riccati ODEs**:

$$\dot{\psi} = F(\psi), \qquad \dot{\phi} = R(\psi)$$

with $\phi(0,u) = 0$, $\psi(0,u) = u$, for model-specific functions $F$ and $R$.

## Example

The CIR process $dr = \kappa(\theta - r)\,dt + \sigma\sqrt{r}\,dW$ is affine: drift $= \kappa\theta - \kappa r$ (linear in $r$), diffusion$^2 = \sigma^2 r$ (linear in $r$). Its Laplace transform $\mathbb{E}[e^{-\lambda r_T}]$ solves the Riccati system analytically, giving closed-form zero-coupon bond prices. The Heston stochastic vol model is a two-dimensional affine process $(S_t, V_t)$ for the same reason.

## Remember

Affine processes are the workhorse of tractable option pricing: because the characteristic function is exponential-affine, Fourier inversion methods (Carr–Madan FFT) can price a full strip of options in milliseconds. This is why virtually every widely used derivatives model — Heston, Bates jump-diffusion, multi-factor short-rate models — is designed to be affine; departing from the affine family typically forces numerical PDE or Monte Carlo methods, which are orders of magnitude slower.
