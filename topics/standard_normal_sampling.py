import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>📐 Standard Normal & Sampling Distribution</h1>
        <p>Z-tables, population vs sample statistics, and how sample means behave.</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🔔 Standard Normal", "📊 Sampling Distribution"])

    with tab1:
        st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Standard Normal Distribution</div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Definition")
            st.latex(r"Z \sim \mathcal{N}(0, 1)")
            st.latex(r"\phi(z) = \frac{1}{\sqrt{2\pi}}e^{-z^2/2}")
            st.markdown("#### Standardising Any Normal")
            st.latex(r"Z = \frac{X - \mu}{\sigma}")
            st.latex(r"X = \mu + Z\sigma")
            st.markdown("#### Symmetry")
            st.latex(r"\Phi(-z) = 1 - \Phi(z)")
            st.latex(r"P(-a < Z < a) = 2\Phi(a) - 1")
        with col2:
            st.markdown("#### Common Z-values")
            st.markdown("""
| Confidence Level | z* |
|-----------------|-----|
| 90% | 1.645 |
| 95% | 1.960 |
| 99% | 2.576 |
| 99.9% | 3.291 |
            """)
            st.markdown("#### Z-table lookup")
            z_in = st.number_input("Enter z:", value=1.96, step=0.01, key="z_lookup")
            p_left = stats.norm.cdf(z_in)
            st.metric(f"Φ({z_in}) = P(Z ≤ {z_in})", f"{p_left:.6f}")
            st.metric(f"P(Z > {z_in})", f"{1-p_left:.6f}")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Population vs Sample Statistics</div>", unsafe_allow_html=True)
        st.markdown(r"""
| Concept | Population (parameter) | Sample (statistic) |
|---------|----------------------|-------------------|
| Mean | μ | x̄ |
| Variance | σ² | s² |
| Std Dev | σ | s |
| Proportion | p | p̂ |
| Size | N | n |
        """)
        st.markdown("""
**Key idea:** We rarely know population parameters → we **estimate** them from sample statistics.
The **sampling distribution** describes how a sample statistic varies from sample to sample.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Sampling Distribution of the Mean</div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.latex(r"E[\bar{X}] = \mu")
            st.latex(r"\text{Var}(\bar{X}) = \frac{\sigma^2}{n}")
            st.latex(r"\sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}} \quad \text{(Standard Error)}")
            st.caption("Standard Error (SE) decreases as n increases — larger samples give more precise estimates")
        with col2:
            st.markdown("#### If population is Normal:")
            st.latex(r"\bar{X} \sim \mathcal{N}\!\left(\mu,\, \frac{\sigma^2}{n}\right) \;\; \text{exactly}")
            st.markdown("#### If population is NOT Normal:")
            st.markdown("By **Central Limit Theorem** (next topic):")
            st.latex(r"\bar{X} \;\dot{\sim}\; \mathcal{N}\!\left(\mu,\, \frac{\sigma^2}{n}\right) \;\text{for large } n")

        st.markdown("---")
        st.markdown("#### 🎛️ Standard Error Visual")
        sigma_pop = st.number_input("Population σ:", value=10.0, min_value=0.1, step=1.0)
        n_vals = [5, 10, 25, 50, 100, 500]
        se_vals = [sigma_pop / np.sqrt(n) for n in n_vals]
        fig = go.Figure(go.Bar(x=[str(n) for n in n_vals], y=se_vals,
                               marker_color='#4f46e5', text=[f"{s:.3f}" for s in se_vals], textposition='outside'))
        fig.update_layout(title=f"Standard Error (σ={sigma_pop}) as sample size grows",
                          xaxis_title="Sample size n", yaxis_title="Standard Error σ/√n",
                          paper_bgcolor='#ffffff', plot_bgcolor='#f8fafc',
                          font_color='#111111', height=300,
                          xaxis=dict(gridcolor='#e2e8f0'), yaxis=dict(gridcolor='#e2e8f0'))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)
    st.markdown("<span class='prob-badge'>Problem 1</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Population has μ=500, σ=100. A random sample of n=25 is taken. Find: (a) E[X̄], (b) SE, (c) P(X̄ > 520).

**Solution:**
    """)
    st.latex(r"(a)\; E[\bar{X}]=\mu=500")
    st.latex(r"(b)\; SE = \frac{\sigma}{\sqrt{n}}=\frac{100}{\sqrt{25}}=20")
    st.latex(r"(c)\; z = \frac{520-500}{20}=1.0,\quad P(\bar{X}>520)=1-\Phi(1.0)=1-0.8413=\mathbf{0.1587}")
    st.markdown("</div>", unsafe_allow_html=True)
