# Covered Interest Parity

**Topic:** Derivatives
**Tags:** fx forward, covered interest parity, no-arbitrage, cross-currency basis, forward points
**Created:** 2026-11-18
**Author:** Claude Opus 5.5

---

## Definition

Covered interest parity (CIP) says that the FX forward rate is fixed by no-arbitrage, not by anyone's forecast. Borrowing in one currency, converting at spot, depositing in the other and locking in the conversion back with a forward is riskless, so the forward must make it earn nothing extra. The forward therefore sits above spot when the quote currency pays the higher interest rate.

## Key Formula

For a pair quoted BASE/QUOTE with spot $S$, base-currency rate $r_b$ and quote-currency rate $r_q$:

$$F = S\,e^{(r_q - r_b)T} \qquad \text{(continuous compounding)}$$

$$F = S\,\frac{1 + r_q\,\tau}{1 + r_b\,\tau} \qquad \text{(simple money-market rates over } \tau)$$

The forward points are $F - S$, quoted in pips.

## Example

GBPUSD spot $S = 1.3000$, one-year USD rate $5\%$, one-year GBP rate $4\%$, simple rates:

$$F = 1.3000 \times \frac{1.05}{1.04} = 1.3125$$

The one-year forward is $1.3125$, or $+125$ forward points. If a bank quoted $1.3200$, you could borrow \$1.30, buy £1, deposit it to receive £1.04, sell that forward for $1.04 \times 1.3200 = \$1.3728$, repay \$1.365 and keep \$0.0078 per pound with no risk.

## Remember

Since 2008 CIP has failed persistently in market prices: the gap is the cross-currency basis, which reached about $-100$ basis points for EURUSD in late 2011. It survives because the "arbitrage" uses scarce bank balance sheet and funding that is not truly risk-free. CIP is about hedged returns; its uncovered cousin, which says forwards predict future spot, fails empirically, and that failure is what the carry trade earns from.
