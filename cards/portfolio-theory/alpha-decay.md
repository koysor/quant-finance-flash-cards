# Alpha Decay

**Topic:** Portfolio Theory & Asset Pricing
**Level:** A Level Mathematics
**Tags:** alpha decay, signal half-life, execution speed, capacity, crowding
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Alpha decay is the rate at which a trading signal's predictive power diminishes after the signal is generated. The moment a signal fires, its alpha begins to erode — through the trader's own execution (market impact), through other participants acting on similar information, and through natural price adjustment to new information. The **half-life** of alpha is the time it takes for half of the expected profit to disappear. Faster-decaying signals require faster execution; slower-decaying signals tolerate patient execution but typically offer lower returns.

## Key Formula

The **alpha decay curve** is commonly modelled as exponential:

$$\alpha(t) = \alpha_0 \cdot e^{-\lambda t}$$

where $\alpha_0$ is the initial signal strength and $\lambda$ is the decay rate.

The **half-life** of the signal:

$$t_{1/2} = \frac{\ln 2}{\lambda}$$

The **realised alpha** after execution delay $\tau$:

$$\alpha_{\text{realised}} = \alpha_0 \cdot \frac{1 - e^{-\lambda \tau}}{\lambda \tau}$$

This is the average alpha captured if the order is executed uniformly over the period $[0, \tau]$.

## Example

A mean-reversion signal has initial alpha $\alpha_0 = 20$ bps and a half-life of 30 minutes ($\lambda = \frac{\ln 2}{30} = 0.0231$ per minute).

If the order takes 10 minutes to execute:

$$\alpha_{\text{realised}} = 20 \times \frac{1 - e^{-0.0231 \times 10}}{0.0231 \times 10} = 20 \times \frac{1 - 0.794}{0.231} = 20 \times \frac{0.206}{0.231} = 17.8 \text{ bps}$$

If execution takes 2 hours (120 minutes):

$$\alpha_{\text{realised}} = 20 \times \frac{1 - e^{-0.0231 \times 120}}{0.0231 \times 120} = 20 \times \frac{1 - 0.063}{2.772} = 20 \times 0.338 = 6.8 \text{ bps}$$

Slow execution captures only a third of the available alpha.

## Remember

Alpha decay is the bridge between signal research and live trading — a brilliant signal is worthless if it decays faster than the fund can execute. For quant developers, understanding decay profiles determines the entire technology stack: sub-second decay requires co-located servers and FPGA hardware; minute-scale decay needs smart order routers; day-scale decay can use standard VWAP algorithms. Alpha decay also explains why strategies become less profitable as more capital chases them (crowding) — when many participants detect the same signal, their collective trading accelerates the price adjustment and shortens the half-life. Measuring and monitoring alpha decay in production is a core responsibility of any quant trading desk.
