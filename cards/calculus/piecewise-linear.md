# Piecewise Linear

**Topic:** Calculus
**Tags:** piecewise linear, kink, linear interpolation, option payoff, relu, breakpoint
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

A **piecewise linear** function is one that is linear on each interval of its domain, but may have a different slope on adjacent intervals. The function is continuous but not smooth — it has sharp **kinks** at the breakpoints where one linear segment meets the next.

## Key Formula

$$f(x) = a_i x + b_i \quad \text{for } x_{i-1} \leq x < x_i, \quad i = 1, 2, \ldots, n$$

where each piece has its own slope $a_i$ and intercept $b_i$, and the pieces join continuously at the breakpoints $x_1, \ldots, x_{n-1}$.

The classic two-piece form appears everywhere in derivatives:

$$f(x) = \begin{cases} 0 & x < K \\ x - K & x \geq K \end{cases} = \max(x - K,\, 0)$$

At each breakpoint the left- and right-hand derivatives differ, so $f$ is **non-differentiable** there.

## Example

A bull spread with strikes $K_1 = 90$ and $K_2 = 110$ has three linear pieces:

$$V(S_T) = \begin{cases} 0 & S_T < 90 \\ S_T - 90 & 90 \leq S_T < 110 \\ 20 & S_T \geq 110 \end{cases}$$

The slope is 0 below \$90, then 1 between the strikes, then 0 above \$110. The delta jumps from 0 to 1 at $S_T = 90$ and from 1 to 0 at $S_T = 110$ — two kinks where the derivative is undefined.

## Remember

Every vanilla option payoff at expiry is piecewise linear: zero slope below the strike, unit slope above it. This single kink at $K$ means the payoff cannot be differentiated at $S_T = K$, which is why Black–Scholes solves the PDE in the smooth region and applies the payoff as a **boundary condition**. The same shape — two linear pieces joined at a threshold — reappears as the ReLU activation function in neural networks, making piecewise linear the structural link between options pricing and modern deep learning.
