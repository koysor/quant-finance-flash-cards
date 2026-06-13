# Two-Factor Pricing PDE

**Topic:** Fixed Income
**Tags:** two-factor PDE, cross-derivative, interest rate, market price of risk, correlated factors
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

The **two-factor pricing PDE** is the parabolic PDE satisfied by any fixed-income instrument whose price depends on two correlated stochastic state variables $r$ and $l$. Compared to the one-factor PDE, it gains a cross-derivative term $\rho wq\,\partial^2 V/\partial r\,\partial l$ — the "mixed gamma" — and two market-price-of-risk adjustments.

## Key Formula

$$\frac{\partial V}{\partial t} + \tfrac{1}{2}w^2\frac{\partial^2 V}{\partial r^2} + \rho wq\frac{\partial^2 V}{\partial r\,\partial l} + \tfrac{1}{2}q^2\frac{\partial^2 V}{\partial l^2} + (u - \lambda_r w)\frac{\partial V}{\partial r} + (p - \lambda_l q)\frac{\partial V}{\partial l} - rV = 0$$

| Term | Meaning |
|---|---|
| $\tfrac{1}{2}w^2\,\partial^2 V/\partial r^2$ | Gamma in $r$ |
| $\rho wq\,\partial^2 V/\partial r\,\partial l$ | Cross-gamma (only when $\rho \neq 0$) |
| $\tfrac{1}{2}q^2\,\partial^2 V/\partial l^2$ | Gamma in $l$ |
| $(u - \lambda_r w)\,\partial V/\partial r$ | Risk-neutral drift in $r$ |
| $(p - \lambda_l q)\,\partial V/\partial l$ | Risk-neutral drift in $l$ |
| $-rV$ | Discounting |

When $\rho = 0$ (uncorrelated factors), the cross-derivative vanishes and the PDE separates.

## Example

If $\rho = 0.5$, $w = 0.01$, $q = 0.02$, the cross-derivative term contributes $0.5 \times 0.01 \times 0.02 \times \partial^2 V/\partial r\,\partial l = 0.0001\,\partial^2 V/\partial r\,\partial l$. For a 10-year bond with correlated short and long rates, this term can account for 5–15% of the total PDE residual at intermediate maturities — omitting it produces systematically mispriced curve derivatives.

## Remember

The cross-derivative $\rho wq\,\partial^2 V/\partial r\,\partial l$ is the most commonly forgotten term in two-factor models. It arises directly from Itô's lemma applied to $V(r,l,t)$ when $r$ and $l$ are correlated: $d(r\cdot l)$ contains a $\rho wq\,dt$ term. Financially, it captures how a joint move in both $r$ and $l$ affects the bond price beyond the separate effects. Any product that is sensitive to the co-movement of two rates — spread options, quanto CMS, CMS steepeners — is priced mainly through this cross-derivative.
