# Vasicek Bond Price Functions

**Topic:** Fixed Income
**Tags:** Vasicek, bond pricing, A function, B function, ODE solution, yield curve, closed form
**Created:** 2026-06-10
**Author:** Claude Sonnet 4.6

---

## Definition

Under the Vasicek model the zero-coupon bond price takes the exponential-affine form $V = e^{A(\tau) - B(\tau)r}$. The two scalar functions $B(\tau)$ and $A(\tau)$ — each depending only on time to maturity $\tau = T - t$ — are the closed-form solutions to the ODEs derived from the fixed-income pricing PDE. Together they fully characterise the Vasicek yield curve.

## Key Formula

$$B(\tau) = \frac{1}{\gamma}\!\left(1 - e^{-\gamma\tau}\right)$$

$$A(\tau) = \frac{1}{\gamma^2}\!\left(B(\tau) - \tau\right)\!\left(\eta\gamma - \tfrac{1}{2}\beta\right) - \frac{\beta\,B(\tau)^2}{4\gamma}$$

where $\tau = T - t$ is time to maturity, $\gamma$ is mean-reversion speed, $\eta$ is the risk-neutral long-run level parameter, and $\beta$ is the variance parameter.

The **yield to maturity** is linear in $r$:

$$Y(r,\tau) = \frac{rB(\tau) - A(\tau)}{\tau}$$

| Limit | $B(\tau)$ behaviour | Interpretation |
|---|---|---|
| $\tau \to 0$ | $B \to \tau$ | Short bond: price $\approx 1 - r\tau$ |
| $\tau \to \infty$ | $B \to 1/\gamma$ | Duration saturates at $1/\gamma$ |

## Example

With $\gamma = 0.5$, $\eta = 0.02$, $\beta = 0.0001$ and $r = 4\%$, the 10-year bond ($\tau = 10$):

$B(10) = (1 - e^{-5})/0.5 = 1.987$. The yield is approximately $Y \approx (0.04 \times 1.987 - A)/10$. The saturation of $B$ at $1/\gamma = 2$ means that very long bond yields are insensitive to today's short rate — they are determined almost entirely by the long-run mean and the convexity adjustment captured in $A$.

## Remember

The saturation of $B$ at $1/\gamma$ is the key economic insight: fast mean reversion (large $\gamma$) means short-rate shocks die out quickly and affect long bond prices less, giving a low $B$-saturation level. The $A$ function encodes the risk premium and convexity adjustment that makes long Vasicek yields lower than the long-run mean — this is the convexity bias that pushes yield curves to be concave at long maturities even when the short rate is at its long-run level.
