# Quantitative Easing

**Topic:** Fixed Income
**Tags:** quantitative easing, qe, asset purchases, term premium, central bank, balance sheet
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

Quantitative Easing (QE) is a monetary policy tool in which a central bank purchases large quantities of long-dated government bonds or other securities to inject liquidity, reduce long-term yields, and compress the term premium when the short-term policy rate is already near zero.

## Key Formula

QE operates through the **duration removal** channel: by purchasing bonds, the central bank removes duration risk from private portfolios. The term premium compression is approximately:

$$\Delta tp_t(T) \approx -\beta \times \frac{\Delta D_{\text{removed}}}{\text{market float duration}}$$

where $\Delta D_{\text{removed}}$ is the 10-year duration equivalent of QE purchases. Empirical estimates suggest each \$100bn of 10-year equivalent duration purchased compresses the 10-year term premium by 3–5bp. Because $y_t(T) = \mathbb{E}_t[\bar{r}] + tp_t(T)$, the yield falls even though rate expectations are unchanged.

## Example

Fed QE1 (November 2008 – March 2010): \$1.25 trillion MBS and \$300bn Treasuries purchased. Estimated 10-year term premium reduction: 40–80bp. The 30-year mortgage rate fell from 6.5% to 4.8%. When the Fed began Quantitative Tightening (QT) in June 2022 — allowing \$95bn of bonds to roll off per month — the 10-year term premium rose from -0.5% to +1.0% over 18 months, contributing 75bp to the rise in long yields independently of rate hikes.

## Remember

QE works by removing duration risk from the private sector, not by changing rate expectations — this is why it can lower long yields even when everyone knows the policy rate will stay at zero for years. The practical implication for bond traders is that QE creates a structural compressor of term premia across all risk assets: QE periods suppress IG credit spreads, mortgage spreads, and equity risk premia via the portfolio balance effect. When QT begins, these effects reverse gradually — but unevenly across assets — creating relative-value opportunities between asset classes that were previously all compressed by the same QE bid.
