# Collateral Discounting

**Topic:** Fixed Income
**Tags:** collateral discounting, ois discounting, csa, overnight rate, derivative pricing, discounting big bang
**Created:** 2026-06-08
**Author:** Claude Sonnet 4.6

---

## Definition

**Collateral discounting** is the rule that collateralised derivatives must be discounted at the **overnight collateral rate** $c$ specified in the Credit Support Annex (CSA), not at LIBOR. The correct discount factor is the OIS discount factor $P^c(0,t)$, which accumulates at the collateral account rate.

## Key Formula

Value at time 0 of a collateralised derivative with payoff $V_u^c$ at time $u$:

$$V_0^c = \mathbb{E}^{\mathbb{X}}\!\left[(N_u^c)^{-1} V_u^c\right]$$

where $N_u^c = \exp\!\left(\int_0^u c_s\,ds\right)$ is the collateral account accumulating at rate $c$.

**OIS coupon pricing identity** — the PV of an overnight compounded coupon over $[s_0, s_n]$ telescopes to:

$$\text{PV}_{\text{OIS float}} = P^c(0, s_0) - P^c(0, s_n)$$

This works because the floating coupon and the discounting use the **same** overnight rate.

## Example

A 2-year USD OIS receives compounded SOFR. With $P^c(0,1) = 0.950$ and $P^c(0,2) = 0.902$, the PV of the floating leg (two annual periods) is:

$$\text{PV} = [P^c(0,0) - P^c(0,1)] + [P^c(0,1) - P^c(0,2)] = 1 - P^c(0,2) = 0.098 \text{ per unit notional}$$

## Remember

Before 2008, banks universally discounted derivatives at LIBOR. After mandatory CCP clearing (2012 Dodd-Frank, 2019 EMIR), the industry switched to OIS discounting — causing large one-off P&L moves across trading desks known as the **"discounting big bang."** The key principle: **the CSA dictates the discount rate**. If a swap has no CSA (uncollateralised), it must be discounted at a funding rate adjusted for credit risk (FVA), not OIS.
