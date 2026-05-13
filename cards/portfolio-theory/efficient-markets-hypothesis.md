# Efficient Markets Hypothesis

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** market efficiency, EMH, random walk, active management, asset pricing
**Created:** 2026-04-19
**Author:** Claude Sonnet 4.6

---

## Definition

The Efficient Markets Hypothesis (EMH) states that asset prices fully reflect all available information at all times. It implies that no investor can consistently earn risk-adjusted excess returns by exploiting available information, because prices already incorporate it.

Three forms describe which information set is reflected:
- **Weak form** — prices reflect all past trading data (price history, volume)
- **Semi-strong form** — prices reflect all publicly available information (earnings, news, analyst reports)
- **Strong form** — prices reflect all information, including private insider information

## Key Formula

Under the weak form, price changes follow a **random walk**:

$$P_t = P_{t-1} + \varepsilon_t, \qquad \varepsilon_t \sim (0, \sigma^2)$$

Where $\varepsilon_t$ is an unpredictable shock with mean zero. Expected excess return above the risk-free rate is zero:

$$\mathbb{E}[R_t - R_f \mid \mathcal{F}_{t-1}] = 0$$

## Example

A UK fund manager backtests a momentum strategy using 12-month price history and finds a Sharpe ratio of 1.2. Under the **weak form** of EMH, this historical pattern should already be priced in, so out-of-sample performance would revert to zero excess return. In practice, momentum is a well-documented anomaly — evidence that weak-form efficiency is imperfect.

## Remember

EMH is the theoretical foundation for **passive investing**: if markets are semi-strong efficient, fundamental analysis cannot beat the index after costs. The debate between efficient markets and observed anomalies (momentum, value, size premia) drives the entire active vs passive management industry. Fama's original evidence supports weak and semi-strong efficiency; strong form efficiency is widely rejected because insider trading bans exist precisely because insiders do earn excess returns.
