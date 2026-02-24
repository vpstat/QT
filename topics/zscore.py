import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>🎯 Z-Score & Standardization</h1>
        <p>Measuring relative standing and making valid comparisons across different distributions.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── INTRODUCTION ──────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
A **z-score** (standard score) measures how many standard deviations a data point is from the mean. It solves the comparison problem: *"Who performed better — a student who scored 75 on Math or 70 on English?"* — when the tests have different means and spreads.

Z-scores allow **standardized comparisons**, **outlier detection**, and transform any normal distribution to the **standard normal distribution** (μ=0, σ=1).
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── CONCEPTS ─────────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Population Z-Score")
        st.latex(r"z = \frac{x - \mu}{\sigma}")

        st.markdown("#### Sample Z-Score")
        st.latex(r"z = \frac{x - \bar{x}}{s}")

        st.markdown("#### Back-Transform (Unstandardize)")
        st.latex(r"x = \mu + z \cdot \sigma")

        st.markdown("#### Standardizing a Variable")
        st.latex(r"Z = \frac{X - \mu}{\sigma} \sim \mathcal{N}(0, 1) \quad \text{if } X \sim \mathcal{N}(\mu, \sigma^2)")

    with col2:
        st.markdown("#### Outlier Detection via Z-Score")
        st.latex(r"|z| > 3 \Rightarrow \text{potential outlier (99.7\% rule)}")
        st.latex(r"|z| > 2 \Rightarrow \text{unusual observation (95\% rule)}")

        st.markdown("#### Z-Score Properties")
        st.markdown("""
- Mean of z-scores = **0**
- SD of z-scores = **1**
- z-scores are **dimensionless** (unitless)
- Sum of z-scores = **0** (always)
        """)

        st.markdown("#### Interpretation Guide")
        st.markdown("""
| z | Interpretation |
|---|----------------|
| z = 0 | At the mean |
| z = +1 | 1 SD above mean |
| z = −2 | 2 SD below mean |
| z > +3 | Extreme high value |
| z < −3 | Extreme low value |
        """)

    st.markdown("---")
    st.markdown("#### 📊 Standardized Comparison Demo")

    col1, col2 = st.columns([1, 2])
    with col1:
        x_math = st.number_input("Math score:", value=75, min_value=0, max_value=100)
        mean_math = st.number_input("Math class mean:", value=65.0)
        sd_math = st.number_input("Math class SD:", value=10.0)
        x_eng = st.number_input("English score:", value=70, min_value=0, max_value=100)
        mean_eng = st.number_input("English class mean:", value=60.0)
        sd_eng = st.number_input("English class SD:", value=8.0)

    with col2:
        z_math = (x_math - mean_math) / sd_math
        z_eng = (x_eng - mean_eng) / sd_eng
        st.markdown(f"#### Results")
        st.latex(r"z_{\text{Math}} = \frac{" + str(x_math) + r" - " + str(mean_math) + r"}{" + str(sd_math) + r"} = " + f"{z_math:.3f}")
        st.latex(r"z_{\text{English}} = \frac{" + str(x_eng) + r" - " + str(mean_eng) + r"}{" + str(sd_eng) + r"} = " + f"{z_eng:.3f}")
        if z_math > z_eng:
            st.success(f"📊 Math performance is **relatively better** (z={z_math:.2f} > z={z_eng:.2f})")
        elif z_eng > z_math:
            st.success(f"📊 English performance is **relatively better** (z={z_eng:.2f} > z={z_math:.2f})")
        else:
            st.info("Both performances are equally good relative to their classes.")
        st.info(f"Percentile (approx): Math ≈ {stats.norm.cdf(z_math)*100:.1f}th, English ≈ {stats.norm.cdf(z_eng)*100:.1f}th")

    st.markdown("</div>", unsafe_allow_html=True)

    # ── SOLVED PROBLEMS ───────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Dataset: {10, 15, 20, 25, 30, 35, 40}. Compute z-score for x = 35.

**Solution:**

Mean x̄ = (10+15+20+25+30+35+40)/7 = 175/7 = 25

s² = [(15²+10²+5²+0²+5²+10²+15²)]/6 = [225+100+25+0+25+100+225]/6 = 700/6 ≈ 116.67

s = √116.67 ≈ 10.80
    """)
    st.latex(r"z = \frac{35 - 25}{10.80} \approx \frac{10}{10.80} \approx +0.926")
    st.markdown("x=35 is **0.926 standard deviations above the mean** — slightly above average, not unusual.")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Class A: μ=70, σ=8. Class B: μ=75, σ=15. Student A scored 82, Student B scored 90. Who performed better relative to their class?

**Solution:**
    """)
    st.latex(r"z_A = \frac{82-70}{8} = \frac{12}{8} = +1.50")
    st.latex(r"z_B = \frac{90-75}{15} = \frac{15}{15} = +1.00")
    st.markdown("""
**Student A (z=1.50) performed better relative to their class.**

Despite scoring lower in absolute terms (82 vs 90), Student A ranked higher *within their own distribution*. Student A is in approximately the 93rd percentile; Student B is at the 84th percentile.
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A distribution has μ=50, σ=10. Find the value 1.5 standard deviations above the mean. Also find the value at z = −2.

**Solution:**

**x for z = +1.5:**
    """)
    st.latex(r"x = \mu + z\sigma = 50 + 1.5(10) = 50 + 15 = 65")
    st.latex(r"x = \mu + z\sigma = 50 + (-2)(10) = 50 - 20 = 30")
    st.markdown("**z = −2 corresponds to x = 30** → 30 is 2 SD below the mean.")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 4 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Dataset: {12, 15, 14, 18, 200, 13, 16, 14}. Identify outliers using z-score method (|z| > 2).

**Solution:**

n=8, Sum=302, Mean=302/8=37.75… wait — let's compute precisely.

Mean = (12+15+14+18+200+13+16+14)/8 = 302/8 = **37.75**

Variance: compute Σ(xᵢ-x̄)²:  
(12-37.75)²=663.0, (15-37.75)²=517.6, (14-37.75)²=564.1, (18-37.75)²=390.1, (200-37.75)²=26379.6, (13-37.75)²=612.6, (16-37.75)²=473.1, (14-37.75)²=564.1  
Sum=30164.1, s²=30164.1/7=4309.2, **s=65.64**

Z-scores: 
- x=200: z=(200-37.75)/65.64 = **+2.47** → |z|>2 → **OUTLIER** ✅
- All others: |z| < 1 → normal

Removing 200: New mean=(102/7)≈14.57, s≈1.99 — completely different distribution!
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── TRICKY QUESTIONS ─────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** All z-scores in a dataset sum to 0. Prove this algebraically.")
    with st.expander("🔍 Reveal Solution"):
        st.latex(r"\sum_{i=1}^{n} z_i = \sum_{i=1}^{n} \frac{x_i - \bar{x}}{s} = \frac{1}{s}\sum_{i=1}^{n}(x_i - \bar{x})")
        st.latex(r"= \frac{1}{s}\left(\sum_{i=1}^{n} x_i - n\bar{x}\right) = \frac{1}{s}\left(n\bar{x} - n\bar{x}\right) = \frac{0}{s} = 0 \quad \blacksquare")
        st.markdown("This is a fundamental identity: the **sum of deviations from the mean is always zero**, which carries over to z-scores.")

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Can z-scores be used to compare data from non-normal distributions? Are z-score outlier thresholds (|z|>2 or |z|>3) universal?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**Z-scores CAN be computed for any distribution** — they don't require normality.

However, the interpretation thresholds **DO depend on distribution shape**:
- For **normal distributions**: |z|>2 → ~5% of data; |z|>3 → ~0.3% of data (the familiar 68-95-99.7 rule)
- For **non-normal distributions**: these percentages change dramatically

**Chebyshev's Inequality** provides a distribution-free guarantee:
- At least 75% of data lies within 2 SDs (regardless of distribution)
- At least 89% within 3 SDs

So while |z|>3 signals an outlier for any distribution, for highly skewed or heavy-tailed distributions, even z=4 or z=5 might not be truly rare.

**Best practice:** Use IQR/Tukey fences for outlier detection in non-normal data, and z-scores specifically for normal data.
        """)
    st.markdown("</div>", unsafe_allow_html=True)
