# Digz icon generator — Appz optical-size matched wordmark
from PIL import Image, ImageDraw, ImageFont

S = 1024
WHITE = "#ffffff"
BLACK = "#000000"
FONT = "Anton.ttf"
WORDMARK_SIZE = 265
WORDMARK_TOP = 436


def draw_shovel(draw, cx, cy):
    draw.rounded_rectangle([cx-70, cy-125, cx+70, cy-95], radius=15, fill=WHITE)
    draw.rounded_rectangle([cx-14, cy-125, cx+14, cy+15], radius=10, fill=WHITE)
    draw.polygon([
        (cx-75, cy+15),
        (cx+75, cy+15),
        (cx+75, cy+75),
        (cx, cy+130),
        (cx-75, cy+75),
    ], fill=WHITE)


def draw_wordmark(draw):
    text = "Digz"
    font = ImageFont.truetype(FONT, WORDMARK_SIZE)
    gap = 0
    widths = []
    for char in text:
        box = draw.textbbox((0, 0), char, font=font)
        widths.append(box[2] - box[0])
    total = sum(widths) + gap * (len(text) - 1)
    x = (S - total) / 2
    for char, width in zip(text, widths):
        draw.text((x, WORDMARK_TOP), char, font=font, fill=WHITE)
        x += width + gap


def make_icon():
    image = Image.new("RGB", (S, S), BLACK)
    draw = ImageDraw.Draw(image)
    draw.rectangle([132, 168, S-132, 180], fill=WHITE)
    draw.rectangle([132, 844, S-132, 856], fill=WHITE)
    draw_shovel(draw, S/2, 330)
    draw_wordmark(draw)
    return image


if __name__ == "__main__":
    icon = make_icon()
    icon.resize((512, 512), Image.Resampling.LANCZOS).save("icon-512.png")
    icon.resize((180, 180), Image.Resampling.LANCZOS).save("icon-180.png")
    print("Digz icons generated")
