# Label Construction

**Topic:** Computational Finance
**Tags:** supervised learning, triple barrier, financial machine learning, look-ahead bias, feature engineering, backtesting
**Created:** 2026-05-31
**Author:** Claude Sonnet 4.6

---

## Definition

**Label construction** is the process of defining the target variable $y_t$ that a supervised model is trained to predict from financial data, where the choice of labelling method determines the label formation horizon $\Delta$, the class balance, and the number of training observations that must be purged during cross-validation.

## Key Formula

**Fixed-horizon label** — simplest approach, binary direction over the next $h$ periods:

$$y_t = \text{sgn}\!\left(\frac{p_{t+h} - p_t}{p_t}\right), \qquad \Delta = h$$

**Triple-barrier label** — labels based on which barrier is hit first from time $t$:

$$y_t = \begin{cases} +1 & \text{upper barrier } p_t(1 + \tau^+) \text{ hit first} \\ -1 & \text{lower barrier } p_t(1 - \tau^-) \text{ hit first} \\ 0 & \text{time barrier } t + h \text{ expires first} \end{cases}$$

where $\tau^+$ and $\tau^-$ are profit-taking and stop-loss thresholds expressed as fractions of price. The label formation horizon $\Delta$ equals $h$ in the fixed-horizon case but is stochastic (up to $h$) in the triple-barrier case.

## Example

A model predicts next-day S&P 500 direction using fixed-horizon labels ($h = 1$, $\Delta = 1$). With triple-barrier labels using $\tau^+ = \tau^- = 0.5\%$ and $h = 5$ days, many trades close early: in a trending week the upper barrier is hit on day 2, giving $\Delta = 2$. This shorter, variable horizon reduces the number of observations to be purged — improving data efficiency — but introduces class imbalance because the neutral label (class 0) dominates in low-volatility regimes.

## Remember

The labelling decision is not merely cosmetic: it determines the entire downstream pipeline. Fixed-horizon labels are path-independent but noisy — a position can show a loss mid-journey yet return to profit by day $h$, mislabelling a good trade. Triple-barrier labels are path-dependent and risk-adjusted, reflecting how an actual trading strategy would behave with explicit profit targets and stop-losses. Critically, the label horizon $\Delta$ sets the minimum purge window in purged cross-validation: choosing $h = 20$ days forces 19 training observations to be removed near each test boundary, making label construction directly responsible for the amount of data lost during validation.
