import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>📊 Student's t-Distribution</h1>
        <p>Inference when σ is unknown — heavier tails, wider intervals, and t-tests.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
When the population standard deviation σ is **unknown** (which is almost always in practice), we replace σ with the sample standard deviation s. This introduces extra uncertainty, which the **t-distribution** accounts for with heavier tails.

**Key difference from Z:** As degrees of freedom (df) increase, the t-distribution approaches the standard normal.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### t-Distribution Properties")
        st.latex(r"t = \frac{\bar{x}-\mu}{s/\sqrt{n}} \;\sim\; t_{n-1}")
        st.markdown("""
- Bell-shaped, symmetric about 0
- **Heavier tails** than standard normal → wider confidence intervals
- Characterised by **degrees of freedom** (df = n − 1)
- As df → ∞, t → Z
- Exact when population is Normal; robust otherwise
        """)
        st.markdown("#### PDF of t-Distribution")
        st.latex(r"f(t) = \frac{\Gamma\!\left(\frac{\nu+1}{2}\right)}{\sqrt{\nu\pi}\;\Gamma\!\left(\frac{\nu}{2}\right)}\left(1+\frac{t^2}{\nu}\right)^{-(\nu+1)/2}")
        st.caption("ν = degrees of freedom")
    with col2:
        st.markdown("#### Key Statistics")
        st.latex(r"E[t] = 0 \quad (\nu > 1)")
        st.latex(r"\text{Var}(t) = \frac{\nu}{\nu-2} \quad (\nu > 2)")
        st.caption("Variance > 1 always — heavier tails than Normal")
        st.markdown("#### When to Use t vs Z")
        st.markdown("""
| Condition | Use |
|-----------|-----|
| σ known, n large | Z-test |
| σ unknown, n ≥ 30 | t-test (or Z, similar) |
| σ unknown, n < 30 | **t-test** (required) |
| Population normal | t exact |
| Population non-normal, n < 30 | t approximate (use with caution) |
        """)

    st.markdown("---")
    st.markdown("#### 🎛️ t vs Z Visual Comparison")
    df_val = st.slider("Degrees of freedom (df):", 1, 50, 5)
    x_range = np.linspace(-4, 4, 300)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_range, y=stats.norm.pdf(x_range), mode='lines',
                              line=dict(color='#059669', width=2, dash='dash'), name='Z ~ N(0,1)'))
    fig.add_trace(go.Scatter(x=x_range, y=stats.t.pdf(x_range, df_val), mode='lines',
                              line=dict(color='#4f46e5', width=3), name=f't(df={df_val})'))
    fig.update_layout(title=f"t(df={df_val}) vs Standard Normal",
                      paper_bgcolor='#ffffff', plot_bgcolor='#f8fafc', font_color='#111111', height=300,
                      xaxis=dict(gridcolor='#e2e8f0'), yaxis=dict(gridcolor='#e2e8f0'))
    st.plotly_chart(fig, use_container_width=True)

    t_var = df_val / (df_val - 2) if df_val > 2 else float('inf')
    st.info(f"t(df={df_val}): Var = {t_var:.4f} | Z: Var = 1.000 | Ratio = {t_var:.4f}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — t-Test</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** 16 students scored x̄ = 72, s = 8 on a test. Test if μ differs from 75 at α = 0.05.

**Solution:** H₀: μ = 75, Hₐ: μ ≠ 75 (two-tailed), df = 15
    """)
    t_stat = (72 - 75) / (8 / np.sqrt(16))
    p_v = 2 * stats.t.sf(abs(t_stat), 15)
    t_crit = stats.t.ppf(0.975, 15)
    st.latex(rf"t = \frac{{72-75}}{{8/\sqrt{{16}}}} = \frac{{-3}}{{2}} = {t_stat:.3f}")
    st.latex(rf"t_{{0.025,15}} = \pm{t_crit:.3f},\quad p\text{{-value}} = {p_v:.4f}")
    st.markdown(f"Since |t| = 1.5 < {t_crit:.3f} (and p = {p_v:.4f} > 0.05): **Fail to reject H₀.** No significant difference from 75.")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — t-CI</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A sample of 25 bags has x̄ = 49.8 kg, s = 1.5 kg. Build a 95% CI for the true mean weight.
    """)
    t_star = stats.t.ppf(0.975, 24)
    se_v = 1.5 / np.sqrt(25)
    moe = t_star * se_v
    st.latex(rf"t_{{0.025,24}} = {t_star:.3f},\quad SE = {se_v:.3f},\quad MOE = {moe:.4f}")
    st.latex(rf"\text{{95\% CI}} = 49.8 \pm {moe:.4f} = \mathbf{{({49.8-moe:.4f},\; {49.8+moe:.4f})}}")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)
    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Why doesn't df=∞ give exactly the same critical value as Z?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**It does!** As df → ∞, the t-distribution converges exactly to the standard normal.

| df | t₀.₀₂₅ | Z₀.₀₂₅ |
|----|--------|--------|
| 5 | 2.571 | 1.960 |
| 30 | 2.042 | 1.960 |
| 100 | 1.984 | 1.960 |
| ∞ | **1.960** | 1.960 |

In practice, once df ≥ 30, the difference is small enough that Z is often used as an approximation.
        """)
    st.markdown("</div>", unsafe_allow_html=True)
