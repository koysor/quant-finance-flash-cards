# Sine Rule

**Topic:** Calculus
**Tags:** trigonometry, triangle, sine, law of sines, proportionality
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The **Sine Rule** (Law of Sines) states that in any triangle the ratio of each side to the sine of its opposite angle is constant, and equals the diameter of the circumscribed circle. It applies to all triangles — acute, obtuse, and right-angled.

## Key Formula

$$\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$$

where $a$, $b$, $c$ are side lengths, $A$, $B$, $C$ are the opposite angles, and $R$ is the circumradius.

**Ambiguous case:** when two sides and a non-included angle are given, two distinct triangles may be consistent with the data.

## Example

A triangle has $a = 8$, $A = 35°$, $B = 65°$. Find side $b$.

First: $C = 180° - 35° - 65° = 80°$.

$$b = a \cdot \frac{\sin B}{\sin A} = 8 \times \frac{\sin 65°}{\sin 35°} = 8 \times \frac{0.9063}{0.5736} \approx 12.64$$

## Remember

The Sine Rule expresses a **proportionality** structure — each side scales with the sine of its opposite angle. This proportionality principle recurs throughout quantitative finance: in Fourier transform pricing, the sinusoidal basis functions $e^{i\omega x} = \cos(\omega x) + i\sin(\omega x)$ decompose an option payoff into frequency components, and the amplitude of each component is proportional to the sine (or cosine) of the corresponding phase angle. The Sine Rule builds the intuition that sine values encode relative magnitudes, not just angles.
