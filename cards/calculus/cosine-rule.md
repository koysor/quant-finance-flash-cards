# Cosine Rule

**Topic:** Calculus
**Tags:** trigonometry, triangle, cosine, law of cosines, portfolio variance
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Cosine Rule** (Law of Cosines) relates the lengths of the three sides of any triangle to the cosine of one of its angles. It generalises Pythagoras' theorem to non-right-angled triangles and reduces to $c^2 = a^2 + b^2$ when $C = 90°$.

## Key Formula

$$c^2 = a^2 + b^2 - 2ab\cos(C)$$

where $a$, $b$, $c$ are side lengths and $C$ is the angle opposite side $c$.

Rearranged to find an angle:

$$\cos(C) = \frac{a^2 + b^2 - c^2}{2ab}$$

## Example

A triangle has sides $a = 5$, $b = 7$ and included angle $C = 60°$.

$$c^2 = 25 + 49 - 2(5)(7)\cos(60°) = 74 - 70 \times 0.5 = 39$$

$$c = \sqrt{39} \approx 6.24$$

## Remember

The Cosine Rule is structurally identical to the **two-asset portfolio variance formula**. Setting $a = w_1\sigma_1$ and $b = w_2\sigma_2$:

$$\sigma_P^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1 w_2 \sigma_1\sigma_2\rho_{12}$$

This maps exactly onto the Cosine Rule with $\cos(C) = -\rho_{12}$. A correlation of $-1$ corresponds to $C = 180°$ (anti-parallel assets, maximum diversification); $\rho = 0$ to $C = 90°$ (Pythagorean addition of risks); $\rho = +1$ to $C = 0°$ (identical direction, no diversification benefit).
