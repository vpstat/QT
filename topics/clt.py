import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>🔁 Central Limit Theorem</h1>
        <p>The most important theorem in statistics — why the normal distribution is everywhere.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
The **Central Limit Theorem (CLT)** states that the distribution of sample means approaches a Normal distribution as sample size increases — **regardless of the population's shape**.

This is why the Normal distribution dominates statistics: hypothesis tests, confidence intervals, and quality control all rely on CLT.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### CLT Statement")
        st.latex(r"\text{If } X_1, X_2, \ldots, X_n \text{ are i.i.d. with } E[X_i]=\mu,\; \text{Var}(X_i)=\sigma^2")
        st.latex(r"\text{then } \bar{X} = \frac{1}{n}\sum_{i=1}^n X_i")
        st.latex(r"\bar{X} \;\xrightarrow{d}\; \mathcal{N}\!\left(\mu,\, \frac{\sigma^2}{n}\right) \text{ as } n \to \infty")
        st.markdown("#### Standardised Form")
        st.latex(r"Z = \frac{\bar{X}-\mu}{\sigma/\sqrt{n}} \;\xrightarrow{d}\; \mathcal{N}(0,1)")
    with col2:
        st.markdown("#### How Large is 'Large Enough'?")
        st.markdown("""
- **Normal population** → CLT exact for any n
- **Symmetric population** → n ≥ 15 usually sufficient
- **Skewed population** → n ≥ 30 (common rule of thumb)
- **Very skewed / heavy tails** → n ≥ 50 or more
        """)
        st.markdown("#### CLT for Sums")
        st.latex(r"S_n = \sum_{i=1}^n X_i \;\dot\sim\; \mathcal{N}(n\mu,\, n\sigma^2)")
        st.markdown("#### CLT for Proportions")
        st.latex(r"\hat{p} = \frac{X}{n} \;\dot\sim\; \mathcal{N}\!\left(p,\, \frac{p(1-p)}{n}\right)")
        st.caption("Requires np ≥ 5 and n(1−p) ≥ 5")
    st.markdown("</div>", unsafe_allow_html=True)

    # Interactive CLT demo
    st.markdown("<div class='section-card'><div class='section-label label-concept'>🎛️ Interactive CLT Demonstration</div>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        pop_shape = st.selectbox("Population shape:", ["Uniform", "Exponential (Skewed)", "Bimodal"])
        n_samp = st.slider("Sample size (n):", 1, 100, 30, key="clt_n")
        n_sims = 2000
    with col2:
        np.random.seed(42)
        if pop_shape == "Uniform":
            pop = np.random.uniform(0, 10, (n_sims, n_samp))
            mu_t, sig_t = 5, np.sqrt(100/12)
        elif pop_shape == "Exponential (Skewed)":
            pop = np.random.exponential(2, (n_sims, n_samp))
            mu_t, sig_t = 2, 2
        else:
            pop = np.concatenate([np.random.normal(3, 0.5, (n_sims, n_samp//2)),
                                  np.random.normal(7, 0.5, (n_sims, n_samp - n_samp//2))], axis=1)
            mu_t, sig_t = 5, np.sqrt(4 + 0.25)
        means = pop.mean(axis=1)
        x_th = np.linspace(means.min(), means.max(), 200)
        y_th = stats.norm.pdf(x_th, mu_t, sig_t / np.sqrt(n_samp))

        fig = go.Figure()
        fig.add_trace(go.Histogram(x=means, nbinsx=40, name="Sample means",
                                    marker_color='#4f46e5', opacity=0.7, histnorm='probability density'))
        fig.add_trace(go.Scatter(x=x_th, y=y_th, name="Normal approx",
                                  line=dict(color='#dc2626', width=3)))
        fig.update_layout(title=f"CLT: {pop_shape} pop, n={n_samp}, {n_sims} samples",
                          paper_bgcolor='#ffffff', plot_bgcolor='#f8fafc',
                          font_color='#111111', height=320,
                          xaxis=dict(gridcolor='#e2e8f0', title="Sample mean"),
                          yaxis=dict(gridcolor='#e2e8f0', title="Density"))
        st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)
    st.markdown("<span class='prob-badge'>Problem 1</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A machine fills bottles with μ=500ml, σ=10ml (non-normal). 36 bottles are sampled. Find P(X̄ < 498).

**Solution:** By CLT (n=36 ≥ 30): X̄ ~ N(500, 10²/36)
    """)
    st.latex(r"SE = \frac{10}{\sqrt{36}} = 1.667,\quad z=\frac{498-500}{1.667}=-1.20")
    st.latex(r"P(\bar{X}<498) = \Phi(-1.20) = \mathbf{0.1151}")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Proportions</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** 40% of voters support candidate A. In a poll of n=200, find P(p̂ > 0.45).

**Solution:** By CLT for proportions: p̂ ~ N(0.40, 0.40×0.60/200)
    """)
    st.latex(r"SE = \sqrt{\frac{0.40\times0.60}{200}} = \sqrt{0.0012} = 0.03464")
    st.latex(r"z = \frac{0.45-0.40}{0.03464} = 1.443,\quad P(\hat{p}>0.45)=1-\Phi(1.443)=\mathbf{0.0745}")
    st.markdown("</div>", unsafe_allow_html=True)
