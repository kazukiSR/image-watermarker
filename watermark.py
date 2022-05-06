from PIL import Image, ImageDraw, ImageFont
import math


class WaterMarker:

    def __init__(self, img_file: str, text: str, font_path: str, opacity: int, mode: bool, output_file, file_format,
                 font_ratio=1.5, diagonal_percentage=0.8, **kwargs):
        self.font_ratio = font_ratio  # Size ratio of font
        self.diagonal_percentage = diagonal_percentage  # Percentage of the diagonal line length
        self.text = text  # Text to be become the watermark
        self.text_len = len(self.text)
        self.font_path = font_path
        self.opacity = int(256 * (opacity * 0.01))  # Passed opacity is 0-100, representing opacity percentage
        # Base image to be used
        self.baseImg = Image.open(img_file).convert('RGBA')
        # Img dimensions
        self.base_width, self.base_height = self.baseImg.size
        self.output_file = output_file
        self.file_format = file_format
        self.save_params = kwargs

        # mode = True for single watermarks
        if mode:
            self.single_watermark()
        else:
            self.multiple_watermarks()

    def single_watermark(self):
        # Diagonal length of full img
        diag_len = int(math.sqrt((self.base_width ** 2) + (self.base_height ** 2)))
        # Diagonal length to be used
        diag_use = diag_len * self.diagonal_percentage
        font_size = int(diag_use / (self.text_len / self.font_ratio))

        # Watermarking
        font = ImageFont.truetype(self.font_path, font_size)
        img_txt = self.create_watermark(size=font.getsize(self.text), font=font)
        # Pasting
        wm_x, wm_y = img_txt.size
        paste_x = int((self.base_width - wm_x) / 2)
        paste_y = int((self.base_height - wm_y) / 2)
        self.baseImg.paste(img_txt, (paste_x, paste_y, paste_x + wm_x, paste_y + wm_y), img_txt)

        self.save_file()

    def multiple_watermarks(self):
        # One text box is 1/5th of the measurements of the original image
        txt_box_width = int(self.base_width / 5)
        txt_box_height = int(self.base_height / 5)
        txt_box = (txt_box_width, txt_box_height)
        # Font size calculation
        txt_box_diag = int(math.sqrt((txt_box_width ** 2) + (txt_box_height ** 2)))
        diag_use = txt_box_diag * self.diagonal_percentage
        font_size = int(diag_use / (self.text_len / self.font_ratio))
        REPEAT_X = 2  # How close together horizontally
        REPEAT_Y = 2  # How close together vertically

        font = ImageFont.truetype(self.font_path, font_size)
        img_txt = self.create_watermark(size=txt_box, font=font)

        step_x = int(self.base_width / img_txt.size[0] * REPEAT_X)
        step_y = int(self.base_height / img_txt.size[1] * REPEAT_Y)
        print(f"Steps: ({step_x}, {step_y})")
        for x_ratio in range(0, step_x):
            x = int(self.base_width * x_ratio / step_x)
            for y_ratio in range(0, step_y):
                y = int(self.base_height * y_ratio / step_y)
                self.baseImg.alpha_composite(img_txt, dest=(x, y))  # in-place adding of txt

        self.save_file()

    def create_watermark(self, size: tuple, font: ImageFont):
        img_txt = Image.new('RGBA', size)  # RGBA mode is required to maintain opacity
        draw_text = ImageDraw.Draw(img_txt)
        draw_text.text((0, 0), self.text, font=font, fill=(255, 255, 255, self.opacity))
        angle = math.degrees(math.atan(self.base_height / self.base_width))
        img_txt = img_txt.rotate(angle, expand=True)
        return img_txt

    def save_file(self):
        self.baseImg.thumbnail((self.base_width, self.base_height), Image.ANTIALIAS)
        if self.file_format == 'JPEG':
            self.baseImg = self.baseImg.convert('RGB')
        self.baseImg.save(fp=self.output_file, format=self.file_format, **self.save_params)
        self.baseImg.close()
