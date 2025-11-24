import os
from PIL import Image
import random

# Уникальные палитры для каждого стиля (1–10)
STYLES = {
    1: {"name": "Grassy Plains", "colors": [(114, 172, 71), (134, 96, 67), (150, 180, 90)]},
    2: {"name": "Desert", "colors": [(217, 204, 161), (194, 178, 128), (170, 150, 100)]},
    3: {"name": "Stone Caves", "colors": [(128, 128, 128), (100, 100, 100), (80, 80, 90)]},
    4: {"name": "Forest", "colors": [(34, 100, 34), (50, 80, 50), (70, 120, 70), (157, 128, 74)]},
    5: {"name": "Ocean", "colors": [(64, 64, 191), (40, 40, 160), (80, 80, 200), (20, 100, 150)]},
    6: {"name": "Nether", "colors": [(200, 30, 30), (150, 20, 20), (100, 10, 10), (220, 150, 50)]},
    7: {"name": "Snowy Tundra", "colors": [(240, 240, 255), (220, 220, 240), (200, 200, 220), (134, 96, 67)]},
    8: {"name": "Jungle", "colors": [(20, 100, 20), (30, 80, 30), (40, 120, 40), (157, 128, 74)]},
    9: {"name": "Mushroom Island", "colors": [(150, 50, 150), (180, 100, 180), (120, 30, 120), (200, 200, 200)]},
    10: {"name": "End", "colors": [(40, 10, 60), (20, 5, 30), (80, 40, 100), (100, 100, 120)]},
}

# Параметры генерации
GRID_SIZE = 32
PIXEL_SCALE = 8

def generate_minecraft_image(style_id):
    if style_id not in STYLES:
        print("Неверный номер стиля!")
        return

    style = STYLES[style_id]
    colors = style["colors"]
    folder = f"style{style_id}"
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, "outlike.png")

    img_width = GRID_SIZE * PIXEL_SCALE
    img_height = GRID_SIZE * PIXEL_SCALE
    image = Image.new("RGB", (img_width, img_height))
    pixels = image.load()

    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = random.choice(colors)
            for dy in range(PIXEL_SCALE):
                for dx in range(PIXEL_SCALE):
                    px = x * PIXEL_SCALE + dx
                    py = y * PIXEL_SCALE + dy
                    pixels[px, py] = color

    image.save(filepath)
    print(f"✅ Стиль '{style['name']}' сохранён как {filepath}")

# Основная программа
if __name__ == "__main__":
    print("Выберите стиль (1–10):")
    for i in range(1, 11):
        print(f"{i}: {STYLES[i]['name']}")
    
    try:
        choice = int(input("\nВведите число от 1 до 10: "))
        if 1 <= choice <= 10:
            generate_minecraft_image(choice)
        else:
            print("Число должно быть от 1 до 10!")
    except ValueError:
        print("Пожалуйста, введите целое число!")