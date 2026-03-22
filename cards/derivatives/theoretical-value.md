# Theoretical Value

**Topic:** Derivatives
**Tags:** theoretical value, fair value, risk-neutral pricing, expected payoff, discounting
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

The **theoretical value** (or fair value) of a derivative is the price predicted by a pricing model, as opposed to the price observed in the market. Under no-arbitrage assumptions, the theoretical value equals the **discounted expected payoff under the risk-neutral measure**. When market price differs from theoretical value, the gap signals either a trading opportunity (if the model is trusted) or a model limitation (if the market is trusted). In practice, traders use theoretical value as a benchmark and investigate the reasons for any discrepancy.

## Key Formula

The general risk-neutral pricing formula:

$$V_0 = e^{-rT} \, \mathbb{E}^{\mathbb{Q}}[\text{Payoff}(S_T)]$$

where $\mathbb{E}^{\mathbb{Q}}$ denotes expectation under the risk-neutral measure and $r$ is the risk-free rate.

For a European call under Black-Scholes, this yields:

$$V_0^{\text{call}} = S_0 \, N(d_1) - K e^{-rT} N(d_2)$$

For a European put:

$$V_0^{\text{put}} = K e^{-rT} N(-d_2) - S_0 \, N(-d_1)$$

The **pricing error** (model vs market) is:

$$\varepsilon = V_{\text{market}} - V_{\text{theoretical}}$$

## Example

A European call has $S_0 = £100$, $K = £100$, $r = 5\%$, $\sigma = 20\%$, $T = 0.5$ years.

Using Black-Scholes:

$$d_1 = \frac{\ln(1) + (0.05 + 0.02) \times 0.5}{0.20 \times \sqrt{0.5}} = \frac{0.035}{0.1414} = 0.2475$$

$$d_2 = 0.2475 - 0.1414 = 0.1061$$

$$V_0 = 100 \times N(0.2475) - 100 e^{-0.025} \times N(0.1061) \approx 100(0.5977) - 97.53(0.5423) \approx £6.87$$

If the market price is £7.50, the pricing error is $\varepsilon = £7.50 - £6.87 = £0.63$. This could reflect the market pricing in higher volatility than 20%, or a limitation of Black-Scholes' constant-volatility assumption.

## Remember

Theoretical value is the bridge between mathematical models and real trading. When a trader says an option is "cheap" or "rich", they mean the market price is below or above their model's theoretical value. The key subtlety is that theoretical value depends entirely on the model and its inputs — change the volatility assumption and the theoretical value changes with it. This is why implied volatility (the $\sigma$ that makes theoretical value equal market price) became the industry's preferred quoting convention: it strips out the model mechanics and isolates the one subjective input. In quantitative finance, the theoretical value framework extends beyond Black-Scholes to Monte Carlo simulation, binomial trees, and finite difference methods — all computing the same discounted risk-neutral expectation with different numerical techniques.
