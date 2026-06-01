# Zipline

**Topic:** Computational Finance
**Tags:** backtesting, event-driven, algorithmic trading, look-ahead bias, quantopian, python
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**Zipline** (maintained as `zipline-reloaded`) is an event-driven Python backtesting framework in which an algorithm is expressed as a set of callback functions — `initialize()`, `handle_data()`, and `before_trading_start()` — that are called sequentially bar-by-bar, ensuring data flows only forward in time and preventing look-ahead bias by construction.

## Key Formula

Zipline's trading API targets portfolio weights rather than share counts, enforcing position sizing discipline:

$$\text{order\_target\_percent}(\text{asset},\, w^*) \implies \Delta \text{shares} = \frac{w^* \cdot \text{portfolio value} - \text{current position value}}{\text{current price}}$$

The daily P&L updates the portfolio value after fills, and slippage and commission models deduct transaction costs:

$$r_t^{\text{net}} = r_t^{\text{gross}} - \underbrace{\left(\frac{\text{spread}}{2} + c \cdot \lvert\Delta\text{shares}\rvert\right)}_{\text{transaction cost}}$$

where $c$ is the per-share commission and spread is the bid-ask spread.

## Example

```python
def initialize(context):
    context.asset = symbol('AAPL')

def handle_data(context, data):
    price_history = data.history(context.asset, 'price', 20, '1d')
    if price_history[-1] > price_history.mean():
        order_target_percent(context.asset, 0.10)  # 10% of portfolio
    else:
        order_target_percent(context.asset, 0.0)
```

Each call to `handle_data` sees only prices up to and including the current bar — the 20-day history on day 50 contains days 31–50, never day 51.

## Remember

The look-ahead bias risk in backtesting is not just about using future prices directly — it also arises from computing signals on data that includes the current bar's close and then executing at that same close. Zipline enforces a one-bar execution lag by default: signals computed in `handle_data` on the close of day $t$ are executed at the open of day $t+1$, matching the realistic constraint that you cannot trade at the price you observed. This single design decision eliminates a class of backtest inflation that is endemic in naive vectorised backtests and is one of the main reasons institutional quant teams use event-driven frameworks.
