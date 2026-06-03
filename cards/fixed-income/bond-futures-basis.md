# Bond Futures Basis

**Topic:** Fixed Income
**Tags:** bond futures basis, gross basis, net basis, carry, delivery option, cash-futures spread
**Created:** 2026-06-04
**Author:** Claude Sonnet 4.6

---

## Definition

The bond futures basis is the difference between the cash price of the CTD bond and the futures-implied price (futures price × conversion factor); gross basis captures financing carry, and net basis — after stripping out carry — equals the delivery option value and is the quantity actively traded by basis traders.

## Key Formula

$$\text{Gross basis} = P_{\text{CTD}} - F \times CF_{\text{CTD}}$$

$$\text{Net carry} = \underbrace{c_{\text{CTD}} \cdot \frac{T-t}{365}}_{\text{coupon income}} - \underbrace{P_{\text{CTD}} \cdot r_{\text{repo}} \cdot \frac{T-t}{365}}_{\text{financing cost}}$$

$$\text{Net basis} = \text{Gross basis} - \text{Net carry} = \text{Delivery option value}$$

At futures expiry the gross basis converges to zero — cash and futures-implied prices equalise. Before expiry, gross basis is largely explained by carry. Net basis is always non-negative (the delivery option has non-negative value) and widens during periods of high rate volatility.

## Example

CTD gilt: cash price £98.00, $CF = 0.8900$, futures price $F = 110.11$. Gross basis: $98.00 - 110.11 \times 0.8900 = 98.00 - 98.00 = 0.00$. That is unusual — let me use $F = 110.00$: gross basis $= 98.00 - 97.90 = +0.10$. Repo rate 4.5%, coupon 4%, 90 days to expiry. Net carry: $4.0 \times 0.247 - 98.00 \times 0.045 \times 0.247 = 0.99 - 1.09 = -0.10$. Net basis: $0.10 - (-0.10) = +0.20$. The delivery option is worth £0.20 per £100 nominal — roughly 6 ticks.

## Remember

Net basis is the trader's P&L in a basis trade (long cash CTD, short futures, funded via repo). A positive net basis means the short holds a valuable delivery option — the basis trader earns this premium over time as long as no CTD switch occurs. The P&L reverses sharply if a large yield move triggers a CTD switch mid-trade: the new CTD has a different gross basis, and the position suddenly reflects the old CTD's delivery option with no offsetting short in the new CTD. Basis traders therefore monitor the spread between the first and second cheapest-to-deliver bonds as a leading indicator of switch risk.
