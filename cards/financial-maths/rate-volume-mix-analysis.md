# Rate-Volume Analysis of Net Interest Income

**Topic:** Financial Mathematics
**Tags:** net interest income, rate volume analysis, variance analysis, NII attribution, yield, balances
**Created:** 2026-10-18
**Author:** Claude Sonnet 5.5

---

## Definition

**Rate-volume analysis** splits a change in interest income or expense between a change in average balances (the **volume** effect) and a change in yield or cost (the **rate** effect), plus a small joint term. It explains why net interest income changed, separating growth from repricing.

## Key Formula

With old balance $V_0$ and rate $r_0$, and new balance $V_1$ and rate $r_1$:

$$\underbrace{V_1 r_1 - V_0 r_0}_{\text{total change}} = \underbrace{(V_1 - V_0)\,r_0}_{\text{volume}} + \underbrace{V_0\,(r_1 - r_0)}_{\text{rate}} + \underbrace{(V_1 - V_0)(r_1 - r_0)}_{\text{joint}}$$

Apply the same split to interest income and to interest expense, then net them to attribute the movement in NII.

## Example

Average loans grow from £10bn to £11bn while the yield rises from 4.0% to 4.5%:

- Income before: $10\text{bn} \times 4.0\% = £400\text{m}$; after: $11\text{bn} \times 4.5\% = £495\text{m}$; change £95m.
- Volume: $1\text{bn} \times 4.0\% = £40\text{m}$.
- Rate: $10\text{bn} \times 0.5\% = £50\text{m}$.
- Joint: $1\text{bn} \times 0.5\% = £5\text{m}$.

$$40 + 50 + 5 = 95 \checkmark$$

## Remember

The rate component is the part that interest rate risk management is about. A bank whose income growth is mostly volume is exposed to the cycle in lending; one whose growth is mostly rate is benefiting from the rate environment and may give it back when rates fall. Analysts and boards use this decomposition to separate earnings that come from the business from earnings that come from the rate cycle.
