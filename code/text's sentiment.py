import PySimpleGUI as sg
from textblob import TextBlob
import emoji

sg.theme('LightGrey1')

layout = [
    [sg.Text('Enter Text:')]
    [sg.InputText(key='-INPUT-')],
    [sg.Button('Submit!')],
    [sg.Text(key='-OUTPUT-')]
    [sg.Button('Close')],
    ]

window = sg.Window('text sentiment', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':
        break
    elif event == 'Submit':
        window['-OUTPUT-'].update('Hello ' + values['-INPUT-'])
        break
window.close()
    
