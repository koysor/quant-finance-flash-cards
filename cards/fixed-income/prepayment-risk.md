# Prepayment Risk

**Topic:** Fixed Income
**Tags:** prepayment, CPR, SMM, PSA model, MBS, option-adjusted spread, negative convexity
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

Prepayment risk is the uncertainty that mortgage borrowers will repay principal ahead of schedule — typically by refinancing when rates fall — shortening the MBS investor's cash-flow horizon and forcing reinvestment at lower yields.

## Key Formula

**Conditional Prepayment Rate (CPR):** annualised fraction of pool that prepays.

**Single Monthly Mortality (SMM):** $\text{SMM} = 1 - (1 - \text{CPR})^{1/12}$

**PSA benchmark:**

$$\text{CPR}(m) = \begin{cases} 6\% \times \dfrac{m}{30} & m \le 30 \\ 6\% & m > 30 \end{cases} \quad \text{(100% PSA)}$$

$k\%$ PSA means CPR $= k/100$ times the PSA benchmark.

**Option-adjusted spread (OAS):** yield spread over the swap curve after removing embedded prepayment optionality.

## Example

200% PSA, month 15: CPR $= 2 \times 6\% \times 15/30 = 6\%$. SMM $= 1 - 0.94^{1/12} = 0.515\%$ of remaining balance prepays each month. On a \$100m pool, approximately \$515,000 of principal returns to investors in that month alone.

## Remember

OAS strips out the value of the borrower's prepayment option (a call on the mortgage they effectively own) from the raw yield spread, leaving the pure credit and liquidity premium. A negative OAS means the MBS is overpriced for its embedded optionality. The PSA model is a convention, not a prediction — actual prepayments depend on refinancing incentives, seasoning, burnout, and housing market conditions.
