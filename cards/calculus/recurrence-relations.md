# Recurrence Relations

**Topic:** Calculus
**Tags:** recurrence relation, sequence, iterative, recursive, convergence, fixed point
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

A **recurrence relation** (or difference equation) defines each term of a sequence in terms of one or more previous terms: $u_{n+1} = f(u_n)$ (first-order) or $u_{n+1} = f(u_n, u_{n-1})$ (second-order). Given an **initial condition** $u_1 = a$, the relation generates the complete sequence. A **fixed point** $L$ satisfies $L = f(L)$ — the sequence converges to $L$ if $|f'(L)| < 1$.

## Key Formula

**First-order linear recurrence** $u_{n+1} = au_n + b$:

$$u_n = a^n u_1 + b \cdot \frac{a^n - 1}{a - 1} \quad (a \neq 1), \qquad u_n = u_1 + (n-1)b \quad (a = 1)$$

**Special cases:**
- $b = 0$: geometric sequence $u_n = u_1 \cdot a^{n-1}$
- $a = 1$: arithmetic sequence $u_n = u_1 + (n-1)b$

**Fixed point** of $u_{n+1} = f(u_n)$: solve $L = f(L)$.

**Convergence condition:** $|f'(L)| < 1$ at the fixed point $L$.

## Example

Compound interest: $u_{n+1} = 1.05\,u_n$, $u_1 = 1000$.

$$u_n = 1000 \times 1.05^{n-1}$$

After 10 years: $u_{10} = 1000 \times 1.05^9 \approx £1551$.

**Iterative root-finding:** $u_{n+1} = \frac{1}{2}\!\left(u_n + \frac{2}{u_n}\right)$ converges to $\sqrt{2}$ from $u_1 = 1$:

$u_2 = 1.5$, $u_3 = 1.4167$, $u_4 = 1.4142$ — converges rapidly (Newton-Raphson).

## Remember

Recurrence relations are the discrete-time foundation of **financial modelling**. The **binomial option pricing tree** is a recurrence: $V_n = e^{-r\Delta t}(p\,V_{n+1}^u + (1-p)\,V_{n+1}^d)$, solved backwards from expiry. GARCH is a recurrence relation: $\sigma^2_{t+1} = \omega + \alpha \varepsilon_t^2 + \beta \sigma_t^2$ — the conditional variance evolves via a first-order difference equation. The fixed-point condition $|f'(L)| < 1$ corresponds to the **mean-reversion** requirement in GARCH: $\alpha + \beta < 1$ ensures variance reverts to the long-run mean $\omega/(1-\alpha-\beta)$ rather than exploding.
