from PIL import Image, ImageDraw
from pathlib import Path

maps = Path("maps")
maps.mkdir(exist_ok=True)

items = [
    ("flood_assam.png", "ASSAM FLOOD DEMO MAP", "Barpeta, Assam"),
    ("flood_bihar.png", "BIHAR FLOOD DEMO MAP", "Darbhanga, Bihar"),
    ("crop_maharashtra.png", "MAHARASHTRA CROP-STRESS DEMO MAP", "Latur, Maharashtra"),
]

for filename, title, place in items:
    image = Image.new("RGB", (1200, 700), "white")
    draw = ImageDraw.Draw(image)

    draw.text((100, 150), "TerraTalk", fill="black")
    draw.text((100, 250), title, fill="black")
    draw.text((100, 330), place, fill="black")
    draw.text((100, 430), "UI PLACEHOLDER", fill="black")
    draw.text(
        (100, 500),
        "Replace with verified Google Earth Engine export before final submission.",
        fill="black"
    )

    image.save(maps / filename)

print("Three map images created successfully.")