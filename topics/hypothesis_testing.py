import streamlit as st
import numpy as np
import plotly.graph_objects as go
from scipy import stats

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>⚖️ Hypothesis Testing</h1>
        <p>A complete guide — framework, p-values, Z-tests, t-tests, errors, and decision making.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
**Hypothesis testing** is the most widely used procedure in inferential statistics. It provides a **formal, repeatable framework** for deciding whether sample data provides strong enough evidence to reject a claim about a population.

**Real-world use cases:**
- Is a new drug more effective than the existing one?
- Has the average delivery time changed after a process change?
- Is the defect rate below the acceptable threshold?
- Do male and female customers spend different amounts?

**The Big Idea:** We assume the status quo (null hypothesis) is true, then ask: *"How unlikely is the observed data under this assumption?"* If the data is very unlikely, we reject the status quo.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📋 Framework & Steps",
        "⚠️ Type I & II Errors",
        "📊 P-Values (Detailed)",
        "🔔 Z-Tests (σ Known)",
        "📈 t-Tests (σ Unknown)"
    ])

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 1: Framework & Steps
    # ═══════════════════════════════════════════════════════════════════════════
    with tab1:
        st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 The 5-Step Hypothesis Testing Procedure</div>", unsafe_allow_html=True)

        st.markdown("### Step 1: State the Hypotheses")
        col1, col2 = st.columns(2)
        with col1:
            st.latex(r"H_0: \text{Null Hypothesis (status quo, claim to test)}")
            st.latex(r"H_a: \text{Alternative Hypothesis (what we want to show)}")
            st.markdown("""
**Rules:**
- H₀ **always** contains the equality (=, ≤, or ≥)
- Hₐ is the **research hypothesis** — what you're trying to prove
- The burden of proof is on Hₐ (we assume H₀ until evidence says otherwise)
            """)
        with col2:
            st.markdown("#### Three Types of Tests")
            st.markdown("""
| Test Name | H₀ | Hₐ | Rejection Region |
|-----------|----|----|-----------------|
| **Two-tailed** | μ = μ₀ | μ ≠ μ₀ | Both tails |
| **Right-tailed (upper)** | μ ≤ μ₀ | μ > μ₀ | Right tail |
| **Left-tailed (lower)** | μ ≥ μ₀ | μ < μ₀ | Left tail |
            """)
            st.info("💡 **Tip:** The direction of Hₐ (>, <, or ≠) is determined by the research question, NOT by the data.")

        st.markdown("### Step 2: Choose the Significance Level (α)")
        st.markdown("""
- **α** = maximum acceptable probability of rejecting H₀ when it is actually true (Type I error)
- Common choices: **α = 0.05** (most common), 0.01 (strict), 0.10 (lenient)
- Must be chosen **before** looking at data
        """)

        st.markdown("### Step 3: Compute the Test Statistic")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Z-test (σ known):**")
            st.latex(r"z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}")
        with col2:
            st.markdown("**t-test (σ unknown):**")
            st.latex(r"t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}, \quad df = n-1")

        st.markdown("### Step 4: Determine the P-Value (or compare with critical value)")
        st.markdown("*See the dedicated P-Value tab for full details →*")

        st.markdown("### Step 5: Make the Decision")
        st.markdown("""
| If... | Decision | Wording |
|-------|----------|---------|
| **p-value < α** | **Reject H₀** | "There is sufficient evidence at the α level to conclude that Hₐ" |
| **p-value ≥ α** | **Fail to reject H₀** | "There is insufficient evidence at the α level to conclude that Hₐ" |
        """)
        st.warning("⚠️ **NEVER say 'Accept H₀'**. We either reject or fail to reject. Failing to reject does not prove H₀ is true — it simply means we don't have enough evidence against it.")

        st.markdown("---")
        st.markdown("#### 📌 Two Equivalent Decision Methods")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("##### Method 1: P-Value Approach")
            st.markdown("""
1. Compute test statistic
2. Compute p-value
3. If **p-value < α** → Reject H₀
4. Most widely used (provides more information)
            """)
        with col2:
            st.markdown("##### Method 2: Critical Value Approach")
            st.markdown("""
1. Find the critical value(s) from z/t table
2. Compute test statistic
3. If test stat falls in **rejection region** → Reject H₀
4. Traditional textbook approach
            """)
        st.markdown("Both methods **always** give the same decision.")
        st.markdown("</div>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 2: Type I & II Errors
    # ═══════════════════════════════════════════════════════════════════════════
    with tab2:
        st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Type I and Type II Errors</div>", unsafe_allow_html=True)

        st.markdown("#### Decision Matrix")
        st.markdown("""
|  | **H₀ is actually TRUE** | **H₀ is actually FALSE** |
|--|------------------------|-------------------------|
| **Reject H₀** | ❌ **Type I Error** (α)<br>False Positive | ✅ **Correct** (Power = 1−β)<br>True Positive |
| **Fail to reject H₀** | ✅ **Correct** (1−α)<br>True Negative | ❌ **Type II Error** (β)<br>False Negative |
        """)

        st.markdown("---")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### ❌ Type I Error (False Positive)")
            st.latex(r"\alpha = P(\text{Reject } H_0 \mid H_0 \text{ is true})")
            st.markdown("""
**Real-world analogy:** Convicting an innocent person.

**Examples:**
- Concluding a drug works when it doesn't → patients take an ineffective drug
- Declaring a manufacturing process out of control when it's fine → unnecessary shutdowns
- Finding a "significant" marketing effect that's actually random noise → wasted budget

**Controlled by:** The researcher sets α before the test.
            """)

        with col2:
            st.markdown("### ❌ Type II Error (False Negative)")
            st.latex(r"\beta = P(\text{Fail to reject } H_0 \mid H_0 \text{ is false})")
            st.markdown("""
**Real-world analogy:** Letting a guilty person go free.

**Examples:**
- Missing a real drug effect → patients denied an effective treatment
- Not detecting an actual shift in quality → defective products shipped
- Missing a real difference in customer preferences → missed opportunity

**Harder to control.** Depends on: sample size n, effect size, σ, and α.
            """)

        st.markdown("---")
        st.markdown("### ⚡ Power of a Test")
        st.latex(r"\text{Power} = 1 - \beta = P(\text{Reject } H_0 \mid H_0 \text{ is false})")
        st.markdown("""
Power is the probability of **correctly detecting a real effect**. Higher is better (target: 0.80+).

#### What Increases Power?
| Factor | Direction | Why |
|--------|-----------|-----|
| ↑ Sample size n | ↑↑ Power | SE decreases → test more sensitive |
| ↑ Effect size (distance from μ₀) | ↑ Power | Bigger effect easier to detect |
| ↑ α (e.g. 0.05 → 0.10) | ↑ Power | Wider rejection region (but more Type I risk) |
| ↓ σ (population spread) | ↑ Power | Less noise → clearer signal |

#### The α-β Trade-off
Decreasing α (being more strict about Type I errors) **increases β** (makes Type II errors more likely). You cannot minimise both simultaneously without increasing n.
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problem</div>", unsafe_allow_html=True)
        st.markdown("<span class='prob-badge'>Problem — Error Classification</span>", unsafe_allow_html=True)
        st.markdown("""
**Q:** A pharmaceutical company tests H₀: μ = 50 (old drug effect) vs Hₐ: μ > 50 (new drug is better) at α = 0.05.

Classify the following scenarios:
1. The new drug actually works (μ = 55) but the test fails to reject H₀.
2. The old drug is fine (μ = 50) but the test rejects H₀ anyway.
3. The new drug works (μ = 55) and the test correctly rejects H₀.

**Solution:**
1. **Type II Error (β)** — a real effect was missed (false negative)
2. **Type I Error (α = 0.05)** — a non-existent effect was declared significant (false positive)
3. **Correct decision (Power = 1−β)** — the test correctly detected the real effect
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 3: P-Values (Detailed)
    # ═══════════════════════════════════════════════════════════════════════════
    with tab3:
        st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 What is a P-Value?</div>", unsafe_allow_html=True)

        st.markdown("#### Formal Definition")
        st.latex(r"p\text{-value} = P(\text{observing data as extreme or more extreme than sample} \mid H_0 \text{ is true})")

        st.markdown("""
**In plain English:** The p-value is the probability of getting results **at least as surprising** as what we observed, **assuming the null hypothesis is true**.

**Key points:**
- It is **NOT** P(H₀ is true) — this is a common misconception!
- It is **NOT** the probability of making an error
- Smaller p-value = stronger evidence against H₀
- It is a measure of **compatibility** between the data and H₀
        """)

        st.markdown("---")
        st.markdown("#### How P-Values Are Computed")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("##### Right-tailed (Hₐ: μ > μ₀)")
            st.latex(r"p = P(Z \geq z_{obs})")
            st.latex(r"= 1 - \Phi(z_{obs})")
            st.caption("Area to the RIGHT of test stat")
        with col2:
            st.markdown("##### Left-tailed (Hₐ: μ < μ₀)")
            st.latex(r"p = P(Z \leq z_{obs})")
            st.latex(r"= \Phi(z_{obs})")
            st.caption("Area to the LEFT of test stat")
        with col3:
            st.markdown("##### Two-tailed (Hₐ: μ ≠ μ₀)")
            st.latex(r"p = 2 \times P(Z \geq |z_{obs}|)")
            st.latex(r"= 2 \times [1 - \Phi(|z_{obs}|)]")
            st.caption("Double the one-tail probability")

        st.markdown("---")
        st.markdown("#### 📊 Interpreting P-Values — Strength of Evidence")
        st.markdown("""
| P-value Range | Interpretation | Star Notation |
|--------------|---------------|---------------|
| p > 0.10 | No evidence against H₀ | (not significant) |
| 0.05 < p ≤ 0.10 | Weak evidence against H₀ | • (marginal) |
| 0.01 < p ≤ 0.05 | Evidence against H₀ | * (significant) |
| 0.001 < p ≤ 0.01 | Strong evidence against H₀ | ** (highly significant) |
| p ≤ 0.001 | Very strong evidence against H₀ | *** (very highly significant) |
        """)

        st.markdown("---")
        st.markdown("#### 🔴 Common P-Value Misconceptions")
        col1, col2 = st.columns(2)
        with col1:
            st.error("""
**❌ WRONG: "p = 0.03 means there's a 3% chance H₀ is true."**

p-value assumes H₀ is true and asks about the data, not the other way around. To get P(H₀ is true | data), you need Bayes' theorem.
            """)
            st.error("""
**❌ WRONG: "p = 0.06 means the study failed."**

p = 0.06 is *marginal* — it suggests some evidence but doesn't meet α = 0.05 cutoff. It does NOT mean there is no effect.
            """)
        with col2:
            st.error("""
**❌ WRONG: "p = 0.001 means the effect is large and important."**

A tiny p-value means the evidence against H₀ is strong, but the effect could be practically **trivial**. With n = 100,000, even a 0.1-unit difference can produce p < 0.001. Always report **effect size** alongside p-value.
            """)
            st.error("""
**❌ WRONG: "Not significant means there's no difference."**

"Fail to reject H₀" ≠ "H₀ is true". The study might simply have been underpowered (too small n) to detect a real effect.
            """)

        st.markdown("---")
        st.markdown("#### 🧮 Interactive P-Value Calculator")
        col1, col2 = st.columns(2)
        with col1:
            dist_type = st.radio("Distribution:", ["Z (Standard Normal)", "t (Student's t)"], key="pv_dist")
            test_dir = st.radio("Tail:", ["Right (>)", "Left (<)", "Two-tailed (≠)"], key="pv_tail")
            stat_val = st.number_input("Test statistic value:", value=2.10, step=0.01, key="pv_stat")
            if "t" in dist_type:
                df_pv = st.number_input("Degrees of freedom:", value=20, min_value=1, key="pv_df")

        with col2:
            if "Z" in dist_type:
                if "Right" in test_dir:
                    pv = 1 - stats.norm.cdf(stat_val)
                elif "Left" in test_dir:
                    pv = stats.norm.cdf(stat_val)
                else:
                    pv = 2 * (1 - stats.norm.cdf(abs(stat_val)))
            else:
                if "Right" in test_dir:
                    pv = 1 - stats.t.cdf(stat_val, df_pv)
                elif "Left" in test_dir:
                    pv = stats.t.cdf(stat_val, df_pv)
                else:
                    pv = 2 * (1 - stats.t.cdf(abs(stat_val), df_pv))

            st.metric("P-value", f"{pv:.6f}")
            if pv <= 0.001:
                stars = "*** (Very highly significant)"
            elif pv <= 0.01:
                stars = "** (Highly significant)"
            elif pv <= 0.05:
                stars = "* (Significant)"
            elif pv <= 0.10:
                stars = "• (Marginal)"
            else:
                stars = "(Not significant)"
            st.info(f"**Evidence level:** {stars}")

            for a_check in [0.01, 0.05, 0.10]:
                if pv < a_check:
                    st.success(f"Reject H₀ at α = {a_check}")
                else:
                    st.warning(f"Fail to reject at α = {a_check}")

        # P-value visual
        x_range = np.linspace(-4, 4, 300)
        if "Z" in dist_type:
            y_curve = stats.norm.pdf(x_range)
        else:
            y_curve = stats.t.pdf(x_range, df_pv)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_range, y=y_curve, mode='lines',
                                  line=dict(color='#4f46e5', width=2), name='Distribution'))
        # Shade p-value region
        if "Right" in test_dir:
            x_shade = x_range[x_range >= stat_val]
            y_shade = stats.norm.pdf(x_shade) if "Z" in dist_type else stats.t.pdf(x_shade, df_pv)
            fig.add_trace(go.Scatter(x=x_shade, y=y_shade, fill='tozeroy',
                                      fillcolor='rgba(220,38,38,0.3)', line=dict(width=0), name=f'p = {pv:.4f}'))
        elif "Left" in test_dir:
            x_shade = x_range[x_range <= stat_val]
            y_shade = stats.norm.pdf(x_shade) if "Z" in dist_type else stats.t.pdf(x_shade, df_pv)
            fig.add_trace(go.Scatter(x=x_shade, y=y_shade, fill='tozeroy',
                                      fillcolor='rgba(220,38,38,0.3)', line=dict(width=0), name=f'p = {pv:.4f}'))
        else:
            for sv in [abs(stat_val), -abs(stat_val)]:
                if sv > 0:
                    xs = x_range[x_range >= sv]
                else:
                    xs = x_range[x_range <= sv]
                ys = stats.norm.pdf(xs) if "Z" in dist_type else stats.t.pdf(xs, df_pv)
                fig.add_trace(go.Scatter(x=xs, y=ys, fill='tozeroy',
                                          fillcolor='rgba(220,38,38,0.3)', line=dict(width=0), showlegend=False))
        fig.add_vline(x=stat_val, line_dash="dash", line_color="#dc2626",
                      annotation_text=f"stat={stat_val:.2f}")
        fig.update_layout(title=f"P-value = {pv:.6f} (shaded area)", paper_bgcolor='#ffffff',
                          plot_bgcolor='#f8fafc', font_color='#111111', height=300,
                          xaxis=dict(gridcolor='#e2e8f0'), yaxis=dict(gridcolor='#e2e8f0'))
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 4: Z-Tests
    # ═══════════════════════════════════════════════════════════════════════════
    with tab4:
        st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Z-Tests (σ Known)</div>", unsafe_allow_html=True)
        st.markdown("#### When to Use")
        st.markdown("""
- Population standard deviation σ is **known**
- Sample size is large (n ≥ 30) — even if σ is estimated, Z is acceptable
- Population is approximately Normal (or n is large enough for CLT)
        """)
        st.markdown("#### Test Statistic")
        st.latex(r"z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}}")
        st.markdown("#### Critical Values")
        st.markdown(r"""
| α | One-tailed z* | Two-tailed ±z* |
|---|--------------|----------------|
| 0.10 | 1.282 | ±1.645 |
| 0.05 | 1.645 | ±1.960 |
| 0.01 | 2.326 | ±2.576 |
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-card'><div class='section-label label-solved'>🧮 Interactive Z-Test Calculator</div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            mu_0 = st.number_input("μ₀ (hypothesised mean):", value=100.0, step=1.0, key="zt_mu")
            xbar = st.number_input("x̄ (sample mean):", value=103.5, step=0.5, key="zt_xbar")
            sigma = st.number_input("σ (population SD):", value=15.0, min_value=0.01, step=0.5, key="zt_sig")
            n_test = st.number_input("n (sample size):", value=36, min_value=2, key="zt_n")
            alpha = st.selectbox("α:", [0.01, 0.05, 0.10], index=1, key="zt_alpha")
            test_type = st.radio("Hₐ:", ["μ > μ₀ (upper)", "μ < μ₀ (lower)", "μ ≠ μ₀ (two-tailed)"], key="zt_type")
        with col2:
            se = sigma / np.sqrt(n_test)
            z_stat = (xbar - mu_0) / se
            if "upper" in test_type:
                p_val = 1 - stats.norm.cdf(z_stat)
                z_crit = stats.norm.ppf(1 - alpha)
                rej = z_stat > z_crit
            elif "lower" in test_type:
                p_val = stats.norm.cdf(z_stat)
                z_crit = stats.norm.ppf(alpha)
                rej = z_stat < z_crit
            else:
                p_val = 2 * (1 - stats.norm.cdf(abs(z_stat)))
                z_crit = stats.norm.ppf(1 - alpha/2)
                rej = abs(z_stat) > z_crit
            st.metric("SE = σ/√n", f"{se:.4f}")
            st.metric("z-statistic", f"{z_stat:.4f}")
            st.metric("p-value", f"{p_val:.6f}")
            st.metric("Critical z*", f"±{z_crit:.3f}" if "two" in test_type else f"{z_crit:.3f}")
            if rej:
                st.error(f"**REJECT H₀** at α={alpha} (p={p_val:.4f} < {alpha})")
            else:
                st.success(f"**Fail to reject H₀** at α={alpha} (p={p_val:.4f} ≥ {alpha})")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)
        st.markdown("<span class='prob-badge'>Problem 1 — Upper Tail Z-Test</span>", unsafe_allow_html=True)
        st.markdown("""
**Q:** A manufacturer claims bulb lifetime μ = 1000 hours (σ = 120). Sample of 50: x̄ = 1035. At α = 0.05, is μ > 1000?

**Solution:** H₀: μ ≤ 1000, Hₐ: μ > 1000 (right-tailed)
        """)
        st.latex(r"z = \frac{1035 - 1000}{120/\sqrt{50}} = \frac{35}{16.97} = 2.063")
        st.latex(r"p\text{-value} = 1-\Phi(2.063) = 0.0196 < 0.05 \implies \text{Reject } H_0")
        st.markdown("**Conclusion:** Sufficient evidence that mean lifetime exceeds 1000 hours.")
        st.divider()

        st.markdown("<span class='prob-badge'>Problem 2 — Lower Tail Z-Test</span>", unsafe_allow_html=True)
        st.markdown("""
**Q:** Fill specification μ ≥ 500ml (σ = 8). n = 40, x̄ = 497.5. At α = 0.01, is fill below standard?

**Solution:** H₀: μ ≥ 500, Hₐ: μ < 500 (left-tailed)
        """)
        st.latex(r"z = \frac{497.5-500}{8/\sqrt{40}} = \frac{-2.5}{1.265} = -1.976")
        st.latex(r"p = \Phi(-1.976) = 0.0241 > 0.01 \implies \text{Fail to reject } H_0")
        st.markdown("**Conclusion at α=0.01:** Insufficient evidence of under-filling. *(Note: Would reject at α=0.05 since 0.0241 < 0.05.)*")
        st.divider()

        st.markdown("<span class='prob-badge'>Problem 3 — Two-Tailed Z-Test</span>", unsafe_allow_html=True)
        st.markdown("""
**Q:** A cereal box should weigh μ = 400g (σ = 12). n = 64, x̄ = 397.9. At α = 0.05, has the mean changed?

**Solution:** H₀: μ = 400, Hₐ: μ ≠ 400 (two-tailed)
        """)
        st.latex(r"z = \frac{397.9-400}{12/\sqrt{64}} = \frac{-2.1}{1.5} = -1.40")
        st.latex(r"p = 2\times\Phi(-1.40) = 2\times0.0808 = 0.1616 > 0.05 \implies \text{Fail to reject } H_0")
        st.markdown("**Conclusion:** No statistically significant change in mean weight.")
        st.markdown("</div>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 5: t-Tests
    # ═══════════════════════════════════════════════════════════════════════════
    with tab5:
        st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 t-Tests (σ Unknown)</div>", unsafe_allow_html=True)
        st.markdown("#### When to Use")
        st.markdown("""
- Population σ is **unknown** (the most common real-world case!)
- We estimate σ with the **sample standard deviation s**
- The t-distribution accounts for the extra uncertainty from estimating σ
- df = n − 1 (for one-sample t-test)
        """)
        st.markdown("#### Test Statistic")
        st.latex(r"t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} \sim t_{n-1}")
        st.markdown("#### Z-test vs t-test — When to Use Which?")
        st.markdown("""
| Scenario | Test | Why |
|----------|------|-----|
| σ known | **Z-test** | No extra uncertainty |
| σ unknown, n ≥ 30 | **t-test** (Z is okay too) | t ≈ Z for large df |
| σ unknown, n < 30, pop ~Normal | **t-test** (required!) | Wider tails compensate for uncertainty |
| σ unknown, n < 30, pop non-Normal | ⚠️ t-test approximate or use **nonparametric** | t less reliable |
        """)
        st.caption("In practice: when in doubt, use the t-test — it's always valid and converges to Z for large n.")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-card'><div class='section-label label-solved'>🧮 Interactive t-Test Calculator</div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            mu_0t = st.number_input("μ₀:", value=75.0, step=1.0, key="tt_mu")
            xbar_t = st.number_input("x̄:", value=72.0, step=0.5, key="tt_xbar")
            s_t = st.number_input("s (sample SD):", value=8.0, min_value=0.01, step=0.5, key="tt_s")
            n_t = st.number_input("n:", value=16, min_value=2, key="tt_n")
            alpha_t = st.selectbox("α:", [0.01, 0.05, 0.10], index=1, key="tt_alpha")
            test_t = st.radio("Hₐ:", ["μ > μ₀", "μ < μ₀", "μ ≠ μ₀"], key="tt_type")
        with col2:
            df_t = n_t - 1
            se_t = s_t / np.sqrt(n_t)
            t_stat = (xbar_t - mu_0t) / se_t
            if ">" in test_t:
                pv_t = 1 - stats.t.cdf(t_stat, df_t)
                tc = stats.t.ppf(1 - alpha_t, df_t)
                rej_t = t_stat > tc
            elif "<" in test_t:
                pv_t = stats.t.cdf(t_stat, df_t)
                tc = stats.t.ppf(alpha_t, df_t)
                rej_t = t_stat < tc
            else:
                pv_t = 2 * (1 - stats.t.cdf(abs(t_stat), df_t))
                tc = stats.t.ppf(1 - alpha_t/2, df_t)
                rej_t = abs(t_stat) > tc
            st.metric("df", f"{df_t}")
            st.metric("SE = s/√n", f"{se_t:.4f}")
            st.metric("t-statistic", f"{t_stat:.4f}")
            st.metric("p-value", f"{pv_t:.6f}")
            st.metric("Critical t*", f"±{tc:.3f}" if "≠" in test_t else f"{tc:.3f}")
            if rej_t:
                st.error(f"**REJECT H₀** at α={alpha_t} (p={pv_t:.4f} < {alpha_t})")
            else:
                st.success(f"**Fail to reject H₀** at α={alpha_t} (p={pv_t:.4f} ≥ {alpha_t})")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)
        st.markdown("<span class='prob-badge'>Problem 1 — One-Sample t-Test</span>", unsafe_allow_html=True)
        st.markdown("""
**Q:** 16 students score x̄ = 72, s = 8 on a test. The expected mean is 75. At α = 0.05, is the class significantly below the expected mean?

**Solution:** H₀: μ ≥ 75, Hₐ: μ < 75 (left-tailed), df = 15
        """)
        t_ex1 = (72-75)/(8/np.sqrt(16))
        pv_ex1 = stats.t.cdf(t_ex1, 15)
        tc_ex1 = stats.t.ppf(0.05, 15)
        st.latex(rf"t = \frac{{72-75}}{{8/\sqrt{{16}}}} = \frac{{-3}}{{2}} = {t_ex1:.3f}")
        st.latex(rf"t_{{0.05,15}} = {tc_ex1:.3f},\quad p = {pv_ex1:.4f}")
        st.markdown(f"Since |t| = 1.5 < |{tc_ex1:.3f}| and p = {pv_ex1:.4f} > 0.05: **Fail to reject H₀.** Insufficient evidence that the class is scoring below 75.")
        st.divider()

        st.markdown("<span class='prob-badge'>Problem 2 — t-Test for Quality Control</span>", unsafe_allow_html=True)
        st.markdown("""
**Q:** A coffee shop claims its large cup is 480ml. A consumer group samples 10 cups: x̄ = 471.2, s = 11.5. At α = 0.05, is the shop under-filling?

**Solution:** H₀: μ ≥ 480, Hₐ: μ < 480 (left-tailed), df = 9
        """)
        t_ex2 = (471.2-480)/(11.5/np.sqrt(10))
        pv_ex2 = stats.t.cdf(t_ex2, 9)
        tc_ex2 = stats.t.ppf(0.05, 9)
        st.latex(rf"t = \frac{{471.2-480}}{{11.5/\sqrt{{10}}}} = \frac{{-8.8}}{{3.637}} = {t_ex2:.3f}")
        st.latex(rf"t_{{0.05,9}} = {tc_ex2:.3f},\quad p = {pv_ex2:.6f}")
        st.markdown(f"Since t = {t_ex2:.3f} < {tc_ex2:.3f} and p = {pv_ex2:.6f} < 0.05: **Reject H₀.** The shop is significantly under-filling its large cups.")
        st.markdown("</div>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TRICKY QUESTIONS (outside tabs)
    # ═══════════════════════════════════════════════════════════════════════════
    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Can we *prove* H₀ is true by failing to reject it?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**No — never.** Hypothesis testing can only reject H₀ or fail to reject it. Failing to reject means the data is *compatible* with H₀ — but it might also be compatible with many alternative values of μ.

**Analogy:** In a courtroom, "Not Guilty" does not mean "Innocent" — it means the prosecution didn't provide sufficient evidence.

To *support* H₀ (equivalence), you need a different framework: **equivalence testing** (TOST procedure), where you show μ is within some practical margin of μ₀.
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** A study with n=100,000 finds p=0.001 for a mean difference of 0.5 points (on a 100-point scale). Is this meaningful?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**Statistically significant? Yes (p=0.001).**  
**Practically significant? No (0.5 points out of 100 is trivial).**

This illustrates the distinction between **statistical significance** and **practical significance**:

- With n = 100,000, SE is tiny, so even minuscule differences produce large test statistics and small p-values.
- **Effect size** (e.g. Cohen's d = 0.5/SD) would reveal the effect is negligible.
- Always report effect size, confidence intervals, AND p-values together.
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q3</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Researcher A tests at α=0.05 and gets p=0.04 → rejects H₀. Researcher B tests the same data at α=0.01 → p=0.04 → fails to reject. Who is correct?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**Both are correct.** They made different decisions because they chose different α levels — different tolerances for Type I error.

- Researcher A: 0.04 < 0.05 → rejects (willing to accept 5% false positive rate)
- Researcher B: 0.04 > 0.01 → fails to reject (requires 1% or less)

This is why **α must be declared before the test**, and why **reporting the exact p-value** is more informative than just "significant" or "not significant".
        """)
    st.markdown("</div>", unsafe_allow_html=True)
