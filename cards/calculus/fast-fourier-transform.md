# Fast Fourier Transform

**Topic:** Calculus
**Level:** A Level Mathematics
**Tags:** FFT, fourier transform, characteristic function, option pricing, numerical methods
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The fast Fourier transform (FFT) is an algorithm that computes the discrete Fourier transform in $O(n \log n)$ operations instead of $O(n^2)$. In quantitative finance, it is used to price options by inverting the characteristic function of the log-price distribution. Models like Heston and Variance Gamma have known characteristic functions but no closed-form option prices — the FFT recovers prices across all strikes simultaneously from a single numerical integration, making it orders of magnitude faster than solving the pricing PDE or running Monte Carlo for each strike.

## Key Formula

The **Carr-Madan formula** (1999) expresses the call price as a Fourier integral:

$$C(K) = \frac{e^{-\alpha \ln K}}{\pi} \int_0^{\infty} e^{-iv \ln K} \psi(v) \, dv$$

where $\alpha > 0$ is a dampening parameter and $\psi(v)$ is the modified characteristic function:

$$\psi(v) = \frac{e^{-rT} \phi_T(v - (\alpha + 1)i)}{\alpha^2 + \alpha - v^2 + i(2\alpha + 1)v}$$

with $\phi_T(u) = E[e^{iu \ln S_T}]$ being the characteristic function of the log-price.

The **FFT** discretises this integral and computes prices at $N$ log-strike points simultaneously.

## Example

Pricing European calls under the Heston model with parameters $v_0 = 0.04$, $\theta = 0.04$, $\kappa = 2$, $\xi = 0.3$, $\rho = -0.7$, $S = 100$, $r = 5\%$, $T = 1$:

Using $N = 4{,}096$ FFT grid points with $\alpha = 1.5$:

1. Evaluate $\psi(v_j)$ at 4,096 points — each evaluation uses the known Heston characteristic function
2. Apply the FFT — one call to the FFT algorithm
3. Extract call prices at all 4,096 strikes

Total computation time: ~2 milliseconds. By contrast, solving the Heston PDE for each strike individually would take ~50 ms per strike, or ~200 seconds for all 4,096 strikes.

## Remember

The FFT is one of the most important computational tools in a quant developer's arsenal. It transforms option pricing from a per-strike problem into a whole-surface problem — calibrating a stochastic volatility model to hundreds of market quotes becomes tractable when each model evaluation prices all strikes at once. The Carr-Madan method (and its refinement, the COS method by Fang and Oosterlee) is the standard approach for pricing under any model with a known characteristic function, including Heston, Variance Gamma, CGMY, and jump-diffusion models. Understanding the FFT is essential for building fast calibration engines, real-time pricing systems, and any infrastructure that must price exotic payoffs under advanced dynamics.
