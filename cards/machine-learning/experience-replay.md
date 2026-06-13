# Experience Replay

**Topic:** Machine Learning
**Tags:** experience replay, replay buffer, dqn, deep reinforcement learning, non-stationarity, prioritised replay
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

**Experience replay** (Lin, 1992; Mnih et al., 2015) stores past agent transitions $(s_t, a_t, r_t, s_{t+1})$ in a fixed-size **replay buffer** and trains the network by sampling random mini-batches from the buffer rather than using transitions in the order they were collected. This breaks the temporal correlation between consecutive training samples and allows rare but important events to be replayed multiple times.

## Key Formula

The replay buffer $\mathcal{D}$ stores the $N$ most recent transitions. A mini-batch of size $B$ is sampled uniformly (or according to priority weights $p_i$) and used to minimise the Bellman residual:

$$\mathcal{L}(\theta) = \frac{1}{B}\sum_{i \in \mathcal{B}} \left(r_i + \gamma\, \max_{a'} Q(s'_i, a'; \theta^{-}) - Q(s_i, a_i; \theta)\right)^2$$

**Prioritised experience replay** (Schaul et al., 2015) samples transition $i$ with probability proportional to its **TD error**:

$$p_i = \lvert r_i + \gamma \max_{a'} Q(s'_i, a'; \theta^{-}) - Q(s_i, a_i; \theta) \rvert^\alpha$$

so high-error transitions — unexpected market moves — are replayed more often.

## Example

An RL trading agent trained sequentially on daily S&P 500 returns (2010–2020) suffers from temporal correlation: consecutive days share the same regime, so the network overfits to the current regime and forgets others. With a replay buffer of 50,000 transitions: mini-batches mix bull-market days (2013–2019), crisis days (March 2020), and range-bound days (2011), reducing the Sharpe ratio's out-of-sample standard deviation from 0.8 to 0.3. Prioritised replay further up-weights the 5% of days with the largest price moves, improving tail-risk management.

## Remember

Experience replay solves two problems simultaneously in financial RL: **correlation** (financial returns are autocorrelated within regimes, violating the i.i.d. assumption of SGD) and **sample efficiency** (rare market events — flash crashes, earnings gaps, limit hits — occur once but contain high learning signal). The central tension for finance is **staleness**: old buffer transitions come from past regimes whose dynamics may no longer apply, so large buffers improve stability but can slow adaptation to regime changes. Adaptive forgetting — discarding transitions from detected regime shifts — addresses this at the cost of needing a reliable regime detector.
