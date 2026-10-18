# Asset Sensitivity and Liability Sensitivity

**Topic:** Financial Mathematics
**Tags:** asset sensitive, liability sensitive, net interest income, repricing, deposit beta, IRRBB
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

A bank is **asset-sensitive** if its net interest income rises when interest rates rise, and **liability-sensitive** if its net interest income falls. The label depends on whether assets or liabilities reprice faster over the chosen horizon, taking into account how fully deposit rates follow market rates.

## Key Formula

Using the cumulative repricing gap over horizon $H$:

$$\Delta\text{NII} \approx \text{CGAP}_H \times \Delta r, \qquad \text{CGAP}_H = \text{RSA}_H - \text{RSL}_H$$

| Gap | Label | Rates up | Rates down |
|---|---|---|---|
| $\text{CGAP} > 0$ | Asset-sensitive | NII rises | NII falls |
| $\text{CGAP} < 0$ | Liability-sensitive | NII falls | NII rises |

Deposit pass-through matters: with a deposit beta $\beta < 1$, only a fraction $\beta$ of the rate rise is paid to depositors, so a bank with many low-beta deposits is asset-sensitive even if its gap schedule looks balanced.

## Example

A bank has a 12-month cumulative gap of $+£1.5\text{bn}$. A 100 bp rise gives $\Delta\text{NII} \approx 1.5\text{bn} \times 0.01 = +£15\text{m}$; a 100 bp fall costs about £15m. A bank with a 12-month gap of $-£2\text{bn}$ would lose £20m on the same rise.

## Remember

Asset sensitivity and the economic value view can point in opposite directions: a bank with long fixed-rate assets may be liability-sensitive in earnings terms yet have a large loss of economic value, which is why both lenses are reported. When rates are expected to fall, an asset-sensitive bank is exposed and tends to lengthen its asset duration with structural hedges, as discussed under the structural hedge.
