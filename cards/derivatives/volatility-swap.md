# Volatility Swap

**Topic:** Derivatives
**Tags:** volatility swap, variance swap, realised volatility, convexity adjustment, volatility trading
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

A **volatility swap** is an over-the-counter forward contract on future realised volatility. The buyer receives the realised volatility $\sigma_{\text{real}}$ and pays a fixed volatility strike $K_{\text{vol}}$ at expiry. Unlike a variance swap (which pays on $\sigma^2$), a volatility swap has a **linear** payoff in volatility, making it more intuitive for traders who think in vol terms. However, this linearity makes volatility swaps harder to replicate and price than variance swaps.

## Key Formula

The **payoff** at expiry:

$$\text{Payoff} = N_{\text{vol}} \times (\sigma_{\text{real}} - K_{\text{vol}})$$

where $N_{\text{vol}}$ is the notional per volatility point.

The **fair strike** of a volatility swap is related to the variance swap strike via a **convexity adjustment**:

$$K_{\text{vol}} \approx K_{\text{var}}^{1/2} - \frac{\text{Var}(\sigma_{\text{real}})}{8 \, K_{\text{var}}^{3/2}}$$

Since $\sqrt{x}$ is concave, Jensen's inequality gives $\mathbb{E}[\sigma] < \sqrt{\mathbb{E}[\sigma^2]}$, so the volatility swap strike is always **below** the implied volatility (the square root of the variance swap strike).

## Example

A 3-month variance swap on the FTSE 100 has a fair strike of $K_{\text{var}} = (20\%)^2 = 0.04$, implying $\sqrt{K_{\text{var}}} = 20\%$. The estimated standard deviation of realised volatility over the period is 4%.

$$K_{\text{vol}} \approx 0.20 - \frac{(0.04)^2}{8 \times (0.04)^{3/2}} = 0.20 - \frac{0.0016}{0.0640} = 0.20 - 0.025 = 17.5\%$$

The convexity adjustment knocks 2.5 points off the strike. A trader entering a long volatility swap at 17.5 vol who sees 20% realised volatility earns:

$$\text{Payoff} = N_{\text{vol}} \times (20\% - 17.5\%) = 2.5\% \times N_{\text{vol}}$$

## Remember

The convexity adjustment is the key distinction between volatility and variance swaps. Because the variance swap payoff is quadratic in volatility ($\sigma^2$), large volatility spikes generate disproportionately large payoffs — a feature valued by tail-risk hedgers. The volatility swap's linear payoff lacks this convexity, making it less attractive as a crash hedge but more predictable for directional volatility views. In practice, variance swaps dominate the institutional market because they can be statically replicated with a strip of options (the basis of the VIX calculation), whereas volatility swaps require dynamic hedging with a model-dependent strategy.
