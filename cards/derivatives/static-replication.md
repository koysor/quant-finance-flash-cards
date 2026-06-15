# Static Replication

**Topic:** Derivatives
**Tags:** static replication, payoff decomposition, variance swap, model-free, vanilla options, option strip
**Created:** 2026-06-15
**Author:** Claude Sonnet 4.6

---

## Definition

**Static replication** expresses any European payoff $f(S_T)$ as a fixed portfolio of vanilla calls, puts, cash, and a forward — assembled once at inception and held unchanged to maturity. Unlike dynamic delta hedging, no rebalancing is required.

## Key Formula

For any twice-differentiable payoff and a pivot $\kappa$ (typically the current forward price):

$$f(S_T) = f(\kappa) + f'(\kappa)\,(S_T - \kappa) + \int_0^{\kappa} f''(K)\,(K - S_T)^+\,dK + \int_{\kappa}^{\infty} f''(K)\,(S_T - K)^+\,dK$$

The **weight** on each put (strike $K < \kappa$) or call (strike $K > \kappa$) is the second derivative of the payoff at that strike: $f''(K)$. A convex payoff ($f'' > 0$) requires buying options; a concave payoff requires selling.

## Example

**Log contract** used in variance swap replication: $f(S_T) = -2\ln(S_T/\kappa)$.

Then $f'(K) = -2/K$ and $f''(K) = 2/K^2$. The replicating portfolio is:

- Short $2/\kappa$ units of forward
- Buy $2/K^2$ puts at each strike $K < \kappa$
- Buy $2/K^2$ calls at each strike $K > \kappa$

This $1/K^2$-weighted option strip is exactly how dealers hedge variance swaps using liquid vanilla options — a model-free result valid for any diffusion.

## Remember

Static replication is **model-free**: the portfolio weights $f''(K)$ depend only on the payoff shape, not on any assumption about the volatility process. This is why the VIX index, which approximates the fair value of a variance swap, is computed from a strip of quoted option prices without any model inputs. Whenever an exotic payoff can be decomposed as a smooth function of the terminal asset price, static replication converts it into a liquid hedge that survives model changes.
