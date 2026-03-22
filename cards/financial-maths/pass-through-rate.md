# Pass-Through Rate

**Topic:** Financial Mathematics
**Tags:** pass-through rate, NMD, deposits, IRRBB, repricing, behavioural modelling
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **pass-through rate** is the proportion of a change in market interest rates that a bank transmits to the rate it pays on non-maturity deposits (NMDs). A pass-through rate of 60% means that for every 100 basis point rise in the policy rate, the bank increases its deposit rate by only 60 basis points. The pass-through rate is a critical behavioural parameter in IRRBB modelling because it determines how quickly NMD funding costs adjust, and therefore how much NII benefit or cost the bank captures from rate movements.

## Key Formula

If the market rate changes by $\Delta r$, the deposit rate changes by:

$$\Delta r_{\text{dep}} = \beta \times \Delta r$$

where $\beta \in [0, 1]$ is the pass-through coefficient.

The **NII impact** from a deposit portfolio of volume $V$:

$$\Delta \text{NII} = V \times (1 - \beta) \times \Delta r$$

This is the "franchise value" the bank earns by not fully passing through rate rises.

## Example

A bank holds £20bn of savings deposits paying 3.00%. The central bank raises rates by 75 bps. The bank's pass-through rate for these deposits is 50%.

- Deposit rate increase: 50% × 0.75% = **0.375%** (new rate: 3.375%)
- Market rate rise captured by bank: 0.75% − 0.375% = 0.375%
- Annual NII benefit: £20bn × 0.375% = **£75m**

If the pass-through had been 100%, the bank would earn no extra NII from the rate rise. The 50% pass-through means half the rate increase flows to depositors and half boosts bank earnings.

## Remember

The pass-through rate is what makes NMDs so valuable as a funding source — a low pass-through means the bank retains a margin that widens as rates rise, creating a natural hedge for the asset side. However, pass-through is not fixed: it depends on competitive pressure, rate levels, and depositor behaviour. In the 2022–2023 rate-hiking cycle, many banks initially enjoyed very low pass-through rates, but political and competitive pressure gradually forced rates higher. Basel IRRBB standards require banks to model pass-through behaviour under stress scenarios, and overly optimistic pass-through assumptions were a contributing factor in the mispricing of deposit franchise value at banks like Silicon Valley Bank.
