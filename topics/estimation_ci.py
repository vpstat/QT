import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>🎯 Point Estimation & Confidence Intervals</h1>
        <p>Estimating population parameters and quantifying uncertainty.</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🎯 Point Estimation", "📐 Confidence Intervals"])

    with tab1:
        st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Point Estimation</div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### What is a Point Estimate?")
            st.markdown("""
A **point estimate** is a single value computed from sample data to approximate an unknown population parameter.

| Parameter | Notation | Point Estimator | Properties |
|-----------|----------|----------------|------------|
| Mean | μ | x̄ | Unbiased, consistent |
| Variance | σ² | s² | Unbiased (with n−1) |
| Proportion | p | p̂ = X/n | Unbiased |
| Std Dev | σ | s | Slightly biased |
            """)
        with col2:
            st.markdown("#### Desirable Properties of Estimators")
            st.markdown("""
1. **Unbiased:** E[θ̂] = θ (on average, hits the true value)
2. **Consistent:** θ̂ → θ as n → ∞
3. **Efficient:** Minimum variance among unbiased estimators (MVUE)
4. **Sufficient:** Uses all information in the data
            """)
            st.latex(r"\text{Bias} = E[\hat{\theta}] - \theta")
            st.latex(r"\text{MSE} = \text{Bias}^2 + \text{Var}(\hat{\theta})")
        st.markdown("</div>", unsafe_allow_html=True)

    with tab2:
        st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Confidence Intervals</div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### CI for Mean (σ known — Z-interval)")
            st.latex(r"\bar{x} \pm z_{\alpha/2}\cdot\frac{\sigma}{\sqrt{n}}")
            st.caption("Use when σ is known or n is very large (≥ 30)")
            st.markdown("#### CI for Mean (σ unknown — t-interval)")
            st.latex(r"\bar{x} \pm t_{\alpha/2,\,n-1}\cdot\frac{s}{\sqrt{n}}")
            st.caption("Use when σ unknown and/or n is small")
            st.markdown("#### CI for Proportion")
            st.latex(r"\hat{p} \pm z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}")
        with col2:
            st.markdown("#### Interpretation")
            st.markdown("""
> **"We are 95% confident that the true population mean lies between [L, U]."**

This does NOT mean there is a 95% probability the parameter is in this specific interval. It means: if we repeated sampling 100 times, about 95 of those intervals would contain the true parameter.

#### Margin of Error (MOE)
            """)
            st.latex(r"MOE = z_{\alpha/2}\cdot\frac{\sigma}{\sqrt{n}}")
            st.markdown("#### Required Sample Size")
            st.latex(r"n = \left(\frac{z_{\alpha/2}\cdot\sigma}{E}\right)^2")
            st.caption("E = desired margin of error")
        st.markdown("---")
        st.markdown("#### 🧮 Interactive CI Calculator")
        col1, col2, col3 = st.columns(3)
        with col1:
            xbar = st.number_input("x̄ (sample mean):", value=50.0, step=1.0)
            n_ci = st.number_input("n (sample size):", value=36, min_value=2)
        with col2:
            sigma_known = st.checkbox("σ known?", value=True)
            if sigma_known:
                sig = st.number_input("σ:", value=10.0, min_value=0.01, step=0.5)
            else:
                sig = st.number_input("s (sample SD):", value=10.0, min_value=0.01, step=0.5)
        with col3:
            conf = st.selectbox("Confidence level:", [0.90, 0.95, 0.99], index=1)
            alpha = 1 - conf
            if sigma_known:
                z_star = stats.norm.ppf(1 - alpha/2)
                se = sig / np.sqrt(n_ci)
                moe = z_star * se
                method = f"Z = {z_star:.3f}"
            else:
                t_star = stats.t.ppf(1 - alpha/2, n_ci - 1)
                se = sig / np.sqrt(n_ci)
                moe = t_star * se
                method = f"t({n_ci-1}) = {t_star:.3f}"
            st.metric("SE", f"{se:.4f}")
            st.metric("MOE", f"{moe:.4f}")
        lo, hi = xbar - moe, xbar + moe
        st.success(f"**{conf:.0%} CI:** ({lo:.4f}, {hi:.4f})  |  Method: {method}")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)
    st.markdown("<span class='prob-badge'>Problem 1 — Z-Interval</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A sample of 49 packages: x̄ = 500g, σ = 14g. Construct a 95% CI for the population mean weight.
    """)
    st.latex(r"SE = \frac{14}{\sqrt{49}}=2,\quad MOE = 1.96\times2 = 3.92")
    st.latex(r"\text{95\% CI} = 500 \pm 3.92 = \mathbf{(496.08,\; 503.92)}")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — t-Interval</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** 12 observations: x̄ = 24.5, s = 3.2. Construct a 99% CI (σ unknown).
    """)
    t_val = stats.t.ppf(0.995, 11)
    se_v = 3.2 / np.sqrt(12)
    moe_v = t_val * se_v
    st.latex(rf"t_{{0.005,11}} = {t_val:.3f},\quad SE = \frac{{3.2}}{{\sqrt{{12}}}} = {se_v:.4f}")
    st.latex(rf"MOE = {t_val:.3f}\times{se_v:.4f} = {moe_v:.4f}")
    st.latex(rf"\text{{99\% CI}} = 24.5 \pm {moe_v:.4f} = \mathbf{{({24.5-moe_v:.4f},\;{24.5+moe_v:.4f})}}")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Sample Size</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** How large a sample is needed to estimate μ within ±2 units with 95% confidence if σ=15?
    """)
    st.latex(r"n = \left(\frac{1.96\times15}{2}\right)^2 = \left(14.7\right)^2 = 216.09 \implies n = \lceil 216.09\rceil = \mathbf{217}")
    st.markdown("</div>", unsafe_allow_html=True)
