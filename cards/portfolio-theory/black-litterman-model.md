# Black-Litterman Model

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** Black-Litterman, portfolio optimisation, Bayesian, mean-variance, asset allocation
**Author:** Claude Opus 4.6

---

## Definition

The **Black-Litterman model** (1992) is a Bayesian approach to portfolio construction that blends a neutral market equilibrium with an investor's subjective views. Instead of feeding raw expected returns into Markowitz optimisation — which produces extreme, unstable weights — Black-Litterman starts from the implied returns that make the market-cap portfolio optimal, then tilts them towards the investor's views with a confidence weighting.

## Key Formula

**Equilibrium excess returns** (implied by the market portfolio):

$$\Pi = \delta \, \Sigma \, \mathbf{w}_{\text{mkt}}$$

where $\delta$ is the risk-aversion coefficient, $\Sigma$ is the covariance matrix, and $\mathbf{w}_{\text{mkt}}$ is the market-cap weight vector.

**Combined (posterior) expected returns:**

$$\mu_{\text{BL}} = \left[(\tau \Sigma)^{-1} + P^\top \Omega^{-1} P\right]^{-1} \left[(\tau \Sigma)^{-1} \Pi + P^\top \Omega^{-1} Q\right]$$

where $P$ is the pick matrix identifying which assets the views apply to, $Q$ is the vector of view returns, $\Omega$ is the diagonal matrix of view uncertainties, and $\tau$ is a scalar controlling the weight of the prior.

## Example

Two assets with market-cap weights $\mathbf{w}_{\text{mkt}} = (0.6, \; 0.4)^\top$, $\delta = 2.5$, and $\Sigma = \begin{pmatrix} 0.04 & 0.006 \\ 0.006 & 0.01 \end{pmatrix}$.

**Step 1 — Equilibrium returns:**

$$\Pi = 2.5 \begin{pmatrix} 0.04 & 0.006 \\ 0.006 & 0.01 \end{pmatrix} \begin{pmatrix} 0.6 \\ 0.4 \end{pmatrix} = \begin{pmatrix} 0.066 \\ 0.019 \end{pmatrix}$$

The market implies asset 1 earns 6.6% excess return and asset 2 earns 1.9%.

**Step 2 — Add a view:** "Asset 2 will outperform by 3%" with moderate confidence. This tilts the posterior return of asset 2 upward, increasing its optimal weight beyond market cap — but only in proportion to the investor's confidence.

## Remember

Black-Litterman solves the two biggest practical problems with Markowitz optimisation: (1) the optimal weights are wildly sensitive to expected return estimates, and (2) small estimation errors produce extreme long-short positions. By anchoring to market equilibrium and only deviating where the investor has a genuine view, the model produces intuitive, stable allocations. It is the standard framework at institutional asset managers for translating investment convictions into portfolio weights — Goldman Sachs, where Black and Litterman worked, developed it specifically for their global fixed income allocation.
