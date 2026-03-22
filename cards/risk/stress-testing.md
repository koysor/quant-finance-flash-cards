# Stress Testing

**Topic:** Risk
**Level:** A Level Mathematics
**Tags:** stress testing, scenario analysis, tail risk, risk management, regulation
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

Stress testing evaluates how a portfolio or financial institution would perform under extreme but plausible adverse scenarios. Unlike VaR, which estimates losses at a specified confidence level under normal conditions, stress tests explicitly model tail events — market crashes, interest rate shocks, liquidity freezes, or geopolitical crises. Stress tests can be **historical** (replaying past crises like 2008), **hypothetical** (constructing scenarios that have not yet occurred), or **reverse** (finding the scenario that would cause a specific loss threshold to be breached).

## Key Formula

The **stressed P&L** under a scenario with risk factor shocks $\Delta x_i$:

$$\Delta V \approx \sum_{i=1}^{n} \delta_i \cdot \Delta x_i + \frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} \Gamma_{ij} \cdot \Delta x_i \cdot \Delta x_j$$

where $\delta_i = \frac{\partial V}{\partial x_i}$ are first-order sensitivities and $\Gamma_{ij} = \frac{\partial^2 V}{\partial x_i \partial x_j}$ are second-order cross-sensitivities.

For a **reverse stress test**, find the scenario $\boldsymbol{\Delta x}^*$ that minimises the Mahalanobis distance subject to a loss constraint:

$$\boldsymbol{\Delta x}^* = \arg\min_{\boldsymbol{\Delta x}} \; \boldsymbol{\Delta x}^\top \Sigma^{-1} \boldsymbol{\Delta x} \quad \text{s.t.} \quad \Delta V(\boldsymbol{\Delta x}) \leq -L$$

## Example

A portfolio has £50 million in equities and £30 million in corporate bonds. A "2008 replay" stress scenario assumes equities fall 40% and credit spreads widen by 300 bps (reducing bond prices by 12%):

$$\Delta V_{\text{equities}} = £50{,}000{,}000 \times (-0.40) = -£20{,}000{,}000$$

$$\Delta V_{\text{bonds}} = £30{,}000{,}000 \times (-0.12) = -£3{,}600{,}000$$

$$\Delta V_{\text{total}} = -£23{,}600{,}000$$

The stressed loss is £23.6 million, or 29.5% of the £80 million portfolio. If the firm's capital is £25 million, this scenario leaves only £1.4 million of buffer — dangerously thin.

## Remember

Stress testing is where risk management moves beyond statistics into judgement. VaR tells you what can happen 99% of the time; stress testing asks what happens in the 1% that matters most. Since the 2008 financial crisis, regulators (Basel III, the Fed's CCAR, the Bank of England's ACS) require banks to run prescribed stress scenarios and demonstrate they can absorb the losses while maintaining minimum capital ratios. For quantitative funds, stress testing is equally critical — a strategy may have an excellent Sharpe ratio under normal conditions but be catastrophically exposed to a specific tail event that VaR does not capture.
