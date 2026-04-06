# Definition and Assignment Notation

**Topic:** Mathematical Notation
**Tags:** notation, definition, assignment, equivalence, colon-equals, triangleq
**Created:** 2026-04-04
**Author:** Claude Sonnet 4.6

---

## Definition

Several symbols are used to introduce new quantities by **defining** them, rather than asserting that two already-known things are equal. Distinguishing these from the ordinary equals sign prevents ambiguity.

| Symbol | Read as | Meaning |
|---|---|---|
| $:=$ | "is defined as" | Left side is being introduced by the right side |
| $\triangleq$ or $\overset{\text{def}}{=}$ | "equals by definition" | Same as $:=$, often more formal |
| $\equiv$ | "is identically equal to" | True for all values of free variables (not just a specific case) |
| $\overset{!}{=}$ | "must equal" | Condition being imposed (e.g., in a constraint) |
| $\approx$ | "approximately equals" | Numerical approximation |
| $\sim$ | "is distributed as" | $X \sim N(0,1)$ — $X$ follows the standard normal |

## Key Formula

**Defining the Sharpe ratio:**

$$S := \frac{E[R_p] - r_f}{\sigma_p}$$

**Defining log-return:**

$$r_t := \ln S_t - \ln S_{t-1} \equiv \ln\!\left(\frac{S_t}{S_{t-1}}\right)$$

**Identity (true for all $x$):**

$$e^{\ln x} \equiv x, \quad x > 0$$

**Constraint in optimisation:**

$$\sum_{i=1}^n w_i \overset{!}{=} 1$$

## Example

When deriving the Black-Scholes equation, one writes:

$$d_1 := \frac{\ln(S/K) + (r + \tfrac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}, \qquad d_2 := d_1 - \sigma\sqrt{T}$$

The $:=$ signals that $d_1$ and $d_2$ are **new notation** being introduced, not equalities to be proved. Using $=$ here would suggest these are non-trivial equalities requiring justification. Similarly, $r_t \equiv \ln(S_t/S_{t-1})$ signals this is true for all $t$, not just a specific period.

## Remember

The colon-equals $:=$ is one of the most important notational habits in rigorous quantitative work. When writing $V = e^{-rT}E^{\mathbb{Q}}[(S_T - K)^+]$, the equals sign asserts that the option price happens to equal this expectation — a non-trivial result requiring a proof (the risk-neutral pricing theorem). By contrast, $V_T := (S_T - K)^+$ introduces the payoff function by definition — no proof needed. Using $=$ for both definitions and proven equalities muddies where the real mathematical content lies.
