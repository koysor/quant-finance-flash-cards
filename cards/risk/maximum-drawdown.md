# Maximum Drawdown

**Topic:** Risk
**Tags:** maximum drawdown, risk, downside, peak-to-trough, hedge funds, performance
**Author:** Claude Opus 4.6

---

## Definition

Maximum drawdown (MDD) is the largest percentage decline from a peak to a subsequent trough in a portfolio's value before a new peak is reached. It measures the worst-case loss an investor would have experienced if they bought at the highest point and sold at the lowest, making it a direct measure of downside risk that captures the pain of real losses rather than statistical volatility.

## Key Formula

$$\text{MDD} = \max_{t \in [0,T]} \left[ \frac{\max_{s \in [0,t]} V_s - V_t}{\max_{s \in [0,t]} V_s} \right]$$

where $V_t$ is the portfolio value at time $t$. Equivalently, if $P_t = \max_{s \leq t} V_s$ is the running peak:

$$\text{Drawdown}_t = \frac{P_t - V_t}{P_t}, \quad \text{MDD} = \max_t \, \text{Drawdown}_t$$

The **Calmar ratio** uses MDD as the risk denominator:

$$\text{Calmar} = \frac{\bar{R}_{\text{annual}}}{\text{MDD}}$$

## Example

A fund's monthly values (£m) are: 100, 108, 112, 98, 95, 103, 110, 106, 115.

The running peak reaches 112 before the fund drops to 95:

$$\text{MDD} = \frac{112 - 95}{112} = \frac{17}{112} = 0.152 = 15.2\%$$

If the fund's annualised return is 12%:

$$\text{Calmar} = \frac{0.12}{0.152} = 0.79$$

A Calmar ratio below 1.0 means the worst drawdown exceeded the annual return — the investor needed patience to recover.

## Remember

Maximum drawdown captures what standard deviation cannot — the real experience of losing money. A fund with low volatility can still suffer a devastating drawdown if losses are persistent rather than large. Hedge fund investors pay close attention to MDD because it reveals tail risk and manager discipline in a way that symmetric measures like variance do not. In practice, many institutional mandates include a maximum drawdown limit (e.g. 10–15%) as a hard risk constraint alongside Value at Risk.
