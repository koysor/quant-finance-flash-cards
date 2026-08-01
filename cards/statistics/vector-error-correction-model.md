# Vector Error Correction Model

**Topic:** Statistics
**Tags:** vecm, cointegration, reduced rank, error correction, adjustment speed, pairs trading
**Created:** 2026-08-01
**Author:** Claude Opus 5

---

## Definition

A vector error correction model is a vector autoregression written in differences with one extra term: the lagged deviation from long-run equilibrium. It describes cointegrated series by combining short-run dynamics with a force pulling the system back towards its long-run relationship.

## Key Formula

$$\Delta \mathbf{P}_t = \Pi\,\mathbf{P}_{t-1} + \Gamma_1 \Delta\mathbf{P}_{t-1} + \boldsymbol{\epsilon}_t$$

For the equation to balance, $\Pi$ must have **reduced rank** — the left side is stationary, so $\Pi \mathbf{P}_{t-1}$ must be stationary too even though $\mathbf{P}_{t-1}$ is not. This forces the factorisation:

$$\Pi = \boldsymbol{\alpha}\boldsymbol{\beta}_C', \qquad \Delta\mathbf{P}_t = \boldsymbol{\alpha}\left(\boldsymbol{\beta}_C'\mathbf{P}_{t-1} + \boldsymbol{\mu}_e\right) + \Gamma_1\Delta\mathbf{P}_{t-1} + \boldsymbol{\epsilon}_t$$

$\boldsymbol{\beta}_C$ holds the cointegrating weights (what combination is stationary) and $\boldsymbol{\alpha}$ the **adjustment speeds** (how fast each series corrects). For a pair:

$$\Pi = \begin{pmatrix}\alpha_1 \\ \alpha_2\end{pmatrix}\begin{pmatrix}1 & -\beta\end{pmatrix} = \begin{pmatrix}\alpha_1 & -\alpha_1\beta \\ \alpha_2 & -\alpha_2\beta\end{pmatrix}$$

## Example

Two cointegrated equities with $\beta_C = 1.4$ and fitted adjustment coefficients $\alpha_1 = -0.08$, $\alpha_2 = 0.03$.

Yesterday the spread sat 2.5 units above equilibrium, so $\beta_C'\mathbf{P}_{t-1} - \mu_e = 2.5$. Today's expected changes are:

$$\mathbb{E}[\Delta P^A_t] = -0.08 \times 2.5 = -0.20, \qquad \mathbb{E}[\Delta P^B_t] = 0.03 \times 2.5 = +0.075$$

Asset A falls and asset B rises — both close the gap. The signs matter: a positive $\alpha_1$ on the leading asset would mean the system diverges rather than corrects, indicating the specification is wrong.

## Remember

The VECM is what makes a cointegrated pair tradeable rather than merely interesting. The $\alpha$ coefficients answer the question a statistical arbitrageur actually needs answered — **which leg does the correcting** — and that determines the trade. If $\lvert\alpha_1\rvert$ is large and $\alpha_2 \approx 0$, asset A does all the adjusting while B behaves as the anchor, so the position should be concentrated in A. A statistically significant adjustment coefficient is also the confirmation step of the Engle-Granger procedure: a stationary residual establishes that an equilibrium exists, but only a significant $\alpha$ establishes that the market actually returns to it within a horizon you can hold. Note the modelling choice implied here — a VAR in returns discards the level information entirely and forecasts poorly, whereas the VECM keeps it in the error correction term.
