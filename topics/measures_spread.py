import streamlit as st
import numpy as np

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>📏 Measures of Spread</h1>
        <p>Quantifying how much variability or dispersion exists in a dataset.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── INTRODUCTION ──────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
Measures of **central tendency** (mean, median) tell us where data is centered. But two datasets can have the same mean yet be vastly different. **Measures of spread** capture this variability:

- A small spread → data is **consistent and predictable**
- A large spread → data is **dispersed and variable**

Key measures: **Range, Variance, Standard Deviation, IQR, Coefficient of Variation**.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── CONCEPTS ─────────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 1. Range")
        st.latex(r"\text{Range} = \text{Max} - \text{Min}")

        st.markdown("#### 2. Population Variance")
        st.latex(r"\sigma^2 = \frac{\sum_{i=1}^{N}(x_i - \mu)^2}{N}")

        st.markdown("#### 3. Sample Variance")
        st.latex(r"s^2 = \frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n-1}")
        st.caption("Dividing by n−1 (Bessel's correction) makes s² an unbiased estimator of σ²")

        st.markdown("#### 4. Computational Formula for s²")
        st.latex(r"s^2 = \frac{\sum x_i^2 - \frac{(\sum x_i)^2}{n}}{n-1}")

    with col2:
        st.markdown("#### 5. Standard Deviation")
        st.latex(r"\sigma = \sqrt{\sigma^2} \qquad s = \sqrt{s^2}")

        st.markdown("#### 6. Interquartile Range (IQR)")
        st.latex(r"\text{IQR} = Q_3 - Q_1")
        st.caption("Q1 = 25th percentile, Q3 = 75th percentile")

        st.markdown("#### 7. Coefficient of Variation (CV%)")
        st.latex(r"\text{CV} = \frac{s}{\bar{x}} \times 100\%")
        st.caption("Allows comparison of spread across datasets with different units/means")

        st.markdown("#### 8. Mean Absolute Deviation (MAD)")
        st.latex(r"\text{MAD} = \frac{\sum_{i=1}^{n}|x_i - \bar{x}|}{n}")

    st.markdown("---")
    st.markdown("#### 📊 Comparison of Spread Measures")
    st.markdown("""
| Measure | Uses All Data? | Sensitive to Outliers? | Units | Best For |
|---------|---------------|----------------------|-------|----------|
| Range | No (only min/max) | **Very high** | Same as data | Quick overview |
| Variance | Yes | High | Squared units | Mathematical derivations |
| Std Dev | Yes | High | Same as data | Most common, interpretable |
| IQR | No (middle 50%) | **Resistant** | Same as data | Skewed data, outlier-robust |
| CV | Yes | High | Unitless (%) | Comparing different scales |
| MAD | Yes | Moderate | Same as data | Robust alternative to SD |
    """)

    # Interactive calculator
    st.markdown("#### 🧮 Live Spread Calculator")
    st.markdown("Enter comma-separated numbers:")
    user_input = st.text_input("Dataset:", "12, 15, 11, 18, 14, 13, 20, 10, 16, 14")
    try:
        arr = np.array([float(x.strip()) for x in user_input.split(',')])
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Range", f"{arr.max()-arr.min():.3f}")
            st.metric("Min", f"{arr.min():.3f}")
        with col2:
            st.metric("Variance (s²)", f"{np.var(arr, ddof=1):.3f}")
            st.metric("Max", f"{arr.max():.3f}")
        with col3:
            st.metric("Std Dev (s)", f"{np.std(arr, ddof=1):.3f}")
            st.metric("Mean", f"{np.mean(arr):.3f}")
        with col4:
            q1, q3 = np.percentile(arr, [25, 75])
            st.metric("IQR", f"{q3-q1:.3f}")
            st.metric("CV%", f"{np.std(arr,ddof=1)/np.mean(arr)*100:.2f}%")
    except:
        st.warning("Please enter valid comma-separated numbers.")

    st.markdown("</div>", unsafe_allow_html=True)

    # ── SOLVED PROBLEMS ───────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Dataset: {4, 7, 2, 9, 5, 6, 3}. Compute Range, Sample Variance, and Sample Standard Deviation.

**Solution:**

n = 7, Values sorted: 2, 3, 4, 5, 6, 7, 9

**Range** = 9 − 2 = **7**

Mean x̄ = (4+7+2+9+5+6+3)/7 = 36/7 ≈ **5.143**

Deviations (xᵢ − x̄): −1.143, 1.857, −3.143, 3.857, −0.143, 0.857, −2.143

Squared deviations: 1.306, 3.449, 9.878, 14.878, 0.020, 0.735, 4.592 → Sum = 34.857

**s²** = 34.857 / (7−1) = 34.857 / 6 = **5.810**

**s** = √5.810 = **2.411**
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Two machines produce bolts. Machine A: mean diameter = 10mm, SD = 0.1mm. Machine B: mean diameter = 25mm, SD = 0.2mm. Which machine is relatively more consistent?

**Solution:**

Use the **Coefficient of Variation (CV)** for fair comparison (different means!):

CV_A = (0.1/10) × 100% = **1.0%**  
CV_B = (0.2/25) × 100% = **0.8%**

**Machine B is relatively more consistent** despite having a larger absolute SD, because its spread relative to its mean (0.8%) is smaller than Machine A's (1.0%).

This shows why CV is essential when comparing spread across datasets with different scales.
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Use the computational formula to find variance of: {3, 7, 5, 11, 9}

**Solution:**
    """)
    st.latex(r"s^2 = \frac{\sum x_i^2 - \frac{(\sum x_i)^2}{n}}{n-1}")
    st.markdown("""
n = 5, Σxᵢ = 3+7+5+11+9 = 35, (Σxᵢ)² = 1225

Σxᵢ² = 9+49+25+121+81 = 285

s² = [285 − (1225/5)] / (5−1) = [285 − 245] / 4 = 40/4 = **10**

s = √10 ≈ **3.162**

**Verify:** Mean = 7; deviations²: 16, 0, 4, 16, 4 → Sum = 40; s² = 40/4 = 10 ✅
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 4 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Dataset A: {10, 10, 10, 10, 100} vs Dataset B: {25, 28, 30, 32, 35}. Both have similar means (~28 vs 30). Compare their spreads and which measure best represents the data.

**Solution:**

Dataset A: Mean=28, SD≈38.99, Median=10, IQR=0  
Dataset B: Mean=30, SD≈3.81, Median=30, IQR=7

For Dataset A, the **mean (28) is misleading** — it's influenced by the extreme value (100). The **median (10) and IQR (0) better represent** the typical observation.

For Dataset B, mean and SD are appropriate — the data is symmetric with no outliers.

**Lesson:** Use (Median + IQR) for skewed/outlier-heavy data; use (Mean + SD) for symmetric data.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── TRICKY QUESTIONS ─────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Can a dataset have a standard deviation of zero? When, and what does it mean?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**Yes.** Standard deviation = 0 if and only if **all observations are identical**.

Example: {5, 5, 5, 5, 5} → Mean = 5, every deviation = 0, SD = 0.

This means there is **absolutely no variability** — the variable is a constant. In practice, this often indicates:
- A data collection error (all values recorded identically by mistake)
- A truly constant measurement (e.g., fixed temperature in a controlled environment)
- A variable that is not informative for analysis (zero-variance predictors should be removed before regression)

**SD can never be negative** — it is a square root of a sum of squared terms, always ≥ 0.
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Why do we divide by (n−1) instead of n when computing sample variance?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
This is **Bessel's correction** and ensures **unbiasedness**.

When we estimate σ² from a sample, we use x̄ (sample mean) instead of μ (population mean). The sample mean is itself computed from the same data, causing the deviations (xᵢ − x̄) to be systematically **smaller** than the true deviations (xᵢ − μ).

Dividing by (n−1) rather than n **inflates the estimate slightly**, compensating for this shrinkage and making:
""")
        st.latex(r"E[s^2] = \sigma^2 \quad \text{(unbiased)}")
        st.markdown("""
If you divide by n, you get a **biased** estimator that consistently underestimates σ².

**Intuition**: With n data points, once you've calculated the mean, you've used up one "degree of freedom" — only n−1 observations are truly free to vary.
        """)
    st.markdown("</div>", unsafe_allow_html=True)
