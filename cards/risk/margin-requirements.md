# Margin Requirements

**Topic:** Risk
**Tags:** margin, initial margin, maintenance margin, collateral, clearing
**Created:** 2026-03-07
**Author:** Claude Opus 4.6

---

## Definition

Margin requirements are the minimum amounts of collateral that a broker, exchange, or clearing house demands from a trader before and during a leveraged position. **Initial margin** is the deposit required to open a position; **maintenance margin** is the minimum equity that must be maintained while the position is open.

## Key Formula

The **initial margin ratio** determines the minimum equity fraction at entry:

$$\text{Initial Margin} = \text{Position Value} \times m_i$$

The **maximum leverage** permitted is the inverse of the initial margin ratio:

$$L_{\max} = \frac{1}{m_i}$$

For derivatives cleared through a central counterparty, initial margin is typically set to cover potential losses at a high confidence level over a specified horizon:

$$\text{IM} \geq \text{VaR}_{99\%}(h)$$

where $h$ is the margin period of risk (commonly 1–2 days for futures, 5–10 days for OTC derivatives).

## Example

A futures exchange sets an initial margin of 10% and a maintenance margin of 7%.

- Maximum leverage: $L_{\max} = 1 / 0.10 = 10\times$
- A trader opens a £100,000 position by posting £10,000 initial margin
- If the position loses £3,500, equity falls to £6,500
- Equity ratio: $6{,}500 / 100{,}000 = 6.5\% < 7\%$ — a margin call is triggered
- The trader must deposit at least £3,500 to restore equity to the initial margin level of £10,000

## Remember

Margin requirements are the primary regulatory mechanism for controlling leverage in financial markets. After the 2008 crisis, reforms such as Basel III and EMIR introduced mandatory central clearing with standardised initial margin calculations, often based on historical VaR or expected shortfall. For quantitative analysts, understanding margin is essential because it determines the maximum leverage a strategy can employ, the funding costs embedded in levered positions, and the liquidity risk from potential margin calls during market stress.
