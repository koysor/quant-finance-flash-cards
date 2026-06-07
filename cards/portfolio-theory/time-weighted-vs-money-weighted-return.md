# Time-Weighted vs Money-Weighted Return

**Topic:** Portfolio Theory & Asset Pricing
**Tags:** twrr, mwrr, irr, performance measurement, cash flows, manager evaluation
**Created:** 2026-06-07
**Author:** Claude Sonnet 4.6

---

## Definition

The **time-weighted return (TWRR)** measures the compound growth of £1 invested throughout the full period, removing the effect of investor cash flows — it isolates manager skill. The **money-weighted return (MWRR)**, also called the internal rate of return (IRR), is the discount rate that sets the net present value of all cash flows to zero — it reflects the investor's actual experience, which depends on the timing of contributions and withdrawals.

## Key Formula

**TWRR** — chain-link sub-period returns:

$$\text{TWRR} = \left(\prod_{k=1}^{n} (1 + r_k)\right)^{1/T} - 1$$

where $r_k$ is the return in sub-period $k$ (between cash flows) and $T$ is the total number of years.

**MWRR (IRR)** — solve for $r$ such that:

$$V_0 + \sum_{k=1}^{n} \frac{C_k}{(1+r)^{t_k}} = \frac{V_T}{(1+r)^T}$$

where $V_0$ is the initial value, $V_T$ is the terminal value, and $C_k$ is a cash flow (positive = inflow) at time $t_k$.

## Example

A fund starts at £100 and rises 50% to £150 in year 1. An investor adds £100 (total £250). In year 2 the fund falls 20%, ending at £200.

- **Sub-period returns:** $r_1 = +50\%$, $r_2 = -20\%$
- **TWRR:** $\sqrt{(1.50)(0.80)} - 1 = \sqrt{1.20} - 1 \approx +9.5\%$ p.a. (manager's perspective)
- **MWRR:** solve $100 + 100/(1+r) = 200/(1+r)^2$ → $r \approx -5.1\%$ p.a. (investor's experience — the large addition before the bad year destroys wealth)

## Remember

The TWRR–MWRR gap is a behavioural finance signature: investors tend to add money after good performance (buying high) and withdraw after bad performance (selling low), resulting in MWRR substantially below TWRR for most retail investors. GIPS (Global Investment Performance Standards) mandates TWRR for institutional manager reporting precisely because it strips out the timing decisions that are beyond the manager's control. MWRR is appropriate for private equity and infrastructure funds where the manager controls the timing of capital calls and distributions.

