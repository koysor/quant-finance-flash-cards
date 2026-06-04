# Neural Network Model Calibration

**Topic:** Computational Finance
**Tags:** model calibration, neural network, surrogate model, implied volatility, heston
**Created:** 2026-06-05
**Author:** Claude Sonnet 4.6

---

## Definition

**Neural network model calibration** replaces the slow iterative optimisation used to fit financial models (e.g. Heston, SABR) to observed market prices with a pre-trained neural network that maps market observables directly to model parameters. The network acts as a **surrogate** (or emulator) for the pricing function, enabling near-instantaneous calibration at inference time after a one-time expensive training phase.

## Key Formula

Classical calibration solves:

$$\hat{\theta} = \arg\min_\theta \sum_{i=1}^{N} w_i \left(C_i^{\text{market}} - C_i^{\text{model}}(\theta)\right)^2$$

where $C_i^{\text{model}}(\theta)$ requires hundreds of PDE or Monte Carlo evaluations per iteration. Neural network calibration instead trains a network $f_\phi$ (offline) so that:

$$\hat{\theta} \approx f_\phi\!\left(C_1^{\text{market}}, \ldots, C_N^{\text{market}}\right)$$

The network maps the vector of observed prices directly to parameters in a single forward pass — reducing calibration time from minutes to milliseconds.

## Example

**Heston model calibration** to S&P 500 option surface (50 strikes × 10 maturities = 500 implied vols). Classical calibration via Levenberg–Marquardt: ~200 pricing evaluations, each taking 5 ms via characteristic function → ~1 second total.

Neural network surrogate: train a feedforward network (3 hidden layers, 256 units) on $10^6$ synthetic $(\theta, \text{vol surface})$ pairs. At inference: feed the 500 observed vols → output $(\kappa, v_0, \bar{\theta}, \rho, \xi)$ in < 1 ms. Calibration error vs classical: < 0.3 vol point on average.

## Remember

Real-time model calibration is a central operational requirement for options trading desks: Greeks, hedges, and risk sensitivities all depend on freshly calibrated model parameters that reflect current market conditions. Neural network surrogates make it feasible to recalibrate every second rather than every few minutes — critical for fast-moving markets. The same technique applies to SABR, Local Volatility, and rough volatility models (Rough Bergomi), where classical calibration is especially slow. The key trade-off is generalisation: the surrogate is only reliable for parameter regimes covered by the training set, so out-of-distribution market conditions (e.g. a vol spike to 80%) require retraining or blending with classical methods.
