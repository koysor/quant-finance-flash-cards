# Feller Condition

**Topic:** Fixed Income
**Tags:** Feller condition, CIR model, positivity, square-root diffusion, parameter constraint, boundary behaviour
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

The Feller condition is the parameter inequality $2\kappa\theta \ge \sigma^2$ that guarantees the CIR short-rate process $dr = \kappa(\theta - r)\,dt + \sigma\sqrt{r}\,dW$ never reaches zero — the boundary is inaccessible and rates stay strictly positive.

## Key Formula

$$2\kappa\theta \ge \sigma^2 \quad \Longleftrightarrow \quad \text{zero is inaccessible (reflecting boundary)}$$

$$2\kappa\theta < \sigma^2 \quad \Longleftrightarrow \quad \text{zero is accessible and reflecting}$$

Feller boundary classification for $dr = \kappa(\theta - r)\,dt + \sigma\sqrt{r}\,dW$:

| $2\kappa\theta$ vs $\sigma^2$ | Behaviour at $r = 0$ |
|---|---|
| $\ge \sigma^2$ | Process reflects immediately; zero never reached |
| $< \sigma^2$ | Process touches zero and reflects; brief zero crossings possible |
| $= \sigma^2$ | Boundary case; just barely inaccessible |

## Example

$\kappa = 0.5$, $\theta = 4\%$, $\sigma = 10\%$. Check: $2 \times 0.5 \times 0.04 = 0.04$ vs $\sigma^2 = 0.01$. Since $0.04 \ge 0.01$, the Feller condition holds and rates remain positive. If instead $\sigma = 30\%$: $\sigma^2 = 0.09 > 0.04$ — condition fails and the rate can hit zero.

## Remember

The Feller condition is routinely violated when the CIR model is calibrated to low-rate environments — e.g. post-2008, when central banks compressed $\theta$ toward zero while market vol $\sigma$ remained elevated. A violated Feller condition does not make the model useless (rates simply reflect at zero), but it does mean the model can produce zero or near-zero rates with positive probability, which can cause numerical issues in discount factor calculations and invalidate some analytical approximations.
