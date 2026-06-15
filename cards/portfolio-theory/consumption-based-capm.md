# Consumption-Based CAPM

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** ccapm, consumption capm, stochastic discount factor, risk premium, consumption growth, macrofinance
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **Consumption-Based CAPM (CCAPM)** is an equilibrium asset pricing model in which the expected excess return on any asset is determined by its covariance with aggregate consumption growth, not with the market portfolio. It derives from the representative investor's Euler equation under CRRA utility.

## Key Formula

The SDF under CRRA utility with coefficient $\gamma$ and time discount $\beta$:

$$M_{t+1} = \beta\left(\frac{C_{t+1}}{C_t}\right)^{-\gamma}$$

The **CCAPM risk premium** for asset $i$:

$$E_t[R_{t+1}^i] - R_f \approx \gamma\,\text{Cov}_t\!\left(\frac{\Delta C_{t+1}}{C_t},\, R_{t+1}^i\right) \cdot R_f$$

Assets with **high consumption beta** — that pay off poorly when consumption falls (recessions) — command high risk premia. The consumption beta replaces the market beta of standard CAPM.

The risk-free rate is:

$$R_f \approx \frac{1}{\beta} + \gamma\,\mu_c - \frac{1}{2}\gamma(\gamma+1)\sigma_c^2$$

where $\mu_c$ is expected consumption growth and $\sigma_c$ is its volatility.

## Example

Suppose $\gamma = 2$, $\mu_c = 2\%$, $\sigma_c = 1\%$, and equities have $\text{Cov}(\Delta c, R_{\text{eq}}) = 0.0003$.

Predicted equity premium: $\gamma \times \text{Cov} \times R_f \approx 2 \times 0.0003 \times 1.03 \approx 0.06\%$ per year.

The empirical equity premium is approximately 5–7% per year — the CCAPM with plausible $\gamma$ falls short by a factor of roughly 100. This gap is the **equity premium puzzle**.

## Remember

CCAPM is theoretically elegant — it prices all assets from a single primitive (consumption) — but empirically weak because aggregate consumption is smooth (low $\sigma_c$) relative to asset price volatility. The model implies risk premia far below those observed unless $\gamma$ is implausibly large. This failure motivated Epstein-Zin preferences (separating risk aversion from intertemporal substitution), habit formation models (Campbell-Cochrane), and long-run risk models (Bansal-Yaron), all of which boost the effective SDF volatility without requiring extreme $\gamma$.
