# Variation Margin

**Topic:** Risk
**Tags:** variation margin, mark-to-market, collateral, clearing, counterparty risk, derivatives
**Author:** Claude Opus 4.6

---

## Definition

Variation margin (VM) is the daily cash payment exchanged between counterparties (or between a clearing member and a central counterparty) to settle the change in mark-to-market value of an open derivatives position. Unlike initial margin, which covers potential future losses, variation margin reflects losses or gains that have already occurred.

## Key Formula

The variation margin payment on day $t$ equals the change in mark-to-market value:

$$\text{VM}_t = \text{MTM}_t - \text{MTM}_{t-1}$$

If $\text{VM}_t > 0$, the party whose position has gained in value receives cash; if $\text{VM}_t < 0$, that party pays. Over a holding period of $n$ days, the cumulative variation margin exchanged is:

$$\text{VM}_{\text{cumulative}} = \sum_{i=1}^{n} \left(\text{MTM}_i - \text{MTM}_{i-1}\right) = \text{MTM}_n - \text{MTM}_0$$

This telescoping sum shows that cumulative VM exactly equals the total change in portfolio value, regardless of the path taken.

## Example

A clearing member holds a long futures position valued at £200,000 at close on Monday. Over the next three days the mark-to-market values are:

| Day | MTM (£) | VM Payment (£) |
|---|---|---|
| Monday close | 200,000 | — |
| Tuesday close | 195,500 | $195{,}500 - 200{,}000 = -4{,}500$ (member pays) |
| Wednesday close | 198,200 | $198{,}200 - 195{,}500 = +2{,}700$ (member receives) |
| Thursday close | 193,800 | $193{,}800 - 198{,}200 = -4{,}400$ (member pays) |

Cumulative VM: $-4{,}500 + 2{,}700 - 4{,}400 = -£6{,}200$, which equals $193{,}800 - 200{,}000 = -£6{,}200$.

## Remember

Variation margin is the mechanism by which central counterparties prevent counterparty credit exposure from accumulating. By settling gains and losses in cash every day, VM ensures that neither side builds up a large unsecured claim against the other. After the 2008 financial crisis, regulators mandated daily VM exchange for both cleared and non-cleared derivatives (under EMIR and the BCBS-IOSCO framework). For quantitative analysts, the shift to mandatory VM has a direct pricing impact: because collateral is exchanged daily, the effective discount rate for collateralised derivatives is the overnight risk-free rate (such as SONIA or SOFR) rather than LIBOR, fundamentally changing how swaps and other instruments are valued.
