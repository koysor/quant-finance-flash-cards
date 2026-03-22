# Yield Curve Risk

**Topic:** Banking Regulation
**Tags:** yield curve risk, IRRBB, non-parallel shift, steepening, flattening, twist
**Created:** 2026-03-22
**Author:** Claude Opus 4.6

---

## Definition

**Yield curve risk** is the IRRBB sub-risk arising from non-parallel changes in the shape of the yield curve — steepening, flattening, or twisting — that affect the bank's assets and liabilities differently depending on their tenor. A bank may be hedged against parallel shifts but still exposed to curve reshaping if the duration of its assets and liabilities is concentrated at different points on the curve.

## Key Formula

Under a non-parallel shock, the change in economic value is:

$$\Delta\text{EVE} = \sum_{k=1}^{n} PV01_k \times \Delta r_k$$

where $PV01_k$ is the present-value sensitivity at tenor vertex $k$ and $\Delta r_k$ is the shock at that tenor.

Basel prescribes six standard scenarios:

| Scenario | Short end | Long end |
|---|---|---|
| Parallel up | $+\Delta$ | $+\Delta$ |
| Parallel down | $-\Delta$ | $-\Delta$ |
| Steepener | $-\Delta_s$ | $+\Delta_l$ |
| Flattener | $+\Delta_s$ | $-\Delta_l$ |
| Short rate up | $+\Delta_s$ | $0$ |
| Short rate down | $-\Delta_s$ | $0$ |

## Example

A bank has $PV01 = +£50{,}000$ at the 1-year vertex and $PV01 = -£80{,}000$ at the 10-year vertex (net position from assets minus liabilities).

Under a **steepener** (short rates fall 50 bps, long rates rise 100 bps):

$$\Delta\text{EVE} = 50{,}000 \times (-0.0050) + (-80{,}000) \times 0.0100$$

$$= -250 + (-800) = -£1{,}050$$

The bank loses EVE despite having offsetting PV01s, because the curve reshaped unfavourably.

## Remember

Yield curve risk explains why duration gap alone is insufficient for IRRBB management — a bank can have a zero duration gap (immunised against parallel shifts) yet still suffer large losses from curve steepening or flattening. The 2022–2023 rate hiking cycle demonstrated this vividly: rapid short-rate increases inverted the curve, crushing the profitability of banks that had assumed rates would move in parallel. Basel's six prescribed shock scenarios are designed to capture yield curve risk explicitly, and banks must report the worst-case EVE impact across all six. ALM teams use key-rate duration (PV01 by tenor bucket) rather than a single duration number to manage this risk.
