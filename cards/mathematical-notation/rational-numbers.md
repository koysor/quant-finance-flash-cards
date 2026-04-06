# Rational Numbers

**Topic:** Mathematical Notation
**Tags:** notation, number sets, fractions, ratios, interest rates, proportions
**Created:** 2026-04-04
**Author:** Claude Opus 4.6

---

## Definition

The **rational numbers**, denoted $\mathbb{Q}$ (from the Latin *quotiens*, meaning "quotient"), are all numbers that can be expressed as a ratio of two integers $\frac{p}{q}$ where $p, q \in \mathbb{Z}$ and $q \neq 0$. They include all integers, fractions, and terminating or repeating decimals.

They sit between the integers and the reals in the standard hierarchy:

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R}$$

## Key Formula

$$\mathbb{Q} = \left\{ \frac{p}{q} \;\middle|\; p \in \mathbb{Z},\; q \in \mathbb{Z},\; q \neq 0 \right\}$$

Key properties:
- $\mathbb{Q}$ is **closed** under addition, subtraction, multiplication, and division (excluding division by zero).
- Every rational number has a decimal expansion that either **terminates** (e.g. $\frac{1}{4} = 0.25$) or **repeats** (e.g. $\frac{1}{3} = 0.333\ldots$).
- Between any two rational numbers there is another rational number — $\mathbb{Q}$ is **dense** in $\mathbb{R}$.

## Example

A bond pays a semi-annual coupon of $\frac{5}{2} = 2.5\%$ per period. The coupon rate $\frac{5}{100}$ and payment fraction $\frac{1}{2}$ are both rational. The day-count fraction for a 90-day period on an Actual/360 basis is:

$$\frac{90}{360} = \frac{1}{4} \in \mathbb{Q}$$

All conventional day-count fractions — Actual/360, Actual/365, 30/360 — produce rational numbers because both numerator and denominator are integers.

## Remember

In quantitative finance, many contractual quantities are naturally rational: coupon rates expressed as fractions, day-count fractions, strike prices quoted in ticks, and notional splits. Computers represent floating-point numbers as ratios of integers (mantissa / $2^{\text{exponent}}$), so all stored values are technically rational — understanding this explains why $0.1 + 0.2 \neq 0.3$ in floating-point arithmetic, a source of subtle pricing errors when accumulating cash flows in bond calculations.
