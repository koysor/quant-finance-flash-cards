# Spread Curve

**Topic:** Fixed Income
**Tags:** spread curve, credit spread, yield spread, relative value, fixed income, term structure
**Created:** 2026-03-11
**Author:** claude-sonnet-4-6

---

## Definition

A **spread curve** plots the yield premium (spread) of a bond or instrument over a benchmark at each maturity, rather than the absolute yield level. It expresses how much extra return an investor demands relative to a risk-free or reference curve — capturing credit risk, liquidity risk, or structural differences — as a function of tenor.

## Key Formula

For each maturity $T$, the spread is:

$$s(T) = r_{\text{instrument}}(T) - r_{\text{benchmark}}(T)$$

where $r_{\text{instrument}}(T)$ is the yield of the instrument and $r_{\text{benchmark}}(T)$ is the benchmark yield (e.g. gilts, OIS, or swaps) at the same maturity. The instrument yield can be decomposed as:

$$r_{\text{instrument}}(T) = r_{\text{risk-free}}(T) + s(T)$$

When the benchmark is the swap curve, the spread is called an **asset swap spread (ASW)**; when it is OIS, it is called a **Z-spread** if constant across all maturities, or a spread curve if it varies by tenor.

## Example

A UK corporate bond trader observes the following yields against gilts:

| Maturity | Gilt Yield | Corporate Yield | Spread |
|---|---|---|---|
| 2Y | 4.00% | 4.60% | +60 bps |
| 5Y | 4.20% | 5.05% | +85 bps |
| 10Y | 4.35% | 5.45% | +110 bps |

The upward-sloping spread curve indicates that investors demand progressively more compensation for credit and liquidity risk at longer maturities — a common pattern for investment-grade issuers where uncertainty compounds over time.

## Remember

Spread curves are the primary tool for relative-value analysis in credit and rates markets. A trader who believes a bond is cheap versus its peers compares spread curves rather than outright yields — because the outright yield mixes risk-free rates (which are market-wide) with the issuer-specific spread. Spread curve movements are also key risk signals: a widening spread curve across all tenors signals deteriorating credit conditions, while a flattening spread curve (long-end spreads narrowing towards short-end) can indicate that the market expects near-term stress but longer-term recovery. Credit default swap (CDS) curves and bond spread curves should theoretically align; any divergence is a potential arbitrage opportunity.
