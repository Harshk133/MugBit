"""
Project: MugBit
Programmer: Harsh Kale
Date: 01/07/2023
"""

# Import Statements
import os
import microproject_data
from pathlib import Path
from docx import Document
from docxtpl import *
from docxtpl import DocxTemplate, InlineImage
import PySimpleGUI as p
from docx.shared import Mm
from docx.shared import Inches

# Document Initialization
file1 = "Sample_template_microproject.docx"
file2 = "Sample_template_certificate.docx"
document_path1 = Path(__file__).parent / file1
document_path2 = Path(__file__).parent / file2
doc1 = DocxTemplate(document_path1)
doc2 = DocxTemplate(document_path2)

# Following shows Window Programming 
# Setting the Window Theme
p.theme("LightGrey3")

# Layout of the Window
logo = [
    [p.Image(r"MugBit.PNG")],
]

form = [
    [p.Text("Student Full Name: "), p.Input(key="STUDENT_NAME")],
    [p.Radio("Male", "gender", default=True, key="male_radio"), p.Radio("Female", "gender", default=False, key="female_radio")],
    [p.Text("Student Roll NO: "), p.Input(key="STUDENT_ROLLNO")],
    [p.Text("Enrollment Number: "), p.Input(key="STUDENT_ENR")],
    [p.Text("Choose Semester: "), p.Combo(["CO5I", "CO6I"], default_value="CO5I", size=(80, 20), enable_events=True, readonly=True, key="COI")],
    [p.Text("Choose Subject: "), p.Combo(list(microproject_data.subjects.keys()),size=(80, 20), enable_events=True, key="COSUBJECT")],
    [p.Text("Choose Teacher Name: "), p.Combo(["Mr. Lokare A. P.", "Mr. Kazi A. S. M.", "Mr. Chavan A. Y.", "Mr. Sugare D. D.", "Ms. Kachare S. M.", "Mr. Osmani F. W.", "Mrs. Dharashive A. S."], size=(80, 20), enable_events=True, readonly=True, key="TEACHER_NAME")],
    [p.Text("Choose Available Micro-project: "), p.Combo([], key="TOPIC", size=(80, 20))]
]

layout = [
    [
        p.Column(logo),
        p.Column(form)
    ],
    [p.Button("Create Micro-project"), p.Exit()]
]

# Initializing the Window
window = p.Window("MugBit V5.0", layout, enable_close_attempted_event=True, element_justification="right")


while True:
    event, values = window.read()
    if event == p.WIN_CLOSED or event == "Exit":
        break
    if event == "COSUBJECT":
        selected_subject = values["COSUBJECT"]
        topics = microproject_data.subjects[selected_subject]
        window["TOPIC"].update(values=topics)
    # elif event == "TOPIC":
    #     selected_topic = values["TOPIC"]
    if event == "Create Micro-project":
        values["STUDENT_NAME"] 
        if values["male_radio"]:
            values["gender"] = "Mr."
        elif values["female_radio"]:
            values["gender"] = "Ms."
        values["STUDENT_ROLLNO"]
        values["STUDENT_ENR"]
        values["COI"]
        values["TEACHER_NAME"]
        selected_topic = values["TOPIC"]
        values["MICROPROJECT_TITLE"] = selected_topic

        doc1.render(values)
        doc2.render(values)
        doc1.save(f'{values["STUDENT_ROLLNO"]} {values["STUDENT_NAME"]}.docx')
        doc2.save(f'Certificate of {values["STUDENT_NAME"]}.docx')
        os.startfile(f'{values["STUDENT_ROLLNO"]} {values["STUDENT_NAME"]}.docx')
        os.startfile(f'Certificate of {values["STUDENT_NAME"]}.docx')       

# Closing the window
window.close()
