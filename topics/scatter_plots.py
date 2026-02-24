import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>🔵 Scatter Plots & Correlation</h1>
        <p>Visualizing and measuring the relationship between two quantitative variables.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── INTRODUCTION ──────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
A **scatter plot** displays pairs of observations (x, y) on a 2D plane, revealing:
- **Direction**: positive or negative association
- **Form**: linear or nonlinear
- **Strength**: how closely points follow a pattern
- **Outliers**: points that deviate markedly from the pattern

**Correlation** quantifies the *linear* relationship strength between two variables.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── CONCEPTS ─────────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Pearson's Correlation Coefficient (r)")
        st.latex(r"""
        r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}
                 {\sqrt{\sum_{i=1}^{n}(x_i-\bar{x})^2 \cdot \sum_{i=1}^{n}(y_i-\bar{y})^2}}
        """)
        st.markdown("#### Equivalent formula using z-scores")
        st.latex(r"r = \frac{1}{n-1}\sum_{i=1}^{n} z_{x_i} \cdot z_{y_i}")
        st.markdown("#### Covariance")
        st.latex(r"s_{xy} = \frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}{n-1}")
        st.latex(r"r = \frac{s_{xy}}{s_x \cdot s_y}")
    with col2:
        st.markdown("#### Interpreting r")
        st.markdown("""
| Value of r | Interpretation |
|------------|----------------|
| r = +1 | Perfect positive linear |
| 0.7 ≤ r < 1 | Strong positive |
| 0.3 ≤ r < 0.7 | Moderate positive |
| 0 < r < 0.3 | Weak positive |
| r = 0 | No linear relationship |
| Negative | Same magnitudes, opposite direction |
| r = −1 | Perfect negative linear |
        """)
        st.markdown("#### Coefficient of Determination")
        st.latex(r"r^2 = \text{proportion of variance in } y \text{ explained by } x")

    st.markdown("---")
    st.markdown("#### 🎛️ Interactive Scatter Plot")
    pattern = st.selectbox("Choose relationship pattern:", ["Strong Positive", "Weak Positive", "No Correlation", "Strong Negative"])
    np.random.seed(42)
    n = 60
    x = np.random.uniform(10, 100, n)
    noise_scale = {'Strong Positive': 5, 'Weak Positive': 25, 'No Correlation': 50, 'Strong Negative': 5}[pattern]
    slope = {'Strong Positive': 0.8, 'Weak Positive': 0.5, 'No Correlation': 0, 'Strong Negative': -0.8}[pattern]
    y = 20 + slope * x + np.random.normal(0, noise_scale, n)
    r, p = stats.pearsonr(x, y)
    m, b, *_ = stats.linregress(x, y)
    x_line = np.array([x.min(), x.max()])
    y_line = m * x_line + b
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='markers',
        marker=dict(color='#667eea', size=8, opacity=0.7, line=dict(color='#a78bfa', width=1)),
        name='Data'))
    fig.add_trace(go.Scatter(x=x_line, y=y_line, mode='lines',
        line=dict(color='#fbbf24', width=2, dash='dash'), name=f'Trend line (r={r:.3f})'))
    fig.update_layout(
        title=f"{pattern} Correlation | r = {r:.3f} | r² = {r**2:.3f}",
        paper_bgcolor='#ffffff', plot_bgcolor='#f8fafc',
        font_color='#111111', height=350,
        xaxis=dict(title='X', gridcolor='#e2e8f0'),
        yaxis=dict(title='Y', gridcolor='#e2e8f0'),
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── SOLVED PROBLEMS ───────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Given 5 data points: (1,2), (2,4), (3,5), (4,4), (5,5). Compute Pearson's r.

**Solution:**

x̄ = 3, ȳ = 4

| i | xᵢ | yᵢ | (xᵢ−x̄) | (yᵢ−ȳ) | (xᵢ−x̄)(yᵢ−ȳ) | (xᵢ−x̄)² | (yᵢ−ȳ)² |
|---|----|----|---------|---------|--------------|---------|---------|
| 1 | 1 | 2 | −2 | −2 | 4 | 4 | 4 |
| 2 | 2 | 4 | −1 | 0 | 0 | 1 | 0 |
| 3 | 3 | 5 | 0 | 1 | 0 | 0 | 1 |
| 4 | 4 | 4 | 1 | 0 | 0 | 1 | 0 |
| 5 | 5 | 5 | 2 | 1 | 2 | 4 | 1 |
| **Σ** | | | | | **6** | **10** | **6** |

r = 6 / √(10 × 6) = 6 / √60 = 6 / 7.746 ≈ **0.775** (strong positive)
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** r = 0.85 between study hours and exam score. Interpret r and r². Can we say studying causes better scores?

**Solution:**
- r = 0.85 → Strong positive linear relationship
- r² = 0.7225 → Study hours explain **72.25%** of the variability in exam scores
- The remaining 27.75% is explained by other factors (sleep, diet, prior knowledge, etc.)
- **Correlation ≠ Causation**: Both variables might be influenced by a third variable (e.g., student motivation). A controlled experiment would be needed to establish causation.
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Two datasets both have r = 0.9. Dataset A has points tightly clustered around a line from (0,0) to (50,50). Dataset B has the same r but includes one extreme outlier at (100, 2). What concerns arise?

**Solution:**
- r = 0.9 for Dataset B may be **heavily influenced by the outlier** — without that single point, r might be much lower (e.g., 0.3)
- With Dataset A, r = 0.9 reflects a genuinely strong, consistent relationship

**Lesson:** Always **visualize data** before interpreting r. Anscombe's Quartet (1973) famously showed four datasets with identical r, mean, and variance but radically different scatter patterns.

**Remedy for outlier influence:**
- Use Spearman's rank correlation (ρ) which is outlier-robust
- Report correlation with and without the outlier
- Investigate whether the outlier is a data error or a genuine observation
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── TRICKY QUESTIONS ─────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** A scatter plot of X = month number and Y = ice cream sales shows r = 0. Is there truly no relationship?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**r = 0 only means no *linear* relationship exists.**

Ice cream sales are likely **seasonally periodic** (high in summer, low in winter, high again next summer). This is a **nonlinear (sinusoidal) relationship** which Pearson's r completely fails to detect.

**Solution:** Plot the scatter diagram first. For periodic/nonlinear relationships, use:
- Spearman's ρ (monotonic relationships)
- Mutual information (general dependency)
- Visual inspection + domain knowledge
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** r between shoe size and reading ability in children is r = 0.8. Does big feet cause better reading?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**No — this is a classic spurious correlation caused by a confounding variable: age.**

Older children have both larger feet AND better reading ability. Both variables are driven by age growth.

**Spurious correlations** are associations that appear to be meaningful but are driven by a lurking (confounding) variable.

Famous real examples:
- Nicolas Cage movies released ↔ pool drownings (r ≈ 0.67)
- Organic food sales ↔ autism diagnoses (r ≈ 0.99)

**Lesson:** Correlation describes association, never causation. Always ask: "What third variable could be driving both?"
        """)
    st.markdown("</div>", unsafe_allow_html=True)
