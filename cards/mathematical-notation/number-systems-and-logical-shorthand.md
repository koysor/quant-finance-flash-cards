# Number Systems and Logical Shorthand

**Topic:** Mathematical Notation
**Tags:** number systems, naturals, integers, rationals, reals, quantifiers, intervals
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

The number systems form a nested chain, each contained in the next, and a small set of logical symbols is used to state facts about them precisely.

## Key Formula

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$$

| Symbol | Meaning |
|---|---|
| $\mathbb{N}$ | Natural numbers $0, 1, 2, \dots$ (some texts start at 1) |
| $\mathbb{Z}$ | Integers, positive and negative |
| $\mathbb{Q}$ | Rationals $p/q$ with $p, q \in \mathbb{Z}$, $q \neq 0$ |
| $\mathbb{R}$ | Reals: rationals together with irrationals such as $\sqrt{2}$, $\pi$, $e$ |
| $\mathbb{C}$ | Complex numbers $x + iy$ with $i = \sqrt{-1}$ |

| Symbol | Reads as | Symbol | Reads as |
|---|---|---|---|
| $\forall$ | for all | $\exists$ | there exists |
| $\in$ | is an element of | $\iff$ | if and only if |
| $\Rightarrow$ | implies | s.t. | such that |

Intervals: $(a, b)$ excludes the endpoints, $[a, b]$ includes them, and $\infty$ always takes a round bracket.

## Example

"$\forall x \in \mathbb{R},\; x^2 \geq 0$" is true. "$\exists x \in \mathbb{R}$ s.t. $x^2 = 2$" is true, but "$\exists x \in \mathbb{Q}$ s.t. $x^2 = 2$" is false because $\sqrt{2}$ is irrational. The interval $[0, \infty)$ contains zero; $(0, \infty)$ does not.

## Remember

A share price lives in $(0, \infty)$, never $\mathbb{R}$, which is why models use geometric rather than arithmetic Brownian motion. Share counts are in $\mathbb{N}$ or $\mathbb{Z}$ (negative when short). No-arbitrage is stated in exactly this shorthand: for every zero-cost portfolio, if the payoff is non-negative almost surely then it is zero almost surely.
