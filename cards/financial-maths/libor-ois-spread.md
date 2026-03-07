# LIBOR-OIS Spread

**Topic:** Financial Mathematics
**Tags:** libor, ois, credit risk, funding stress, money market, systemic risk
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

The LIBOR-OIS spread is the difference between the London Interbank Offered Rate (LIBOR) — an unsecured term lending rate — and the overnight index swap (OIS) rate of the same maturity. Since the OIS rate reflects the expected path of the risk-free overnight rate, the spread isolates the **bank credit risk premium** and **liquidity premium** embedded in term interbank lending.

## Key Formula

$$\text{LIBOR-OIS Spread} = r_{\text{LIBOR}}(T) - r_{\text{OIS}}(T)$$

In normal markets ($\sim$10 basis points), the spread reflects minimal bank credit risk. During crises, it widens dramatically as banks become reluctant to lend unsecured.

The spread can be decomposed:

$$\text{Spread} = \underbrace{\text{Credit Risk Premium}}_{\text{default probability} \times \text{LGD}} + \underbrace{\text{Liquidity Premium}}_{\text{hoarding + uncertainty}}$$

## Example

On 1 October 2008, at the height of the financial crisis:

- 3-month USD LIBOR: 4.15%
- 3-month USD OIS rate: 1.80%

$$\text{Spread} = 4.15\% - 1.80\% = 2.35\% = 235 \text{ basis points}$$

In January 2007, the same spread was just 8 basis points. The 30-fold widening reflected the market's assessment that lending to other banks had become extremely risky — banks were hoarding cash and refusing to lend for terms beyond overnight.

## Example

Post-LIBOR transition, an analogous measure is the SOFR-OIS spread or the term SOFR basis, though these tend to be much smaller because SOFR is itself a secured overnight rate.

## Remember

The LIBOR-OIS spread became the single most-watched indicator of financial system health during the 2008 crisis. It captures something that equity markets and credit default swaps cannot — the willingness of banks to lend to each other on an unsecured basis. When the spread blows out, it signals that the interbank market is freezing, which starves the real economy of credit. For quantitative analysts, the spread is essential for derivatives pricing: pre-crisis, LIBOR was treated as risk-free for discounting, but the crisis revealed that it contains significant credit risk. The transition from LIBOR to risk-free rates (SONIA, SOFR) was driven by this realisation — and by the 2012 scandal showing that LIBOR submissions were being manipulated.
