# Long-Short Equity

**Topic:** Financial Mathematics
**Tags:** long-short, equity, hedge funds, alpha, market neutral, portfolio management
**Author:** Claude Opus 4.6

---

## Definition

Long-short equity is an investment strategy that takes long positions in stocks expected to appreciate and short positions in stocks expected to decline. By combining both sides, the portfolio can profit from stock selection (alpha) while reducing or eliminating exposure to the overall market direction (beta).

## Key Formula

The portfolio return of a long-short strategy is:

$$R_p = w_L \cdot R_L - w_S \cdot R_S$$

where $w_L$ and $w_S$ are the capital weights allocated to the long and short books, and $R_L$ and $R_S$ are their respective returns.

**Net exposure** measures directional bias:

$$\text{Net Exposure} = w_L - w_S$$

A net exposure of zero is called **market neutral**. **Gross exposure** $= w_L + w_S$ measures total capital at work.

## Example

A fund allocates 70% of capital long and 30% short. The long book returns 10% and the short book returns 4% (i.e. the shorted stocks rose 4%):

$$R_p = 0.70 \times 0.10 - 0.30 \times 0.04 = 0.07 - 0.012 = 0.058$$

The portfolio return is 5.8%. The net exposure is $0.70 - 0.30 = 0.40$ (40% net long), and the gross exposure is $0.70 + 0.30 = 1.00$ (100%).

## Remember

Long-short equity is the most common hedge fund strategy because it allows managers to express views on individual stocks without betting on the market as a whole. The Sharpe ratio of a well-constructed long-short portfolio can exceed that of a long-only fund because hedging out market risk reduces volatility while preserving alpha — this is why institutional investors pay hedge fund fees for genuine stock-picking skill.
