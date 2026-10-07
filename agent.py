from router import route_question
from tools import flood_assam, flood_bihar, crop_maharashtra


def answer_question(question: str) -> dict:
    route = route_question(question)

    if route["tool"] == "flood" and route["region"] == "Assam":

        data = flood_assam()
        m = data["metrics"]

        answer = (
            f"Cached analysis for {data['district']}, Assam: "
            f"about {m['flooded_area_km2']} km² is flagged as flooded."
        )

    elif route["tool"] == "flood" and route["region"] == "Bihar":

        data = flood_bihar()
        m = data["metrics"]

        answer = (
            f"Cached analysis for {data['district']}, Bihar: "
            f"about {m['flooded_area_km2']} km² is flagged as flooded."
        )

    elif route["tool"] == "crop" and route["region"] == "Maharashtra":

        data = crop_maharashtra()
        m = data["metrics"]

        answer = (
            f"Cached analysis for {data['district']}, Maharashtra: "
            f"NDVI fell from {m['previous_ndvi']} to "
            f"{m['current_ndvi']}, classified as "
            f"{m['stress']} crop stress."
        )

    else:

        return {
            "answer": (
                "I cannot answer that with the TerraTalk demo data. "
                "Ask about flood in Assam/Barpeta, flood in Bihar/Darbhanga, "
                "or crop stress in Maharashtra/Latur."
            ),
            "data": None
        }

    return {
        "answer": answer,
        "data": data
    }


if __name__ == "__main__":

    for q in [
        "How much area is flooded in Barpeta?",
        "Which fields in Latur show crop stress?"
    ]:
        print(answer_question(q))