import streamlit as st
import numpy as np

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>🔄 Bayes' Theorem</h1>
        <p>Reversing conditional probability — updating beliefs with new evidence.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
**Bayes' Theorem** (Thomas Bayes, 1763) answers: *"Given that we observed evidence B, how should we update our belief about cause A?"*

It is the engine of **Bayesian statistics**, machine learning classifiers, spam filters, medical diagnosis, and scientific reasoning.

Key vocabulary:
- **Prior probability P(A)** — our belief *before* seeing evidence
- **Likelihood P(B|A)** — how probable is the evidence if A is true?
- **Posterior probability P(A|B)** — updated belief *after* seeing evidence
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts & Formulas</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### Bayes' Theorem (Simple Form)")
        st.latex(r"P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}")

        st.markdown("#### Expanded Form (using Total Probability)")
        st.latex(r"P(A_i|B) = \frac{P(B|A_i) \cdot P(A_i)}{\sum_{j=1}^{k} P(B|A_j) \cdot P(A_j)}")
        st.caption("Where A₁, A₂, ..., Aₖ form a partition of S")

        st.markdown("#### Bayesian Formula in Words")
        st.latex(r"\text{Posterior} = \frac{\text{Likelihood} \times \text{Prior}}{\text{Evidence}}")

    with col2:
        st.markdown("#### Odds Form of Bayes' Theorem")
        st.latex(r"\frac{P(A|B)}{P(A^c|B)} = \frac{P(B|A)}{P(B|A^c)} \times \frac{P(A)}{P(A^c)}")
        st.markdown("Posterior Odds = **Likelihood Ratio** × Prior Odds")

        st.markdown("#### Sequential Updating")
        st.markdown("""
In Bayesian inference, each new piece of evidence updates the posterior, which becomes the new prior:
1. Start: Prior P(A)
2. See evidence B₁ → compute P(A|B₁) using Bayes
3. P(A|B₁) becomes new prior
4. See evidence B₂ → compute P(A|B₁,B₂)
5. Repeat — each observation refines our belief
        """)

    st.markdown("---")

    # Interactive Bayes calculator
    st.markdown("#### 🧮 Interactive Bayes Calculator")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Setup (choose scenario or enter values):**")
        scenario = st.selectbox("Quick scenario:", [
            "Custom values",
            "Medical test (1% prevalence, 95% sensitivity, 90% specificity)",
            "Spam filter (40% spam, 80% keyword in spam, 5% keyword in ham)",
            "Factory defects (60%/40% split, 2%/5% defect rates)"
        ])
        if scenario == "Medical test (1% prevalence, 95% sensitivity, 90% specificity)":
            pA = 0.01; pBgA = 0.95; pBgAc = 0.10
        elif scenario == "Spam filter (40% spam, 80% keyword in spam, 5% keyword in ham)":
            pA = 0.40; pBgA = 0.80; pBgAc = 0.05
        elif scenario == "Factory defects (60%/40% split, 2%/5% defect rates)":
            pA = 0.60; pBgA = 0.02; pBgAc = 0.05
        else:
            pA = st.number_input("P(A) — Prior:", value=0.30, min_value=0.001, max_value=0.999, step=0.01)
            pBgA = st.number_input("P(B|A) — Likelihood:", value=0.70, min_value=0.001, max_value=1.0, step=0.01)
            pBgAc = st.number_input("P(B|Aᶜ) — False positive rate:", value=0.20, min_value=0.001, max_value=1.0, step=0.01)

    with col2:
        pAc = 1 - pA
        pB = pBgA * pA + pBgAc * pAc
        posterior = (pBgA * pA) / pB
        st.markdown("**Results:**")
        st.metric("P(B) — Total evidence probability", f"{pB:.4f}")
        st.metric("P(A|B) — Posterior", f"{posterior:.4f} ({posterior*100:.1f}%)")
        st.metric("Likelihood Ratio", f"{pBgA/pBgAc:.2f}×")
        lift = posterior / pA
        st.info(f"📈 Prior {pA:.0%} → Posterior {posterior:.1%} (×{lift:.2f} update factor)")

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A box contains 2 red and 3 blue balls. A ball is drawn, replaced, and another drawn. Given the second is red, what is P(first was also red)?

**Solution:**

Events: A = "First ball red" (P(A) = 2/5), B = "Second ball red"

P(B|A) = 2/5 (with replacement, same composition regardless of first draw)
P(B|Aᶜ) = 2/5 (same — draws are independent with replacement!)

Since draws are independent here: P(A|B) = P(A) = **2/5 = 0.40**

This confirms: with replacement, knowledge of second draw gives NO information about first draw.
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Three urns: U₁(3R,2B), U₂(1R,4B), U₃(4R,1B). An urn is selected randomly (P=1/3 each). A red ball is drawn. Find P(ball came from U₁).

**Solution:**
    """)
    st.latex(r"P(R|U_1)=\frac{3}{5},\quad P(R|U_2)=\frac{1}{5},\quad P(R|U_3)=\frac{4}{5}")
    st.latex(r"P(R) = \frac{1}{3}\cdot\frac{3}{5}+\frac{1}{3}\cdot\frac{1}{5}+\frac{1}{3}\cdot\frac{4}{5} = \frac{1}{3}\cdot\frac{8}{5} = \frac{8}{15}")
    st.latex(r"P(U_1|R) = \frac{P(R|U_1)\cdot P(U_1)}{P(R)} = \frac{\frac{3}{5}\cdot\frac{1}{3}}{\frac{8}{15}} = \frac{\frac{1}{5}}{\frac{8}{15}} = \frac{1}{5}\times\frac{15}{8} = \frac{3}{8} = 0.375")
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Disease prevalence = 2%. Test sensitivity = 99%, specificity = 95%. 
(a) If positive, find P(disease). (b) If negative, find P(disease-free). (c) Why is a positive result not very alarming?

**Solution:**
    """)
    p_d = 0.02; p_pos_d = 0.99; p_pos_no_d = 0.05
    p_no_d = 1 - p_d
    p_pos = p_pos_d*p_d + p_pos_no_d*p_no_d
    ppv = (p_pos_d * p_d) / p_pos
    p_neg = 1 - p_pos
    p_neg_d = 1 - p_pos_d
    p_neg_no_d = 1 - p_pos_no_d
    npv = (p_neg_no_d * p_no_d) / p_neg
    st.latex(r"P(D|+) = \frac{0.99\times0.02}{0.99\times0.02+0.05\times0.98} = \frac{0.0198}{0.0198+0.049} = \frac{0.0198}{0.0688} \approx 0.288")
    st.latex(r"P(\bar{D}|-) = \frac{0.96\times0.98}{0.96\times0.98+0.01\times0.02} \approx 0.9998")
    st.markdown(f"""
(a) **PPV (Positive Predictive Value) ≈ 28.8%** — only about 1 in 3.5 positives actually has the disease!

(b) **NPV (Negative Predictive Value) ≈ 99.98%** — a negative test very reliably rules out disease.

(c) **Why not alarming?** Because disease prevalence is only 2% (rare). Even with a very accurate test, the *false positive pool* (healthy people × 5% false positive rate = 49 per 1000) overwhelms the *true positive pool* (sick people × 99% = 19.8 per 1000). This is the **base rate neglect** phenomenon.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** If prior P(A) = 0.5, does Bayes' theorem always give P(A|B) = 0.5?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**No.** P(A|B) = 0.5 only if B gives no information about A, which happens when P(B|A) = P(B|Aᶜ).

If P(A) = 0.5 and P(B|A) ≠ P(B|Aᶜ), then Bayes' theorem will shift the posterior away from 0.5.

**Example:** P(A) = 0.5, P(B|A) = 0.9, P(B|Aᶜ) = 0.1

P(B) = 0.9(0.5) + 0.1(0.5) = 0.5

P(A|B) = 0.9×0.5/0.5 = **0.9** — very different from 0.5!

Starting with 50/50 uncertainty, a strong likelihood ratio (9:1) updates the posterior to 90%.
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Two children problem — A family has 2 children. You learn at least one is a boy. P(both boys)?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**Using conditional probability (Bayes):**

Sample space: {BB, BG, GB, GG} — 4 equally likely outcomes.

Event A = "both boys" = {BB}; Event B = "at least one boy" = {BB, BG, GB}

P(A|B) = P(A∩B)/P(B) = P({BB}) / P({BB,BG,GB}) = (1/4)/(3/4) = **1/3**

⚠️ **Counterintuitive!** Many people say 1/2 (thinking: one is a boy, so the other is 50/50). But the problem says "at least one" which restricts us to a 3-outcome reduced space, not a 2-outcome one.

**If instead you're told "the OLDER child is a boy":** Now space = {BB, BG} → P(both boys) = **1/2**. The specific information matters enormously.
        """)
    st.markdown("</div>", unsafe_allow_html=True)
