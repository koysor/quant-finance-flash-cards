# Variance Swap

**Topic:** Volatility
**Level:** A Level Mathematics
**Tags:** variance swap, realised variance, implied variance, volatility trading, convexity
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A variance swap is an over-the-counter derivative contract in which one party pays a fixed amount (the **variance strike** $K_{\text{var}}$) and receives the **realised variance** of an underlying asset over the contract period. The payoff is proportional to the difference between realised and implied variance, making it a pure bet on volatility without the path-dependency and delta-hedging complications of options. Variance swaps are the cleanest instrument for trading volatility as an asset class.

## Key Formula

The **payoff** at expiry:

$$\text{Payoff} = N_{\text{var}} \times (\sigma_{\text{realised}}^2 - K_{\text{var}})$$

where $N_{\text{var}}$ is the variance notional and $\sigma_{\text{realised}}^2$ is the annualised realised variance:

$$\sigma_{\text{realised}}^2 = \frac{252}{n} \sum_{i=1}^{n} \left(\ln \frac{S_i}{S_{i-1}}\right)^2$$

The **fair strike** (no-arbitrage) is determined by the portfolio of options that replicates variance:

$$K_{\text{var}} = \frac{2}{T} \left[\int_0^F \frac{P(K)}{K^2} dK + \int_F^{\infty} \frac{C(K)}{K^2} dK\right]$$

where $F$ is the forward price, $P(K)$ and $C(K)$ are put and call prices.

## Example

A 3-month variance swap on the FTSE 100 has strike $K_{\text{var}} = (18\%)^2 = 0.0324$ (quoted as 18 vol). The variance notional is £100,000 per variance point. Over the 3 months, realised volatility is 22%:

$$\sigma_{\text{realised}}^2 = (0.22)^2 = 0.0484$$

$$\text{Payoff} = £100{,}000 \times (0.0484 - 0.0324) = £100{,}000 \times 0.016 = £1{,}600$$

The long variance position profits because realised vol (22%) exceeded implied (18%). Note: in practice, notional is often quoted in **vega notional** terms, where $N_{\text{vega}} = N_{\text{var}} \times 2K_{\text{var}}^{0.5}$, to make the P&L approximately linear in volatility near the strike.

## Remember

Variance swaps are central to the volatility trading ecosystem at London hedge funds. The replication formula shows that the fair variance strike is determined by the prices of all out-of-the-money options across every strike — this is the theoretical basis of the VIX index and connects the options market to the volatility market. For quant developers, implementing variance swap pricing requires building a complete volatility surface, integrating over strikes, and handling the discrete-monitoring adjustment (the difference between continuous and daily-sampled variance). The convexity of the variance payoff in volatility means that long variance positions profit disproportionately from volatility spikes — a feature that makes them attractive as tail risk hedges.
