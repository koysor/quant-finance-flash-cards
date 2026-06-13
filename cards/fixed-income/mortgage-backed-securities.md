# Mortgage-Backed Securities

**Topic:** Fixed Income
**Tags:** MBS, mortgage-backed securities, pass-through, securitisation, negative convexity, agency MBS
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A mortgage-backed security (MBS) is a bond backed by a pool of residential mortgage loans; investors receive monthly cash flows of scheduled interest, scheduled amortisation, and prepayments pro-rata to their pool share.

## Key Formula

Monthly mortgage payment (level-pay):

$$\text{PMT} = \frac{P \cdot r_m}{1 - (1 + r_m)^{-N}}$$

where $P$ = remaining balance, $r_m$ = monthly interest rate, $N$ = remaining months.

Pass-through price:

$$P_{\text{MBS}} = \sum_{t=1}^{N} \frac{CF_t}{(1 + y/12)^t}$$

where $CF_t = $ scheduled P+I $+$ prepayment at month $t$ (dependent on prepayment model).

## Example

\$100m pool of 30yr $6\%$ mortgages, 200% PSA. Monthly payment on \$100m $= \$599{,}551$. As rates fall to $4\%$, CPR accelerates to $25\%$+: investors receive principal early at par and must reinvest at lower rates — duration shortens when it should lengthen for a price-rally beneficiary.

## Remember

MBS exhibit negative convexity: when rates fall, prepayments accelerate and duration shortens (investors get their money back early); when rates rise, prepayments slow and duration extends. This asymmetry means the MBS price–yield curve bends the wrong way versus plain vanilla bonds — hedging requires constant rebalancing as rates move, creating path dependence.
