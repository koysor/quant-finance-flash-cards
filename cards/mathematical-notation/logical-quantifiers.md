# Logical Quantifiers

**Topic:** Mathematical Notation
**Tags:** notation, logic, quantifiers, proof
**Author:** Claude Opus 4.6

---

## Definition

**Logical quantifiers** express statements about elements of a set. They are essential for writing precise mathematical definitions, theorems, and proofs.

Key symbols:

- $\forall$ — **for all** (universal quantifier): "$\forall x \in S, \; P(x)$" means "$P(x)$ is true for every $x$ in $S$"
- $\exists$ — **there exists** (existential quantifier): "$\exists x \in S \; \text{such that} \; P(x)$" means "at least one $x$ in $S$ makes $P(x)$ true"
- $\Rightarrow$ — **implies**: "$P \Rightarrow Q$" means "if $P$ is true then $Q$ is true"
- $\Leftrightarrow$ — **if and only if**: "$P \Leftrightarrow Q$" means "$P$ and $Q$ are logically equivalent"
- $\neg$ — **negation**: "$\neg P$" means "not $P$"

## Key Formula

**Negating a universal quantifier produces an existential:**

$$\neg (\forall x, \; P(x)) \equiv \exists x, \; \neg P(x)$$

**Negating an existential quantifier produces a universal:**

$$\neg (\exists x, \; P(x)) \equiv \forall x, \; \neg P(x)$$

**Contrapositive** (logically equivalent to the original implication):

$$(P \Rightarrow Q) \equiv (\neg Q \Rightarrow \neg P)$$

**Biconditional expansion:**

$$(P \Leftrightarrow Q) \equiv (P \Rightarrow Q) \wedge (Q \Rightarrow P)$$

## Example

The **no-arbitrage principle** in mathematical finance states:

$$\nexists \; \text{portfolio } \theta \; \text{such that} \; V_0(\theta) \leq 0 \; \text{and} \; P(V_T(\theta) \geq 0) = 1 \; \text{and} \; P(V_T(\theta) > 0) > 0$$

In plain English: there is no portfolio with zero or negative initial cost that has no chance of loss and a positive chance of profit. Equivalently, using the negation rule:

$$\forall \; \text{portfolios } \theta, \; \left(V_0(\theta) \leq 0 \text{ and } P(V_T(\theta) \geq 0) = 1\right) \Rightarrow P(V_T(\theta) > 0) = 0$$

## Remember

- **Coherent risk measure** axioms use $\forall$ extensively — for example, monotonicity states $\forall X, Y: X \leq Y \Rightarrow \rho(X) \geq \rho(Y)$.
- The **martingale** definition is a quantified statement: $\forall \, s \leq t, \; E[X_t \mid \mathcal{F}_s] = X_s$ — understanding the quantifier is essential to grasping what the property requires.
- **Proof by contradiction** works by assuming $\neg P$ and deriving a contradiction, which establishes $P$. The no-arbitrage principle is typically proved this way — assume an arbitrage exists, then construct a contradiction with market equilibrium.
