# Repricing Risk

**Topic:** Banking Regulation
**Tags:** repricing risk, IRRBB, repricing gap, interest rate risk, maturity mismatch
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Repricing risk** is the most fundamental component of IRRBB. It arises when a bank's assets and liabilities reprice (reset to current market rates) at different times. If a bank funds long-term fixed-rate loans with short-term deposits, a rate rise increases funding costs immediately while loan income stays fixed — squeezing net interest income. Repricing risk is measured by the **repricing gap**: the difference between rate-sensitive assets and rate-sensitive liabilities in each time bucket.

## Key Formula

$$\text{Repricing Gap}_i = \text{RSA}_i - \text{RSL}_i$$

where $\text{RSA}_i$ and $\text{RSL}_i$ are the volumes of assets and liabilities that reprice in time bucket $i$.

**Cumulative gap** up to bucket $n$:

$$\text{CGAP}_n = \sum_{i=1}^{n} \text{Gap}_i$$

**NII sensitivity** to a uniform rate change $\Delta r$ over horizon $n$:

$$\Delta\text{NII} \approx \text{CGAP}_n \times \Delta r$$

| Gap sign | Rates rise | Rates fall |
|---|---|---|
| Positive (RSA > RSL) | NII rises | NII falls |
| Negative (RSA < RSL) | NII falls | NII rises |

## Example

A bank's repricing schedule (£ billions):

| Bucket | RSA | RSL | Gap | Cumulative gap |
|---|---|---|---|---|
| 0–3 months | 4.0 | 6.0 | −2.0 | −2.0 |
| 3–6 months | 2.0 | 1.0 | +1.0 | −1.0 |
| 6–12 months | 3.0 | 2.0 | +1.0 | 0.0 |

If rates rise by 100 bps, the 3-month NII impact is approximately:

$$\Delta\text{NII}_{3\text{m}} \approx (-2.0\text{bn}) \times 0.01 \times \tfrac{3}{12} = -£5\text{m}$$

The negative gap in the first bucket means funding costs rise before asset income does.

## Remember

Repricing risk is the "bread and butter" of banking book risk management — it explains why banks care about the maturity structure of their deposits and loans. The repricing gap analysis is simple but powerful: it immediately shows which time buckets expose the bank to rising or falling rates. Basel's IRRBB standard interest rate shocks are designed primarily to stress repricing risk. In practice, the simple gap model is supplemented by cash-flow simulation models that account for behavioural optionality — depositors may withdraw early, borrowers may prepay mortgages — but the repricing gap remains the starting point for every ALM discussion.
