import os
import shutil
from pdf2image import convert_from_path, convert_from_bytes

to_convert_path = './to_convert/'
converted_path = './converted/'
pdf_path = './PDFs/'
formats = ('png', 'pdf', 'jpeg')

files = os.listdir(to_convert_path)
pdfs = []
for file in files:
    name = file[:-3]
    shutil.copy2('./to_convert/' + file, pdf_path + name + '.pdf')
    images = convert_from_bytes(open(pdf_path + name + '.pdf', 'rb').read())
    print("Converting...")
    for form in formats:
        images[0].save(converted_path + name + '.' + form ,format=form)
