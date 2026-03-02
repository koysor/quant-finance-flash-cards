# Zero-Drift Condition

**Topic:** Stochastic Processes
**Tags:** martingale, zero drift, Itô's lemma, risk-neutral pricing, change of variable
**Author:** Claude Opus 4.6

---

## Definition

The **zero-drift condition** is the requirement on a function $g(S)$ such that the process $g(S_t)$ has no deterministic drift — making it a **local martingale**. Given an SDE for $S$, one applies Itô's lemma to $g(S)$ and sets the drift equal to zero, yielding an ordinary differential equation for $g$.

## Key Formula

For an SDE $dS = B(S, t) \, dt + A(S, t) \, dW$, apply Itô's lemma to $g(S)$. The drift of $dg$ is:

$$B \frac{dg}{dS} + \frac{1}{2} A^2 \frac{d^2g}{dS^2}$$

Setting this to zero gives the ODE:

$$B \frac{dg}{dS} + \frac{1}{2} A^2 \frac{d^2g}{dS^2} = 0$$

which can be rearranged to:

$$\frac{d^2g}{dS^2} = -\frac{2B}{A^2} \frac{dg}{dS}$$

This is solvable when $2B / A^2$ depends only on $S$ (not on $t$), allowing direct integration.

**Example for GBM** ($B = \mu S$, $A = \sigma S$):

$$\frac{2B}{A^2} = \frac{2\mu S}{\sigma^2 S^2} = \frac{2\mu}{\sigma^2 S}$$

The ODE becomes $g'' = -\frac{2\mu}{\sigma^2 S} g'$, which is solved by separation of variables.

## Example

For GBM, separating variables in $g'' / g' = -2\mu / (\sigma^2 S)$ and integrating gives $\ln g' = -\frac{2\mu}{\sigma^2} \ln S + C$, so $g'(S) = K S^{-2\mu/\sigma^2}$. Integrating once more yields a power-law transformation of $S$ that removes the drift entirely.

## Remember

The zero-drift condition is the mathematical mechanism behind risk-neutral pricing. By finding the right transformation $g(S)$ that eliminates drift, you construct a martingale — a process where today's value is the best forecast of all future values ($\mathbb{E}[g(S_{t+\delta t}) \mid S_t] = g(S_t)$). This is precisely the property exploited by the equivalent martingale measure in derivative pricing.
