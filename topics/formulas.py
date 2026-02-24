import streamlit as st

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>🧮 Formula Reference Sheet</h1>
        <p>Every formula covered in this guide, organised for quick exam revision.</p>
    </div>
    """, unsafe_allow_html=True)

    SECTIONS = [
        ("📏", "Center & Spread"),
        ("📊", "Frequency & Data"),
        ("🎲", "Probability"),
        ("📦", "Distributions (Discrete)"),
        ("🌊", "Distributions (Continuous)"),
        ("🔁", "Sampling & CLT"),
        ("🎯", "Estimation & CI"),
        ("⚖️", "Hypothesis Testing"),
        ("📊", "ANOVA"),
        ("📈", "Regression"),
    ]

    if "formula_section" not in st.session_state:
        st.session_state.formula_section = 0

    # Tile grid
    cols_per_row = 5
    for i in range(0, len(SECTIONS), cols_per_row):
        row = SECTIONS[i:i+cols_per_row]
        cols = st.columns(cols_per_row)
        for j, (icon, name) in enumerate(row):
            with cols[j]:
                idx = i + j
                selected = st.session_state.formula_section == idx
                label = f"{'✅ ' if selected else ''}{icon} {name}"
                if st.button(label, key=f"fsec_{idx}", use_container_width=True):
                    st.session_state.formula_section = idx
                    st.rerun()

    active = st.session_state.formula_section

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 1: Center & Spread
    # ═══════════════════════════════════════════════════════════════════════════
    if active == 0:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("### Measures of Center")
        st.latex(r"\bar{x} = \frac{\sum x_i}{n} \quad\text{(Sample Mean)}")
        st.latex(r"\mu = \frac{\sum x_i}{N} \quad\text{(Population Mean)}")
        st.latex(r"\text{Median} = \text{Middle value when sorted (or avg of two middle values)}")
        st.latex(r"\text{Mode} = \text{Most frequent value}")
        st.latex(r"\bar{x}_w = \frac{\sum w_i x_i}{\sum w_i} \quad\text{(Weighted Mean)}")
        st.latex(r"\bar{x}_G = \left(\prod x_i\right)^{1/n} \quad\text{(Geometric Mean)}")
        st.latex(r"\text{Grouped Mean: }\bar{x} = \frac{\sum f_i m_i}{\sum f_i} \quad(m_i = \text{class midpoint})")

        st.markdown("---")
        st.markdown("### Measures of Spread")
        st.latex(r"\text{Range} = x_{\max} - x_{\min}")
        st.latex(r"s^2 = \frac{\sum(x_i - \bar{x})^2}{n-1} \quad\text{(Sample Variance)}")
        st.latex(r"\sigma^2 = \frac{\sum(x_i - \mu)^2}{N} \quad\text{(Population Variance)}")
        st.latex(r"s = \sqrt{s^2}, \quad \sigma = \sqrt{\sigma^2} \quad\text{(Standard Deviation)}")
        st.latex(r"\text{IQR} = Q_3 - Q_1")
        st.latex(r"CV = \frac{s}{\bar{x}} \times 100\% \quad\text{(Coefficient of Variation)}")

        st.markdown("---")
        st.markdown("### Z-Score")
        st.latex(r"z = \frac{x - \mu}{\sigma} \quad\text{(Population)}")
        st.latex(r"z = \frac{x - \bar{x}}{s} \quad\text{(Sample)}")

        st.markdown("---")
        st.markdown("### Quartiles & Outliers")
        st.latex(r"\text{Lower fence} = Q_1 - 1.5 \times \text{IQR}")
        st.latex(r"\text{Upper fence} = Q_3 + 1.5 \times \text{IQR}")
        st.latex(r"P_k = \frac{k}{100}(n+1)\text{-th value (percentile position)}")
        st.markdown("</div>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 2: Frequency & Data
    # ═══════════════════════════════════════════════════════════════════════════
    if active == 1:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("### Frequency Distribution")
        st.latex(r"k = 1 + 3.322\log_{10}(n) \quad\text{(Sturges' Rule — number of classes)}")
        st.latex(r"\text{Class Width} = \frac{\text{Range}}{k} \;\text{(round up)}")
        st.latex(r"\text{Relative Freq.} = \frac{f_i}{n}, \quad \text{Cumul. Freq.} = \sum_{j=1}^{i} f_j")
        st.latex(r"\text{Grouped Variance: } s^2 = \frac{\sum f_i(m_i-\bar{x})^2}{n-1}")

        st.markdown("---")
        st.markdown("### Correlation")
        st.latex(r"r = \frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum(x_i-\bar{x})^2 \sum(y_i-\bar{y})^2}} \quad\text{(Pearson's r)}")
        st.latex(r"r = \frac{S_{xy}}{\sqrt{S_{xx} \cdot S_{yy}}}, \quad -1 \leq r \leq 1")
        st.latex(r"R^2 = r^2 \quad\text{(Coefficient of Determination)}")
        st.markdown("</div>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 3: Probability
    # ═══════════════════════════════════════════════════════════════════════════
    if active == 2:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("### Basic Probability")
        st.latex(r"P(A) = \frac{n(A)}{n(S)} \quad\text{(Classical)}")
        st.latex(r"0 \leq P(A) \leq 1, \quad P(S)=1, \quad P(\emptyset)=0")
        st.latex(r"P(A^c) = 1 - P(A) \quad\text{(Complement)}")

        st.markdown("---")
        st.markdown("### Set Operations & Inclusion-Exclusion")
        st.latex(r"P(A \cup B) = P(A) + P(B) - P(A \cap B)")
        st.latex(r"P(A \cup B \cup C) = \sum P - \sum P(\text{pairs}) + P(A\cap B\cap C)")
        st.latex(r"P(A \setminus B) = P(A) - P(A \cap B)")

        st.markdown("---")
        st.markdown("### De Morgan's Laws")
        st.latex(r"(A \cup B)^c = A^c \cap B^c")
        st.latex(r"(A \cap B)^c = A^c \cup B^c")

        st.markdown("---")
        st.markdown("### Conditional Probability & Independence")
        st.latex(r"P(A|B) = \frac{P(A \cap B)}{P(B)}")
        st.latex(r"P(A \cap B) = P(A|B) \cdot P(B) = P(B|A) \cdot P(A) \quad\text{(Multiplication Rule)}")
        st.latex(r"A \perp B \iff P(A \cap B) = P(A) \cdot P(B)")

        st.markdown("---")
        st.markdown("### Law of Total Probability")
        st.latex(r"P(B) = \sum_{i=1}^{k} P(B|A_i) P(A_i)")

        st.markdown("---")
        st.markdown("### Bayes' Theorem")
        st.latex(r"P(A_i|B) = \frac{P(B|A_i)\,P(A_i)}{\sum_{j} P(B|A_j)\,P(A_j)}")

        st.markdown("---")
        st.markdown("### Counting Rules")
        st.latex(r"n! = n \times (n-1) \times \cdots \times 1")
        st.latex(r"P(n,r) = \frac{n!}{(n-r)!} \quad\text{(Permutations)}")
        st.latex(r"C(n,r) = \binom{n}{r} = \frac{n!}{r!(n-r)!} \quad\text{(Combinations)}")
        st.latex(r"\text{Multiplication Rule: } n_1 \times n_2 \times \cdots \times n_k")
        st.markdown("</div>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 4: Discrete Distributions
    # ═══════════════════════════════════════════════════════════════════════════
    if active == 3:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("### Random Variables — General")
        st.latex(r"E[X] = \sum_x x \cdot P(X=x) \quad\text{(Expected Value, discrete)}")
        st.latex(r"\text{Var}(X) = E[X^2]-(E[X])^2 = \sum_x (x-\mu)^2 P(X=x)")
        st.latex(r"E[aX+b]=aE[X]+b, \quad \text{Var}(aX+b)=a^2\text{Var}(X)")
        st.latex(r"\sigma = \sqrt{\text{Var}(X)}")

        st.markdown("---")
        st.markdown("### Bernoulli(p)")
        st.latex(r"P(X=x) = p^x(1-p)^{1-x},\; x\in\{0,1\}")
        st.latex(r"E[X]=p, \quad \text{Var}(X)=p(1-p)")

        st.markdown("---")
        st.markdown("### Binomial(n, p)")
        st.latex(r"P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}, \quad k=0,1,\ldots,n")
        st.latex(r"E[X]=np, \quad \text{Var}(X)=np(1-p), \quad \sigma=\sqrt{npq}")

        st.markdown("---")
        st.markdown("### Poisson(λ)")
        st.latex(r"P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!}, \quad k=0,1,2,\ldots")
        st.latex(r"E[X]=\lambda, \quad \text{Var}(X)=\lambda \quad\text{(Mean = Variance!)}")
        st.latex(r"X+Y \sim \text{Pois}(\lambda_1+\lambda_2) \;\text{if independent}")

        st.markdown("---")
        st.markdown("### Discrete Uniform(a, b)")
        st.latex(r"P(X=x) = \frac{1}{b-a+1}, \quad x=a,a+1,\ldots,b")
        st.latex(r"E[X]=\frac{a+b}{2}, \quad \text{Var}(X)=\frac{(b-a+1)^2-1}{12}")

        st.markdown("---")
        st.markdown("### Geometric(p)")
        st.latex(r"P(X=k) = (1-p)^{k-1}p, \quad k=1,2,\ldots")
        st.latex(r"E[X]=\frac{1}{p}, \quad \text{Var}(X)=\frac{1-p}{p^2}")
        st.markdown("</div>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 5: Continuous Distributions
    # ═══════════════════════════════════════════════════════════════════════════
    if active == 4:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("### Continuous RV — General")
        st.latex(r"P(a\leq X\leq b) = \int_a^b f(x)\,dx")
        st.latex(r"E[X] = \int_{-\infty}^{\infty} x\,f(x)\,dx")
        st.latex(r"\text{Var}(X) = \int_{-\infty}^{\infty}(x-\mu)^2 f(x)\,dx = E[X^2]-(E[X])^2")
        st.latex(r"F(x) = P(X\leq x) = \int_{-\infty}^{x}f(t)\,dt, \quad f(x)=F'(x)")

        st.markdown("---")
        st.markdown("### Continuous Uniform(a, b)")
        st.latex(r"f(x) = \frac{1}{b-a}, \quad a \leq x \leq b")
        st.latex(r"E[X]=\frac{a+b}{2}, \quad \text{Var}(X)=\frac{(b-a)^2}{12}")

        st.markdown("---")
        st.markdown("### Exponential(λ)")
        st.latex(r"f(x)=\lambda e^{-\lambda x}, \quad x\geq0")
        st.latex(r"F(x) = 1-e^{-\lambda x}")
        st.latex(r"E[X]=\frac{1}{\lambda}, \quad \text{Var}(X)=\frac{1}{\lambda^2}")

        st.markdown("---")
        st.markdown("### Normal Distribution N(μ, σ²)")
        st.latex(r"f(x) = \frac{1}{\sigma\sqrt{2\pi}}\,e^{-\frac{(x-\mu)^2}{2\sigma^2}}")
        st.latex(r"E[X]=\mu, \quad \text{Var}(X)=\sigma^2")
        st.markdown("**Empirical Rule:** 68-95-99.7% within 1σ, 2σ, 3σ")

        st.markdown("---")
        st.markdown("### Standard Normal Z ~ N(0, 1)")
        st.latex(r"Z = \frac{X-\mu}{\sigma}, \quad X = \mu + Z\sigma")
        st.latex(r"\Phi(-z) = 1-\Phi(z) \quad\text{(Symmetry)}")

        st.markdown("---")
        st.markdown("### Chebyshev's Inequality")
        st.latex(r"P(|X-\mu|\geq k\sigma) \leq \frac{1}{k^2} \quad\text{for any distribution, } k>1")
        st.latex(r"P(\mu-k\sigma < X < \mu+k\sigma) \geq 1-\frac{1}{k^2}")
        st.markdown("</div>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 6: Sampling & CLT
    # ═══════════════════════════════════════════════════════════════════════════
    if active == 5:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("### Sampling Distribution of the Mean")
        st.latex(r"E[\bar{X}] = \mu")
        st.latex(r"\text{Var}(\bar{X}) = \frac{\sigma^2}{n}")
        st.latex(r"SE = \sigma_{\bar{X}} = \frac{\sigma}{\sqrt{n}} \quad\text{(Standard Error)}")

        st.markdown("---")
        st.markdown("### Central Limit Theorem")
        st.latex(r"\bar{X} \;\dot\sim\; \mathcal{N}\!\left(\mu,\,\frac{\sigma^2}{n}\right) \quad\text{for large } n")
        st.latex(r"Z = \frac{\bar{X}-\mu}{\sigma/\sqrt{n}} \;\dot\sim\; \mathcal{N}(0,1)")

        st.markdown("---")
        st.markdown("### CLT for Sums")
        st.latex(r"S_n = \sum X_i \;\dot\sim\; \mathcal{N}(n\mu,\, n\sigma^2)")

        st.markdown("---")
        st.markdown("### CLT for Proportions")
        st.latex(r"\hat{p} \;\dot\sim\; \mathcal{N}\!\left(p,\,\frac{p(1-p)}{n}\right)")
        st.caption("Requires np ≥ 5 and n(1−p) ≥ 5")

        st.markdown("---")
        st.markdown("### t-Distribution")
        st.latex(r"t = \frac{\bar{x}-\mu}{s/\sqrt{n}} \sim t_{n-1}")
        st.latex(r"E[t]=0, \quad \text{Var}(t)=\frac{\nu}{\nu-2}\;(\nu>2)")
        st.markdown("</div>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 7: Estimation & CI
    # ═══════════════════════════════════════════════════════════════════════════
    if active == 6:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("### Point Estimators")
        st.latex(r"\hat{\mu}=\bar{x}, \quad \hat{\sigma}^2 = s^2, \quad \hat{p}=\frac{X}{n}")
        st.latex(r"\text{Bias} = E[\hat{\theta}]-\theta, \quad \text{MSE} = \text{Bias}^2 + \text{Var}(\hat{\theta})")

        st.markdown("---")
        st.markdown("### Confidence Intervals")

        st.markdown("**Mean (σ known — Z-interval):**")
        st.latex(r"\bar{x} \pm z_{\alpha/2}\,\frac{\sigma}{\sqrt{n}}")

        st.markdown("**Mean (σ unknown — t-interval):**")
        st.latex(r"\bar{x} \pm t_{\alpha/2,\,n-1}\,\frac{s}{\sqrt{n}}")

        st.markdown("**Proportion:**")
        st.latex(r"\hat{p} \pm z_{\alpha/2}\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}")

        st.markdown("**Difference of two means:**")
        st.latex(r"(\bar{x}_1-\bar{x}_2) \pm t_{\alpha/2}\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}")

        st.markdown("---")
        st.markdown("### Margin of Error & Sample Size")
        st.latex(r"MOE = z_{\alpha/2}\,\frac{\sigma}{\sqrt{n}}")
        st.latex(r"n = \left(\frac{z_{\alpha/2}\,\sigma}{E}\right)^2 \quad\text{(for desired margin E)}")
        st.latex(r"n = \hat{p}(1-\hat{p})\left(\frac{z_{\alpha/2}}{E}\right)^2 \quad\text{(for proportions)}")

        st.markdown("---")
        st.markdown("### Common Critical Values")
        st.latex(r"z_{0.10}=1.282,\; z_{0.05}=1.645,\; z_{0.025}=1.960,\; z_{0.005}=2.576")
        st.markdown("</div>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 8: Hypothesis Testing
    # ═══════════════════════════════════════════════════════════════════════════
    if active == 7:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("### Test Statistics")

        st.markdown("**Z-test (σ known):**")
        st.latex(r"z = \frac{\bar{x}-\mu_0}{\sigma/\sqrt{n}}")

        st.markdown("**t-test (σ unknown):**")
        st.latex(r"t = \frac{\bar{x}-\mu_0}{s/\sqrt{n}}, \quad df = n-1")

        st.markdown("**Two-sample t-test:**")
        st.latex(r"t = \frac{\bar{x}_1-\bar{x}_2}{\sqrt{\frac{s_1^2}{n_1}+\frac{s_2^2}{n_2}}}")

        st.markdown("**Proportion test:**")
        st.latex(r"z = \frac{\hat{p}-p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}")

        st.markdown("---")
        st.markdown("### P-Value Rules")
        st.markdown(r"""
| Tail | P-value |
|------|---------|
| Right (Hₐ: μ > μ₀) | 1 − Φ(z) |
| Left (Hₐ: μ < μ₀) | Φ(z) |
| Two-tailed (Hₐ: μ ≠ μ₀) | 2[1 − Φ(\|z\|)] |
        """)

        st.markdown("---")
        st.markdown("### Decision Rule")
        st.latex(r"p\text{-value} < \alpha \implies \text{Reject } H_0")

        st.markdown("---")
        st.markdown("### Error Types")
        st.latex(r"\alpha = P(\text{Type I}) = P(\text{Reject } H_0 | H_0 \text{ true})")
        st.latex(r"\beta = P(\text{Type II}) = P(\text{Fail to reject } H_0 | H_0 \text{ false})")
        st.latex(r"\text{Power} = 1 - \beta")
        st.markdown("</div>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 9: ANOVA
    # ═══════════════════════════════════════════════════════════════════════════
    if active == 8:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("### One-Way ANOVA")
        st.latex(r"H_0: \mu_1=\mu_2=\cdots=\mu_k")
        st.latex(r"\text{SST} = \text{SSTR} + \text{SSE}")

        st.markdown("---")
        st.markdown("### Sum of Squares")
        st.latex(r"\text{SST} = \sum_i\sum_j(x_{ij}-\bar{x})^2")
        st.latex(r"\text{SSTR} = \sum_{i=1}^k n_i(\bar{x}_i - \bar{x})^2 \quad\text{(Between groups)}")
        st.latex(r"\text{SSE} = \sum_{i=1}^k\sum_{j=1}^{n_i}(x_{ij}-\bar{x}_i)^2 \quad\text{(Within groups)}")

        st.markdown("---")
        st.markdown("### Mean Squares & F-Statistic")
        st.latex(r"\text{MSTR} = \frac{\text{SSTR}}{k-1}")
        st.latex(r"\text{MSE} = \frac{\text{SSE}}{n_T-k}")
        st.latex(r"F = \frac{\text{MSTR}}{\text{MSE}} \sim F_{k-1,\,n_T-k}")

        st.markdown("---")
        st.markdown("### Effect Size")
        st.latex(r"\eta^2 = \frac{\text{SSTR}}{\text{SST}} \quad\text{(proportion of variance explained)}")
        st.markdown("Small: 0.01–0.06 | Medium: 0.06–0.14 | Large: > 0.14")
        st.markdown("</div>", unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════════
    # TAB 10: Regression
    # ═══════════════════════════════════════════════════════════════════════════
    if active == 9:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.markdown("### Simple Linear Regression")
        st.latex(r"\hat{y} = b_0 + b_1 x")
        st.latex(r"b_1 = \frac{\sum(x_i-\bar{x})(y_i-\bar{y})}{\sum(x_i-\bar{x})^2} = \frac{S_{xy}}{S_{xx}} = r\frac{s_y}{s_x}")
        st.latex(r"b_0 = \bar{y} - b_1\bar{x}")

        st.markdown("---")
        st.markdown("### Decomposition of Variance")
        st.latex(r"\text{SST} = \text{SSR} + \text{SSE}")
        st.latex(r"\text{SSR} = \sum(\hat{y}_i-\bar{y})^2 \quad\text{(Explained)}")
        st.latex(r"\text{SSE} = \sum(y_i-\hat{y}_i)^2 \quad\text{(Residual)}")

        st.markdown("---")
        st.markdown("### Coefficient of Determination")
        st.latex(r"R^2 = \frac{\text{SSR}}{\text{SST}} = 1 - \frac{\text{SSE}}{\text{SST}} = r^2")

        st.markdown("---")
        st.markdown("### Standard Error of Estimate")
        st.latex(r"s_e = \sqrt{\frac{\text{SSE}}{n-2}} = \sqrt{\text{MSE}}")

        st.markdown("---")
        st.markdown("### F-Test for Overall Significance")
        st.latex(r"F = \frac{\text{MSR}}{\text{MSE}} = \frac{\text{SSR}/1}{\text{SSE}/(n-2)} \sim F_{1,\,n-2}")
        st.latex(r"H_0: \beta_1=0, \quad H_a: \beta_1 \neq 0")

        st.markdown("---")
        st.markdown("### t-Test for Slope")
        st.latex(r"t = \frac{b_1}{s_{b_1}}, \quad s_{b_1} = \frac{s_e}{\sqrt{S_{xx}}}")
        st.caption("In simple regression: t² = F (equivalent tests)")

        st.markdown("---")
        st.markdown("### Prediction Interval")
        st.latex(r"\hat{y}_0 \pm t_{\alpha/2,\,n-2}\, s_e \sqrt{1 + \frac{1}{n} + \frac{(x_0-\bar{x})^2}{S_{xx}}}")

        st.markdown("---")
        st.markdown("### Assumptions (LINE)")
        st.markdown("**L**inearity · **I**ndependence · **N**ormality of residuals · **E**qual variance")
        st.markdown("</div>", unsafe_allow_html=True)
