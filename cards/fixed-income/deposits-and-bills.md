# Deposits and Bills

**Topic:** Fixed Income
**Tags:** deposit, bill, money market, add-on rate, discount rate, accrual factor
**Created:** 2026-06-08
**Author:** Claude Sonnet 4.6

---

## Definition

A **deposit** and a **bill** (or certificate of deposit) are both short-term money-market instruments that pay principal plus interest at maturity, but they differ in how the interest is quoted: deposits use an **add-on rate** (interest added to principal at maturity), while bills use a **discount rate** (interest deducted from principal at inception).

## Key Formula

Let $\delta$ be the accrual factor (year fraction), $R$ the annualised rate, and $N$ the notional.

**Deposit (add-on rate):** pay $N$ at $t_0$, receive at $t_1$:

$$\text{Receive at } t_1 = N(1 + \delta R)$$

**Bill / CD (discount rate):** pay at $t_0$, receive $N$ at $t_1$:

$$\text{Pay at } t_0 = N(1 - \delta R)$$

## Example

3-month period ($\delta = 90/360 = 0.25$), rate $R = 5\%$, notional $N = \$1{,}000{,}000$:

| Instrument | Pay at $t_0$ | Receive at $t_1$ |
|---|---|---|
| Deposit | \$1,000,000 | $1{,}000{,}000 \times (1 + 0.25 \times 0.05) = \$1{,}012{,}500$ |
| Bill | $1{,}000{,}000 \times (1 - 0.25 \times 0.05) = \$987{,}500$ | \$1,000,000 |

A 5% deposit rate and a 5% bill discount rate are **not equivalent** — the deposit earns more because interest is computed on the full principal, not the discounted price paid.

## Remember

The two conventions arose historically in different markets and remain in use today: deposits are OTC bilateral (no secondary market), whilst bills and CDs are securities that trade. In the multi-curve framework the accrual factor $\delta$ from a deposit's day count convention feeds directly into the forward rate $F^j = (1/\delta)(P^j(t,u)/P^j(t,v) - 1)$ — getting the day count wrong by one convention can move a large swap's PV by tens of thousands of pounds.
