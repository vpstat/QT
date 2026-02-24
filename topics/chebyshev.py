import streamlit as st
import numpy as np
import plotly.graph_objects as go

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>📐 Chebyshev's Inequality</h1>
        <p>A universal bound on probability for ANY distribution — no normality required.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── INTRODUCTION ──────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
The **Normal Distribution** guarantees that 68-95-99.7% of data falls within 1-2-3 standard deviations. But what if you don't know whether your data is normally distributed?

**Chebyshev's Inequality** (Pafnuty Chebyshev, 1867) gives a **guaranteed minimum proportion** of data within k standard deviations — for **any distribution** with a finite mean and variance. No distributional assumption required.

It is a *worst-case guarantee* — the actual proportion is often much higher, as given by the empirical rule for normal data.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── CONCEPTS ─────────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Chebyshev's Inequality")
        st.latex(r"P\!\left(|X - \mu| \geq k\sigma\right) \leq \frac{1}{k^2}, \quad k > 1")

        st.markdown("#### Complementary Form (More Useful)")
        st.latex(r"P\!\left(|X - \mu| < k\sigma\right) \geq 1 - \frac{1}{k^2}")

        st.markdown("#### Interval Form")
        st.latex(r"P\!\left(\mu - k\sigma < X < \mu + k\sigma\right) \geq 1 - \frac{1}{k^2}")

        st.markdown("#### Finding k for Target Coverage p")
        st.latex(r"1 - \frac{1}{k^2} \geq p \implies k \geq \frac{1}{\sqrt{1-p}}")

    with col2:
        st.markdown("#### Chebyshev vs Normal Distribution")
        st.markdown("""
| k (SDs) | Chebyshev (ANY dist) | Normal Distribution |
|---------|---------------------|---------------------|
| 1 | No bound | 68.27% |
| 1.5 | ≥ 55.6% | 86.64% |
| 2 | ≥ **75.0%** | 95.45% |
| 3 | ≥ **88.9%** | 99.73% |
| 4 | ≥ **93.75%** | 99.994% |
| 5 | ≥ **96.0%** | 99.9999% |
| 10 | ≥ **99.0%** | ≈ 100% |
        """)
        st.info("⚠️ Chebyshev gives a **conservative lower bound**. For normal data, the actual proportions (right column) are much higher.")

    st.markdown("---")

    # Interactive Chebyshev calculator
    st.markdown("#### 🧮 Interactive Chebyshev Calculator")
    col1, col2 = st.columns(2)
    with col1:
        mode = st.radio("Calculate:", ["Given k, find minimum %", "Given target %, find k"])
    with col2:
        if mode == "Given k, find minimum %":
            k = st.slider("k (number of standard deviations):", 1.1, 10.0, 2.0, 0.1)
            pct = (1 - 1/k**2) * 100
            st.metric("Chebyshev minimum % within k·σ:", f"≥ {pct:.2f}%")
            st.metric("Chebyshev max % outside k·σ:", f"≤ {100/k**2:.2f}%")
        else:
            p = st.slider("Desired coverage (%):", 50, 99, 75)
            p_dec = p / 100
            k_min = 1 / np.sqrt(1 - p_dec)
            st.metric(f"k needed for ≥{p}% coverage:", f"k ≥ {k_min:.3f}")
            st.caption(f"Data interval: [μ − {k_min:.2f}σ, μ + {k_min:.2f}σ]")

    # Visualization
    st.markdown("#### 📊 Chebyshev Bounds vs Normal Distribution")
    k_vals = np.linspace(1.1, 5, 100)
    cheb = (1 - 1/k_vals**2) * 100
    from scipy import stats
    normal = stats.norm.cdf(k_vals)*100 - stats.norm.cdf(-k_vals)*100

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=k_vals, y=cheb, name="Chebyshev (any dist)", line=dict(color='#fbbf24', width=3)))
    fig.add_trace(go.Scatter(x=k_vals, y=normal, name="Normal (68-95-99.7)", line=dict(color='#667eea', width=3)))
    fig.add_hline(y=75, line_dash="dot", line_color="rgba(255,255,255,0.3)", annotation_text="75%")
    fig.add_hline(y=95, line_dash="dot", line_color="rgba(255,255,255,0.3)", annotation_text="95%")
    fig.update_layout(
        title="Coverage within k Standard Deviations",
        xaxis_title="k (number of SDs)", yaxis_title="% of data captured",
        paper_bgcolor='#ffffff', plot_bgcolor='#f8fafc',
        font_color='#111111', height=350, legend=dict(bgcolor='rgba(240,240,255,0.9)', font=dict(color='#111111')),
        xaxis=dict(gridcolor='#e2e8f0'),
        yaxis=dict(gridcolor='#e2e8f0', range=[50, 101]),
    )
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── SOLVED PROBLEMS ───────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A distribution has μ=50, σ=8. Using Chebyshev's inequality, find the minimum % of data within:
(a) 2 standard deviations  (b) 3 standard deviations

**Solution:**

(a) k = 2: P(|X−50| < 16) ≥ 1 − 1/4 = **0.75 → at least 75%** of data lies in [34, 66]

(b) k = 3: P(|X−50| < 24) ≥ 1 − 1/9 ≈ **0.889 → at least 88.9%** of data lies in [26, 74]

Note: If the distribution were normal, the actual percentages would be 95.45% and 99.73% respectively — Chebyshev gives conservative guarantees.
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A factory's machine produces bolts. μ=10mm, σ=0.5mm (distribution unknown). Specifications require bolts between 8.5mm and 11.5mm. What is the minimum % of bolts meeting specs?

**Solution:**

Interval [8.5, 11.5] corresponds to μ ± ? :  
Distance from mean = 11.5 − 10 = 1.5 mm = 3σ (since σ=0.5)

So k = 3:
    """)
    st.latex(r"P(|X - 10| < 1.5) = P(8.5 < X < 11.5) \geq 1 - \frac{1}{3^2} = 1 - \frac{1}{9} \approx 88.9\%")
    st.markdown("**At least 88.9% of bolts** meet specifications — regardless of the distribution shape. If normal, it would be ~99.73%.")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** What value of k guarantees at least 96% of data lies within k standard deviations? Find the interval if μ=100, σ=15.

**Solution:**

Using: 1 − 1/k² ≥ 0.96 → 1/k² ≤ 0.04 → k² ≥ 25 → **k ≥ 5**
    """)
    st.latex(r"k = \frac{1}{\sqrt{1-0.96}} = \frac{1}{\sqrt{0.04}} = \frac{1}{0.2} = 5")
    st.markdown("""
Interval: [μ − 5σ, μ + 5σ] = [100 − 75, 100 + 75] = **[25, 175]**

At least 96% of data lies in [25, 175]. For a normal distribution, 5σ would capture 99.9999% — again, Chebyshev is conservative.
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 4 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Test scores for a large unknown distribution: μ=72, σ=10. (a) At most what % scored below 42 or above 102? (b) At least what % scored between 52 and 92?

**Solution:**

**(a)** Interval [42, 102] = [μ−3σ, μ+3σ], so k=3.  
P(|X−72| ≥ 30) ≤ 1/k² = 1/9 ≈ **11.1%** scored outside (below 42 or above 102).

**(b)** Interval [52, 92] = [μ−2σ, μ+2σ], so k=2.  
P(|X−72| < 20) ≥ 1 − 1/4 = **75%** scored between 52 and 92.

**Important:** For normally distributed scores, (b) would give 95.45% — Chebyshev's 75% is the *worst-case guarantee* for ANY distribution.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── TRICKY QUESTIONS ─────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Can Chebyshev's inequality be applied with k=1? What about k < 1?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**k = 1:** Chebyshev gives P(|X−μ| < σ) ≥ 1 − 1/1 = 0%. This is trivially true but useless — it guarantees **at least 0%** in the interval, which tells us nothing.

The inequality requires **k > 1** to give a useful non-trivial bound.

**k < 1 (e.g., k=0.5):** The formula would give 1 − 1/0.25 = 1 − 4 = −3, which is negative and meaningless. Probability cannot be negative.

For k ≤ 1, no useful lower bound on P(|X−μ| < kσ) exists via Chebyshev.

**Practical implication:** Chebyshev only provides useful information for intervals wider than 1 standard deviation from the mean.
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("""**Q:** A dataset has μ=50, σ=10. Someone claims exactly 70% of data is within [30, 70]. Does this violate Chebyshev's inequality?""")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**No — it does not violate Chebyshev.**

The interval [30, 70] = [μ−2σ, μ+2σ], so k=2.

Chebyshev guarantees: **at least 75%** within k=2 SDs.

But someone claiming **70%** would be IN VIOLATION — 70% < 75% minimum.

Wait — let me re-read: "exactly 70%". This would indeed **violate Chebyshev's guarantee** because the inequality states P(|X−μ| < 2σ) ≥ 75%, meaning at least 75% must lie in [30, 70].

If only 70% lie within [30, 70], that contradicts the inequality.

**Conclusion:** Either the data is wrong, σ is wrong, or Chebyshev applies and 70% < 75% is impossible → the claim is **inconsistent** with the stated mean and standard deviation.

This demonstrates Chebyshev's inequality as a **data validation tool** — if your data doesn't satisfy it, your statistics are incorrect.
        """)
    st.markdown("</div>", unsafe_allow_html=True)
