# Bates Model

**Topic:** Stochastic Processes
**Tags:** Bates model, Heston, jump-diffusion, stochastic volatility, characteristic function, equity derivatives
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The Bates (1996) model extends Heston stochastic volatility by adding compound Poisson jumps in the log stock price; it captures both the persistent vol smile from stochastic vol and the short-dated skew from crash-risk jumps, and retains a closed-form characteristic function suitable for FFT pricing.

## Key Formula

Stock and variance dynamics:

$$\frac{dS}{S} = (r - \lambda\bar{J})\,dt + \sqrt{V}\,dW_1 + (e^J - 1)\,dN_t$$

$$dV = \kappa(\theta - V)\,dt + \xi\sqrt{V}\,dW_2, \qquad \mathbb{E}[dW_1\,dW_2] = \rho\,dt$$

where $N_t$ is Poisson with intensity $\lambda$, $J \sim \mathcal{N}(\mu_J, \sigma_J^2)$, and $\bar{J} = e^{\mu_J + \sigma_J^2/2} - 1$ is the mean proportional jump (compensator).

Characteristic function factorises as:

$$\phi_{\text{Bates}}(u) = \phi_{\text{Heston}}(u) \cdot \exp\!\bigl(\lambda T\bigl(e^{iu\mu_J - u^2\sigma_J^2/2} - 1\bigr)\bigr)$$

The extra factor is the characteristic function of a Gaussian mixture of Poisson arrivals — the jump contribution to the log-return CF.

## Example

$S_0 = 100$, $V_0 = 0.04$, $\kappa = 2$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.7$ (Heston parameters), plus jumps: $\lambda = 0.5$ yr$^{-1}$, $\mu_J = -0.05$, $\sigma_J = 0.07$. The jump parameters add $-2.5\%$ mean annual jump and occasional $\pm 7\%$ random shocks. This steepens the short-dated implied vol skew relative to pure Heston, matching the market's behaviour around earnings or macro events.

## Remember

Bates solves Heston's empirical failure: at short maturities (1 week to 1 month), Heston's continuous vol process cannot generate the steep skew observed in index options because diffusion-driven smiles flatten toward ATM at short horizons. The jumps fill this gap by contributing immediate left-tail risk that does not diffuse away. In practice, Bates is the baseline equity derivatives model when both the term structure of skew and the level of implied vol matter — Heston for long maturities and exotics, Bates when short-dated vanilla calibration is also required.
