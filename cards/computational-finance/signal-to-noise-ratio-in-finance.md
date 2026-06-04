# Signal-to-Noise Ratio in Finance

**Topic:** Computational Finance
**Tags:** signal-to-noise ratio, alpha decay, sharpe ratio, information ratio, factor signal
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

The **signal-to-noise ratio (SNR)** in finance measures how much genuine predictive information (signal) a factor or strategy contains relative to random variation (noise). A high SNR indicates a factor whose predictions are reliably correct; a low SNR — the norm in financial markets — means that even a genuine alpha signal is overwhelmed by random returns, making it extremely difficult to distinguish skill from luck in short samples.

## Key Formula

For a trading signal $f_t$ predicting next-period returns $r_{t+1}$, the SNR is:

$$\text{SNR} = \frac{\text{Var}(\mathbb{E}[r_{t+1} \mid f_t])}{\text{Var}(r_{t+1} \mid f_t)} = \frac{\sigma_\alpha^2}{\sigma_\varepsilon^2}$$

where $\sigma_\alpha^2$ is the variance of the predictable component and $\sigma_\varepsilon^2$ is the variance of the unpredictable residual. The **information ratio** is related:

$$\text{IR} = \frac{\mu_\alpha}{\sigma_\alpha} \approx \text{IC} \times \sqrt{N}$$

where IC (information coefficient) is the correlation between signal and realised return, and $N$ is the number of independent bets. The minimum number of observations to detect a signal with power $1-\beta$ at significance level $\alpha$ is:

$$T \geq \left(\frac{z_{1-\alpha/2} + z_{1-\beta}}{\text{SNR}}\right)^2$$

## Example

A momentum factor has IC = 0.05 (correlation between signal and next-month return). The residual volatility is $\sigma_\varepsilon = 15\%$ per month. SNR $\approx$ IC $= 0.05$ — very low. To detect this signal at 95% confidence with 80% power:

$$T \geq \left(\frac{1.96 + 0.84}{0.05}\right)^2 = (56)^2 = 3{,}136 \text{ months} \approx 261 \text{ years}$$

This illustrates why backtesting financial signals is so difficult: even genuine factors require implausibly long histories to be statistically confirmed.

## Remember

The low SNR of financial data is the fundamental reason why **overfitting is endemic in quantitative finance**: with hundreds of candidate factors and only decades of monthly returns, the probability of finding a spuriously significant signal by data mining is very high. Lopez de Prado's research shows that most backtested strategies are overfit — the "discovered" alpha is largely noise. This motivates techniques like walk-forward testing, combinatorially symmetric cross-validation (CSCV), and the deflated Sharpe ratio, all of which correct for the multiple testing problem that low SNR makes severe. It also explains why ML models trained on financial data require far more regularisation than those trained on image or text data.
