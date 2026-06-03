# Almost Sure

**Topic:** Probability
**Tags:** almost sure, probability one, convergence, measure theory, martingale
**Created:** 2026-06-03
**Author:** Claude Sonnet 4.6

---

## Definition

An event $A$ occurs **almost surely** (a.s.) if $P(A) = 1$, meaning its complement has probability zero: $P(A^c) = 0$. Almost sure is stronger than "likely" but weaker than "always" — probability-zero events are not impossible, merely negligible under the measure. A sequence of random variables $X_n$ converges **almost surely** to $X$ if the set of outcomes where convergence fails has probability zero.

## Key Formula

$$X_n \xrightarrow{\text{a.s.}} X \iff P\!\left(\lim_{n \to \infty} X_n = X\right) = 1 \iff P\!\left(\{\omega : X_n(\omega) \to X(\omega)\}\right) = 1$$

Equivalently, for every $\varepsilon > 0$:

$$P\!\left(\limsup_{n \to \infty} \lvert X_n - X \rvert > \varepsilon\right) = 0$$

## Example

Brownian motion $W_t$ has paths of **infinite variation** almost surely. Concretely, for any partition $0 = t_0 < t_1 < \cdots < t_n = T$ with mesh $\to 0$:

$$P\!\left(\sum_{i=1}^{n} \lvert W_{t_i} - W_{t_{i-1}} \rvert \to \infty\right) = 1$$

The set of sample paths with finite variation has probability zero — they theoretically exist, but the measure assigned to them is nil.

## Remember

In quantitative finance, "almost sure" appears wherever martingale theory is applied. The **martingale convergence theorem** guarantees that a bounded martingale $M_t$ converges to a finite limit $M_\infty$ almost surely — this underpins the pricing of perpetual options and the existence of risk-neutral pricing measures. Crucially, it also explains why the Itô integral is well-defined: the quadratic variation of Brownian motion equals $t$ almost surely, giving the $dW_t^2 = dt$ rule in Itô's lemma a rigorous foundation.
