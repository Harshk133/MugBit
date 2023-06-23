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
    [p.Txt("Chosse the Teacher: "), p.Combo(["Mr. Kazi A. S. M.", "Mr. Lokare A. P.", "Mr. Chavan A. Y.", "Mr. Sugare D. D.", "Ms. Kachare S. M.", "Mr. Patwari P. M.", "Mrs. Tele S. N.", "Ms. Nagrgoje A.", "Mr. Omkare R. S."], default_value="Mr. Sugare D. D.", s=(43,22), enable_events=True, readonly=True, key='TEACHER_NAME')],
    [p.Text("Micro-Project Title: "), p.Input(key="MICROPROJECT_TITLE")],
    [p.Text("Micro-Project Subject: "), p.Input(key="MICROPROJECT_SUBJECT")],
    [p.Text("Micro-Project Image Subject: "), p.Input(key="MICROPROJECT_IMG_SUBJECT")],
    [p.Button("Create Document"), p.Exit()],
]

OS_MicroProject_Dictionary = {
    0: "Comparative Analysis of Operating System Types and Mobile OS Examples",
    1: "Comparative Analysis of Page Faults in Different Page Replacement Algorithms for a Given Page Reference String",
    2: "Linux Command Helper",
    3: "Comparative Analysis of CPU Scheduling Algorithms: Total Waiting and Turnaround Time Calculation for n Processes",
    4: "Shell Process Manager",
    "Skill Developed": {
        # Skilled Developed/ Learning Out of this MicroProject Section
        1: "We learn that how to make the project that solves the real world problem.",
        2: "How the Operating System plays the essential role in computer engineering.",
        3: "By working on micro-projects, you'll gain a deeper understanding of various operating system concepts such as process scheduling, memory allocation",
        4: "Operating system also involves the debugging skills, helps you learn how to identify and resolve errors, and strengthens your troubleshooting abilities",
        5: "We learn much more commands used in the Linux Operating System."
    },
    "Application": {
        # Application of this MicroProject Section
        1: "Operating system micro-projects are often used in educational settings to help students understand and apply operating system concepts",
        2: "This Micro-projects focused on system optimization can help improve the performance and efficiency of operating systems. By analyzing bottlenecks, implementing optimizations, and refining algorithms, these projects aim to enhance the overall system performance and user experience.",
        3: "Operating system micro-projects centered around file system design, implementation, or optimization contribute to the development of efficient and reliable file systems."
    },
    "course_outcome": {
        # Course Outcome for this Operating System MicroProject Section
        1: "Install Linux operating system and configure it.",
        2: "Use operating system tools to perform various functions.",
        3: "Execute process commands for performing process management operations.",
        4: "Apply scheduling algorithms to calculate turnaround time and average waiting time.",
        5: "Calculate efficiency of different memory management techniques.",
        6: "Apply file management techniques."
    }
}

AdvJPR_MicroProject_Dictionary = {
    0: "Energy Billing System: Usage-Based Billing Module Development",
    1: "Medical Store Inventory Management System",
    2: "Library Book Issue Management System",
    3: "Restaurant Order Management and Billing System",
    4: "Online Bus Ticket Booking Module",
    5: "Java mini application based on applet or swing.",
    6: "IP finder",
    7: "Word counter based on swing.",
    8: "Notepad using applet",
    9: "Simple games like snake, tic tac toe, Pac man, etc.",
    "Skill Developed": {
        # Skilled Developed/ Learning Out of this MicroProject Section
        1: "We can understand the importance of code optimization for enhancing the performance of our Java applications.",
        2: "We can comprehend the significance of implementing proper error handling mechanisms to ensure the robustness of our software.",
        3: "We can appreciate the value of using design patterns to improve the maintainability and scalability of our Java projects.",
        4: "We can acknowledge the benefits of using frameworks like Spring to simplify the development process and enhance the modularity of our code",
        5: "Java teach us to realize the importance of conducting thorough testing and debugging to ensure the reliability and stability of our Java programs."
    },
    "Application": {
        # Application of this MicroProject Section
        1: "Advanced Java micro-projects can be used to build dynamic and interactive web applications",
        2: "This includes developing server-side components using Java Servlets, JavaServer Pages (JSP), JavaServer Faces (JSF), and Java Persistence API (JPA). You can create web applications for e-commerce, content management systems, social networking platforms, and more.",
        3: " Advanced Java micro-projects can involve developing IoT solutions using Java and frameworks like Eclipse IoT or MQTT (Message Queuing Telemetry Transport)."
    },
    "course_outcome": {
        # Course Outcome for this Java Advance MicroProject Section
        1: "Develop program using GUI framework (AWT and Swing)",
        2: "Handle events of AWT and Swing Components",
        3: "Develop programs to handle events in Java Programming.",
        4: "Develop Java Programs using Networking Concepts",
        5: "Develop programs using Database.",
        6: "Develop programs using Servlets."
    }
}

CSS_MicroProject_Dictionary = {
    0: "Develop a website on Storage management.",
    1: "Develop a website on E-Shopping cart.",
    2: "Develop a website on Travel agency.",
    3: "Develop a website on movie ticket booking.",
    4: "Develop a website on Railway ticket booking.",
    5: "Develop a website on bus ticket booking.",
    6: "Develop a website on Exam quiz.",
    7: "Develop a website on Lab management.",
    8: "Develop a website on Airplane reservation.",
    9: "Develop a website on Food shop.",
    10: "Develop a website on To-do list",
    11: " Develop a website on online appointment booking for spa",
    12: "Buyer Information Entry Form with JavaScript Validation",
    13: "Interactive Image Slideshow",
    14: "Interactive Institute Website with Menu Validation and Information Display",
    15: "Circle Animation: Rotating Marbles",
    "Skill Developed": {
        # Skilled Developed/ Learning Out of this MicroProject Section
        1: "JavaScript is the most common language used for client-side scripting. Working on micro-projects will help you improve your JavaScript programming skills, including syntax, functions, variables, data types, and control structures.",
        2: "The Document Object Model (DOM) is a programming interface for HTML and XML documents. With client-side scripting, you can manipulate the DOM to dynamically modify web pages, add or remove elements, change styles, and handle events. Micro-projects can help you gain proficiency in DOM manipulation techniques.",
        3: "Client-side scripting involves responding to user interactions such as button clicks, form submissions, and mouse movements. By working on micro-projects, you can learn how to handle various events effectively and create responsive and interactive web experiences.",
        4: "As client-side scripts become more complex, organizing code and maintaining modularity becomes crucial. Micro-projects can teach you how to structure your codebase effectively, separate concerns, and apply design patterns to improve maintainability and reusability.",
        5: "Overall, micro-projects involving client-side scripting can help you develop a wide range of skills that are valuable in web development and enhance your ability to create dynamic, interactive, and user-friendly web applications."
    },
    "Application": {
        # Application of this MicroProject Section
        1: "Create a micro-project that involves designing and implementing interactive web forms using client-side scripting languages like JavaScript.",
        2: "Build a micro-project where you focus on responsive web design using HTML, CSS, and JavaScript. Develop a website that adapts and displays content optimally across various devices and screen sizes, ensuring a seamless user experience.",
        3: "Implement dynamic content loading using AJAX (Asynchronous JavaScript and XML) or other client-side scripting techniques. Build a micro-project that retrieves data from a server asynchronously and dynamically updates specific sections of a webpage without requiring a full page reload."
    }
}

ENV_MicroProject_Dictionary = {
    0: "Prepare a report on visit to PUC Center. ",
    1: "Visit a near by RO plant and prepare detail technical report.",
    2: "Prepare report on Household water filtration unit.",
    3: "Prepare a list of polluted natural resources which are responsible for pollution and collect information on how to manage them.",
    4: "Hospital Waste Analysis: Monitoring Solid Hazardous and Toxic Waste Percentage Over Two Months.",
    5: "Visit of Municipal Effluent Treatment Plant: Visit effluent treatment plant and prepare report on waste management.",
    6: "Visit of Water Treatment Plant: Visit water treatment plant and prepare report on various units of water treatment and its management.",
    7: "Preparation of report: Prepare the chart of solid waste management showing effects on environment. ",
    "Skill Developed": {
        # Skilled Developed/ Learning Out of this MicroProject Section
        1: "Micro-projects often involve conducting research on specific environmental topics, which can help develop skills in information gathering, data analysis, and critical thinking..",
        2: "Environmental studies micro-projects often require collecting and analyzing data related to environmental parameters, such as air or water quality, biodiversity, or climate patterns. This process helps develop skills in data collection methods, statistical analysis, and data interpretation",
        3: "Micro-projects require participants to analyze complex environmental challenges and identify key problems or areas for improvement. ",
        4: "Micro-projects often involve planning, organizing, and implementing specific tasks within a given timeframe.",
        5: "This fosters the development of communication skills, including effective written and verbal communication, public speaking, and presenting complex information in a concise and understandable manner."
    },
    "Application": {
        # Application of this MicroProject Section
        1: "If the micro-project focuses on a specific environmental issue, the findings can be applied to develop strategies for conservation and management.",
        2: "Micro-projects can contribute to raising awareness about environmental issues. The findings can be shared through presentations, reports, or outreach activities to educate others and promote environmental consciousness.",
        3: "The findings of a micro-project may contribute to the existing body of knowledge in environmental studies."
    }
}


# # Document Initialization
file1 = "Sample_template_microproject.docx"
file2 = "Sample_template_certificate.docx"
document_path1 = Path(__file__).parent / file1
document_path2 = Path(__file__).parent / file2 
# doc = docxtpl.DocxTemplate('temp.docx')
doc1 = DocxTemplate(document_path1)
doc2 = DocxTemplate(document_path2)


# Showing the Window 
# TODO: Add this to following after testing --> element_justification="right"
window = p.Window("Mugbit V2.0", layout, element_justification="right",enable_close_attempted_event=True)

# While Loop for fetching User Inputed Data
while True:
    event, values = window.read()
    if event == p.WIN_CLOSED or event == "Exit" and p.popup_yes_no('Do You Really Want to Close MugBit?') == 'Yes':
        break
    if event == "Create Document":
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
            for i, value in OS_MicroProject_Dictionary["Skill Developed"].items():  
                values[f"SK_LINE{i}"] = value 

            # Application of this MicroProject Section
            for i, value in OS_MicroProject_Dictionary["Application"].items():
                values[f'APPLN_LINE{i}'] = value
            
            for i, value in OS_MicroProject_Dictionary["course_outcome"].items():
                values[f"MANNUAL_LINE_{i}"] = value

        elif values["COSUBJECT"] == "Advanced Java Programming (22517)":
            # Skill Developed / Learning out of this microproject section.
            for i, value in AdvJPR_MicroProject_Dictionary["Skill Developed"].items():  
                values[f"SK_LINE{i}"] = value 

            # Application of this MicroProject Section
            for i, value in AdvJPR_MicroProject_Dictionary["Application"].items():
                values[f'APPLN_LINE{i}'] = value

            for i, value in AdvJPR_MicroProject_Dictionary["course_outcome"].items():
                values[f"MANNUAL_LINE_{i}"] = value

        elif values["COSUBJECT"] == "Client side scripting language (22519)":
            # Skill Developed / Learning out of this microproject section.
            for i, value in CSS_MicroProject_Dictionary["Skill Developed"].items():  
                values[f"SK_LINE{i}"] = value 

            # Application of this MicroProject Section
            for i, value in CSS_MicroProject_Dictionary["Application"].items():
                values[f'APPLN_LINE{i}'] = value

        elif values["COSUBJECT"] == "Environmental Studies (22447)":
            # Skill Developed / Learning out of this microproject section.
            for i, value in ENV_MicroProject_Dictionary["Skill Developed"].items():  
                values[f"SK_LINE{i}"] = value 

            # Application of this MicroProject Section
            for i, value in ENV_MicroProject_Dictionary["Application"].items():
                values[f'APPLN_LINE{i}'] = value
        else:
            p.popup("Work is going on")
        

        

        # Absolute Image Path
        # imgPath = ["D:/MyPrograms/Micro Project Versions/Latest Version/Python/3rd Year/3rd Year/5th_sem/images/img1.jpg",
        # "D:/MyPrograms/Micro Project Versions/Latest Version/Python/3rd Year/3rd Year/5th_sem/images/img2.jpg"]
        ImgSub = values["MICROPROJECT_IMG_SUBJECT"]

        downloader.download(ImgSub, limit=1, output_dir='download_imageHD_shriram', adult_filter_off=True, force_replace=False, timeout=60)

        # imgPath = f"download_imageHD_shriram/{ImgSub}/Image_1.png"
        # imgPath = f"download_imageHD_shriram/{ImgSub}/Image_1.jpg"
        # imgPath = f"download_imageHD_shriram/{ImgSub}/Image_1.png"

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

        # Image Handling
        image1 = InlineImage(doc1, imgPath, width=Mm(70))
        # image2 = InlineImage(doc1, imgPath[1], width=Mm(20))

        # Add the image to the template
        # context = {"IMG": image}
        values["IMG"] = image1
        # values["IMG2"] = image2

        
        

        doc1.render(values)
        doc2.render(values)
        output_path1 = Path(__file__).parent / f"{values['MICROPROJECT_TITLE']}-microproject.docx"
        output_path2 = Path(__file__).parent / f"{values['MICROPROJECT_TITLE']}-certificate.docx"
        doc1.save(output_path1)
        doc2.save(output_path2)
        p.popup("Project Created!", f"File Saved at this path: {output_path1}")
        

# Closing the Window
window.close()




