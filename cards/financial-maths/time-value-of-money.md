# Time Value of Money

**Topic:** Financial Mathematics
**Level:** A Level Mathematics
**Tags:** TVM, discounting, compounding, present value, future value
**Created:** 2026-02-28
**Author:** Unknown

---

## Definition

**Time value of money (TVM)** is the principle that a sum of money today is worth more than the same sum in the future, because money today can be invested to earn a return.

## Key Formulae

**Future value** (amount received after n periods):

$$FV = PV \times (1 + r)^n$$

**Present value** (today's value of a future cash flow):

$$PV = \frac{FV}{(1 + r)^n}$$

**Continuous compounding** (used extensively in derivatives pricing):

$$FV = PV \times e^{rT}$$
$$PV = FV \times e^{-rT}$$

Where r is the continuously compounded rate and T is time in years.

## Example

What is the present value of £1,000 received in 3 years, if the discount rate is 5% per annum?

$$PV = \frac{1000}{(1.05)^3} = \frac{1000}{1.1576} \approx \textbf{£863.84}$$

## Remember

- **Discounting** converts future cash flows to today's value — the foundation of all valuation.
- In the Black-Scholes model and other derivatives formulae, the **risk-free discount factor** e^(−rT) appears to bring the expected future payoff back to a present value.
- **Net Present Value (NPV)** of a project = sum of all discounted cash flows minus initial investment. Accept the project if NPV > 0.
