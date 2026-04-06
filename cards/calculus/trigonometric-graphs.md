# Trigonometric Graphs

**Topic:** Calculus
**Tags:** trigonometry, graphs, amplitude, period, phase shift, Fourier, sinusoidal
**Created:** 2026-04-06
**Author:** Claude Sonnet 4.6

---

## Definition

The graphs of $\sin$, $\cos$, and $\tan$ are periodic curves with characteristic shapes. A **transformed sinusoidal graph** $y = A\sin(Bx + C) + D$ is described by four parameters: amplitude $|A|$, period $2\pi/|B|$, phase shift $-C/B$, and vertical shift $D$.

## Key Formula

$$y = A\sin(Bx + C) + D$$

| Parameter | Effect |
|---|---|
| $|A|$ | Amplitude (half the peak-to-trough height) |
| $2\pi/|B|$ | Period (horizontal length of one full cycle) |
| $-C/B$ | Phase shift (horizontal translation) |
| $D$ | Vertical shift (midline) |

**Key graph facts:** $\sin$ and $\cos$ have range $[-1, 1]$ and period $2\pi$; $\tan$ has period $\pi$ and vertical asymptotes at $x = \pi/2 + n\pi$.

## Example

Identify the features of $y = 3\sin(2x - \pi/4) + 1$.

Rewrite as $y = 3\sin\!\left(2\left(x - \frac{\pi}{8}\right)\right) + 1$.

- Amplitude: $3$
- Period: $2\pi/2 = \pi$
- Phase shift: $\pi/8$ to the right
- Vertical shift: $+1$ (midline at $y = 1$, oscillating between $-2$ and $+4$)

## Remember

Fourier series decompose any periodic signal into a sum of sinusoidal graphs of different frequencies and amplitudes. In quantitative finance, **characteristic function pricing** (Lewis, Carr-Madan) works by representing an option payoff as a superposition of complex exponentials $e^{i\omega x} = \cos(\omega x) + i\sin(\omega x)$ — each a sinusoidal graph at angular frequency $\omega$. Reading off amplitude, frequency, and phase from a sinusoidal graph directly translates into reading the magnitude and argument of a characteristic function.
