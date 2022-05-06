from PIL import Image, ImageDraw, ImageFont
import math


class WaterMarker:

    def __init__(self, img_file, text, font_path, opacity, font_ratio=1.75, diagonal_percentage=0.8):
        self.font_ratio = font_ratio  # Size ratio of font
        self.diagonal_percentage = diagonal_percentage  # Percentage of the diagonal line length
        self.text = text
        self.text_len = len(self.text)
        self.font_path = font_path
        self.opacity = int(256 * (opacity * 0.01))  # Passed opacity is 0-100, representing opacity percentage
        # Base image to be used
        self.baseImg = Image.open(img_file).convert('RGBA')
        # Img dimensions
        self.width, self.height = self.baseImg.size

        self.single_watermark()

    def single_watermark(self):
        # Diagonal length of full img
        diag_len = int(math.sqrt((self.width ** 2) + (self.height ** 2)))
        # Diagonal length to be used
        diag_use = diag_len * self.diagonal_percentage
        font_size = int(diag_use / (self.text_len / self.font_ratio))
        # Watermarking
        font = ImageFont.truetype(self.font_path, font_size)
        img_txt = Image.new('RGBA', font.getsize(self.text))  # RGBA mode is required to maintain opacity
        draw_text = ImageDraw.Draw(img_txt)
        draw_text.text((0, 0), self.text, font=font, fill=(255, 255, 255, self.opacity))
        angle = math.degrees(math.atan(self.height / self.width))
        img_txt = img_txt.rotate(angle, expand=True)
        # Pasting
        wm_x, wm_y = img_txt.size
        paste_x = int((self.width - wm_x) / 2)
        paste_y = int((self.height - wm_y) / 2)
        self.baseImg.paste(img_txt, (paste_x, paste_y, paste_x + wm_x, paste_y + wm_y), img_txt)
        self.baseImg.show()
