# Tree vs PDE Pricing

**Topic:** Computational Finance
**Tags:** finite difference, lattice, pde, backward induction, numerical methods, interest rate derivatives
**Created:** 2026-06-21
**Author:** Claude Sonnet 4.6

---

## Definition

Lattice (tree) methods and PDE finite-difference methods are two numerical implementations of the same no-arbitrage pricing equation for interest rate derivatives; they are mathematically equivalent under the explicit finite-difference scheme but differ in convergence order, implementation convenience, and suitability for different product structures.

## Key Formula

The bond pricing PDE in one-factor short-rate models:

$$\frac{\partial V}{\partial t} + \tfrac{1}{2}\sigma^2 \frac{\partial^2 V}{\partial r^2} + (\mu - \lambda\sigma)\frac{\partial V}{\partial r} - rV = 0$$

The **explicit finite-difference** discretisation of this PDE — approximating $\partial^2 V/\partial r^2$ and $\partial V/\partial r$ by centred differences — recovers **exactly** the trinomial backward-induction formula:

$$V_{t,j} = e^{-r_{t,j}\,\Delta t}\!\left[p_u\,V_{t+1,j+1} + p_m\,V_{t+1,j} + p_d\,V_{t+1,j-1}\right]$$

where $p_u, p_m, p_d$ are the finite-difference stencil weights. The **implicit** (Crank-Nicolson) scheme breaks this identity but achieves second-order accuracy in time — unavailable in the tree formulation.

## Example

A 5-year callable bond priced on a 100-step grid: the trinomial tree evaluates $100 \times 201 \approx 20{,}000$ nodes; an equivalent PDE on a $100 \times 200$ finite-difference grid evaluates the same count. Both give indistinguishable prices under the explicit scheme.

Switching to Crank-Nicolson halves the required grid steps (50 time steps give the same error as 100 explicit steps), roughly halving computation time. For a strongly path-dependent product such as an Asian rate option, the tree must track path history — exponentially many branches — while the PDE adds one state dimension (e.g. running average $A_t$) and remains an $O(N^2)$ grid.

## Remember

The tree-vs-PDE question is about **implementation convenience, not mathematical substance**: both solve the same PDE. Use a tree when discrete optionality (Bermudan swaptions, callable bonds) maps naturally to node comparisons and column-by-column calibration is transparent. Use a PDE grid when higher accuracy per unit of computation is needed (Crank-Nicolson) or when the model is multi-factor and a regular grid is cleaner than a bushy lattice. Reach for Monte Carlo when the product is strongly path-dependent and neither method is tractable.
