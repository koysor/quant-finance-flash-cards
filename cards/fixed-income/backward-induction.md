# Backward Induction

**Topic:** Fixed Income
**Tags:** backward induction, rate tree, callable bond, early exercise, lattice, bermudan
**Created:** 2026-06-21
**Author:** Claude Sonnet 4.6

---

## Definition

Backward induction is the algorithm for pricing fixed income securities on a rate tree: terminal payoffs are set at maturity, then the value at each earlier node is computed as the discounted risk-neutral expectation of the two successor nodes, with an early-exercise override applied at any date when the issuer or holder may exercise an embedded option.

## Key Formula

**Vanilla bond** (no optionality) at node $(t, j)$:

$$V_{t,j} = e^{-r_{t,j}\,\Delta t}\bigl[p\,V_{t+1,\,j+1} + (1-p)\,V_{t+1,\,j}\bigr] + C_t$$

where $C_t$ is any coupon paid at time $t$ and $p = \tfrac{1}{2}$ under the symmetric convention.

**Callable bond** — at each call date the issuer redeems at $K$ if doing so is cheaper than letting the bond continue:

$$V_{t,j} = C_t + \min\!\Bigl(K,\; e^{-r_{t,j}\,\Delta t}\bigl[p\,V_{t+1,\,j+1} + (1-p)\,V_{t+1,\,j}\bigr]\Bigr)$$

The $\min$ replaces $V$ with the call price $K$ whenever the continuation value exceeds $K$ — capturing the issuer's rational call decision at every node simultaneously.

## Example

Two-step tree, $\Delta t = 1$ yr, $p = \tfrac{1}{2}$: $r_0 = 5.00\%$; $r_u = 6.20\%$, $r_d = 5.80\%$ at $t = 1$.

A 6% annual coupon bond, face £100, callable at $K = £100$ after year 1.

**$t = 2$ (terminal):** $V_{2,\cdot} = 100 + 6 = £106$ at every node.

**$t = 1$ (apply call rule, then add coupon):**

$$\text{PV}_u = e^{-0.062} \times 106 = 0.9399 \times 106 = £99.63 \quad (\text{not called: } 99.63 < 100)$$
$$\text{PV}_d = e^{-0.058} \times 106 = 0.9437 \times 106 = £100.03 \quad (\text{called: } 100.03 > 100)$$

$$V_{1,u} = 6 + \min(100,\;99.63) = £105.63 \qquad V_{1,d} = 6 + \min(100,\;100.03) = £106.00$$

**$t = 0$:**

$$V_0 = e^{-0.05}\bigl[\tfrac{1}{2}(105.63) + \tfrac{1}{2}(106.00)\bigr] = 0.9512 \times 105.82 \approx \textbf{£100.65}$$

The straight (non-callable) bond prices at £101.46; the £0.81 difference is the value of the call option to the issuer.

## Remember

The early-exercise $\min(\cdot)$ at each call node — or $\max(\cdot)$ for a Bermudan swaption receiver — is what makes backward induction the standard production pricing engine for bonds and derivatives with embedded optionality. No closed-form formula can encode this node-by-node decision; the tree resolves it automatically, one comparison per node. The same algorithm also handles step-up coupons, lockout periods, and make-whole provisions by simply changing the exercise condition at the relevant nodes.
