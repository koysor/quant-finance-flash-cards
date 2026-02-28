# Put-Call Parity

**Topic:** Derivatives
**Tags:** options, put-call parity, arbitrage, no-arbitrage
**Created:** 2026-02-28 20:46:20
**Author:** Unknown

---

## Definition

**Put-call parity** is a fundamental no-arbitrage relationship between European call and put option prices on the same underlying asset with the same strike price K and expiry T.

## Key Formula

$$C - P = S_0 - K e^{-rT}$$

Where:
- **C** — price of European call option
- **P** — price of European put option
- **S₀** — current price of the underlying asset
- **K** — strike price
- **r** — continuously compounded risk-free rate
- **T** — time to expiry (in years)

Rearranged to find the put price: P = C − S₀ + K e^(−rT)

## Example

A European call on a stock costs £8. The stock is at £50, strike is £48, r = 5%, T = 0.5 years.

K e^(−rT) = 48 × e^(−0.025) ≈ 48 × 0.9753 = £46.81

Put price: P = 8 − 50 + 46.81 = **£4.81**

## Remember

- Put-call parity **only holds for European options** (American options can be exercised early, breaking the relationship).
- Violations create **riskless arbitrage** opportunities — in practice, transaction costs set the bounds within which small deviations are possible.
- The relationship implies you can **replicate** a call using a put + stock − borrowing, or vice versa. Understanding replication is key to derivatives pricing.
