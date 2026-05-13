# Difference Equations

**Topic:** Calculus
**Tags:** recurrence relation, discrete-time, amortisation, bond pricing, compounding
**Created:** 2026-04-22
**Author:** Claude Sonnet 4.6

---

## Definition

A **difference equation** (or recurrence relation) is an equation that expresses the value of a sequence at step $n$ in terms of one or more earlier values. It is the discrete-time analogue of a differential equation: where a differential equation describes continuous change via derivatives, a difference equation describes stepwise change between successive periods.

## Key Formula

**First-order linear difference equation** (general form):

$$y_{n+1} = a\,y_n + b$$

with solution:

$$y_n = A\,a^n + \frac{b}{1 - a}, \quad a \neq 1$$

where $A = y_0 - \dfrac{b}{1-a}$ is determined by the initial condition.

**Second-order linear difference equation** (general form):

$$y_{n+2} + p\,y_{n+1} + q\,y_n = f_n$$

Solved via the characteristic equation $r^2 + pr + q = 0$; roots $r_1, r_2$ give the homogeneous solution $y_n^{(h)} = C_1 r_1^n + C_2 r_2^n$ (distinct real roots).

## Example

A borrower takes a mortgage of £200,000 at a monthly interest rate of $r = 0.5\%$ and makes fixed monthly payments of $P = £1{,}200$. The outstanding balance $B_n$ after $n$ months satisfies:

$$B_{n+1} = (1 + r)\,B_n - P = 1.005\,B_n - 1{,}200$$

This is a first-order difference equation with $a = 1.005$ and $b = -1{,}200$. The fixed point (equilibrium) is $B^* = \dfrac{1{,}200}{0.005} = £240{,}000$. The general solution is:

$$B_n = \left(200{,}000 - 240{,}000\right)(1.005)^n + 240{,}000 = 240{,}000 - 40{,}000 \times (1.005)^n$$

Since $a = 1.005 > 1$ and $B_0 < B^*$, the balance declines to zero over time (the loan is repaid) provided payments exceed the interest accruing each period.

## Remember

Difference equations are the natural language of discrete-time finance. The mortgage amortisation formula, the bond pricing recursion (pricing backward from maturity through coupon dates), and the binomial option pricing tree (backward induction step $V_n = \frac{1}{1+r}[p'\,V_{n+1}^+ + (1-p')\,V_{n+1}^-]$) are all first-order difference equations. Recognising the structure $y_{n+1} = a\,y_n + b$ immediately reveals whether the sequence converges ($|a| < 1$), explodes ($|a| > 1$), or oscillates ($a < 0$) — a quick stability check that tells you whether a discrete-time model is well-behaved before you run a single simulation.
