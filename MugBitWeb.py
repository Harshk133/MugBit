import PySimpleGUIWeb as p
from pathlib import Path
from docxtpl import DocxTemplate, InlineImage
from docx import Document
import wikipedia
from docxtpl import *
from docx.shared import Mm
from docx.shared import Inches
import random
import glob
from bing_image_downloader import downloader
import os

# Setting the Program Theme
p.theme('LightGrey3')

# Layout of the Program
layout = [
    [p.Text("Student Full Name: "), p.Input(key="STUDENT_NAME")],
    [p.Text("Enrollment Number: "), p.Input(key="STUDENT_ENR")],
    [p.Text("Micro-Project Title: "), p.Input(key="MICROPROJECT_TITLE")],
    [p.Text("Micro-Project Subject: "), p.Input(key="MICROPROJECT_SUBJECT")],
    [p.Text("Micro-Project Image Subject: "), p.Input(key="MICROPROJECT_IMG_SUBJECT")],
    [p.Button("Create Document"), p.Exit()],
]

# Create a DocxTemplate object
doc = DocxTemplate('template.docx')

# Populate the document with data from the GUI
def populate_doc(data):
    for key, value in data.items():
        doc.render(**{key: value})

window = p.Window("Mugbit V2.0")

# Event loop
event = window.read(layout)
values = window.read(layout)

# Populate the document with data from the GUI
data = {
        'STUDENT_NAME': values['STUDENT_NAME'],
        'STUDENT_ENR': values['STUDENT_ENR'],
        'MICROPROJECT_TITLE': values['MICROPROJECT_TITLE'],
        'MICROPROJECT_SUBJECT': values['MICROPROJECT_SUBJECT'],
        'MICROPROJECT_IMG_SUBJECT': values['MICROPROJECT_IMG_SUBJECT'],
    }

while True:
    if event == "Create Document":
        populate_doc(data)  
    
    doc.save('mugbit.docx')

# Save the document

