# Corollary

**Topic:** Calculus
**Tags:** corollary, proof, theorem, lemma, mathematical reasoning
**Created:** 2026-11-27
**Author:** Claude Opus 5.5

---

## Definition

A **corollary** is a result that follows directly from a theorem (or lemma) that has already been proved, usually with only a line or two of extra reasoning. A lemma comes *before* a main result as a stepping stone; a corollary comes *after* it as an immediate consequence.

## Key Formula

If a theorem establishes $P \Rightarrow Q$, and $Q$ quickly implies $R$, then the corollary is

$$P \Rightarrow Q \Rightarrow R \quad\text{so}\quad P \Rightarrow R$$

The work lies in proving $P \Rightarrow Q$; the corollary only needs the short step $Q \Rightarrow R$.

## Example

**Result:** if $X_1, \dots, X_n$ are independent with equal variance $\sigma^2$, then

$$\operatorname{Var}(X_1 + \dots + X_n) = n\sigma^2$$

**Corollary:** taking square roots, the standard deviation of the sum is $\sigma\sqrt{n}$.

With daily return volatility $\sigma = 1.2\%$ and $n = 252$ trading days:

$$\sigma_{\text{annual}} = 1.2\% \times \sqrt{252} = 1.2\% \times 15.87 \approx 19.0\%$$

The one-line corollary, not the variance result itself, is the formula traders use every day.

## Remember

Many working rules in quantitative finance are corollaries of a bigger result. The square-root rule for scaling volatility and VaR follows from variance additivity. Put-call parity, $C - P = S_0 - Ke^{-rT}$, has the corollary that a call and a put struck at the forward price $K = S_0e^{rT}$ have equal value. With $S_0 = 100$, $r = 5\%$ and $T = 1$, the forward is $105.13$, so the call and put at that strike cost the same. This is why FX desks quote at-the-money-forward straddles and risk reversals. A corollary inherits every assumption of its parent theorem, so the square-root rule fails when returns are autocorrelated, and the equal-price corollary fails when parity breaks (for example, with dividends left out of the model).
