from pathlib import Path
from docxtpl import DocxTemplate


document_path = Path(__file__).parent / "Sample_template_microproject.docx"
doc = DocxTemplate(document_path)

STUDENT_NAME = "Harsh Moreshwar Kale"
STUDENT_ENR = 2110950051
STUDENT_ROLLNO = 3
TEACHER_NAME = "Mr. Lokare A. P."
MICROPROJECT_TITLE = "Python Programming"

context = {
    "STUDENT_NAME": STUDENT_NAME,
    "STUDENT_ENR": STUDENT_ENR,
    "STUDENT_ROLLNO": STUDENT_ROLLNO,
    "TEACHER_NAME": TEACHER_NAME,
    "MICROPROJECT_TITLE": MICROPROJECT_TITLE
}

doc.render(context)
doc.save(Path(__file__).parent / f"{MICROPROJECT_TITLE}.docx")




