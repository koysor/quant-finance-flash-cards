# Collar Strategy

**Topic:** Derivatives
**Tags:** collar, options strategy, protective put, covered call, hedging, concentrated stock
**Created:** 2026-06-13
**Author:** Claude Sonnet 4.6

---

## Definition

A collar holds the underlying asset, buys a protective put at $K_p < S$, and sells a covered call at $K_c > S$; the call premium offsets the put cost, capping both downside and upside.

## Key Formula

$$\text{P\&L at }T = (S_T - S_0) + \max(K_p - S_T,\,0) - \max(S_T - K_c,\,0) - \text{net premium}$$

Bounded range: $\bigl[K_p - S_0 - \text{net premium},\; K_c - S_0 - \text{net premium}\bigr]$

Zero-cost collar: choose $K_p$, $K_c$ such that $P(K_p) = C(K_c)$, so net premium $= 0$.

## Example

$S_0 = 100$. Buy put at $K_p = 90$ for \$4, sell call at $K_c = 115$ for \$4. Net cost $= 0$. If $S_T = 80$: receive $90 - 100 = -10$ on stock, $+10$ on put, $0$ on call → net $= 0$. If $S_T = 130$: stock $+30$, put $0$, call $-15$ → net $= +15$. Locked range: $[-10,\, +15]$.

## Remember

Zero-cost collars are widely used by corporate insiders hedging concentrated stock positions — the call sale funds the put purchase, locking in an effective exit price range without triggering immediate tax. They also appear in structured notes: a capital-protected note is effectively a zero-coupon bond plus a long collar on an equity index.
