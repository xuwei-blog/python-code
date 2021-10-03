import os
from docx import Document
import glob


#for item in os.listdir():
#    print(item)

#print(os.listdir())



for dirpath,dirnames,files in os.walk('./'):
    for item in files:
        print(item)

