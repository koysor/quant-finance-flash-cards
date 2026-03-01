# Model Limitations

**Topic:** Risk
**Tags:** limitations, fat tails, volatility clustering, model risk, assumptions

---

## Definition

The standard asset price model ($dS = \mu S \, dt + \sigma S \, dX$) assumes constant drift, constant volatility, independent returns, and normally distributed returns. Real markets violate all four assumptions, leading to systematic model risk that practitioners must account for.

## Key Formula

The model predicts extreme moves are vanishingly rare under the normal distribution:

$$P(|Z| > n) \quad \text{drops as} \quad e^{-n^2/2}$$

A 5-sigma daily move should occur once every 14,000 years, yet markets produce events of this magnitude every few years.

## Example

The October 1987 crash saw the S&P 500 fall 20.5% in a single day — roughly a 25-sigma event under the normal model. The probability of this is approximately $10^{-135}$, essentially zero. Yet it happened, demonstrating that real return distributions have much fatter tails than the model predicts.

## Remember

Model limitations directly affect every quantitative tool: Black-Scholes misprices deep out-of-the-money options (the volatility smile exists because of fat tails), parametric VaR underestimates tail risk, and constant-$\sigma$ hedging strategies fail during volatility spikes. Advanced models — GARCH, jump-diffusion, stochastic volatility — address these issues at the cost of complexity.
