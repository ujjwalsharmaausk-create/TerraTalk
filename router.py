import re


def route_question(question: str) -> dict:
    q = question.lower().strip()

    if any(word in q for word in ["flood", "flooded", "water spread", "inundation"]):

        if "assam" in q or "barpeta" in q:
            return {"tool": "flood", "region": "Assam"}

        if "bihar" in q or "darbhanga" in q:
            return {"tool": "flood", "region": "Bihar"}

    if any(word in q for word in ["crop", "stress", "ndvi", "drying", "dry"]):

        if "maharashtra" in q or "latur" in q:
            return {"tool": "crop", "region": "Maharashtra"}

    return {"tool": "cannot_answer", "region": None}


def extract_region(question: str):
    return route_question(question)["region"]


if __name__ == "__main__":

    tests = [
        "How much area is flooded in Barpeta?",
        "Which fields in Latur show crop stress?",
        "Tell me the flood area in Bihar.",
        "What is the weather in Delhi?"
    ]

    for q in tests:
        print(q, "=>", route_question(q))