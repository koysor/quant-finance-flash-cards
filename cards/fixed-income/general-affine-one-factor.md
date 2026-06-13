# General Affine One-Factor Model

**Topic:** Fixed Income
**Tags:** affine model, one-factor, short rate, Riccati ODE, Vasicek, CIR, tractability
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **general affine one-factor model** is the most general one-factor short-rate model for which the zero-coupon bond price has the exponential-affine form $V = e^{A(t) - rB(t)}$. This requires the risk-neutral drift to be **linear** in $r$ and the squared diffusion to be **affine** in $r$; Vasicek and CIR are the two canonical special cases.

## Key Formula

The conditions for exponential-affine bond prices are:

$$u(r,t) - \lambda(r,t)\,w(r,t) = \eta(t) - \gamma(t)\,r \quad \text{(linear in }r\text{)}$$

$$w(r,t)^2 = \alpha(t)\,r + \beta(t) \quad \text{(affine in }r\text{)}$$

Substituting $V = e^{A - rB}$ into the PDE gives two scalar Riccati ODEs:

$$\dot{B} = \tfrac{1}{2}\alpha(t)\,B^2 + \gamma(t)\,B - 1, \quad B(T) = 0$$

$$\dot{A} = \eta(t)\,B - \tfrac{1}{2}\beta(t)\,B^2, \quad A(T) = 0$$

| Model | $\alpha(t)$ | $\beta(t)$ | $\gamma(t)$, $\eta(t)$ |
|---|---|---|---|
| Vasicek | 0 | constant | constant |
| CIR | constant | 0 | constant |
| Hull–White (Vasicek) | 0 | $\beta(t)$ | time-dependent |
| Hull–White (CIR) | $\alpha(t)$ | 0 | time-dependent |

## Example

If both $\alpha > 0$ and $\beta > 0$, the model interpolates between Vasicek (when $r$ is large, $\alpha r \gg \beta$ so CIR-like) and Gaussian (when $r$ is near zero, $\beta$ dominates). The rate has a natural lower bound of $-\beta/\alpha$ since the diffusion must remain real ($w^2 \geq 0$).

## Remember

The affine one-factor class achieves analytical tractability at the cost of restricting the functional forms of drift and volatility. The Riccati ODE for $B$ has a closed-form solution only for constant parameters (Vasicek and CIR); Hull–White's time-dependent parameters require numerical ODE integration. Any model outside this affine class — e.g. a cubic drift — cannot produce exponential-affine bond prices and must be solved numerically throughout.
