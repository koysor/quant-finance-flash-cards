# Lévy Processes

**Topic:** Stochastic Processes
**Tags:** lévy process, independent increments, stationary increments, jump diffusion, characteristic exponent
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A **Lévy process** $X_t$ is a stochastic process with $X_0 = 0$ that has **stationary** and **independent increments** and is continuous in probability (stochastically continuous). These three properties generalise both Brownian motion (the continuous case) and compound Poisson processes (the pure-jump case). Every Lévy process is fully characterised by three ingredients: a drift $b$, a diffusion coefficient $\sigma$, and a **Lévy measure** $\nu$ that describes the rate and size of jumps. The **Lévy–Khintchine formula** encodes all three into the characteristic function.

## Key Formula

The characteristic function of a Lévy process at time $t$ is:

$$E\!\left[e^{i u X_t}\right] = e^{t\,\psi(u)}$$

where the **characteristic exponent** $\psi(u)$ is given by the Lévy–Khintchine representation:

$$\psi(u) = i b u - \tfrac{1}{2}\sigma^2 u^2 + \int_{\mathbb{R}\setminus\{0\}} \!\left(e^{iux} - 1 - iux\,\mathbf{1}_{|x|<1}\right) \nu(dx)$$

| Symbol | Meaning |
|---|---|
| $b \in \mathbb{R}$ | Drift coefficient |
| $\sigma \geq 0$ | Diffusion (Gaussian) coefficient |
| $\nu$ | Lévy measure satisfying $\int \min(1, x^2)\,\nu(dx) < \infty$ |

The triplet $(b, \sigma^2, \nu)$ is called the **Lévy–Khintchine triplet** or **characteristic triplet**.

## Example

Consider identifying the Lévy–Khintchine triplet for a standard Brownian motion with drift $\mu = 0.05$ and volatility $\sigma = 0.2$.

Since Brownian motion has no jumps, the Lévy measure is $\nu = 0$. The integral term vanishes, leaving:

$$\psi(u) = i(0.05)u - \tfrac{1}{2}(0.04)u^2 = 0.05\,iu - 0.02\,u^2$$

The triplet is $(b, \sigma^2, \nu) = (0.05,\; 0.04,\; 0)$.

For a compound Poisson process with arrival rate $\lambda = 3$ and jump sizes $J \sim N(0, 0.01)$, we instead have $\sigma = 0$ and $\nu(dx) = 3\,f_J(x)\,dx$ where $f_J$ is the jump-size density. The drift $b$ is chosen to compensate small jumps.

## Remember

Standard geometric Brownian motion assumes continuous paths and normally distributed returns, but empirical asset returns exhibit **jumps** (e.g. earnings surprises, flash crashes) and **fat tails**. Lévy processes provide a principled framework for building models that capture these features. The Merton jump-diffusion model, the Variance Gamma model, and the CGMY model are all Lévy processes with different choices of $(b, \sigma^2, \nu)$. In option pricing, replacing GBM with a Lévy process produces volatility smiles and skews that match market prices more closely, particularly for short-dated options where jump risk dominates.
