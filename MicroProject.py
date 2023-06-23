"""
Project: MugBit
Programmer: Harsh Kale
Date: 6/19/2023
"""
# Import Statements
from pathlib import Path
from docxtpl import DocxTemplate
import PySimpleGUI as p
from wikipedia import *

# Document Initialization
document_path1 = Path(__file__).parent / "Sample_template_microproject.docx"
document_path2 = Path(__file__).parent / "Sample_template_certificate.docx"
doc1 = DocxTemplate(document_path1)
doc2 = DocxTemplate(document_path2)

# Setting the Program Theme
p.theme('LightGrey3')

# Layout of the Program
layout = [
    [p.Image(r'MugBit.PNG')],
    [p.Text("Student Full Name: "), p.Input(key="STUDENT_NAME")],
    [p.Radio("Male", 'gender', default=True, key="male_radio")], 
    [p.Radio("Female", 'gender', default=False, key="female_radio")], 
    [p.Text("Enrollment Number: "), p.Input(key="STUDENT_ENR")],
    [p.Txt("Chose the Semester: "), p.Combo(["CO5I", "CO6I"], default_value="CO5I", s=(43,22), enable_events=True, readonly=True, key='COI')],
    [p.Txt("Chose the Subject: "), p.Combo(["Environmental Studies (22447)", "Advanced Java Programming (22517)", "Operating System (22516)", "Client side scripting language (22519)"], default_value="Advanced Java Programming (22517)", s=(43,22), enable_events=True, readonly=True, key='COSUBJECT')],
    [p.Text("Student Roll NO: "), p.Input(key="STUDENT_ROLLNO")],
    # [p.Text("Teacher Name: "), p.Input(key="TEACHER_NAME")],
    [p.Txt("Chose the Subject: "), p.Combo(["Mr. Kazi A. S. M.", "Mr. Lokare A. P.", "Mr. Chavan A. Y.", "Mr. Sugare D. D.", "Ms. Kachare S. M.", "Mr. Patwari P. M.", "Mrs. Tele S. N.", "Ms. Nagrgoje A.", "Mr. Omkare R. S."], default_value="Mr. Sugare D. D.", s=(43,22), enable_events=True, readonly=True, key='TEACHER_NAME')],
    [p.Text("Micro-Project Title: "), p.Input(key="MICROPROJECT_TITLE")],
    [p.Text("Micro-Project Subject: "), p.Input(key="MICROPROJECT_SUBJECT")],
    [p.Button("Create Document"), p.Exit()],
]

# Showing the Window 
# TODO: Add this to following after testing --> element_justification="right"
window = p.Window("Mugbit", layout, element_justification="right",enable_close_attempted_event=True)

# While Loop for fetching User Inputed Data
while True:
    event, values = window.read()
    if event == p.WIN_CLOSED or event == "Exit" and p.popup_yes_no('Do You Really Want to Close MugBit?') == 'Yes':
        break
    if event == "Create Document":
        values["STUDENT_NAME"]
        values["STUDENT_ENR"]
        values["STUDENT_ROLLNO"]
        values["TEACHER_NAME"]
        values["MICROPROJECT_TITLE"]
        values['COI']
        values['COSUBJECT']
        if values['male_radio']:
            values['gender'] = 'Mr.'
        elif values['female_radio']:
            values['gender'] = 'Ms.'
            

        subject = values["MICROPROJECT_SUBJECT"]
        para = summary(subject, sentences=20)
        PROPOSED_METHODOLOGY_INFO = summary(subject, sentences=5)
        RATIONALE = summary(subject, sentences=5)

        values["MICROPROJECT_SUBJECT"] = para
        values["PROPOSED_METHODOLOGY_INFO"] = PROPOSED_METHODOLOGY_INFO
        values["RATIONALE"] = RATIONALE

        doc1.render(values)
        doc2.render(values)
        output_path1 = Path(__file__).parent / f"{values['MICROPROJECT_TITLE']}-microproject.docx"
        output_path2 = Path(__file__).parent / f"{values['MICROPROJECT_TITLE']}-certificate.docx"
        doc1.save(output_path1)
        doc2.save(output_path2)
        p.popup("Project Created!", f"File Saved at this path: {output_path1}")
        

# Closing the Window
window.close()




