# C++ in Quantitative Finance

**Topic:** Computational Finance
**Tags:** c++, performance, latency, compiled language, monte carlo, high frequency trading
**Created:** 2026-04-23
**Author:** Claude Sonnet 4.6

---

## Definition

**C++** is the dominant language for performance-critical quantitative finance systems because it compiles to native machine code with zero-overhead abstractions, giving direct control over memory layout, CPU cache utilisation, and SIMD vectorisation. It is used wherever latency or throughput requirements exceed what interpreted languages can deliver: high-frequency trading execution engines, bank-grade risk systems that must reprice millions of options in seconds, and adjoint algorithmic differentiation (AAD) libraries for XVA sensitivity computation.

## Key Formula

**Throughput** of a vectorised Monte Carlo kernel: modern C++ with AVX-256 processes 8 single-precision floats per instruction per CPU cycle. For $N$ paths of length $T$ on a CPU running at frequency $f$:

$$\text{wall time} \approx \frac{N \times T}{f \times W_{\text{SIMD}}}$$

where $W_{\text{SIMD}} = 8$ (AVX-256, 32-bit float). At $f = 3\,\text{GHz}$: 24 billion float operations per second, roughly **50× the throughput of a single-threaded Python loop** on the same hardware.

## Example

European call pricer in standard C++17:

```cpp
#include <cmath>
#include <random>

double mc_call(double S, double K, double r,
               double sigma, double T, int N) {
    std::mt19937_64 rng(42);
    std::normal_distribution<> dist(0.0, 1.0);
    double sum = 0.0;
    for (int i = 0; i < N; ++i) {
        double ST = S * std::exp((r - 0.5*sigma*sigma)*T
                                 + sigma*std::sqrt(T)*dist(rng));
        sum += std::max(ST - K, 0.0);
    }
    return std::exp(-r * T) * sum / N;
}
```

With $N = 10^7$ paths: Python/NumPy ≈ 4 s, C++ ≈ 80 ms (50× speedup). Adding OpenMP parallelism across 8 cores reduces this to ≈ 10 ms — within a typical intraday risk-reporting SLA.

## Remember

The rule of thumb on a trading desk is **Python for research, C++ for production**. A quant prototypes a new volatility model in Python in a day; the performance desk then rewrites the pricing kernel in C++ to meet sub-10 ms risk-reporting SLAs. C++ is also the only practical language for HFT execution engines, where the full loop — signal computation, risk check, order construction, and network transmission — must complete in under one microsecond. Understanding C++ performance concepts (cache lines, branch prediction, SIMD, memory alignment) is therefore part of the quant toolkit even for practitioners who never write production C++ themselves, because they must specify latency and throughput requirements for the engineers who implement their models.
