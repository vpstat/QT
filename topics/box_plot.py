import streamlit as st
import numpy as np
import plotly.graph_objects as go

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>📦 Box Plot & Outliers</h1>
        <p>The five-number summary visualized — and identifying unusual observations.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── INTRODUCTION ──────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
A **box plot** (or box-and-whisker plot) provides a visual summary of the distribution using the **five-number summary**: Min, Q1, Median, Q3, Max. It highlights:
- The **center** (median)
- The **spread** (IQR, range)
- **Skewness** (asymmetry of the box/whiskers)
- **Outliers** (individual points beyond the fences)

Box plots are particularly powerful for **comparing multiple groups** side-by-side.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── CONCEPTS ─────────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Five-Number Summary")
        st.latex(r"\{\text{Min},\ Q_1,\ Q_2 (\text{Median}),\ Q_3,\ \text{Max}\}")

        st.markdown("#### IQR")
        st.latex(r"\text{IQR} = Q_3 - Q_1")

        st.markdown("#### Outlier Fences (Tukey's Method)")
        st.latex(r"\text{Lower Fence} = Q_1 - 1.5 \times \text{IQR}")
        st.latex(r"\text{Upper Fence} = Q_3 + 1.5 \times \text{IQR}")
        st.markdown("Any point **below Lower Fence** or **above Upper Fence** is a **mild outlier**.")

        st.markdown("#### Extreme Outlier Fences")
        st.latex(r"\text{Extreme Lower} = Q_1 - 3 \times \text{IQR}")
        st.latex(r"\text{Extreme Upper} = Q_3 + 3 \times \text{IQR}")

    with col2:
        st.markdown("#### Quartile Calculation")
        st.markdown("""
**Q1** = median of the lower half  
**Q3** = median of the upper half  
*(Inclusive or exclusive of the median — conventions differ)*

**Percentile formula (inclusive):**
        """)
        st.latex(r"L_p = \frac{p}{100}(n+1)\text{-th ordered value}")
        st.markdown("#### Skewness from Box Plot")
        st.markdown("""
- **Symmetric**: Box centered, equal whiskers
- **Right-skewed**: Long right whisker, box shifted left
- **Left-skewed**: Long left whisker, box shifted right
        """)

    st.markdown("---")

    # Interactive box plot
    st.markdown("#### 🎛️ Interactive Box Plot")
    np.random.seed(42)
    group_a = np.random.normal(70, 10, 50)
    group_b = np.concatenate([np.random.normal(65, 8, 45), [20, 110, 115]])  # with outliers
    group_c = np.random.normal(80, 5, 50)

    fig = go.Figure()
    for data, name, color in zip([group_a, group_b, group_c],
                                  ['Group A (Normal)', 'Group B (Outliers)', 'Group C (Tight)'],
                                  ['#667eea', '#fbbf24', '#34d399']):
        fig.add_trace(go.Box(y=data, name=name, marker_color=color,
                             boxpoints='outliers', jitter=0.3))
    fig.update_layout(
        title="Comparing Three Groups with Box Plots",
        paper_bgcolor='#ffffff', plot_bgcolor='#f8fafc',
        font_color='#111111', height=380,
        yaxis=dict(title='Value', gridcolor='#e2e8f0'),
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── SOLVED PROBLEMS ───────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Dataset (sorted): 3, 7, 8, 12, 14, 18, 21, 25, 30, 34. Find Q1, Q3, IQR, and the outlier fences.

**Solution:**

n = 10  
Q1 = median of lower half {3,7,8,12,14} = **8** (but often Q1 = (7+8)/2=7.5 depending on method; using inclusive: **8**)  
Q3 = median of upper half {18,21,25,30,34} = **25**  

Actually using median position method:  
Q1 = average of 2nd and 3rd values when split = (7+8)/2 = **7.5**  
Q3 = (25+30)/2 = **27.5**

IQR = 27.5 − 7.5 = **20**  
Lower Fence = 7.5 − 1.5(20) = 7.5 − 30 = **−22.5**  
Upper Fence = 27.5 + 1.5(20) = 27.5 + 30 = **57.5**

No outliers (all values between −22.5 and 57.5). ✅
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Test scores: 55, 60, 62, 64, 65, 67, 68, 70, 72, 75, 78, 80, 85, 90, 150. Identify outliers.

**Solution:**

n = 15 (including 150)  
Q1 = 8th value when n=15 → 4th value counted from bottom in lower half = 64  

Using Python/standard quartile method:  
Q1 = 63, Median = 70, Q3 = 81.5, IQR = 18.5

Lower Fence = 63 − 1.5(18.5) = 63 − 27.75 = **35.25**  
Upper Fence = 81.5 + 1.5(18.5) = 81.5 + 27.75 = **109.25**

**150 > 109.25 → 150 is an outlier** (likely a recording error or exceptional case)

5-number summary: Min=55, Q1=63, Median=70, Q3=81.5, Max=150 (with outlier shown as dot)
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Box plot A shows: Min=10, Q1=20, Median=30, Q3=50, Max=80. Box plot B shows: Min=10, Q1=25, Median=40, Q3=55, Max=80.

(a) Which dataset has greater variability? (b) Which is more right-skewed?

**Solution:**

(a) **IQR_A** = 50−20 = 30; **IQR_B** = 55−25 = 30 → Same IQR!  
But range is identical too (80−10=70 for both).  
However, examining the box shape:
- Dataset A: upper whisker = 80−50=30, lower = 20−10=10 → longer upper whisker
- Dataset B: upper whisker = 80−55=25, lower = 25−10=15 → more balanced

(b) **Dataset A is more right-skewed**: The median (30) is much closer to Q1 (20) than Q3 (50), and the upper whisker is much longer than the lower whisker. This indicates data is concentrated on the left with a long tail to the right.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── TRICKY QUESTIONS ─────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** If you remove an outlier from a dataset, will the IQR always decrease? What about the SD?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**IQR:** Not necessarily. The IQR is determined only by Q1 and Q3. If the outlier is beyond the fence (in the whisker region), removing it **doesn't change Q1 or Q3** at all, so IQR stays the same.

**SD:** Removing an outlier will **almost always decrease SD** because:
1. The outlier inflates the mean (moving it away from most points)
2. The large squared deviation of the outlier dominates the variance formula
3. After removal, the mean shifts closer to most points and all squared deviations shrink

This is exactly why SD is **sensitive** to outliers but IQR is **resistant**.
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Two students both score 90 on a test. In Class A (mean=70, SD=5), the 90 is an outlier. In Class B (mean=70, SD=20), it's not. Explain using Tukey fences and z-scores simultaneously.")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**Z-score check:**
- Class A: z = (90−70)/5 = **4.0** (beyond 3σ → flagged as outlier)
- Class B: z = (90−70)/20 = **1.0** (within 3σ → not an outlier)

**Tukey fence check** (approximate, assuming symmetric distribution where Q1 ≈ μ−0.675σ, Q3 ≈ μ+0.675σ):

*Class A:* IQR ≈ 1.35×5 = 6.75; Upper fence ≈ 73.375 + 10.125 = **83.5** → 90 > 83.5 → **outlier** ✅  
*Class B:* IQR ≈ 1.35×20 = 27; Upper fence ≈ 83.5 + 40.5 = **124** → 90 < 124 → **not an outlier** ✅

**Key insight:** Being an outlier is relative to the distribution's spread. The same value can be extreme in one context and ordinary in another — this is exactly why z-scores and context matter.
        """)
    st.markdown("</div>", unsafe_allow_html=True)
