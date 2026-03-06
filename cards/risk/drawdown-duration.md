# Drawdown Duration

**Topic:** Risk
**Tags:** drawdown duration, recovery time, risk, maximum drawdown, time underwater, performance
**Author:** Claude Opus 4.6

---

## Definition

Drawdown duration is the length of time a portfolio spends below its previous peak value before recovering to that peak (or higher). While maximum drawdown measures the depth of the worst loss, drawdown duration measures how long the pain lasts. A fund can have a modest maximum drawdown but an extremely long recovery period, or a deep drawdown with a quick recovery — the two metrics capture different dimensions of investor pain.

## Key Formula

Let $P_t = \max_{s \leq t} V_s$ be the running peak at time $t$. A drawdown begins at time $t_1$ when $V_{t_1} < P_{t_1}$ and ends at the first time $t_2 > t_1$ when $V_{t_2} \geq P_{t_1}$:

$$\text{Drawdown Duration} = t_2 - t_1$$

The **maximum drawdown duration** is:

$$\text{MDD Duration} = \max_k (t_{2,k} - t_{1,k})$$

over all drawdown episodes $k$.

**Time underwater** is the total fraction of the observation period spent in drawdown:

$$\text{Time Underwater} = \frac{\sum_k (t_{2,k} - t_{1,k})}{T}$$

## Example

A fund peaks at £110 million in March, drops to £95 million in June (maximum drawdown of 13.6%), then recovers back to £110 million in November:

$$\text{Drawdown Duration} = \text{November} - \text{March} = 8 \text{ months}$$

Over a 3-year track record, if the fund spends a total of 18 months in various drawdown episodes:

$$\text{Time Underwater} = \frac{18}{36} = 50\%$$

The fund was below its previous peak for half of its entire history — a psychologically challenging experience for investors even if the final return was attractive.

## Remember

Drawdown duration is the metric that separates tolerable losses from career-ending ones. A hedge fund that drops 15% but recovers within two months causes far less damage to investor confidence than one that drops 10% and takes two years to recover. Institutional investors often track maximum drawdown duration alongside maximum drawdown depth, and some mandates set explicit limits on both. In quantitative backtesting, long drawdown durations can also signal that a strategy has decayed or that market conditions have shifted away from the factors the strategy exploits.
