# Fund of Funds

**Topic:** Financial Mathematics
**Tags:** fund of funds, diversification, hedge funds, portfolio construction, fees, alternative investments
**Author:** Claude Opus 4.6

---

## Definition

A fund of funds (FoF) is an investment vehicle that allocates capital across multiple underlying hedge funds rather than investing directly in securities. This provides diversification across strategies, managers, and risk factors, but introduces a double layer of fees that can significantly erode net returns.

## Key Formula

The **net return** after the double fee structure is:

$$R_{\text{net}} = R_{\text{gross}} - f_{\text{underlying}} - f_{\text{FoF}}$$

where $f_{\text{underlying}}$ is the aggregate fee drag from the underlying funds (typically "2 and 20": 2% management fee plus 20% performance fee) and $f_{\text{FoF}}$ is the fund of funds layer (typically 1% management plus 10% performance).

The **effective fee** on gross profits can be expressed as:

$$f_{\text{total}} = m_1 + m_2 + p_1 \cdot R_{\text{gross}} + p_2 \cdot (R_{\text{gross}} - m_1 - p_1 \cdot R_{\text{gross}})$$

where $m_1, m_2$ are management fees and $p_1, p_2$ are performance fee rates.

## Example

An underlying fund generates a gross return of 15%. With a "2 and 20" structure:

$$f_{\text{underlying}} = 0.02 + 0.20 \times 0.15 = 0.02 + 0.03 = 0.05$$

The return passed to the FoF is $0.15 - 0.05 = 0.10$ (10%). The FoF charges "1 and 10":

$$f_{\text{FoF}} = 0.01 + 0.10 \times 0.10 = 0.01 + 0.01 = 0.02$$

$$R_{\text{net}} = 0.10 - 0.02 = 0.08$$

From a 15% gross return, the investor receives only 8% — fees consumed nearly half the gains.

## Remember

Funds of funds were historically the primary way institutional investors accessed hedge funds, offering diversification and due diligence services. However, the double fee layer means that the underlying managers must generate substantial alpha just to break even for the end investor. Modern portfolio theory shows that diversification reduces idiosyncratic risk, but if the underlying funds are correlated, the FoF provides less diversification benefit than expected — making correlation analysis between underlying funds a critical part of FoF construction.
