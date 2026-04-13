# Default Risk Charge (DRC)

**Topic:** Banking Regulation
**Tags:** drc, frtb, jump to default, credit risk, trading book
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

The Default Risk Charge (DRC) is an FRTB capital add-on that captures the risk of sudden jump-to-default in trading book positions — the loss that would occur if an issuer or reference entity immediately defaulted, independently of any gradual credit spread deterioration captured by the Sensitivity-Based Method. DRC applies under both the Standardised Approach and the Internal Models Approach, ensuring that default risk is always capitalised even when spread risk is already covered elsewhere.

## Key Formula

Under the FRTB Standardised Approach, DRC is computed as a one-year 99.9th percentile loss using a single-factor model. For a portfolio of $n$ positions with notional $N_i$, loss-given-default $LGD_i$, and default probability $PD_i$:

$$\text{DRC} = \sum_i N_i \cdot LGD_i \cdot JTD_i$$

where $JTD_i$ (Jump-To-Default) is a position's net long or short exposure adjusted for any offsetting hedge. Gross JTD is:

$$\text{Gross JTD}_{\text{long}} = \max(LGD \times \text{Notional} + P\&L_{\text{on default}},\; 0)$$

Long and short positions in the same obligor can be offset; the net position is bucketed by credit quality (investment grade, high yield, defaulted) with partial offset allowed across buckets via a hedge benefit ratio $WtS$.

## Example

A bank is long a 5-year bond issued by Company X (notional £10 m, LGD = 60%) and short a CDS referencing Company X (notional £6 m, LGD = 60%). Gross JTD long = £6 m, Gross JTD short = £3.6 m. Net JTD = £2.4 m. Applying the IG bucket DRC weight (say 0.5% for AA-rated), DRC = £2.4 m × 0.5% = £12,000. A speculative-grade obligor at 15% weight on the same net notional would give DRC = £360,000.

## Remember

DRC exists because the Sensitivity-Based Method in FRTB captures only gradual spread movements (a 1 bp shift in the credit spread curve), not the discrete jump from par to (1-LGD) × notional that occurs on default. This distinction matters for concentrated credit books: a trading desk long £500 m of a single IG issuer might have modest spread risk (DV01-based capital) but enormous DRC from a single default event. For quant developers, DRC requires maintaining a separate default simulation layer alongside the market risk sensitivities engine, using historical or model-implied default probabilities rather than the parallel-shift sensitivities used for SBM capital.

