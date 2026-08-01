# Credit DV01

**Topic:** Fixed Income
**Tags:** credit spread, cs01, risky annuity, sensitivity, cds, hedging
**Created:** 2026-08-01
**Author:** Claude Opus 5

---

## Definition

Credit DV01 — also written CS01 — is the change in the value of a credit position for a one basis point parallel shift in its credit spread curve. It plays the same role for spread risk that DV01 plays for interest rate risk, and it is the unit in which credit desks size and hedge exposure.

## Key Formula

For a CDS, value changes are transmitted through the **risky annuity** (the discounted, survival-weighted sum of premium payments):

$$\text{Credit DV01} \approx \text{Notional} \times \text{RPV01} \times 0.0001$$

$$\text{RPV01} = \Delta t\sum_{i=1}^{m} Z(0,t_i)\,P(0,t_i)$$

where $Z$ is the risk-free discount factor and $P$ the survival probability. For a par bond the sensitivity is close to its spread duration:

$$\text{Credit DV01} \approx \text{Notional} \times D_{\text{spread}} \times 0.0001$$

Unlike DV01, credit DV01 is not symmetric in stress: as spreads widen, survival probabilities fall, the risky annuity shortens, and the sensitivity itself shrinks.

## Example

A five-year par bond yielding 5.5% has a credit DV01 of about \$435 per \$1m of notional — roughly the spread duration of 4.35 years times one basis point.

Scale that to AIG Financial Products' 2008 book of \$450bn notional:

$$\$435 \times 450{,}000 = \$196\text{m per basis point}$$

Spreads on five-year AAA financial issues moved from about 50 bps to about 150 bps between mid-2007 and early 2008. At roughly \$200m per basis point, a 100 bp move implies losses near \$20bn — on positions that required almost no capital outlay to establish.

## Remember

The AIG episode is the reason this number is computed and reported daily rather than derived when needed. Selling CDS protection is economically a leveraged long position in the underlying bond: the same spread exposure, but without the funding cost that buying \$450bn of subordinated bank debt would have required, and therefore without the balance-sheet footprint that would have alerted counterparties, regulators or the firm's own management. Notional is a poor measure of that risk — credit DV01 converts it into the currency amount actually at stake per basis point, making a synthetic book comparable to a cash one. For a kth-to-default basket the same sensitivity is computed per reference name by bumping that name's curve by a basis point and repricing, which decomposes the total spread risk into the individual credits driving it.
