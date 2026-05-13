# High Frequency Trading

**Topic:** Financial Mathematics
**Tags:** high frequency trading, hft, market microstructure, latency, algorithmic trading, co-location
**Created:** 2026-04-23
**Author:** Claude Sonnet 4.6

---

## Definition

**High-frequency trading (HFT)** is algorithmic trading characterised by extremely high order submission rates, very short holding periods (milliseconds to seconds), and strategies that exploit microstructure signals unavailable to slower participants. HFT firms compete on latency — the time from market data receipt to order transmission — using co-location (placing servers inside the exchange data centre), FPGA-based network processing, and C++ execution engines. The three principal HFT strategies are **market making** (posting quotes on both sides to earn the bid-ask spread), **latency arbitrage** (exploiting stale prices on slower venues), and **statistical arbitrage** (mean-reversion on correlated instruments at high frequency).

## Key Formula

**Market-making profit per round trip** (simplified):

$$\Pi_{\text{MM}} = \frac{s}{2} - \lambda \cdot |\Delta P|$$

where $s = P_{\text{ask}} - P_{\text{bid}}$ is the spread captured, $\lambda$ is the probability of trading against an informed order, and $|\Delta P|$ is the adverse price move after the trade. Market making is profitable only when $\frac{s}{2} > \lambda |\Delta P|$.

**Annualised Sharpe ratio** with $n$ trades per day, each with mean profit $\mu$ and standard deviation $\sigma$:

$$\text{SR}_{\text{annual}} = \sqrt{252 \cdot n} \cdot \frac{\mu}{\sigma}$$

High $n$ (thousands of trades per day) means HFT Sharpe ratios can exceed 5 even when per-trade edge is tiny.

## Example

Latency arbitrage on two S&P 500 ETFs — SPY and IVV:

| Event | Time | Action |
|-------|------|--------|
| SPY quote updates to £500.01 | $t = 0\,\mu\text{s}$ | — |
| HFT detects stale IVV quote at £499.98 | $t = 2\,\mu\text{s}$ | Buy IVV at £499.98 |
| IVV quote updates to £500.01 | $t = 50\,\mu\text{s}$ | — |
| HFT sells IVV at £500.01 | $t = 52\,\mu\text{s}$ | £0.03 profit per share |

At 10,000 such trades per day of 1,000 shares each, gross profit is £300,000 per day — but only while the firm maintains a latency advantage over competitors.

## Remember

HFT illustrates the distinction between **alpha** (genuine predictive skill) and **speed** (a structural information advantage). Latency arbitrage profits disappear once a slower competitor upgrades its infrastructure — the edge is not a forecast of future prices but a race to act on a stale quote first. For broader quantitative finance, the key lesson from HFT research is that **microstructure frictions are real and costly**: bid-ask spreads, market impact, and adverse selection must be explicitly modelled in any execution strategy. The Almgren-Chriss optimal liquidation model arose precisely because practitioners needed a rigorous framework for trading off market impact against timing risk when executing large orders, whether in HFT or traditional portfolio management.
