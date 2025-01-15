import os, sys
from PIL import Image
from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))

inputFile = sys.argv[1]

image = Image.open(inputFile)

inputFileNoExt = Path(inputFile).stem

pdf_file = inputFileNoExt + ".pdf"

# print(pdf_file)

# exit()

image.save(pdf_file, "PDF", resolution = 100.0, save_all=True)