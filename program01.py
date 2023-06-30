# import PySimpleGUI as sg

# # Define the layout of your window
# layout = [
#     [sg.Listbox(['Option 1', 'Option 2', 'Option 3'], size=(20, 3), key='-LISTBOX-')],
#     [sg.Text('Selected Option:'), sg.Text('', key='-OUTPUT-')],
#     [sg.Button('Add Content')]
# ]

# # Create the window
# window = sg.Window('Dynamic Content Example', layout)

# while True:
#     event, values = window.read()
#     if event == sg.WINDOW_CLOSED:
#         break
#     if event == 'Add Content':
#         selected_option = values['-LISTBOX-'][0]  # Get the selected option from the ListBox
#         # Add content based on the selected option
#         if selected_option == 'Option 1':
#             content = 'Content for Option 1'
#         elif selected_option == 'Option 2':
#             content = 'Content for Option 2'
#         elif selected_option == 'Option 3':
#             content = 'Content for Option 3'
#         else:
#             content = 'No content available'

#         # Update the output text element with the selected option
#         window['-OUTPUT-'].update(content)

# # Close the window
# window.close()
# ================================================================================================
# import PySimpleGUI as sg

# layout = [
#     [sg.Listbox(values=[], size=(30, 6), key='-LISTBOX-')],
#     [sg.Button('Add Item', key='-ADD-')]
# ]

# window = sg.Window('List Box Example', layout)
# items = []

# while True:
#     event, values = window.read()
#     if event == sg.WINDOW_CLOSED:
#         break
#     elif event == '-ADD-':
#         new_item = sg.popup_get_text('Enter item:')
#         if new_item:
#             items.append(new_item)
#             window['-LISTBOX-'].update(values=items)

# window.close()
# ================================================================================================

import PySimpleGUI as sg

# Define the options for each subject
subjects = {
    'Java': ['Java Basics', 'OOP in Java', 'Java Collections'],
    'Python': ['Python Basics', 'Data Science with Python', 'Web Development with Python']
}

# Create a layout with a Combo Box for subjects and a second Combo Box for topic selection
layout = [
    [sg.Text('Select a subject:')],
    [sg.Combo(list(subjects.keys()), key='-SUBJECT-', enable_events=True)],
    [sg.Text('Select a topic:')],
    [sg.Combo([], key='-TOPIC-', size=(40, 20))]
]

# Create the window using the defined layout
window = sg.Window('Subject Selection', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-SUBJECT-':
        selected_subject = values['-SUBJECT-']
        topics = subjects[selected_subject]
        window['-TOPIC-'].update(values=topics)

window.close()
