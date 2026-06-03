# Yield Curve Control

**Topic:** Fixed Income
**Tags:** yield curve control, ycc, bond yield peg, bank of japan, monetary policy, term premium
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

Yield Curve Control (YCC) is a monetary policy framework in which a central bank commits to purchasing unlimited quantities of government bonds to keep yields at or below a specified target at a chosen maturity, directly pegging a point on the yield curve rather than merely influencing it.

## Key Formula

Under YCC, the central bank sets a target yield $y^*(T)$ and intervenes whenever the market exceeds it:

$$\text{Purchase quantity} = \begin{cases} \infty & \text{if } y_t(T) > y^*(T) \\ 0 & \text{if } y_t(T) \leq y^*(T) \end{cases}$$

The peg forces the term premium to absorb the residual between expected short rates and the target:

$$tp_t(T) = y^*(T) - \frac{1}{T}\sum_{k=0}^{T-1}\mathbb{E}_t[r_{t+k}]$$

When expected short rates rise without a corresponding increase in $y^*$, the central bank must buy more bonds to compress the term premium further, expanding its balance sheet endogenously.

## Example

Bank of Japan YCC from September 2016: 10-year JGB yield pegged at 0% (later ±0.25%, then ±0.5%). With expected short rates at -0.1%, the implied term premium was pinned at +0.1% — roughly 40bp below its natural level. When the BoJ widened the target band to ±1.0% in July 2023, the 10-year yield immediately rose to 0.9% and the BoJ purchased ¥5 trillion of JGBs in a single week to defend the new ceiling, illustrating how the balance sheet expands to enforce the peg.

## Remember

YCC is the most direct form of term premium suppression: unlike QE, which reduces the term premium as a side effect of asset purchases, YCC explicitly prices the long bond and forces the term premium to whatever residual achieves the target. Exiting YCC is one of the most challenging monetary policy operations because the artificially compressed term premium can snap back violently — global bond funds that used the BoJ peg as a carry trade (short JGBs, long foreign bonds) faced sudden large losses when the band was widened, illustrating how YCC creates a one-sided market that unwinds discontinuously.
