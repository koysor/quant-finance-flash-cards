# SPAN Methodology

**Topic:** Banking Regulation
**Tags:** span, initial margin, futures, scenario, exchange-traded derivatives
**Created:** 2026-04-13
**Author:** Claude Sonnet 4.6

---

## Definition

SPAN (Standard Portfolio Analysis of Risk) is the scenario-based margin methodology developed by the CME Group and used by most exchanges and CCPs for exchange-traded futures and options. It calculates Initial Margin as the largest loss the portfolio would suffer across 16 standardised scenarios combining price and volatility moves, after allowing offsets between correlated positions.

## Key Formula

For each contract, a **risk array** of 16 values is pre-computed by the exchange. Each value represents the portfolio loss under a specific scenario:

| Scenario | Price move | Vol move | Weight |
|---|---|---|---|
| 1–6 | $\pm\tfrac{1}{3}, \pm\tfrac{2}{3}, \pm 1 \times$ range | Up/Down | 100% |
| 7–12 | Same | No change | 100% |
| 13–14 | Extreme: $\pm 2\times$ range | — | 35% |
| 15–16 | Zero | Up/Down | 100% |

The SPAN margin $IM$ is the **maximum loss** across all scenarios:

$$IM = \max_{s=1,\ldots,16}\; \text{Loss}(s)$$

Offsets between correlated products reduce the combined margin below the sum of individual margins.

## Example

A long position in 10 FTSE futures contracts (£1,000 per index point, index at 7,500). The exchange sets a price scan range of 300 points and vol scan range of 2%. Scenario 5 (price down by $\frac{2}{3} \times 300 = 200$ points): loss = $10 \times 1{,}000 \times 200 = £2\text{m}$. Scenario 6 (price down 300 points): loss = £3 m. The SPAN margin is set to £3 m.

## Remember

SPAN's scenario approach was designed before sensitivity-based methods (like SIMM) were computationally feasible, and it remains widely used because exchanges can pre-compute and publish risk arrays daily, allowing members to calculate their own margin requirements without complex models. The 35% weighting on extreme scenarios (13–14) ensures that deep out-of-the-money options — which have small delta but large gamma risk — still attract meaningful margin, preventing the "gamma surprise" that caused losses in the 1987 crash when portfolios with large short-option positions posted zero SPAN margin until extreme moves materialised.
