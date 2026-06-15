# Epstein-Zin Preferences

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** epstein zin, recursive utility, risk aversion, intertemporal substitution, equity premium puzzle, asset pricing
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

**Epstein-Zin preferences** (Epstein and Zin, 1989) are a class of recursive utility functions that separate two distinct preferences that are conflated in standard CRRA utility: **risk aversion** (aversion to cross-sectional uncertainty) and the **elasticity of intertemporal substitution (EIS)** (willingness to shift consumption across time). This separation is essential for matching observed asset prices without requiring implausible risk aversion coefficients.

## Key Formula

The Epstein-Zin utility satisfies the recursion:

$$V_t = \left[(1-\beta)\,C_t^{1-1/\psi} + \beta\,\bigl(E_t[V_{t+1}^{1-\gamma}]\bigr)^{\frac{1-1/\psi}{1-\gamma}}\right]^{\frac{1}{1-1/\psi}}$$

where $\gamma$ is the **coefficient of relative risk aversion** and $\psi$ is the **elasticity of intertemporal substitution (EIS)**. In standard CRRA utility, $\psi = 1/\gamma$ is forced — Epstein-Zin allows them to be set independently.

The corresponding **stochastic discount factor**:

$$M_{t+1} = \beta^\theta \left(\frac{C_{t+1}}{C_t}\right)^{-\theta/\psi} R_{W,t+1}^{\theta-1}$$

where $\theta = (1-\gamma)/(1-1/\psi)$ and $R_{W,t+1}$ is the return on total wealth (the market portfolio proxy).

## Example

Consider calibrating to US data: equity premium $\approx 6\%$, Sharpe ratio $\approx 0.40$, consumption growth volatility $\sigma_c = 1\%$.

- **Standard CRRA** ($\psi = 1/\gamma$): matching the equity premium requires $\gamma \approx 75$ — implausibly high.
- **Epstein-Zin** with $\gamma = 10$ (moderately high risk aversion) and $\psi = 1.5$ (high EIS — investor willing to substitute intertemporally): the SDF loads on both consumption growth and market return, generating higher effective volatility. Bansal and Yaron (2004) match the equity premium with $\gamma = 10$, $\psi = 1.5$ via the long-run risk mechanism.

## Remember

The key insight is that when $\psi > 1/\gamma$ (high EIS, moderate risk aversion), the investor cares more about long-run growth risks than period-by-period fluctuations. This makes the SDF volatile enough to clear the Hansen-Jagannathan bound without requiring $\gamma \approx 75$. Epstein-Zin preferences underpin the **long-run risk model** (Bansal-Yaron): if consumption growth contains a small persistent component — invisible year-to-year but large over decades — investors with high EIS are very sensitive to it, generating substantial risk premia. This is why Epstein-Zin is the standard preference specification in modern macro-asset pricing.
