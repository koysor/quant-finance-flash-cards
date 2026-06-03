# Breakeven Inflation

**Topic:** Fixed Income
**Tags:** breakeven inflation, tips, inflation-linked bonds, real yield, inflation expectations, term structure
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

The breakeven inflation rate is the yield spread between a nominal bond and an inflation-linked bond (such as a TIPS) of the same maturity, representing the market's implied average inflation rate at which an investor would be indifferent between the two instruments.

## Key Formula

$$\text{Breakeven inflation}(\tau) = y_{\text{nominal}}(\tau) - y_{\text{real}}(\tau)$$

where $y_{\text{nominal}}$ is the nominal yield and $y_{\text{real}}$ is the real yield on the inflation-linked bond. Decomposing further:

$$\text{Breakeven}(\tau) = \underbrace{\mathbb{E}_t[\pi_{t,\tau}]}_{\text{expected inflation}} + \underbrace{ilp(\tau)}_{\text{inflation risk premium}}$$

where $ilp > 0$ means investors demand extra yield for bearing inflation uncertainty. The **real yield** $y_{\text{real}} = y_{\text{nominal}} - \text{breakeven}$ measures the expected purchasing-power return and enters the Taylor Rule as the relevant policy rate variable: monetary policy is restrictive when the real yield exceeds $r^*$.

## Example

US 10-year nominal Treasury yield: 4.50%. US 10-year TIPS yield: 2.10%. Breakeven inflation = 4.50% - 2.10% = 2.40%. This exceeds the Fed's 2% target, implying either expected inflation of 2.4% or expected inflation of 2.1% plus a 30bp inflation risk premium. When the Fed hiked aggressively in 2022, the 5-year breakeven fell from 3.6% to 2.4% in 6 months — a 120bp compression driven by the market repricing the Fed's credibility at controlling inflation.

## Remember

Breakeven inflation is the single most direct market measure of inflation expectations, which is why it appears in every central bank's communications and is the primary input for Taylor Rule forecasting. When the 5-year breakeven rises above 2.5% despite policy tightening, markets are signalling they doubt the central bank's credibility — this typically triggers additional hikes that are not priced into the short end, creating bear-flattener dynamics. Conversely, a breakeven collapse signals deflation risk, prompting the bull-steepener pattern that precedes major rate-cutting cycles.
