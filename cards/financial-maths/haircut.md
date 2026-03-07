# Haircut

**Topic:** Financial Mathematics
**Tags:** haircut, collateral, margin, repo, risk management, secured lending
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

A haircut is the percentage reduction applied to the market value of an asset when it is used as collateral for a loan or repo. It reflects the lender's estimate of how much the collateral's value could fall before the position can be liquidated, protecting against both market risk and liquidity risk.

## Key Formula

The **haircut** as a percentage:

$$h = \frac{\text{Market Value} - \text{Loan Value}}{\text{Market Value}} \times 100\%$$

The **loan value** (cash advanced) given the haircut:

$$\text{Loan Value} = \text{Market Value} \times (1 - h)$$

The **effective leverage** from a repo with haircut $h$:

$$L = \frac{1}{h}$$

## Example

A hedge fund pledges £20 million of corporate bonds as collateral in a repo. The lender applies a 10% haircut.

$$\text{Loan Value} = £20{,}000{,}000 \times (1 - 0.10) = £18{,}000{,}000$$

$$L = \frac{1}{0.10} = 10\times$$

The fund can lever up 10x on these bonds. If it instead pledged gilts (2% haircut):

$$L = \frac{1}{0.02} = 50\times$$

This is why government bonds allow far higher leverage than corporate bonds — the lower haircut reflects lower price volatility and better liquidity.

## Example

During the 2008 crisis, haircuts on asset-backed securities jumped from 3–5% to 40–50% almost overnight. A fund that had been running 25x leverage suddenly found its maximum leverage capped at 2–2.5x, forcing massive deleveraging.

## Remember

Haircuts are the market's real-time assessment of collateral quality and are a primary driver of the leverage cycle. In normal times, low haircuts enable high leverage and abundant liquidity. During crises, haircuts spike as lenders demand more protection, which forces deleveraging, fire sales, and further price declines — creating a procyclical feedback loop. Basel III and EMIR now mandate minimum haircuts for non-centrally cleared transactions to dampen this cycle. For quantitative analysts, modelling how haircuts change under stress is essential for realistic leverage and liquidity risk assessment.
