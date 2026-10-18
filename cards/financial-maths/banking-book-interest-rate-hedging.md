# Hedging Interest Rate Risk in the Banking Book

**Topic:** Financial Mathematics
**Tags:** hedging, interest rate swap, DV01, duration matching, banking book, fixed-rate loans
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

Banks hedge interest rate risk in the banking book mainly with **interest rate swaps**. A bank holding fixed-rate loans funded with floating-rate deposits pays fixed and receives floating on a swap, so the swap gains when rates rise and offsets the loss of economic value on the loans. The hedge notional is set by matching the interest rate sensitivities (DV01) of the hedged item and the swap.

## Key Formula

$$N_{\text{swap}} = \frac{\text{DV01}_{\text{hedged item}}}{\text{DV01 per unit notional of the swap}} \approx N_{\text{item}} \times \frac{D_{\text{item}}}{D_{\text{swap}}}$$

where $D$ is modified duration. The residual risk is the portion not matched: differences in tenor, reference rate and prepayment behaviour.

## Example

A bank holds £5bn of five-year fixed-rate loans with modified duration $D_{\text{item}} = 4.4$. A five-year pay-fixed swap has a fixed-leg duration $D_{\text{swap}} = 4.5$:

$$N_{\text{swap}} \approx 5\text{bn} \times \frac{4.4}{4.5} \approx £4.9\text{bn}$$

A 100 bp rise lowers the loans' value by about $5\text{bn} \times 4.4 \times 1\% = £220\text{m}$, while the swap gains about the same.

## Remember

The hedge is never perfect. Mortgages can be prepaid, so the true duration of the loans shrinks when rates fall, leaving the bank over-hedged just when the swap has lost value. The floating leg of the swap (an overnight index) differs from the rates on the loans and deposits, leaving basis risk. Hedges are therefore reviewed regularly and their effect on both EVE and NII is monitored, and accounting treatment decides whether the swap's value changes create profit-and-loss volatility.
