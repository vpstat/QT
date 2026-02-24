import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats
from math import comb as math_comb

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>🎮 Distribution Playground</h1>
        <p>Interactively explore PMF, PDF, and CDF for all major distributions.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 How to Use</div>", unsafe_allow_html=True)
    st.markdown("""
Select a distribution and adjust its parameters using the sliders. The playground shows:
- **PMF/PDF** — where probability mass or density is located
- **CDF** — cumulative probability up to a value
- **Key statistics** — mean, variance, and SD for the selected parameters
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    dist_choice = st.selectbox("Choose a Distribution:", [
        "Bernoulli", "Binomial", "Poisson",
        "Discrete Uniform", "Geometric",
        "Normal (Continuous)", "Exponential (Continuous)", "Uniform (Continuous)"
    ])

    st.markdown("<div class='section-card'><div class='section-label label-concept'>🎛️ Parameters</div>", unsafe_allow_html=True)

    if dist_choice == "Bernoulli":
        p = st.slider("p (success probability):", 0.01, 0.99, 0.5, 0.01)
        x_vals = [0, 1]; pmf_vals = [1-p, p]
        cdf_vals = [1-p, 1.0]
        mean_v, var_v = p, p*(1-p)
        title = f"Bernoulli(p={p})"
        is_discrete = True

    elif dist_choice == "Binomial":
        n = st.slider("n (trials):", 1, 50, 10)
        p = st.slider("p (success prob):", 0.01, 0.99, 0.5, 0.01)
        x_vals = list(range(n+1))
        pmf_vals = [math_comb(n, k) * p**k * (1-p)**(n-k) for k in x_vals]
        cdf_vals = np.cumsum(pmf_vals).tolist()
        mean_v, var_v = n*p, n*p*(1-p)
        title = f"Binomial(n={n}, p={p})"
        is_discrete = True

    elif dist_choice == "Poisson":
        lam = st.slider("λ (rate / mean):", 0.1, 20.0, 3.0, 0.1)
        max_x = max(20, int(lam*3))
        x_vals = list(range(max_x+1))
        pmf_vals = [stats.poisson.pmf(k, lam) for k in x_vals]
        cdf_vals = [stats.poisson.cdf(k, lam) for k in x_vals]
        mean_v, var_v = lam, lam
        title = f"Poisson(λ={lam})"
        is_discrete = True

    elif dist_choice == "Discrete Uniform":
        a = st.number_input("a (min):", value=1, min_value=-20)
        b = st.number_input("b (max):", value=6, min_value=int(a)+1)
        x_vals = list(range(int(a), int(b)+1)); n_u = len(x_vals)
        pmf_vals = [1/n_u]*n_u; cdf_vals = [(i+1)/n_u for i in range(n_u)]
        mean_v = (a+b)/2; var_v = (n_u**2-1)/12
        title = f"DiscreteUniform({int(a)}, {int(b)})"
        is_discrete = True

    elif dist_choice == "Geometric":
        p = st.slider("p (success prob):", 0.01, 0.99, 0.3, 0.01)
        max_x = min(50, int(10/p))
        x_vals = list(range(1, max_x+1))
        pmf_vals = [(1-p)**(k-1)*p for k in x_vals]
        cdf_vals = [1-(1-p)**k for k in x_vals]
        mean_v = 1/p; var_v = (1-p)/p**2
        title = f"Geometric(p={p})"
        is_discrete = True

    elif dist_choice == "Normal (Continuous)":
        mu = st.number_input("μ (mean):", value=0.0, step=0.5)
        sigma = st.number_input("σ (std dev):", value=1.0, min_value=0.01, step=0.1)
        x_vals = np.linspace(mu-4*sigma, mu+4*sigma, 300)
        pmf_vals = stats.norm.pdf(x_vals, mu, sigma)
        cdf_vals = stats.norm.cdf(x_vals, mu, sigma)
        mean_v = mu; var_v = sigma**2
        title = f"Normal(μ={mu}, σ={sigma})"
        is_discrete = False

    elif dist_choice == "Exponential (Continuous)":
        lam = st.slider("λ (rate):", 0.1, 5.0, 1.0, 0.1)
        x_vals = np.linspace(0, 8/lam, 300)
        pmf_vals = stats.expon.pdf(x_vals, scale=1/lam)
        cdf_vals = stats.expon.cdf(x_vals, scale=1/lam)
        mean_v = 1/lam; var_v = 1/lam**2
        title = f"Exponential(λ={lam})"
        is_discrete = False

    elif dist_choice == "Uniform (Continuous)":
        a = st.number_input("a (lower):", value=0.0, step=0.5)
        b = st.number_input("b (upper):", value=1.0, min_value=float(a)+0.01, step=0.5)
        x_vals = np.linspace(float(a)-0.2, float(b)+0.2, 300)
        pmf_vals = stats.uniform.pdf(x_vals, loc=a, scale=b-a)
        cdf_vals = stats.uniform.cdf(x_vals, loc=a, scale=b-a)
        mean_v = (a+b)/2; var_v = (b-a)**2/12
        title = f"Uniform({a}, {b})"
        is_discrete = False

    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Mean E[X]", f"{mean_v:.4f}")
    col2.metric("Variance Var(X)", f"{var_v:.4f}")
    col3.metric("Std Dev σ", f"{var_v**0.5:.4f}")

    col_pmf, col_cdf = st.columns(2)
    label = "PMF" if is_discrete else "PDF"

    with col_pmf:
        fig1 = go.Figure()
        if is_discrete:
            fig1.add_trace(go.Bar(x=x_vals, y=pmf_vals, marker_color='#4f46e5',
                                  marker_line_color='#1e1b4b', marker_line_width=1))
        else:
            fig1.add_trace(go.Scatter(x=x_vals, y=pmf_vals, mode='lines',
                                       line=dict(color='#4f46e5', width=3), fill='tozeroy',
                                       fillcolor='rgba(79,70,229,0.15)'))
        fig1.update_layout(title=f"{label}: {title}", paper_bgcolor='#ffffff',
                           plot_bgcolor='#f8fafc', font_color='#111111', height=300,
                           xaxis=dict(gridcolor='#e2e8f0'), yaxis=dict(gridcolor='#e2e8f0'))
        st.plotly_chart(fig1, use_container_width=True)

    with col_cdf:
        fig2 = go.Figure()
        if is_discrete:
            fig2.add_trace(go.Scatter(x=x_vals, y=cdf_vals, mode='lines+markers',
                                       line=dict(color='#059669', width=2), marker=dict(size=6)))
        else:
            fig2.add_trace(go.Scatter(x=x_vals, y=cdf_vals, mode='lines',
                                       line=dict(color='#059669', width=3)))
        fig2.update_layout(title=f"CDF: {title}", paper_bgcolor='#ffffff',
                           plot_bgcolor='#f8fafc', font_color='#111111', height=300,
                           xaxis=dict(gridcolor='#e2e8f0'),
                           yaxis=dict(gridcolor='#e2e8f0', range=[-0.05, 1.05]))
        st.plotly_chart(fig2, use_container_width=True)

    # P(a ≤ X ≤ b) calculator
    st.markdown("<div class='section-card'><div class='section-label label-solved'>🔢 Probability Calculator</div>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        x_arr = np.array(x_vals)
        lo = float(st.number_input("Lower bound a:", value=float(x_arr.min()), step=0.5 if not is_discrete else 1.0))
        hi = float(st.number_input("Upper bound b:", value=float(x_arr.max()), step=0.5 if not is_discrete else 1.0))
    with col2:
        if is_discrete:
            prob = sum(p for x, p in zip(x_vals, pmf_vals) if lo <= x <= hi)
        else:
            mask = (x_arr >= lo) & (x_arr <= hi)
            prob = np.trapz(np.array(pmf_vals)[mask], x_arr[mask]) if mask.any() else 0.0
        st.metric(f"P({lo} ≤ X ≤ {hi})", f"{prob:.6f}")
        st.metric("As percentage:", f"{prob*100:.3f}%")
    st.markdown("</div>", unsafe_allow_html=True)
