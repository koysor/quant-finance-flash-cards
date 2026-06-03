# Risk-Adjusted Return Objectives for RL

**Topic:** Computational Finance
**Tags:** reward function, sharpe ratio, sortino ratio, calmar ratio, maximum drawdown, reinforcement learning
**Created:** 2026-06-02
**Author:** Claude Sonnet 4.6

---

## Definition

The choice of reward signal in financial RL directly determines what behaviour the agent learns to optimise. Raw P&L rewards produce high-return but high-risk agents; **risk-adjusted objectives** embed return-per-unit-risk into the reward, steering the agent towards strategies that are practically deployable. Different risk-adjusted measures penalise different failure modes and produce qualitatively distinct trading policies.

## Key Formula

Four common per-episode or rolling reward signals:

**Sharpe-based** (penalises total volatility):
$$R_{\text{Sharpe}} = \frac{\mathbb{E}[r_t - r_f]}{\text{std}(r_t)}$$

**Sortino-based** (penalises downside volatility only):
$$R_{\text{Sortino}} = \frac{\mathbb{E}[r_t - r_f]}{\sqrt{\mathbb{E}[\min(r_t - r_f, 0)^2]}}$$

**Calmar-based** (penalises maximum drawdown):
$$R_{\text{Calmar}} = \frac{\text{annualised return}}{\text{max drawdown over episode}}$$

**CVaR-based** (penalises tail losses; coherent — see deep hedging):
$$R_{\text{CVaR}} = \mathbb{E}[r_t] - \lambda\,\text{CVaR}_\alpha(-r_t)$$

## Example

Three PPO agents trained on identical FTSE 100 futures data with different rewards. After 1,000 episodes:

| Objective | Annualised return | Sharpe | Max drawdown |
|---|---|---|---|
| Raw P&L | +28% | 0.9 | −22% |
| Sortino reward | +19% | 1.6 | −11% |
| Calmar reward | +14% | 1.4 | −6% |

The raw P&L agent earns the most but experiences large drawdowns that would trigger risk limits. The Calmar agent earns less but stays within a −10% drawdown budget, making it deployable within a real fund's mandate.

## Remember

Each risk-adjusted objective encodes a different **risk budget**: Sharpe treats upside and downside volatility symmetrically, so the agent avoids all large moves including profitable ones — it learns smooth, conservative strategies. Sortino allows large upside moves while penalising downside, producing more aggressive trend-following behaviour. Calmar is acutely sensitive to the single worst episode in training, producing highly defensive strategies that may sacrifice alpha to avoid any drawdown exceeding the historic maximum. For RL hedging agents on derivatives desks, CVaR-based rewards align most directly with regulatory capital requirements (FRTB Expected Shortfall), making them the natural choice when the hedging mandate is expressed in risk-capital terms.
