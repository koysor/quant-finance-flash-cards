# Dai–Singleton Classification

**Topic:** Fixed Income
**Tags:** Dai-Singleton, affine classification, Am(n), square-root factors, Gaussian factors, admissibility
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The Dai–Singleton (2000) classification organises all $n$-factor affine term structure models into families $A_m(n)$, where $m$ is the number of square-root (CIR-type) factors and $n - m$ is the number of Gaussian (Vasicek-type) factors; it identifies exactly which models are admissible and what yield-curve shapes each sub-family can generate.

## Key Formula

$$A_m(n): \quad m \text{ CIR factors},\; (n-m) \text{ Gaussian factors}, \quad 0 \le m \le n$$

State vector $X_t \in \mathbb{R}^n$, canonical form under risk-neutral measure:

$$dX_t = \kappa(\theta - X_t)\,dt + \Sigma\,\text{diag}\!\bigl(\sqrt{\alpha_i + \beta_i^\top X_t}\bigr)\,dW_t$$

where $\alpha_i + \beta_i^\top X_t \ge 0$ are the affine variance functions. The $m$ factors with $\beta_i \ne 0$ are the square-root factors; the remaining $n - m$ have $\beta_i = 0$ (Gaussian).

| Family | Description | Canonical member |
|---|---|---|
| $A_0(1)$ | 1 Gaussian | Vasicek |
| $A_1(1)$ | 1 CIR | CIR |
| $A_0(2)$ | 2 Gaussian | G2++ |
| $A_1(2)$ | 1 CIR + 1 Gaussian | Fong–Vasicek type |
| $A_2(2)$ | 2 CIR | Longstaff–Schwartz |

## Example

The Longstaff–Schwartz model is $A_2(2)$: both factors are square-root, so stochastic variance is driven by the state itself. The G2++ model is $A_0(2)$: both factors are Gaussian, giving Gaussian yield distributions and easy swaption pricing. An $A_1(3)$ model has one CIR factor controlling conditional variance and two Gaussian level/slope factors — this class is popular for capturing volatility smiles in caps.

## Remember

Dai–Singleton proved that not all combinations of $m$ and $n$ produce valid (admissible) models — the parameter constraints required to keep variances non-negative can be mutually inconsistent. Their paper resolved years of confusion about which multi-factor models were internally consistent. In practice, the classification tells practitioners that increasing $m$ captures more stochastic volatility but reduces analytical tractability, while reducing $m$ toward $A_0(n)$ restores Gaussian tractability at the cost of deterministic conditional variance.
