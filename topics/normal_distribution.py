import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>🔔 Normal Distribution</h1>
        <p>The most important distribution in statistics — the bell curve that describes natural phenomena.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── INTRODUCTION ──────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
The **Normal Distribution** (or Gaussian distribution) is the cornerstone of statistical analysis. Its famous bell-shaped curve describes heights, IQ scores, measurement errors, exam grades, and countless natural phenomena.

Its importance stems from the **Central Limit Theorem (CLT)**: regardless of the original distribution, sample means approach normality as sample size grows — making it the foundation of hypothesis testing and confidence intervals.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── CONCEPTS ─────────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)

    tab1, tab2, tab3 = st.tabs(["📐 The Distribution", "📏 Empirical Rule", "🔔 Normal vs Chebyshev"])

    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Probability Density Function (PDF)")
            st.latex(r"f(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)")
            st.markdown("#### Notation")
            st.latex(r"X \sim \mathcal{N}(\mu, \sigma^2)")
            st.markdown("#### Parameters")
            st.markdown("""
- **μ** (mu) = mean → controls the **location** (center) of the bell
- **σ** (sigma) = SD → controls the **spread** (width) of the bell
- **σ²** = variance
            """)
            st.markdown("#### Standard Normal")
            st.latex(r"Z \sim \mathcal{N}(0, 1), \quad \phi(z) = \frac{1}{\sqrt{2\pi}}e^{-z^2/2}")

        with col2:
            st.markdown("#### Key Properties")
            st.markdown("""
1. **Symmetric** about μ
2. Mean = Median = Mode = μ
3. Total area under curve = 1
4. Bell-shaped (asymptotes to x-axis)
5. Defined for all x ∈ (−∞, +∞)
6. **Tails never touch the x-axis** (asymptotic)
            """)
            st.markdown("#### Transformations")
            st.latex(r"\text{Standardize: } Z = \frac{X-\mu}{\sigma}")
            st.latex(r"\text{Unstandardize: } X = \mu + Z\sigma")
            st.markdown("#### Cumulative Distribution (CDF)")
            st.latex(r"\Phi(z) = P(Z \leq z) = \int_{-\infty}^{z} \phi(t)\,dt")
            st.markdown("#### Symmetry of CDF")
            st.latex(r"\Phi(-z) = 1 - \Phi(z)")

    with tab2:
        st.markdown("#### The 68-95-99.7% Empirical Rule")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.success("**Within 1σ**\nP(μ−σ < X < μ+σ)\n= **68.27%**")
            st.latex(r"P(\mu-\sigma < X < \mu+\sigma) \approx 0.6827")
        with col2:
            st.info("**Within 2σ**\nP(μ−2σ < X < μ+2σ)\n= **95.45%**")
            st.latex(r"P(\mu-2\sigma < X < \mu+2\sigma) \approx 0.9545")
        with col3:
            st.warning("**Within 3σ**\nP(μ−3σ < X < μ+3σ)\n= **99.73%**")
            st.latex(r"P(\mu-3\sigma < X < \mu+3\sigma) \approx 0.9973")

        st.markdown("#### Computing Areas: The Z-Table Approach")
        st.markdown("""
1. Convert to z-score: z = (x − μ)/σ
2. Look up Φ(z) from z-table (or use scipy/calculator)
3. Apply symmetry/subtraction as needed

**Common scenarios:**
- P(X < x) = Φ(z)
- P(X > x) = 1 − Φ(z)  
- P(x₁ < X < x₂) = Φ(z₂) − Φ(z₁)
        """)

    with tab3:
        st.markdown("#### Normal vs Chebyshev — Side by Side Comparison")
        st.markdown("""
| k SDs | Chebyshev (Min Guarantee) | Normal (Exact) | Gap |
|-------|--------------------------|----------------|-----|
| 1 | No guarantee (0%) | 68.27% | Large |
| 1.5 | ≥ 55.6% | 86.64% | 31 pp |
| 2 | ≥ 75.0% | 95.45% | 20 pp |
| 3 | ≥ 88.9% | 99.73% | 11 pp |
| 4 | ≥ 93.75% | 99.994% | 6 pp |
| 5 | ≥ 96.0% | 99.9999% | 4 pp |
        """)
        st.markdown("""
**Key insight:** Chebyshev is conservative because it makes no distributional assumption.
The Normal's exact values are much higher because it has "thin tails" — probability drops off exponentially.

**When to use which:**
- Know distribution is normal → use **68-95-99.7 rule**
- Distribution unknown → use **Chebyshev** (safe, guaranteed)
        """)

    # Interactive bell curve
    st.markdown("---")
    st.markdown("#### 🎛️ Interactive Normal Distribution Explorer")
    col1, col2, col3 = st.columns(3)
    with col1:
        mu = st.number_input("Mean (μ):", value=0.0, step=0.5)
    with col2:
        sigma = st.number_input("Std Dev (σ):", value=1.0, step=0.1, min_value=0.1)
    with col3:
        k = st.slider("Highlight within k σ:", 0.5, 4.0, 2.0, 0.1)

    x = np.linspace(mu - 4.5*sigma, mu + 4.5*sigma, 500)
    y = stats.norm.pdf(x, mu, sigma)
    mask = (x >= mu - k*sigma) & (x <= mu + k*sigma)
    coverage = stats.norm.cdf(mu + k*sigma, mu, sigma) - stats.norm.cdf(mu - k*sigma, mu, sigma)
    cheb_bound = max(0, 1 - 1/k**2) if k > 1 else 0.0

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, fill=None, line=dict(color='#667eea', width=2), name='Normal PDF'))
    fig.add_trace(go.Scatter(
        x=x[mask], y=y[mask], fill='tozeroy',
        fillcolor='rgba(102,126,234,0.35)', line=dict(color='rgba(0,0,0,0)'),
        name=f'Within {k}σ ({coverage*100:.2f}%)'
    ))
    fig.add_vline(x=mu, line_dash="dash", line_color="#fbbf24", annotation_text=f"μ={mu}")
    fig.add_vline(x=mu+k*sigma, line_dash="dot", line_color="#34d399")
    fig.add_vline(x=mu-k*sigma, line_dash="dot", line_color="#34d399")
    fig.update_layout(
        title=f"N({mu}, {sigma}²) — Normal: {coverage*100:.2f}%  |  Chebyshev: ≥{cheb_bound*100:.1f}%",
        paper_bgcolor='#ffffff', plot_bgcolor='#f8fafc',
        font_color='#111111', height=360, showlegend=True,
        xaxis=dict(gridcolor='#e2e8f0'),
        yaxis=dict(gridcolor='#e2e8f0', title='Density'),
        legend=dict(bgcolor='rgba(240,240,255,0.9)', font=dict(color='#111111')),
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── SOLVED PROBLEMS ───────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Heights of adult males follow N(μ=175cm, σ=7cm). What % of men are (a) taller than 189cm, (b) between 161cm and 189cm?

**Solution:**

(a) z = (189−175)/7 = 14/7 = **+2.0**  
P(X > 189) = 1 − Φ(2.0) = 1 − 0.9772 = **0.0228 ≈ 2.28%**

(b) z₁ = (161−175)/7 = −14/7 = **−2.0**; z₂ = **+2.0**  
P(161 < X < 189) = Φ(2.0) − Φ(−2.0) = 0.9772 − 0.0228 = **0.9545 ≈ 95.45%**  
(This is the empirical rule at 2σ ✅)
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Exam scores X ~ N(70, 100) [i.e., μ=70, σ=10]. Find: (a) P(X < 85), (b) P(55 < X < 85), (c) 90th percentile score.

**Solution:**

(a) z = (85−70)/10 = 1.5; P(X < 85) = Φ(1.5) = **0.9332 ≈ 93.3%**

(b) z₁=(55−70)/10=−1.5; z₂=1.5; P(55<X<85) = Φ(1.5)−Φ(−1.5) = 0.9332−0.0668 = **0.8664 ≈ 86.64%**

(c) 90th percentile: Φ(z)=0.90 → z ≈ **1.2816**  
x = μ + zσ = 70 + 1.2816(10) = **82.82**
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A machine fills bags with weight X ~ N(500g, 25g²). A bag is "underweight" if < 490g. What fraction is underweight?

**Solution:**

z = (490 − 500)/5 = −10/5 = **−2.0** (σ = √25 = 5)

P(X < 490) = Φ(−2) = 1 − Φ(2) = 1 − 0.9772 = **0.0228 ≈ 2.28%**

In a batch of 10,000 bags: 10,000 × 0.0228 = **228 underweight bags**

To reduce this to 1%: need P(X<490) ≤ 0.01 → z ≤ −2.326  
Re-solve: −10/σ = −2.326 → σ ≤ 4.30g

The machine's SD must be reduced to **≤ 4.30g** to keep underweight rate below 1%.
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 4 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** IQ scores X ~ N(100, 225) [σ=15]. Mensa requires top 2%. What minimum IQ qualifies? Also verify with Chebyshev for the statement "at least 94% of people have IQ between 40 and 160."

**Solution:**

**Part 1 — Mensa IQ cutoff:**  
Top 2% means P(X > x) = 0.02, i.e., P(X < x) = 0.98  
Φ(z) = 0.98 → z ≈ 2.054  
x = 100 + 2.054(15) = **130.8 ≈ IQ 131**
    """)
    st.latex(r"x_{\text{Mensa}} = 100 + 2.054 \times 15 \approx 131")
    st.markdown("""
**Part 2 — Chebyshev verification:**  
[40, 160] = [100±60] = [μ±4σ], so k=4  
Chebyshev: P(|X−100| < 60) ≥ 1 − 1/16 = **93.75%** → the statement "at least 94%" is slightly off (should be 93.75%), but approximately correct. The actual normal value = P(−4<Z<4) = 99.994%.

This illustrates that Chebyshev's bound is tight enough to approximate real claims.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── TRICKY QUESTIONS ─────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** The area to the LEFT of z = −1.5 equals the area to the RIGHT of z = 1.5. Prove this using the symmetry property.")
    with st.expander("🔍 Reveal Solution"):
        st.latex(r"\Phi(-z) = 1 - \Phi(z)")
        st.latex(r"P(Z \leq -1.5) = \Phi(-1.5) = 1 - \Phi(1.5)")
        st.latex(r"P(Z \geq 1.5) = 1 - \Phi(1.5)")
        st.markdown("""
Therefore: P(Z ≤ −1.5) = P(Z ≥ 1.5) ✅

This follows directly from the **symmetry of the normal distribution about 0**. The left tail at −z has exactly the same area as the right tail at +z.

**Practical use:** You need only one half of the z-table to compute any probability. The other half is obtained via this symmetry relationship.
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** A teacher grades 'on a curve' by assigning A to top 10%, B to next 20%, C to next 40%, D to next 20%, F to bottom 10%. Exam scores X ~ N(65, 100). Find the cutoff scores for each grade.")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
μ=65, σ=10. Grades are defined by percentiles:

| Grade | Percentile Range | z-cutoffs | Score cutoffs |
|-------|-----------------|-----------|---------------|
| A | Top 10% (90th–100th) | z ≥ 1.282 | x ≥ **77.8** |
| B | 70th–90th | 0.524 ≤ z < 1.282 | **70.2** ≤ x < 77.8 |
| C | 30th–70th | −0.524 ≤ z < 0.524 | **59.8** ≤ x < 70.2 |
| D | 10th–30th | −1.282 ≤ z < −0.524 | **52.2** ≤ x < 59.8 |
| F | Bottom 10% (0–10th) | z < −1.282 | x < **52.2** |

Calculations: x = μ + z·σ = 65 + z(10)

- 90th percentile: z=1.282, x=65+12.82=77.82 ≈ **77.8**
- 70th percentile: z=0.524, x=65+5.24=70.24 ≈ **70.2**
- 30th percentile: z=−0.524, x=65−5.24=59.76 ≈ **59.8**
- 10th percentile: z=−1.282, x=65−12.82=52.18 ≈ **52.2**

This is exactly how many university curve-grading systems work!
        """)
    st.markdown("</div>", unsafe_allow_html=True)
