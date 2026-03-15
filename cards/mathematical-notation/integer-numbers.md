# Integer Numbers

**Topic:** Mathematical Notation
**Tags:** notation, number sets, integers, signed numbers, counting
**Author:** Claude Sonnet 4.6

---

## Definition

The **integers**, denoted $\mathbb{Z}$ (from the German *Zahlen*, meaning "numbers"), are the set of all whole numbers together with their negatives and zero:

$$\mathbb{Z} = \{\ldots,\, -3,\, -2,\, -1,\, 0,\, 1,\, 2,\, 3,\, \ldots\}$$

They sit between the natural numbers and the rationals in the standard number-set hierarchy:

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$$

Key properties:
- $\mathbb{Z}$ is **closed** under addition, subtraction, and multiplication, but not division (e.g. $1 \div 2 \notin \mathbb{Z}$).
- Every natural number is an integer: $\mathbb{N} \subset \mathbb{Z}$.
- The set $\mathbb{Z}^+ = \{1, 2, 3, \ldots\}$ coincides with $\mathbb{N}$ (positive integers); $\mathbb{Z}^- = \{-1, -2, -3, \ldots\}$ are the negative integers.

## Key Formula

**Signed position indicator** (long/short):

$$\delta \in \{+1, -1\} \subset \mathbb{Z}$$

**Coupon period count** — a bond paying $n$ coupons requires $n \in \mathbb{Z}^+$:

$$P = \sum_{k=1}^{n} \frac{C}{(1+r)^k} + \frac{F}{(1+r)^n}, \quad n \in \mathbb{Z}^+$$

**Integer part (floor function)**, used in accrued-interest calculations:

$$\lfloor x \rfloor = \max\{n \in \mathbb{Z} : n \leq x\}$$

## Example

A trader holds three positions: long 2 contracts of a future, flat on a swap, and short 1 bond.

$$\delta_{\text{future}} = +2,\quad \delta_{\text{swap}} = 0,\quad \delta_{\text{bond}} = -1$$

All three quantities are drawn from $\mathbb{Z}$ — positive integers denote long exposure, zero denotes no position, and negative integers denote short exposure. Fractional positions ($\delta = 0.5$) are not permitted in standardised contracts, so the domain is explicitly $\mathbb{Z}$, not $\mathbb{R}$.

## Remember

Integers appear in quantitative finance wherever quantities must be **whole and signed**: contract sizes, coupon periods, tree time-steps, and long/short indicators. The sign convention $\delta \in \{+1, -1\}$ is a concise way to write parity-symmetric payoffs — for example, a straddle payoff can be written $\delta \cdot (S_T - K)^+$ with $\delta = +1$ for a call and $\delta = -1$ for a put. Recognising when a variable is constrained to $\mathbb{Z}$ rather than $\mathbb{R}$ prevents specification errors in discrete-time models and accrual calculations.
