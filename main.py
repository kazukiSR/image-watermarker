from PIL import Image, ImageDraw, ImageFont

# TODO TKInter GUI
# TODO Freedom on watermarking orientation, opacity, and word size
# TODO open file with a choose file, output file to directory of choice.
# TODO identify all fonts installed on windows default and show a dropdown list to choose font
# TODO finalize as .exe


image1 = Image.open('funky.jpg').convert("RGBA")

image1.save('funky.png')

# output img
image2 = Image.new("RGBA", image1.size, (255, 255, 255, 0))

# font
fnt = ImageFont.truetype("C:/Windows/Fonts/Arial.ttf", 200)

# drawer
draw = ImageDraw.Draw(image2)

# draw text, half opacity
draw.text((10, 10), "TEST", font=fnt, fill=(255, 255, 255, 64))


out = Image.alpha_composite(image1, image2)

out.show()