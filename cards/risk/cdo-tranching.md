# CDO Tranching

**Topic:** Risk
**Tags:** CDO, structured products, tranching, credit correlation, waterfall, first loss, attachment point
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A Collateralised Debt Obligation (CDO) repackages a pool of credit assets into tranches with different seniority; losses flow first to the equity (first-loss) tranche, then mezzanine, then senior, protecting senior investors at the cost of leveraged junior exposure.

## Key Formula

Let $L$ = pool loss rate. Tranche $[A, B]$ loss:

$$\ell(L) = \frac{\max(0,\;\min(L - A,\; B - A))}{B - A}$$

Expected tranche loss (using risk-neutral distribution $F$ of $L$):

$$\mathbb{E}[\ell] = \frac{1}{B - A}\int_A^B [1 - F(l)]\,dl$$

Tranche spread $\approx \mathbb{E}[\ell] / \text{tranche duration}$.

## Example

Pool: 100 equally-weighted BBB bonds, each PD $= 2\%$, $R = 40\%$, correlation $\rho = 0.3$ (Gaussian copula). Equity $[0\%, 3\%]$: high expected loss $\approx 30\%$, absorbs first defaults. Senior $[10\%, 30\%]$: expected loss $\approx 0.05\%$ — near risk-free even with many defaults, unless correlation spikes.

## Remember

CDO equity is extremely sensitive to default correlation — at high $\rho$, either no names default (senior safe) or many default together (equity wiped out). The 2008 crisis arose partly because rating agency models severely underestimated stress-period correlation: senior tranches rated AAA were in practice much riskier than advertised, and the convexity of loss distributions amplified mistakes.
