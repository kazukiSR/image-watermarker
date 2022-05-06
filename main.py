from watermark import WaterMarker

ARIAL_PATH = r'C:/Windows/Fonts/Arial.ttf'
CALIBRI_PATH = r'C:/Windows/Fonts/Calibri.ttf'
IMG = r'cat.jpg'

ayo = WaterMarker(IMG, u"scooby doo", CALIBRI_PATH, opacity=25, mode=True, output_file="output.jpg",
                  file_format='JPEG')


# TODO (Functionality)



# TODO TKInter GUI
# TODO Freedom on watermarking orientation, opacity, and word size
# TODO open file with a choose file, output file to directory of choice.
# TODO identify all fonts installed on windows default and show a dropdown list to choose font
# TODO finalize as .exe

