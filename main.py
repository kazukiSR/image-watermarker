from watermark import WaterMarker

ARIAL_PATH = r'C:/Windows/Fonts/Arial.ttf'
CALIBRI_PATH = r'C:/Windows/Fonts/Calibri.ttf'
IMG = r'funky.jpg'

ayo = WaterMarker(IMG, u"scooby doo", CALIBRI_PATH, opacity=25, mode=False, output_file="output.jpg",
                  file_format='JPEG')




# TODO finalize as .exe

