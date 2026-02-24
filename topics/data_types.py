import streamlit as st

def render():
    st.markdown("""
    <div class='topic-header'>
        <h1>📦 Data Types & Variables</h1>
        <p>Understanding the building blocks of statistical analysis: types of data and variables.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── INTRODUCTION ──────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-intro'>📖 Introduction</div>", unsafe_allow_html=True)
    st.markdown("""
Data is the raw material of statistics. Before performing any analysis, it is essential to understand **what kind of data** you are working with — because the type of data determines which statistical techniques are appropriate.

Data can be broadly divided into:
- **Qualitative (Categorical)** — describes categories or groups
- **Quantitative (Numerical)** — represents measurable quantities
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── CONCEPTS ─────────────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-concept'>💡 Key Concepts</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("#### 🔷 Qualitative Data")
        st.markdown("""
**Nominal** — categories with *no natural order*
- Examples: Gender, Color, Religion, Blood type

**Ordinal** — categories with a *natural order*
- Examples: Education level (High/Medium/Low), Rating (1–5 stars), Satisfaction (Poor/Fair/Good/Excellent)
        """)
    with col2:
        st.markdown("#### 🔶 Quantitative Data")
        st.markdown("""
**Discrete** — countable, whole numbers
- Examples: Number of students, number of cars

**Continuous** — measurable, can take any value in a range
- Examples: Height, Weight, Temperature, Time
        """)

    st.markdown("---")
    st.markdown("#### 📐 Types of Variables")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("**Independent Variable**\nThe variable that is manipulated or controlled. Also called *predictor* or *explanatory* variable.\n\n*Example: Hours of study*")
    with col2:
        st.info("**Dependent Variable**\nThe variable being measured/observed. It depends on the independent variable.\n\n*Example: Exam score*")
    with col3:
        st.info("**Confounding Variable**\nA hidden variable that influences both independent and dependent variables, potentially causing a spurious association.\n\n*Example: Student's IQ*")

    st.markdown("---")
    st.markdown("#### 📏 Scales of Measurement (NOIR)")
    st.markdown("""
| Scale | Order | Equal Intervals | True Zero | Example |
|-------|-------|-----------------|-----------|---------|
| **Nominal** | ❌ | ❌ | ❌ | Blood type, Gender |
| **Ordinal** | ✅ | ❌ | ❌ | Ranking, Rating |
| **Interval** | ✅ | ✅ | ❌ | Temperature (°C), IQ |
| **Ratio** | ✅ | ✅ | ✅ | Height, Weight, Income |
    """)

    st.markdown("#### 🧮 Notation")
    st.latex(r"""
    \text{Population size} = N \qquad \text{Sample size} = n
    """)
    st.latex(r"""
    X = \text{Random Variable}, \quad x_i = i\text{-th observation}, \quad i = 1, 2, \ldots, n
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── SOLVED PROBLEMS ───────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-solved'>✅ Solved Problems</div>", unsafe_allow_html=True)

    st.markdown("<span class='prob-badge'>Problem 1 — Basic</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** Classify each of the following as Nominal, Ordinal, Interval, or Ratio:
(a) ZIP codes  (b) Movie ratings (1–5 stars)  (c) Body temperature in °F  (d) Number of siblings

**Solution:**
- (a) ZIP codes → **Nominal** (numeric labels, no meaningful order or arithmetic)
- (b) Movie ratings → **Ordinal** (ordered, but gaps between ratings aren't equal)
- (c) Body temperature °F → **Interval** (ordered, equal gaps, but 0°F doesn't mean "no temperature")
- (d) Number of siblings → **Ratio** (ordered, equal gaps, true zero = no siblings)
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 2 — Intermediate</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A researcher studies whether a new drug reduces blood pressure. Identify the independent, dependent, and a possible confounding variable.

**Solution:**
- **Independent variable**: Whether the patient takes the drug (Yes/No) — the manipulated factor
- **Dependent variable**: Blood pressure reading (mmHg) — what is being measured
- **Confounding variable**: Patient's age, diet, or exercise habits — these also affect blood pressure and are not controlled in the study
    """)
    st.divider()

    st.markdown("<span class='prob-badge'>Problem 3 — Advanced</span>", unsafe_allow_html=True)
    st.markdown("""
**Q:** A dataset contains: annual income (₹), satisfaction rating (1=low, 5=high), city name, and number of children. 
(a) Classify each variable. (b) Which statistical operations are valid for each?

**Solution:**

| Variable | Type | Scale | Valid Operations |
|----------|------|-------|-----------------|
| Annual income | Quantitative – Continuous | Ratio | Mean, SD, ratios (₹60L is double ₹30L) |
| Satisfaction rating | Qualitative – Ordinal | Ordinal | Median, mode, rank comparisons |
| City name | Qualitative – Nominal | Nominal | Mode, frequency count only |
| Number of children | Quantitative – Discrete | Ratio | Mean, SD, ratios (4 children = 2× of 2) |

Key insight: **Never compute a mean for ordinal or nominal data** — the result is mathematically meaningless.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ── TRICKY QUESTIONS ─────────────────────────────────────────────────────
    st.markdown("<div class='section-card'><div class='section-label label-tricky'>🧠 Tricky Questions</div>", unsafe_allow_html=True)

    st.markdown("<span class='tricky-badge'>Tricky Q1</span>", unsafe_allow_html=True)
    st.markdown("**Q:** Temperature measured in Kelvin (K) — is it Interval or Ratio scale? What about Celsius?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**Kelvin → Ratio scale** ✅
- 0 K = absolute zero = complete absence of thermal energy → *true zero exists*
- Therefore 200 K is literally twice as hot as 100 K

**Celsius → Interval scale** ✅
- 0°C is arbitrary (freezing point of water), not absence of temperature
- 20°C is NOT twice as hot as 10°C

**Takeaway:** The same physical quantity can be on different measurement scales depending on the unit used!
        """)

    st.markdown("<span class='tricky-badge'>Tricky Q2</span>", unsafe_allow_html=True)
    st.markdown("**Q:** A student argues: \"Ordinal data is just discrete quantitative data with limited values.\" Is this correct?")
    with st.expander("🔍 Reveal Solution"):
        st.markdown("""
**No — this is a common misconception.**

Ordinal data has *order* but **not equal intervals**. The gap between satisfaction ratings 1→2 and 4→5 is not necessarily the same psychological distance, even though numerically both differ by 1.

Discrete quantitative data has *equal intervals*: the difference between 3 and 4 apples is exactly the same as between 7 and 8 apples.

**Practical consequence:** You can compute mean for discrete quantitative data. Computing mean for ordinal data (e.g., average of satisfaction ratings) is technically invalid, though commonly done in practice.
        """)
    st.markdown("</div>", unsafe_allow_html=True)
