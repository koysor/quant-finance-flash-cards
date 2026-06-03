# Portfolio Costs

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** portfolio costs, transaction costs, market impact, turnover, alpha hurdle, slippage
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

**Portfolio costs** are the total frictional drag on a strategy's returns, comprising transaction costs (bid-ask spread and market impact paid when trading) and financing costs (stock borrow fees on short positions, margin interest, and fund expenses). They set the minimum gross alpha a strategy must generate to remain profitable after all trading-related expenses.

## Key Formula

Net alpha equals gross alpha minus the sum of all cost components:

$$\alpha_{\text{net}} = \alpha_{\text{gross}} - C_{\text{transaction}} - C_{\text{financing}}$$

The transaction cost component depends on one-way annual turnover $\tau$ and the average round-trip cost per trade $c$ (spread plus estimated market impact):

$$C_{\text{transaction}} = c \cdot \tau$$

The financing cost on a short book of notional $N_S$ at borrow rate $b$ is:

$$C_{\text{financing}} = b \cdot N_S / N_{\text{total}}$$

## Example

A long–short equity strategy has gross alpha of 120 bps per year. Annual one-way turnover is 200%, average round-trip cost is 15 bps, and the short book is 50% of portfolio notional at a 40 bps stock borrow rate.

$$C_{\text{transaction}} = 15 \times 2 = 30 \text{ bps}, \quad C_{\text{financing}} = 40 \times 0.5 = 20 \text{ bps}$$

$$\alpha_{\text{net}} = 120 - 30 - 20 = 70 \text{ bps}$$

The cost hurdle is 50 bps; the strategy survives, but a weaker signal generating only 60 bps gross would be unprofitable.

## Remember

Portfolio costs explain why alpha decay matters so much to practitioners. A signal with a two-week half-life requires very high turnover to act on it in time, which multiplies transaction costs and may destroy all the gross alpha it generates. Quant funds routinely reject strategies with strong backtested returns once realistic cost assumptions are applied — the cost hurdle $c \cdot \tau$ is the first filter any new strategy must survive before live trading is considered.
