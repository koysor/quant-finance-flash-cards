# Cost-of-Carry Markets

**Topic:** Derivatives
**Tags:** cost of carry, forwards, futures, no-arbitrage, storage costs, convenience yield
**Author:** Claude Opus 4.6

---

## Definition

A **cost-of-carry market** is one in which the forward (or futures) price of an asset is fully determined by the spot price plus the net cost of holding the asset until delivery. The "carry" includes financing costs, storage costs, and insurance, minus any income earned (dividends, coupons) or convenience yield enjoyed by holding the physical asset.

## Key Formula

The general cost-of-carry relationship for a forward maturing at time $T$ is:

$$F_0 = S_0 \, e^{(r + u - q - y) \, T}$$

where:

- $S_0$ is the current spot price
- $r$ is the continuously compounded risk-free rate (financing cost)
- $u$ is the storage cost rate
- $q$ is the continuous dividend or income yield
- $y$ is the convenience yield
- $T$ is the time to maturity in years

When the market obeys cost-of-carry perfectly (i.e. $y = 0$ and storage is negligible), the formula simplifies to:

$$F_0 = S_0 \, e^{(r - q) \, T}$$

## Example

Gold trades at a spot price of $S_0 = \$1{,}900$. The risk-free rate is $r = 5\%$ per annum and annual storage costs are $u = 0.5\%$. Gold pays no income ($q = 0$) and assume no convenience yield ($y = 0$). The six-month forward price is:

$$F_0 = 1{,}900 \times e^{(0.05 + 0.005) \times 0.5} = 1{,}900 \times e^{0.0275} \approx 1{,}900 \times 1.02788 \approx \$1{,}952.97$$

If the quoted forward were $\$1{,}970$, an arbitrageur could buy gold spot, store it, and sell the forward to lock in a riskless profit of approximately $\$17.03$ per ounce.

## Remember

Cost-of-carry is the bridge between spot and forward markets. When the relationship holds, forward prices contain no additional information beyond today's spot price and known carry costs — they are not forecasts of future spot prices. In commodities, a breakdown of the cost-of-carry relationship (backwardation) signals that the convenience yield of holding physical inventory exceeds carry costs, which is critical intelligence for traders pricing energy and agricultural futures.
