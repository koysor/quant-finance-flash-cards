# Wishart Affine Term Structure Model

**Topic:** Fixed Income
**Tags:** wishart process, affine model, multi-currency, yield curve, stochastic correlation, matrix-valued
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The Wishart affine term structure model (Gourieroux, 2006) replaces the scalar variance factor of a standard CIR-type affine model with a Wishart matrix process $\Sigma_t$, extending the affine class to matrix-valued diffusions and enabling joint modelling of multiple yield curves with stochastic correlation between them.

## Key Formula

**Wishart state process** ($n \times n$ positive definite):

$$d\Sigma_t = (Q^\top Q + M\Sigma_t + \Sigma_t M^\top)\,dt + \sqrt{\Sigma_t}\,dW_t\,Q + Q^\top dW_t^\top\sqrt{\Sigma_t}$$

**Short rates** (one per currency $k = 1, \ldots, n$):

$$r_t^{(k)} = \delta_0^{(k)} + \delta_1^{(k)\top}\,\text{vech}(\Sigma_t)$$

**Bond price** (exponential-affine in $\Sigma_t$):

$$P^{(k)}(t,T) = \exp\!\bigl(A^{(k)}(\tau) + \text{tr}\!\bigl[B^{(k)}(\tau)\,\Sigma_t\bigr]\bigr)$$

where $A^{(k)}(\tau)$ is a scalar and $B^{(k)}(\tau)$ is an $n\times n$ matrix satisfying a matrix Riccati ODE. The off-diagonal elements of $\Sigma_t$ drive the correlation between the yield curves of different currencies.

## Example

A joint USD–EUR two-factor Wishart model uses a $2 \times 2$ covariance matrix:

$$\Sigma_t = \begin{pmatrix}\sigma_{\text{USD}}^2 & \rho_t\sigma_{\text{USD}}\sigma_{\text{EUR}}\\ \rho_t\sigma_{\text{USD}}\sigma_{\text{EUR}} & \sigma_{\text{EUR}}^2\end{pmatrix}$$

In 2022, USD rate volatility spiked to $\sigma_\text{USD} = 120$ bps/year while EUR volatility rose to $\sigma_\text{EUR} = 90$ bps/year, and the cross-market correlation $\rho_t$ climbed from 0.4 to 0.75 as the ECB and Fed hiked simultaneously. A scalar CIR model for each currency, estimated independently, cannot capture the rising $\rho_t$; the Wishart model prices cross-currency swaptions and differential rate options consistently across both curves.

## Remember

When pricing instruments that depend on both the level and the co-movement of multiple yield curves — cross-currency swaps, quanto caplets, or differential interest rate swaps — the correlation between yield curves is not a constant. The Wishart affine model guarantees the covariance matrix $\Sigma_t$ remains positive definite at all times (the matrix analogue of the Feller condition for CIR), while retaining the exponential-affine pricing formula so bond prices remain analytically tractable across all currencies simultaneously.
