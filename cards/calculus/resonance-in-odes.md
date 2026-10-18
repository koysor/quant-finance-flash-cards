# Resonance: When the Trial Solution Fails

**Topic:** Calculus
**Tags:** ODE, resonance, particular integral, repeated root, undetermined coefficients
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

When the forcing term is already a solution of the homogeneous equation, the usual trial for the particular integral gives zero and cannot work. Multiply the trial by $x$ until it is no longer part of the complementary function. Physically this is **resonance**: forcing at the system's natural frequency.

## Key Formula

$$\text{trial} \times x^k, \qquad k = \text{multiplicity of that root in the auxiliary equation}$$

Always check first: is the forcing exponent already a root of the auxiliary equation?

## Example

Solve $y'' - 4y' + 4y = e^{2x}$. The auxiliary equation $(m - 2)^2 = 0$ has a **double** root $m = 2$, so $y_c = (A + Bx)\,e^{2x}$. Both $Ce^{2x}$ and $Cxe^{2x}$ already lie in $y_c$ and give zero, so take $y_p = Cx^2 e^{2x}$:

$$y_p'' - 4y_p' + 4y_p = 2Ce^{2x} = e^{2x} \;\Longrightarrow\; C = \tfrac{1}{2}$$

Likewise $y'' + 4y = \cos 2x$ needs $y_p = x\,(D\sin 2x + E\cos 2x)$.

## Remember

Resonance is where the response grows without bound because the input matches the system's own dynamics. In a model, a source whose timescale coincides with the mean-reversion rate produces a response that grows like $x\,e^{kx}$ rather than settling. The check costs five seconds and is skipped constantly, which is where marks are lost.
