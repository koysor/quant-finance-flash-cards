# VIX Futures Term Structure

**Topic:** Volatility
**Tags:** VIX, futures, term structure, contango, backwardation, roll yield, volatility ETPs
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **VIX futures term structure** is the curve of VIX futures prices plotted against their expiration dates. Because the VIX is not a tradeable asset (it is a calculation), VIX futures do not converge to spot VIX via a simple cost-of-carry relationship. Instead, the term structure reflects the market's expectation of future implied volatility levels plus a risk premium. It is typically in **contango** (futures above spot), but inverts into **backwardation** during market stress.

## Key Formula

The **roll yield** from holding a long VIX futures position:

$$\text{Roll yield} \approx \frac{F_1 - F_2}{F_1} \times \frac{252}{\Delta t}$$

where $F_1$ is the front-month futures price, $F_2$ is the second-month price, and $\Delta t$ is the number of trading days between rolls.

In contango ($F_2 > F_1$ on a given day, but the position rolls from an expiring $F_1$ down to a cheaper new front-month), the long position **loses** roll yield as it systematically buys high and sells low. The annualised cost of maintaining a long VIX position via futures rolling has historically been 5–10% per month in contango environments.

## Example

Spot VIX is 15. The term structure shows:

| Contract | Price |
|---|---|
| Front month (15 days) | 16.2 |
| Second month (45 days) | 17.8 |
| Third month (75 days) | 18.5 |

The curve is in contango. A long VIX futures ETN must roll from the expiring front month into the more expensive second month. If it sells at 16.2 and buys at 17.8, the roll cost is:

$$\frac{17.8 - 16.2}{16.2} \approx 9.9\% \text{ per roll}$$

Over a year with monthly rolls, this drag compounds to substantial losses even if spot VIX is unchanged — explaining why products like VXX lose value systematically over time.

## Remember

The VIX futures term structure is the most important concept for anyone trading volatility ETPs. In normal markets, contango means long-volatility products (VXX, UVXY) bleed value through negative roll yield, while inverse products (SVXY) earn positive roll yield — this is why short-vol strategies appear to generate steady income. However, during sharp sell-offs the term structure inverts into backwardation (front month above back months), and the violent spot VIX spike overwhelms months of accumulated roll yield, causing catastrophic losses for short-vol positions. The February 2018 "Volmageddon" event, which destroyed the XIV ETN, demonstrated that the roll yield is compensation for bearing this precise tail risk.
