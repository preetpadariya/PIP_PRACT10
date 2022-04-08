# Generate PDF file of your 3rd Semester Mark-sheet
#pip install PIL
from PIL import Image
#Path where image store
image_1=Image.open(r'D:\Result sem-3.jpeg')
#converting into PDF
im_1=image_1.convert('RGB')
#Path where your pdf file will be save
im_1.save(r'D:\Studies\20ce063_PIP.pdf')
