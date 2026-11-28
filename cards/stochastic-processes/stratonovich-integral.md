# Stratonovich Integral

**Topic:** Stochastic Processes
**Tags:** stratonovich, ito integral, stochastic integral, chain rule, midpoint rule, martingale
**Created:** 2026-11-28
**Author:** Claude Opus 5.5

---

## Definition

The **Stratonovich integral** $\int f(W_t) \circ dW_t$ is a stochastic integral built from sums that evaluate the integrand at the **midpoint** of each time step (the average of its two endpoint values) rather than at the start, as the Itô integral does. In exchange, the ordinary chain rule of calculus holds with no Itô correction, but the integral is no longer a martingale.

## Key Formula

Defined as a mean square limit of midpoint sums:

$$\int_0^T f(W_t) \circ dW_t = \underset{n \to \infty}{\text{ms-lim}} \sum_{j=1}^{n} \tfrac{1}{2}\bigl[f(W_{t_{j-1}}) + f(W_{t_j})\bigr]\bigl(W_{t_j} - W_{t_{j-1}}\bigr)$$

**Conversion to Itô:** the two differ by half a $dt$ integral:

$$\int_0^T f(W_t) \circ dW_t = \int_0^T f(W_t)\,dW_t + \frac{1}{2}\int_0^T f'(W_t)\,dt$$

For an SDE, the Stratonovich form $dX = a\,dt + b \circ dW$ is the same process as the Itô SDE

$$dX = \Bigl(a + \tfrac{1}{2}\,b\,\frac{\partial b}{\partial x}\Bigr)dt + b\,dW$$

## Example

Take $f(W) = W$ on $[0, 1]$, with the path ending at $W_1 = 1.2$.

**Stratonovich:** the midpoint sum telescopes exactly, because $\tfrac{1}{2}(W_{j-1} + W_j)(W_j - W_{j-1}) = \tfrac{1}{2}(W_j^2 - W_{j-1}^2)$. So, as in ordinary calculus,

$$\int_0^1 W \circ dW = \tfrac{1}{2}W_1^2 = \tfrac{1}{2}(1.2)^2 = 0.72$$

**Itô:** $\int_0^1 W\,dW = \tfrac{1}{2}W_1^2 - \tfrac{1}{2}(1) = 0.72 - 0.5 = 0.22$

The gap is $\tfrac{1}{2}\int_0^1 f'(W)\,dt = \tfrac{1}{2}(1)(1) = 0.5$. Averaged over all paths, the Itô integral has expected value $0$, while the Stratonovich one has $\mathbb{E}[\tfrac{1}{2}W_1^2] = 0.5$.

## Remember

Finance uses Itô, not Stratonovich, because a trader must fix a position **before** the price moves. Read $\int W \circ dW$ as the gains from holding $W$ units of a driftless asset. The midpoint rule sets each holding partly from the price at the end of the step, a price the trader cannot yet know. That foresight is worth exactly the expected gain of $0.5$ above, a profit on a fair game, which is an arbitrage. Itô's left-endpoint rule keeps gains a martingale and so keeps pricing arbitrage-free. Stratonovich still matters in practice. Smooth, real-world approximations of noise converge to Stratonovich solutions (the Wong-Zakai theorem), so a model written in Stratonovich form must be converted with the $\tfrac{1}{2}\,b\,\partial b/\partial x$ drift correction before it is used to price.
