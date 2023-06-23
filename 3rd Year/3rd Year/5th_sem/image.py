import docxtpl
from docxtpl import InlineImage
from docx.shared import Mm

# Create a docxtpl template object
doc = docxtpl.DocxTemplate('temp.docx')

# Create an inline image object
image = InlineImage(doc, 'D:/MyPrograms/Micro Project Versions/Latest Version/Python/3rd Year/3rd Year/5th_sem/images/html.jpg', width=Mm(20))


# Add the image to the template
context = {"IMG": image}
doc.render(context)

# Save the document
doc.save('my_document_with_image.docx')
