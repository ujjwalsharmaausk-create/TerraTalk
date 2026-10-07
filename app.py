import streamlit as st
from pathlib import Path

from agent import answer_question


st.set_page_config(
    page_title="TerraTalk",
    page_icon="🌍",
    layout="wide"
)


st.title("🌍 TerraTalk")

st.caption(
    "Ask your land, get answers — cached satellite-data prototype"
)


st.info(
    "Demo scope: flood in Assam/Bihar and crop stress in Maharashtra. "
    "Results are cached/precomputed for fast demonstration."
)


question = st.text_input(
    "Ask a question",
    placeholder="How much area is flooded in Barpeta?"
)


if st.button("Analyze"):

    if not question.strip():
        st.warning("Type a question first.")
        st.stop()

    result = answer_question(question)

    st.subheader("Answer")
    st.write(result["answer"])

    data = result["data"]

    if data:

        m = data["metrics"]

        st.subheader("Key metrics")

        if data["analysis_type"] == "flood":

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "Flooded area",
                f"{m['flooded_area_km2']} km²"
            )

            c2.metric(
                "Confidence",
                f"{m['confidence'] * 100:.0f}%"
            )

            c3.metric(
                "Region",
                data["region"]
            )

        else:

            c1, c2, c3 = st.columns(3)

            c1.metric(
                "NDVI drop",
                m["ndvi_drop"]
            )

            c2.metric(
                "Stress",
                m["stress"].title()
            )

            c3.metric(
                "Confidence",
                f"{m['confidence'] * 100:.0f}%"
            )

        st.subheader("Map / analysis image")

        map_path = Path(__file__).resolve().parent / data["map"]

        if map_path.exists():
            st.image(
                str(map_path),
                width="stretch"
            )
        else:
            st.warning(
                f"Map image not found: {data['map']}"
            )

        st.subheader("How computed")
        st.write(data["method"])

        st.caption(
            "Advisory result — verify on the ground before making "
            "operational decisions."
        )


with st.expander("Try these demo questions"):

    st.write("• How much area is flooded in Barpeta?")
    st.write("• Tell me the flood area in Bihar.")
    st.write("• Which fields in Latur show crop stress?")
    st.write("• What is the weather in Delhi?")