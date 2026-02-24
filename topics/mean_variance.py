import streamlit as st
import numpy as np

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>➗ Mean, Variance & IQR</h1>
        <p>Measures of central tendency and spread — the core summary statistics of any dataset.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── INTRODUCTION ──────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
Every dataset can be characterized by two fundamental questions:
1. **Where is the center?** → Mean, Median, Mode
2. **How spread out is it?** → Variance, Standard Deviation, IQR

Together, these give a compact, powerful description of any distribution. Understanding which measure to use — and when — is a core statistical skill.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── CONCEPTS ─────────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📍 Measures of Center", "📏 Variance & SD", "📦 IQR & Percentiles"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Population Mean (μ)")
            st.latex(r"\mu = \frac{\sum_{i=1}^{N} x_i}{N}")

            st.markdown("#### Sample Mean (x̄)")
            st.latex(r"\bar{x} = \frac{\sum_{i=1}^{n} x_i}{n}")

            st.markdown("#### Weighted Mean")
            st.latex(r"\bar{x}_w = \frac{\sum_{i=1}^{n} w_i x_i}{\sum_{i=1}^{n} w_i}")

            st.markdown("#### Geometric Mean")
            st.latex(r"G = \left(\prod_{i=1}^{n} x_i\right)^{1/n} = \sqrt[n]{x_1 \cdot x_2 \cdots x_n}")

        with col2:
            st.markdown("#### Median")
            st.latex(r"\text{Median} = \begin{cases} x_{(n+1)/2} & \text{if } n \text{ odd} \\ \frac{x_{n/2}+x_{n/2+1}}{2} & \text{if } n \text{ even} \end{cases}")

            st.markdown("#### Mean from Grouped Data")
            st.latex(r"\bar{x} = \frac{\sum f_i m_i}{\sum f_i}")
            st.caption("fᵢ = class frequency, mᵢ = class midpoint")

            st.markdown("#### Relationship: Skewness & Averages")
            st.markdown("""
- Right-skewed: Mode < Median < Mean
- Symmetric: Mode = Median = Mean  
- Left-skewed: Mean < Median < Mode
            """)

    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Population Variance")
            st.latex(r"\sigma^2 = \frac{\sum_{i=1}^{N}(x_i - \mu)^2}{N}")

            st.markdown("#### Sample Variance")
            st.latex(r"s^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}")

            st.markdown("#### Computational (Shortcut) Formula")
            st.latex(r"s^2 = \frac{n\sum x_i^2 - (\sum x_i)^2}{n(n-1)}")

        with col2:
            st.markdown("#### Standard Deviation")
            st.latex(r"s = \sqrt{s^2} = \sqrt{\frac{\sum(x_i-\bar{x})^2}{n-1}}")

            st.markdown("#### Variance from Grouped Data")
            st.latex(r"s^2 = \frac{\sum f_i(m_i - \bar{x})^2}{n-1}")

            st.markdown("#### Coefficient of Variation")
            st.latex(r"\text{CV} = \frac{s}{\bar{x}} \times 100\%")

    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Percentile Location")
            st.latex(r"L_p = \frac{p}{100}(n+1)")
            st.caption("p = desired percentile, n = sample size")

            st.markdown("#### First Quartile (Q1)")
            st.latex(r"Q_1 = \text{value at } L_{25}")

            st.markdown("#### Third Quartile (Q3)")
            st.latex(r"Q_3 = \text{value at } L_{75}")

            st.markdown("#### IQR")
            st.latex(r"\text{IQR} = Q_3 - Q_1")

        with col2:
            st.markdown("#### Interquartile Mean")
            st.latex(r"\text{IQM} = \text{mean of middle 50\% of data}")

            st.markdown("#### Mid-Range")
            st.latex(r"\text{MidRange} = \frac{\text{Max} + \text{Min}}{2}")

            st.markdown("#### Why IQR over Range?")
            st.info("Range uses only 2 values (max/min) and is very sensitive to outliers. IQR represents the **middle 50%** and is **outlier-resistant**.")

    st.markdown("</div>", unsafe_allow_html=True)

    # ── SOLVED PROBLEMS ───────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Data: {8, 3, 5, 7, 2, 9, 4, 6, 1, 5}. Find mean, median, mode, and sample variance.

**Solution:**

Sorted: {1, 2, 3, 4, 5, 5, 6, 7, 8, 9}, n = 10

**Mean** = (8+3+5+7+2+9+4+6+1+5)/10 = 50/10 = **5**

**Median** = (5+5)/2 = **5** (average of 5th and 6th values)

**Mode** = **5** (appears twice)

This is **symmetric** (mean = median = mode = 5).

Deviations² from mean: 9,4,4,1,0,16,1,4,9,0,16 → wait, let's compute:  
(8-5)²=9, (3-5)²=4, (5-5)²=0, (7-5)²=4, (2-5)²=9, (9-5)²=16, (4-5)²=1, (6-5)²=1, (1-5)²=16, (5-5)²=0  
Sum = 60; **s²** = 60/9 ≈ **6.67**, **s** ≈ **2.582**
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A student scores: Maths (80, weight 4), Physics (70, weight 3), Chemistry (60, weight 2). Compute the weighted mean.

**Solution:**
    """)
    st.latex(r"\bar{x}_w = \frac{80\times4 + 70\times3 + 60\times2}{4+3+2} = \frac{320+210+120}{9} = \frac{650}{9} \approx 72.2")
    st.markdown("Simple (unweighted) mean = (80+70+60)/3 = 70. Weighted mean (72.2) is higher, reflecting Maths having 4× the weight.")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Compute mean and variance from this grouped frequency table:

| Class | Midpoint (m) | Frequency (f) |
|-------|-------------|---------------|
| 10–20 | 15 | 4 |
| 20–30 | 25 | 8 |
| 30–40 | 35 | 12 |
| 40–50 | 45 | 6 |

**Solution:**

n = Σf = 30, Σfm = 4(15)+8(25)+12(35)+6(45) = 60+200+420+270 = 950

**Mean** = 950/30 ≈ **31.67**

Σf(m−x̄)² = 4(15-31.67)²+8(25-31.67)²+12(35-31.67)²+6(45-31.67)²  
= 4(277.9)+8(44.5)+12(11.1)+6(177.9) = 1111.6+355.6+133.3+1067.4 = **2667.9**

**s²** = 2667.9/(30-1) = 2667.9/29 ≈ **91.99**, **s** ≈ **9.59**
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 4 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Investment returns over 4 years: 10%, 20%, −10%, 30%. Compute arithmetic mean and geometric mean. Which is the correct measure for investment performance?

**Solution:**

**Arithmetic Mean** = (10+20−10+30)/4 = 50/4 = **12.5%**

**Geometric Mean** = (1.10 × 1.20 × 0.90 × 1.30)^(1/4) − 1
    """)
    val = (1.10 * 1.20 * 0.90 * 1.30) ** 0.25 - 1
    st.latex(r"G = (1.10 \times 1.20 \times 0.90 \times 1.30)^{1/4} - 1")
    st.markdown(f"= (1.5444)^0.25 − 1 = 1.1144 − 1 ≈ **{val*100:.2f}%**")
    st.markdown("""
The **geometric mean (11.44%)** is the correct measure for investment performance — it represents the **compound annual growth rate (CAGR)**.

The arithmetic mean (12.5%) overstates performance when returns fluctuate. Verify: ₹100 × 1.10 × 1.20 × 0.90 × 1.30 = ₹154.44, which corresponds to (1.1144)⁴ = 1.5444 ✅
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── TRICKY QUESTIONS ─────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Dataset: {1, 2, 3, 4, 100}. Mean=22, Median=3. Which should represent 'typical' value? What does this reveal about salary/income data?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**Median = 3** is the better representation of "typical" value here. The mean (22) is pulled up by the extreme value (100), misrepresenting 4 out of 5 observations.

**Income data analogy:** If 4 workers earn ₹30,000 and 1 CEO earns ₹3,000,000, the mean salary might be ₹630,000 — making it seem like everyone is comfortably middle-class, when 80% earn ₹30,000.

This is why:
- **Income inequality** is measured using median household income (not mean)
- **Median home prices** are reported (not mean)
- When data is right-skewed, **median + IQR** is always preferred over **mean + SD**
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** If every value in a dataset increases by 5, how do mean, variance, and IQR change?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
Let transformed data: yᵢ = xᵢ + 5

**Mean:** ȳ = x̄ + 5 → **increases by 5**

**Variance:**
""")
        st.latex(r"s_y^2 = \frac{\sum(y_i - \bar{y})^2}{n-1} = \frac{\sum((x_i+5)-(\bar{x}+5))^2}{n-1} = \frac{\sum(x_i-\bar{x})^2}{n-1} = s_x^2")
        st.markdown("""
**Variance stays the same** — adding a constant shifts all values equally, so all deviations from the mean are unchanged.

**SD also stays the same** (since SD = √variance)

**IQR stays the same** — Q3 and Q1 both increase by 5, so Q3−Q1 is unchanged.

**General rule:**
- Adding constant c: Mean shifts by c; SD, Variance, IQR unchanged
- Multiplying by constant k: Mean × k; SD × |k|; Variance × k²; IQR × |k|
        """)
    st.markdown("</div>", unsafe_allow_html=True)
