# Identification of Affine Term Structure Models

**Topic:** Fixed Income
**Tags:** identification, normalisation, dai-singleton, observational equivalence, canonical form, affine model
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

Affine term structure models are not uniquely identified because any invertible linear transformation $\tilde{X}_t = AX_t$ of the state vector produces an observationally equivalent model with different parameters but identical bond prices; the identification problem is resolved by imposing a **canonical form** — a minimal set of restrictions that selects exactly one representative from each equivalence class.

## Key Formula

**Observational equivalence:** for any invertible $A \in \mathbb{R}^{N \times N}$, define $\tilde{X}_t = AX_t$. Then:

$$\tilde{K}_0 = AK_0, \quad \tilde{K}_1 = AK_1 A^{-1}, \quad \tilde{\Sigma} = A\Sigma, \quad \tilde{\delta}_1 = (A^{-\top})\delta_1$$

Bond prices are unchanged: $A(\tau)$ is invariant, $\tilde{B}(\tau) = (A^{-\top})B(\tau)$.

**Counting restrictions (Dai–Singleton canonical form):**

For an $A_m(n)$ model with $n$ factors, the unconstrained parameter space has $\mathcal{O}(n^2)$ redundant degrees of freedom. The canonical form removes them by fixing:
- $\kappa$ to triangular form
- $\theta$ to a specific vector
- Specific elements of $\delta_1$ and $\Sigma$ to $0$ or $1$

The number of free parameters after normalisation is $\frac{1}{2}n(n+7) + m(n-m) + $ lower-order terms.

## Example

Consider a two-factor $A_0(2)$ (Gaussian) model. The state dynamics under $\mathbb{Q}$ are:

$$dX_t = K(\theta - X_t)\,dt + \Sigma\,dW_t^{\mathbb{Q}}$$

Without restrictions, $K, \Sigma \in \mathbb{R}^{2\times2}$ — 8 parameters. But rotating $X_t \to AX_t$ with any invertible $A$ gives the same yields. The canonical form fixes $\Sigma = I_2$ (identity) and $K$ lower-triangular, reducing 8 to 5 free parameters. Without this: two researchers could fit the same bond prices and report completely different "$\kappa$" and "$\sigma$" values — both correct, neither comparable.

## Remember

The identification problem matters acutely when comparing estimated parameters across studies or calibrating the risk premium $\lambda_t$. A model estimated in one rotation cannot be directly compared with the same model estimated in another — the term premia could look very different numerically while describing identical market dynamics. Central banks and hedge funds imposing their own "intuitive" parametrisations (e.g., naming factors "level," "slope," "curvature") are implicitly making a normalisation choice; the Dai–Singleton canonical form is the theoretically rigorous version of that choice.
