
import streamlit as st
from pathlib import Path

from agent import answer_question


st.set_page_config(
    page_title="TerraTalk | Geospatial Intelligence",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)


st.markdown(
    """
    <style>
    :root {
        --bg: #061322;
        --panel: #0b1c2e;
        --border: #203b52;
        --text: #edf6ff;
        --muted: #9bb0c5;
        --teal: #43ded1;
    }

    header[data-testid="stHeader"],
    [data-testid="stHeader"],
    [data-testid="stToolbar"],
    [data-testid="stAppDeployButton"],
    [data-testid="stMainMenu"],
    .stAppDeployButton,
    .stDeployButton {
        display: none !important;
        height: 0 !important;
        visibility: hidden !important;
    }

    footer,
    #MainMenu {
        visibility: hidden !important;
    }

    [data-testid="stDecoration"] {
        display: none !important;
    }

    .stApp {
        background:
            radial-gradient(
                circle at 12% 0%,
                rgba(29, 151, 165, 0.17),
                transparent 34%
            ),
            radial-gradient(
                circle at 95% 10%,
                rgba(43, 93, 190, 0.13),
                transparent 30%
            ),
            var(--bg);
        color: var(--text);
    }

    [data-testid="stAppViewContainer"] > .main {
        background: transparent;
    }

    .block-container {
        max-width: 1480px;
        padding-top: 1.1rem;
        padding-bottom: 3rem;
    }

    [data-testid="stMarkdownContainer"] p {
        color: #c3d1df;
    }

    h1, h2, h3 {
        color: var(--text) !important;
    }

    .tt-topbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 16px;
        padding: 8px 2px 24px;
        border-bottom: 1px solid rgba(132, 169, 199, 0.17);
        margin-bottom: 26px;
    }

    .tt-brand {
        display: flex;
        align-items: center;
        gap: 13px;
    }

    .tt-logo {
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 15px;
        background: linear-gradient(135deg, #143d51, #10263b);
        border: 1px solid #2c6875;
        font-size: 27px;
    }

    .tt-brandname {
        color: #f2f8ff;
        font-size: 25px;
        font-weight: 850;
        letter-spacing: -0.8px;
        line-height: 1.15;
    }

    .tt-brandline {
        color: #91aabe;
        font-size: 10px;
        letter-spacing: 2px;
        margin-top: 5px;
    }

    .tt-mode {
        border: 1px solid #315263;
        color: #b5d9df;
        background: rgba(35, 91, 102, 0.18);
        padding: 9px 13px;
        border-radius: 99px;
        font-size: 10px;
        font-weight: 750;
        letter-spacing: 1px;
    }

    .tt-hero {
        padding: 32px 34px;
        border-radius: 23px;
        border: 1px solid #23455b;
        background: linear-gradient(
            115deg,
            rgba(15, 47, 67, 0.98),
            rgba(10, 30, 50, 0.98) 58%,
            rgba(12, 37, 57, 0.95)
        );
        margin-bottom: 25px;
    }

    .tt-eyebrow {
        color: var(--teal);
        font-size: 10px;
        font-weight: 850;
        letter-spacing: 2.2px;
        margin-bottom: 12px;
    }

    .tt-hero-title {
        color: #f3f8ff;
        font-size: clamp(30px, 4vw, 47px);
        font-weight: 850;
        line-height: 1.13;
        letter-spacing: -1.8px;
        max-width: 850px;
    }

    .tt-hero-title span {
        color: var(--teal);
    }

    .tt-hero-copy {
        color: #b0c4d6;
        font-size: 15px;
        line-height: 1.8;
        max-width: 710px;
        margin-top: 14px;
    }

    .tt-pills {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 22px;
    }

    .tt-pill {
        font-size: 11px;
        color: #c5e7ed;
        background: rgba(49, 112, 126, 0.19);
        border: 1px solid rgba(83, 171, 183, 0.28);
        border-radius: 99px;
        padding: 7px 11px;
    }

    .tt-section-label {
        color: var(--teal);
        font-size: 10px;
        font-weight: 850;
        letter-spacing: 2px;
        margin-bottom: 7px;
    }

    .tt-panel-title {
        color: #f0f6ff;
        font-size: 23px;
        font-weight: 780;
        line-height: 1.3;
        letter-spacing: -0.5px;
    }

    .tt-panel-copy {
        color: var(--muted);
        font-size: 13px;
        line-height: 1.7;
        margin-top: 7px;
        margin-bottom: 17px;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(11, 28, 46, 0.88);
        border: 1px solid var(--border);
        border-radius: 19px;
    }

    div[data-testid="stTextInput"] label {
        color: #dce9f5;
        font-size: 12px;
        font-weight: 700;
    }

    div[data-testid="stTextInput"] input {
        color: #f3f8ff;
        background: #071729;
        border: 1px solid #29465e;
        border-radius: 11px;
        min-height: 48px;
    }

    div[data-testid="stTextInput"] input:focus {
        border-color: var(--teal);
        box-shadow: 0 0 0 1px rgba(67, 222, 209, 0.2);
    }

    div[data-testid="stFormSubmitButton"] button {
        color: #06202a;
        background: var(--teal);
        border: 1px solid var(--teal);
        border-radius: 11px;
        min-height: 46px;
        font-weight: 850;
        transition: all 0.15s ease;
    }

    div[data-testid="stFormSubmitButton"] button:hover {
        color: #041720;
        background: #8bf5eb;
        border-color: #8bf5eb;
    }

    div[data-testid="stButton"] button {
        border-radius: 11px;
        min-height: 42px;
        font-size: 12px;
        font-weight: 650;
        transition: all 0.15s ease;
    }

    div[data-testid="stButton"] button[kind="secondary"] {
        color: #d8e7f5;
        background: #0d2135;
        border: 1px solid #29455d;
    }

    div[data-testid="stButton"] button[kind="secondary"]:hover {
        color: var(--teal);
        border-color: #4b9d9e;
        background: #122c41;
    }

    [data-testid="stMetric"] {
        background: linear-gradient(140deg, #10283c, #0b1c2e);
        border: 1px solid #29465e;
        border-radius: 15px;
        padding: 17px 19px;
    }

    [data-testid="stMetricLabel"] {
        color: #a6bdce !important;
        font-size: 12px;
    }

    [data-testid="stMetricValue"] {
        color: #f3f8ff !important;
        font-size: 25px;
        font-weight: 800;
    }

    [data-testid="stImage"] img {
        border: 1px solid #29465e;
        border-radius: 15px;
    }

    [data-testid="stExpander"] {
        background: rgba(11, 28, 46, 0.7);
        border: 1px solid #29445b;
        border-radius: 13px;
    }

    [data-testid="stAlert"] {
        border-radius: 12px;
    }

    hr {
        border-color: rgba(132, 169, 199, 0.18);
    }

    .tt-feature {
        padding: 15px 0;
        border-bottom: 1px solid rgba(132, 169, 199, 0.16);
    }

    .tt-feature:last-child {
        border-bottom: 0;
    }

    .tt-feature-top {
        display: flex;
        gap: 10px;
        align-items: center;
    }

    .tt-feature-icon {
        width: 36px;
        height: 36px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 11px;
        background: #15374a;
        border: 1px solid #2a5a6b;
        font-size: 18px;
    }

    .tt-feature-title {
        color: #eaf4ff;
        font-size: 14px;
        font-weight: 760;
    }

    .tt-feature-copy {
        color: #9fb4c7;
        font-size: 12px;
        line-height: 1.7;
        margin-top: 9px;
    }

    .tt-feature-tag {
        color: #69dacf;
        font-size: 9px;
        letter-spacing: 1.3px;
        font-weight: 800;
        margin-top: 10px;
    }

    .tt-footer {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 8px;
        color: #7892a8;
        font-size: 10px;
        letter-spacing: 0.5px;
        padding: 22px 2px 0;
        border-top: 1px solid rgba(132, 169, 199, 0.15);
        margin-top: 35px;
    }

    @media (max-width: 700px) {
        .block-container {
            padding: 1rem 1rem 2rem;
        }

        .tt-hero {
            padding: 23px 20px;
        }

        .tt-mode {
            font-size: 9px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)


DEMO_QUESTIONS = [
    "How much area is flooded in Barpeta?",
    "Tell me the flood area in Bihar.",
    "Which fields in Latur show crop stress?",
    "What is NDVI in Latur?",
]


def select_prompt(prompt):
    st.session_state["question_input"] = prompt
    st.session_state.pop("analysis_result", None)
    st.session_state.pop("analysis_question", None)


st.markdown(
    """
    <div class="tt-topbar">
        <div class="tt-brand">
            <div class="tt-logo">🌍</div>
            <div>
                <div class="tt-brandname">TerraTalk</div>
                <div class="tt-brandline">
                    GEOSPATIAL INTELLIGENCE, IN CONVERSATION
                </div>
            </div>
        </div>
        <div class="tt-mode">
            ● DEMO MODE · PRECOMPUTED RESULTS
        </div>
    </div>

    <div class="tt-hero">
        <div class="tt-eyebrow">
            LAND INTELLIGENCE, MADE CONVERSATIONAL
        </div>
        <div class="tt-hero-title">
            See what's happening on your land<span>.</span>
        </div>
        <div class="tt-hero-copy">
            Ask questions about flood extent and crop stress.
            TerraTalk turns supported geospatial demo data into
            clear answers, useful metrics, and visual evidence.
        </div>
        <div class="tt-pills">
            <span class="tt-pill">🌊 Flood intelligence</span>
            <span class="tt-pill">🌱 Crop stress</span>
            <span class="tt-pill">🗺️ Geospatial insights</span>
            <span class="tt-pill">⚡ Fast demo results</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


query_col, feature_col = st.columns([1.55, 0.85], gap="large")


with query_col:
    with st.container(border=True):
        st.markdown(
            """
            <div class="tt-section-label">01 / ASK TERRATALK</div>
            <div class="tt-panel-title">
                What would you like to understand?
            </div>
            <div class="tt-panel-copy">
                Ask naturally. Start with a supported location or
                choose one of the example questions below.
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.form("analysis_form", clear_on_submit=False):
            question = st.text_input(
                "Your question",
                key="question_input",
                placeholder="e.g. How much area is flooded in Barpeta?",
            )

            submitted = st.form_submit_button(
                "Analyze area  →",
                use_container_width=True,
                type="primary",
            )

        st.markdown(
            """
            <div class="tt-section-label" style="margin-top:24px;">
                TRY A DEMO QUESTION
            </div>
            """,
            unsafe_allow_html=True,
        )

        prompt_col1, prompt_col2 = st.columns(2, gap="small")

        with prompt_col1:
            st.button(
                "🌊  Flood in Barpeta",
                key="prompt_barpeta",
                use_container_width=True,
                type="secondary",
                on_click=select_prompt,
                args=(DEMO_QUESTIONS[0],),
            )

            st.button(
                "🌱  Crop stress in Latur",
                key="prompt_latur",
                use_container_width=True,
                type="secondary",
                on_click=select_prompt,
                args=(DEMO_QUESTIONS[2],),
            )

        with prompt_col2:
            st.button(
                "🗺️  Flood area in Bihar",
                key="prompt_bihar",
                use_container_width=True,
                type="secondary",
                on_click=select_prompt,
                args=(DEMO_QUESTIONS[1],),
            )

            st.button(
                "📈  NDVI in Latur",
                key="prompt_ndvi",
                use_container_width=True,
                type="secondary",
                on_click=select_prompt,
                args=(DEMO_QUESTIONS[3],),
            )


with feature_col:
    with st.container(border=True):
        st.markdown(
            """
            <div class="tt-section-label">02 / EXPLORE</div>
            <div class="tt-panel-title">
                Geospatial insights
            </div>

            <div class="tt-feature">
                <div class="tt-feature-top">
                    <div class="tt-feature-icon">🌊</div>
                    <div class="tt-feature-title">
                        Flood intelligence
                    </div>
                </div>
                <div class="tt-feature-copy">
                    Explore cached flood-area estimates and
                    supporting visualizations for the demo regions.
                </div>
                <div class="tt-feature-tag">ASSAM · BIHAR</div>
            </div>

            <div class="tt-feature">
                <div class="tt-feature-top">
                    <div class="tt-feature-icon">🌿</div>
                    <div class="tt-feature-title">
                        Crop stress
                    </div>
                </div>
                <div class="tt-feature-copy">
                    Review NDVI-related indicators and crop-stress
                    summaries from the existing demo data.
                </div>
                <div class="tt-feature-tag">MAHARASHTRA</div>
            </div>

            <div class="tt-feature">
                <div class="tt-feature-top">
                    <div class="tt-feature-icon">🧭</div>
                    <div class="tt-feature-title">
                        Natural-language questions
                    </div>
                </div>
                <div class="tt-feature-copy">
                    Ask a supported question in plain language and
                    receive the corresponding cached response.
                </div>
                <div class="tt-feature-tag">
                    CONVERSATIONAL INTERFACE
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.caption(
            "Prototype scope: this screen uses existing cached/"
            "precomputed results, not a live satellite-processing job."
        )


if submitted:
    if not question.strip():
        st.warning("Please type a question or choose a demo question.")
    else:
        with st.spinner("Preparing your geospatial result..."):
            result = answer_question(question.strip())

        st.session_state["analysis_result"] = result
        st.session_state["analysis_question"] = question.strip()


result = st.session_state.get("analysis_result")


if result is not None:
    st.markdown("---")

    st.markdown(
        """
        <div class="tt-section-label">03 / ANALYSIS REPORT</div>
        <div class="tt-panel-title">
            Your TerraTalk result
        </div>
        <div class="tt-panel-copy">
            Review the response, supporting metrics, and available
            visualization for this demo question.
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.container(border=True):
        st.markdown(
            '<div class="tt-section-label">QUESTION</div>',
            unsafe_allow_html=True,
        )

        st.write(st.session_state.get("analysis_question", ""))

        st.markdown(
            '<div class="tt-section-label" style="margin-top:20px;">'
            'TERRATALK RESPONSE</div>',
            unsafe_allow_html=True,
        )

        st.write(result.get("answer", "No answer was returned."))

        data = result.get("data")

        if data:
            metrics = data["metrics"]

            st.markdown(
                """
                <div class="tt-section-label" style="margin-top:26px;">
                    KEY INDICATORS
                </div>
                """,
                unsafe_allow_html=True,
            )

            if data["analysis_type"] == "flood":
                col1, col2, col3 = st.columns(3)

                col1.metric(
                    "Flooded area",
                    f"{metrics['flooded_area_km2']} km²",
                )

                col2.metric(
                    "Confidence",
                    f"{metrics['confidence'] * 100:.0f}%",
                )

                col3.metric("Region", data["region"])

            else:
                col1, col2, col3 = st.columns(3)

                col1.metric("NDVI drop", metrics["ndvi_drop"])
                col2.metric("Stress level", metrics["stress"].title())

                col3.metric(
                    "Confidence",
                    f"{metrics['confidence'] * 100:.0f}%",
                )

            st.markdown(
                """
                <div class="tt-section-label" style="margin-top:26px;">
                    MAP / ANALYSIS IMAGE
                </div>
                """,
                unsafe_allow_html=True,
            )

            map_path = Path(__file__).resolve().parent / data["map"]

            if map_path.exists():
                st.image(str(map_path), width="stretch")
            else:
                st.warning(f"Map image not found: {data['map']}")

            with st.expander("How this result was computed"):
                st.write(data["method"])

            st.info(
                "Advisory result based on the existing demo data. "
                "Verify results with ground observations and qualified "
                "experts before making operational decisions."
            )

        else:
            st.caption(
                "This response does not include structured metrics "
                "or a map in the current demo."
            )


st.markdown(
    """
    <div class="tt-footer">
        <span>🌍 TERRATALK · GEOSPATIAL INTELLIGENCE</span>
        <span>
            PROTOTYPE · CACHED/PRECOMPUTED RESULTS · NOT FOR
            EMERGENCY DECISION-MAKING
        </span>
    </div>
    """,
    unsafe_allow_html=True,
)