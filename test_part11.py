from agent import answer_question
from pathlib import Path


tests = [
    ("How much area is flooded in Barpeta?", "flood", "Assam"),
    ("Is Barpeta flooded?", "flood", "Assam"),
    ("Tell me the flood area in Assam.", "flood", "Assam"),
    ("Flood in Bihar", "flood", "Bihar"),
    ("How much water spread is in Darbhanga?", "flood", "Bihar"),
    ("What is the Bihar flood area?", "flood", "Bihar"),
    ("Which fields in Latur show crop stress?", "crop", "Maharashtra"),
    ("Is Latur crop stress severe?", "crop", "Maharashtra"),
    ("What is NDVI in Latur?", "crop", "Maharashtra"),
    ("Which crop is stressed in Maharashtra?", "crop", "Maharashtra"),
    ("Flood in Maharashtra", "cannot_answer", None),
    ("Flood in Delhi", "cannot_answer", None),
    ("Crop stress in Bihar", "cannot_answer", None),
    ("Weather in Delhi", "cannot_answer", None),
    ("Earthquake in Assam", "cannot_answer", None),
    ("Hello", "cannot_answer", None),
    ("Give me live flood data", "cannot_answer", None),
    ("What is U-Net?", "cannot_answer", None),
    ("Show WhatsApp alerts", "cannot_answer", None),
    ("Can you analyze Latur crop stress?", "crop", "Maharashtra"),
]


print("\nTerraTalk Part 11 Testing")
print("=" * 60)

passed = 0

for number, (question, expected_tool, expected_region) in enumerate(tests, 1):

    result = answer_question(question)
    data = result["data"]

    if expected_tool == "cannot_answer":

        success = data is None

    else:

        success = (
            data is not None
            and (
                "flood" if data["analysis_type"] == "flood"
                else "crop"
            ) == expected_tool
            and data["region"] == expected_region
        )

    if success:
        print(f"PASS {number:02d}: {question}")
        passed += 1
    else:
        print(f"FAIL {number:02d}: {question}")
        print("       Expected:", expected_tool, expected_region)
        print("       Got:", data)


print("=" * 60)
print(f"Result: {passed}/{len(tests)} tests passed.")

maps = [
    "maps/flood_assam.png",
    "maps/flood_bihar.png",
    "maps/crop_maharashtra.png",
]

print("\nMap file check:")

for map_file in maps:
    if Path(map_file).exists():
        print(f"PASS: {map_file}")
    else:
        print(f"FAIL: {map_file}")

print("\nTesting complete.")