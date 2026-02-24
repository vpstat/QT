import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>📊 Frequency Distribution</h1>
        <p>Organizing data into classes and understanding patterns of occurrence.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── INTRODUCTION ──────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
A **frequency distribution** is a tabular or graphical summary showing how often each value (or range of values) appears in a dataset. It is the foundation for:
- Understanding the **shape** of data (symmetric, skewed, bimodal)
- Building **histograms** and **ogives**
- Computing relative and cumulative frequencies

**Key terms:** Class interval, class width, class midpoint, frequency, relative frequency, cumulative frequency.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── CONCEPTS ─────────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Number of Classes (Sturges' Rule)")
        st.latex(r"k \approx 1 + 3.322 \cdot \log_{10}(n)")
        st.markdown("#### Class Width")
        st.latex(r"w = \frac{\text{Range}}{k} = \frac{\text{Max} - \text{Min}}{k}")
        st.markdown("#### Class Midpoint")
        st.latex(r"m_i = \frac{\text{Lower limit}_i + \text{Upper limit}_i}{2}")
    with col2:
        st.markdown("#### Relative Frequency")
        st.latex(r"rf_i = \frac{f_i}{n}")
        st.markdown("#### Cumulative Frequency")
        st.latex(r"CF_i = \sum_{j=1}^{i} f_j")
        st.markdown("#### Cumulative Relative Frequency")
        st.latex(r"CRF_i = \frac{CF_i}{n}")

    st.markdown("---")
    st.markdown("#### 📈 Shapes of Distributions")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Symmetric (Normal)**\nMean ≈ Median ≈ Mode\nBell-shaped")
    with col2:
        st.warning("**Right-Skewed (Positive)**\nMean > Median > Mode\nTail on the right\nE.g., Income, waiting times")
    with col3:
        st.error("**Left-Skewed (Negative)**\nMean < Median < Mode\nTail on the left\nE.g., Age at retirement")

    # Interactive histogram
    st.markdown("#### 🎛️ Interactive Frequency Histogram")
    np.random.seed(7)
    data = np.concatenate([np.random.normal(70, 10, 80), np.random.normal(85, 5, 20)])
    data = np.clip(data, 40, 100).round(0)

    n_bins = st.slider("Number of classes (bins):", 4, 15, 8)
    fig = go.Figure(go.Histogram(
        x=data, nbinsx=n_bins,
        marker_color='#667eea',
        marker_line_color='#a78bfa',
        marker_line_width=1.5,
    ))
    fig.update_layout(
        title=f"Exam Score Distribution ({len(data)} students)",
        xaxis_title="Score", yaxis_title="Frequency",
        paper_bgcolor='#ffffff', plot_bgcolor='#f8fafc',
        font_color='#111111', height=320,
        xaxis=dict(gridcolor='#e2e8f0'),
        yaxis=dict(gridcolor='#e2e8f0'),
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # ── SOLVED PROBLEMS ───────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** For n = 50 observations ranging from 15 to 75, determine (a) number of classes using Sturges' rule, and (b) class width.

**Solution:**

**(a)** k = 1 + 3.322 × log₁₀(50) = 1 + 3.322 × 1.699 = 1 + 5.64 ≈ **6 classes**

**(b)** Range = 75 − 15 = 60; w = 60/6 = **10** (class width = 10)

Classes: [15–25), [25–35), [35–45), [45–55), [55–65), [65–75]
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Given frequencies: 4, 8, 15, 10, 3 for classes 0–10, 10–20, 20–30, 30–40, 40–50. Build a complete frequency distribution table.
    """)
    df = pd.DataFrame({
        'Class': ['0–10', '10–20', '20–30', '30–40', '40–50'],
        'Midpoint': [5, 15, 25, 35, 45],
        'Freq (f)': [4, 8, 15, 10, 3],
        'Rel. Freq': ['0.100', '0.200', '0.375', '0.250', '0.075'],
        'Cum. Freq': [4, 12, 27, 37, 40],
        'Cum. Rel. Freq': ['0.100', '0.300', '0.675', '0.925', '1.000'],
    })
    st.table(df)
    st.markdown("n = 40. Dominant class = 20–30 (mode class). Distribution is slightly right-skewed (mode class < midpoint of range).")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** From a cumulative frequency ogive, you know: CF at 50 = 12, CF at 60 = 28, n = 50. Estimate the median using interpolation.

**Solution:**

Median = value where CF = n/2 = 25.

The 25th observation falls in the class [50–60) since CF jumps from 12 to 28 in this class.

Using **linear interpolation (ogive method)**:
    """)
    st.latex(r"""
    \text{Median} = L + \left(\frac{\frac{n}{2} - CF_{prev}}{f_{class}}\right) \times w
    """)
    st.markdown("""
Where: L = 50 (lower boundary), n/2 = 25, CF_prev = 12, f_class = 28−12 = 16, w = 10

Median = 50 + ((25 − 12)/16) × 10 = 50 + (13/16) × 10 = 50 + **8.125 = 58.125**
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── TRICKY QUESTIONS ─────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Two histograms of the same data are drawn — one with 5 bins and one with 20 bins. Which one is 'correct'?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**Neither — and both.**

The number of bins is a **smoothing parameter** that controls the trade-off between:
- **Too few bins (5)**: Over-smoothed, may hide the true shape (e.g., bimodality)
- **Too many bins (20)**: Under-smoothed, may show noise as structure

**Best practice:** Use Sturges' rule or Freedman–Diaconis rule as a starting point, then examine multiple bin widths and choose the one that most clearly reveals the underlying distribution shape. For n=50, Sturges suggests ≈ 7 bins.
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** The relative frequency for one class is 0.35. What does this mean, and can cumulative relative frequency ever exceed 1?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**Relative frequency of 0.35 means:**
- 35% of all observations fall in that class
- If n = 200, then 0.35 × 200 = 70 observations are in that class

**Can cumulative relative frequency exceed 1?**  
**No** — the cumulative relative frequency rises monotonically from 0 to exactly 1.0 at the final class. It represents the proportion of data *up to and including* a given class, which can never exceed 100%.

If your CRF exceeds 1, it indicates:
- An arithmetic error in summation, OR
- An observation has been double-counted, OR
- A class boundary overlap error
        """)
    st.markdown("</div>", unsafe_allow_html=True)
