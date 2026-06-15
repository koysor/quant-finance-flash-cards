# Bond Pricing Equation

**Topic:** Fixed Income
**Tags:** bond pricing, risk-neutral pricing, discount factor, short rate, feynman-kac, term structure
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

The **bond pricing equation** is the risk-neutral expectation formula that gives the no-arbitrage price of a zero-coupon bond in terms of the future path of the short rate. It is the fundamental starting point from which all short-rate models — Vasicek, CIR, Hull–White — derive their bond pricing formulae.

## Key Formula

The time-$t$ price of a zero-coupon bond paying £1 at maturity $T$ is:

$$P(t, T) = E_t^Q\!\left[\exp\!\left(-\int_t^T r_s\,ds\right)\right]$$

where $r_s$ is the short rate at time $s$ and $E_t^Q[\,\cdot\,]$ is the expectation under the **risk-neutral measure** $Q$, conditional on information at time $t$.

A coupon bond with cash flows $C_i$ at times $t_i$ is then a sum:

$$P_{\text{coupon}}(t) = \sum_{i} C_i \cdot P(t,\, t_i)$$

The integral $\int_t^T r_s\,ds$ is the **continuously compounded discount** accumulated over the life of the bond; $\exp(-\int r_s\,ds)$ is the corresponding stochastic discount factor for each path.

## Example

Under the Vasicek model, $r_s$ is Gaussian with known conditional distribution under $Q$. Because the integral of a Gaussian process is Gaussian, the expectation can be evaluated in closed form:

$$P(t,T) = \exp\!\bigl(A(\tau) - B(\tau)\,r_t\bigr), \quad \tau = T - t$$

with $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$ and $A(\tau)$ a deterministic function of model parameters. For $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.01$, $r_t = 0.03$, $\tau = 1$: $B \approx 0.787$, so $P \approx e^{A - 0.787 \times 0.03}$ — a discount factor slightly above $e^{-0.03} \approx 0.970$.

## Remember

The bond pricing equation connects stochastic calculus to term structure via Feynman–Kac: the same quantity $P(t,T)$ that satisfies the fixed-income PDE (derived from hedging two bonds) equals the conditional expectation above (derived from risk-neutral pricing). This duality means bond prices can be computed either by solving a PDE backwards from $V(r,T)=1$, or by simulating short-rate paths and averaging the discount factors — two routes to the same answer that underpin all Monte Carlo and lattice methods in interest rate modelling.
