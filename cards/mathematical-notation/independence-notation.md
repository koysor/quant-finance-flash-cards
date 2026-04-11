# Independence Notation

**Topic:** Mathematical Notation
**Tags:** notation, independence, conditional independence, perpendicular, probability
**Created:** 2026-04-11
**Author:** Claude Sonnet 4.6

---

## Definition

**Independence notation** uses the perpendicular symbol $\perp\!\!\!\perp$ to state that two random variables or events carry no information about each other. Conditional independence adds a vertical bar to restrict the statement to given information.

| Symbol | Read as | Meaning |
|---|---|---|
| $X \perp\!\!\!\perp Y$ | "X is independent of Y" | $f_{X,Y}(x,y) = f_X(x)\,f_Y(y)$; knowing $Y$ tells you nothing about $X$ |
| $A \perp\!\!\!\perp B$ | "A is independent of B" | $P(A \cap B) = P(A)\,P(B)$ |
| $X \perp\!\!\!\perp Y \mid Z$ | "X is independent of Y given Z" | $f_{X,Y \mid Z}(x,y\mid z) = f_{X\mid Z}(x\mid z)\,f_{Y\mid Z}(y\mid z)$ |
| $X \not\perp\!\!\!\perp Y$ | "X is not independent of Y" | The two variables are dependent |

## Key Formula

**Independence conditions (all equivalent):**

$$X \perp\!\!\!\perp Y \iff P(X \leq x,\, Y \leq y) = P(X \leq x)\,P(Y \leq y) \quad \forall\, x, y$$

$$\iff f_{X,Y}(x,y) = f_X(x)\,f_Y(y) \quad \text{(continuous case)}$$

$$\iff E[g(X)\,h(Y)] = E[g(X)]\,E[H(Y)] \quad \text{for all bounded measurable } g, h$$

**Consequence for covariance** (independence implies, but is not implied by, zero covariance):

$$X \perp\!\!\!\perp Y \implies \text{Cov}(X, Y) = 0$$

## Example

Daily log-returns of two companies in different sectors: $R_A \perp\!\!\!\perp R_B$ means $P(R_A > 2\%, R_B > 2\%) = P(R_A > 2\%)\,P(R_B > 2\%)$. However, during a market crisis, $R_A \not\perp\!\!\!\perp R_B \mid \text{crisis}$ — conditional on a market crash, the returns become strongly positively correlated, even if they appeared independent in normal times.

## Remember

The distinction between independence ($X \perp\!\!\!\perp Y$) and uncorrelated ($\text{Cov}(X,Y) = 0$) is critical in risk management. Two assets with zero correlation can still crash together during tail events — they are correlated but not linearly so. Independence is the stronger condition: it rules out all forms of dependence, not just linear. Copula models capture dependence beyond correlation precisely because real financial assets are rarely truly independent.
