"""
Project: MugBit
Programmer: Harsh Kale
Date: 6/19/2023
"""
# Import Statements
from pathlib import Path
from docxtpl import DocxTemplate, InlineImage
from docxtpl import *
from docx import Document
import PySimpleGUI as p
from wikipedia import *
from docxtpl import InlineImage
from docx.shared import Mm
from docx.shared import Inches
import random
import glob
from bing_image_downloader import downloader
import os
import microproject_data

# Setting the Program Theme
p.theme('LightGrey3')

# Layout of the Program
logo = [
    [p.Image(r'MugBit.PNG')],
]

form = [
    [p.Text("Student Full Name: "), p.Input(key="STUDENT_NAME")],
    [p.Radio("Male", 'gender', default=True, key="male_radio")], 
    [p.Radio("Female", 'gender', default=False, key="female_radio")], 
    [p.Text("Enrollment Number: "), p.Input(key="STUDENT_ENR")],
    [p.Txt("Chose the Semester: "), p.Combo(["CO5I", "CO6I"], default_value="CO5I", s=(43,22), enable_events=True, readonly=True, key='COI')],
    [p.Txt("Choose the Subject: "), p.Combo(["Environmental Studies (22447)", "Advanced Java Programming (22517)", "Operating System (22516)", "Client side scripting language (22519)", "Software Testing (22518)"], default_value="Advanced Java Programming (22517)", s=(43,22), enable_events=True, readonly=True, key='COSUBJECT')],
    [p.Text("Student Roll NO: "), p.Input(key="STUDENT_ROLLNO")],
    # [p.Text("Teacher Name: "), p.Input(key="TEACHER_NAME")],
    [p.Txt("Chosse the Teacher: "), p.Combo(["Mr. Kazi A. S. M.", "Mr. Lokare A. P.", "Mr. Chavan A. Y.", "Mr. Sugare D. D.", "Ms. Kachare S. M.", "Mr. Patwari P. M.", "Mrs. Tele S. N.", "Ms. Nagrgoje A.", "Mr. Omkare R. S."], default_value="Mr. Sugare D. D.", s=(43,22), enable_events=True, readonly=True, key='TEACHER_NAME')],
    # [p.Text("Micro-Project Title: "), p.Input(key="MICROPROJECT_TITLE")],
    # [p.Text("Micro-Project Subject: "), p.Input(key="MICROPROJECT_SUBJECT")],
    # [p.Text("Micro-Project Image Subject: "), p.Input(key="MICROPROJECT_IMG_SUBJECT")],
    [p.Txt("Choose Available Microproject: "), p.Combo([
        "Energy Billing System: Usage-Based Billing Module Development",
        "Medical Store Inventory Management System",
        "Library Book Issue Management System",
        "Restaurant Order Management and Billing System",
        "Online Bus Ticket Booking Module",
        "Java mini application based on applet or swing.",
        "IP finder",
        "Word counter based on swing.",
        "Notepad using applet",
        "Simple games like snake, tic tac toe, Pac man, etc."
    ], default_value="IP finder", s=(43,22), enable_events=True, readonly=True, key='COSUBJECT')],
]

layout = [
    [
        p.Column(logo),
        # p.VSeparator(),
        p.Column(form),
    ],
    [p.Button("Create Document"), p.Exit()]
]

# # Document Initialization
file1 = "Sample_template_microproject.docx"
file2 = "Sample_template_certificate.docx"
document_path1 = Path(__file__).parent / file1
document_path2 = Path(__file__).parent / file2 
doc1 = DocxTemplate(document_path1)
doc2 = DocxTemplate(document_path2)


# Showing the Window 
# TODO: Add this to following after testing --> element_justification="right"
window = p.Window("Mugbit V2.0", layout, element_justification="right", enable_close_attempted_event=True)

# Showing the Progress Window
progressLayout = [
    # [p.ProgressBar(1000, orientation='h', size=(20, 20), key='progress_bar'), p.Cancel()],
    [p.Text("Creating YOur Microproject..")],
    [p.Text("Pulling Data From Internet...")],
    [p.ProgressBar(1000, orientation='h', size=(20, 20), key='progress_bar')],
]

# Handling the Progress Bar Window
progressWin = p.Window("Creating Your Projects...", progressLayout)
progress_bar = progressWin['progress_bar']
def progressBar():
    '''
    This Function Handles the Progress Bar
    '''
    for i in range(1000):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = progressWin.read(timeout=10)
        if event == 'Cancel'  or event == p.WIN_CLOSED:
            break
    # update bar with loop value +1 so that bar eventually reaches the maximum
        progress_bar.UpdateBar(i + 1)
        if(i == 1000):
            break
    
    return True

# While Loop for fetching User Inputed Data
while True:
    event, values = window.read()
    if event == p.WIN_CLOSED or event == "Exit" and p.popup_yes_no('Do You Really Want to Close MugBit?') == 'Yes':
        break
    if event == "Create Document":
        progressBar()
        values["STUDENT_NAME"].capitalize()
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
        # elif event == 'COSUBJECT':
        #     # selected_option = values['COSUBJECT']
        #     selected_option = "Advanced Java Programming (22517)"
        #     # window['-OUTPUT-'].update(f'You selected: {selected_option}')
        #     if(selected_option):
        #         window['-OUTPUT-'].update()

        subject = values["MICROPROJECT_SUBJECT"]
        try: 
            para = summary(subject, sentences=20)
            PROPOSED_METHODOLOGY_INFO = summary(subject, sentences=5)
            RATIONALE = summary(subject, sentences=3)
        except Exception as e:
            p.popup("Error NO WikiPedia Page Found", e)
            continue

        values["MICROPROJECT_SUBJECT"] = para
        values["PROPOSED_METHODOLOGY_INFO"] = PROPOSED_METHODOLOGY_INFO
        values["RATIONALE"] = RATIONALE
        # ImgSub = values["MICROPROJECT_IMG_SUBJECT"]

        if values["COSUBJECT"] == "Operating System (22516)":                
            # Skill Developed / Learning out of this microproject section.
            for i, value in microproject_data.OS_MicroProject_Dictionary["Skill Developed"].items():  
                values[f"SK_LINE{i}"] = value 

            # Application of this MicroProject Section
            for i, value in microproject_data.OS_MicroProject_Dictionary["Application"].items():
                values[f'APPLN_LINE{i}'] = value
            
            for i, value in microproject_data.OS_MicroProject_Dictionary["course_outcome"].items():
                values[f"MANNUAL_LINE_{i}"] = value

        elif values["COSUBJECT"] == "Advanced Java Programming (22517)":
            # Skill Developed / Learning out of this microproject section.
            for i, value in microproject_data.AdvJPR_MicroProject_Dictionary["Skill Developed"].items():  
                values[f"SK_LINE{i}"] = value 

            # Application of this MicroProject Section
            for i, value in microproject_data.AdvJPR_MicroProject_Dictionary["Application"].items():
                values[f'APPLN_LINE{i}'] = value

            for i, value in microproject_data.AdvJPR_MicroProject_Dictionary["course_outcome"].items():
                values[f"MANNUAL_LINE_{i}"] = value

        elif values["COSUBJECT"] == "Client side scripting language (22519)":
            # Skill Developed / Learning out of this microproject section.
            for i, value in microproject_data.CSS_MicroProject_Dictionary["Skill Developed"].items():  
                values[f"SK_LINE{i}"] = value 

            # Application of this MicroProject Section
            for i, value in microproject_data.CSS_MicroProject_Dictionary["Application"].items():
                values[f'APPLN_LINE{i}'] = value

        elif values["COSUBJECT"] == "Environmental Studies (22447)":
            # Skill Developed / Learning out of this microproject section.
            for i, value in microproject_data.ENV_MicroProject_Dictionary["Skill Developed"].items():  
                values[f"SK_LINE{i}"] = value 

            # Application of this MicroProject Section
            for i, value in microproject_data.ENV_MicroProject_Dictionary["Application"].items():
                values[f'APPLN_LINE{i}'] = value
        else:
            p.popup("Work is going on")

        ImgSub = values["MICROPROJECT_IMG_SUBJECT"]

        downloader.download(ImgSub, limit=1, output_dir='download_imageHD_shriram', adult_filter_off=True, force_replace=False, timeout=60)

        def get_first_image(ImgSub):
            for file in os.listdir(ImgSub):
                if file.endswith(".png") or file.endswith(".jpg"):
                    return os.path.join(ImgSub, file)
            return None
        
        imgPath = get_first_image(f"download_imageHD_shriram/{ImgSub}")

        if imgPath is not None:
            print(f"First image found: {imgPath}")
        else:
            print("No image found in the specified directory.")
            p.popup_error("No image found in the specified directory.")

        # Image Handling
        image1 = InlineImage(doc1, imgPath, width=Mm(70))

        # Add the image to the template
        values["IMG"] = image1
        # values["IMG2"] = image2  

        doc1.render(values)
        doc2.render(values)
        output_path1 = Path(__file__).parent / f"{values['MICROPROJECT_TITLE']}-microproject.docx"
        output_path2 = Path(__file__).parent / f"{values['MICROPROJECT_TITLE']}-certificate.docx"
        doc1.save(output_path1)
        doc2.save(output_path2)

        if(progressBar() == True):
            progressWin.close()
            p.popup(f"Project Created! File Saved at this path: {output_path1}")    
            # To Open a file we can use os.startFile(pathOfFile)      
        
# Closing the Window
window.close()




