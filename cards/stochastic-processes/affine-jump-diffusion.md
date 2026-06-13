# Affine Jump-Diffusion

**Topic:** Stochastic Processes
**Tags:** affine jump-diffusion, Duffie-Pan-Singleton, Bates model, Poisson jumps, characteristic function, credit risk
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

An affine jump-diffusion (AJD) extends an affine diffusion by adding Poisson jumps whose intensity and jump-size distribution parameters are affine functions of the state; the log-characteristic function remains affine in the initial state, preserving Fourier tractability.

## Key Formula

State dynamics under risk-neutral measure:

$$dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t + dJ_t$$

where $\mu(x) = K_0 + K_1 x$ (affine drift), $(\sigma\sigma^\top)(x) = H_0 + H_1 x$ (affine variance), and $J_t$ is a compound Poisson process with intensity $\lambda(x) = l_0 + l_1^\top x$ (affine in $x$).

Log-characteristic function: $\ln \mathbb{E}[e^{u X_t}] = \phi(t, u) + \psi(t, u)^\top x$, where $\phi$ and $\psi$ satisfy **generalised Riccati ODEs** that include an extra jump term:

$$\dot{\psi} = K_1^\top \psi + \tfrac{1}{2}H_1(\psi \otimes \psi) + l_1(\theta_J(\psi) - 1)$$

with $\theta_J(u) = \mathbb{E}[e^{u \cdot \Delta J}]$ the jump MGF.

## Example

**Bates (1996) model** — Heston with log-normal jumps in the stock price: $V_t$ follows CIR (affine), jump intensity $\lambda$ is constant, jump size $\ln(1 + Z) \sim N(\mu_J, \sigma_J^2)$. The characteristic function is $\exp(\phi + \psi_V V_t + i u \ln S_t)$ — still exponential-affine, so Carr–Madan FFT pricing applies immediately.

$S_0 = 100$, $V_0 = 0.04$, $\lambda = 0.5$ jumps/yr, $\mu_J = -0.05$, $\sigma_J = 0.07$: one or two negative jumps per year, adding left-skew and fat tails on top of the Heston smile.

## Remember

AJDs are the natural habitat of credit risk modelling (Duffie–Singleton, 1999): the default intensity $\lambda(X_t)$ is affine in macroeconomic state variables, so survival probabilities $\mathbb{E}[e^{-\int_0^T \lambda(X_s)\,ds}]$ are exponential-affine — exactly the same Riccati ODE machinery as bond pricing. This unified framework links equity vol models (Bates), credit models (Duffie-Singleton), and interest rate models (CIR) into a single mathematically tractable class.
