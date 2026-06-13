# Longstaff–Schwartz Interest Rate Model

**Topic:** Fixed Income
**Tags:** Longstaff-Schwartz, two CIR factors, short rate, non-negative rates, affine, closed form
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The Longstaff–Schwartz (1992) interest rate model expresses the short rate as a linear combination $r = cx + dy$ of two independent CIR (square-root) processes $x$ and $y$, inheriting non-negativity from the CIR factors while retaining closed-form bond prices.

## Key Formula

$$dx = a(\bar{x} - x)\,dt + \sqrt{x}\,dW_1, \qquad dy = b(\bar{y} - y)\,dt + \sqrt{y}\,dW_2$$

$$r = c\,x + d\,y, \qquad \mathbb{E}[dW_1\,dW_2] = 0$$

Bond price: $P(x, y, t) = e^{A(t) - B(t)x - C(t)y}$, where the three ODEs decouple into two independent CIR Riccati equations (for $B$ and $C$) plus quadrature for $A$ — all solvable analytically.

Yield: $y(\tau) = -A/\tau + Bx/\tau + Cy/\tau$ (affine in the latent factors $x, y$).

## Example

$a = 0.4$, $\bar{x} = 0.02$, $b = 0.06$, $\bar{y} = 0.02$, $c = d = 1$. The fast factor $x$ (half-life $\ln 2 / 0.4 \approx 1.7$ yr) drives short-end dynamics; the slow factor $y$ (half-life $\approx 11.6$ yr) drives long-end dynamics. This separation allows the model to capture slope changes without correlated factors.

## Remember

The Longstaff–Schwartz (1992) interest rate model is entirely distinct from the Longstaff–Schwartz (2001) Least-Squares Monte Carlo method for American options — both bear the same authors' names but are different contributions from the same pair a decade apart. The key feature of the IR model is that each CIR factor is independently non-negative, ensuring $r = cx + dy \ge 0$; the model predates the G2++ framework but trades its analytical elegance for the constraint that factors must be independent and unobservable.
