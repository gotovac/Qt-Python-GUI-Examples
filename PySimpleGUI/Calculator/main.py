import PySimpleGUI as sg

layout = [[sg.Input(size=(13,3), font=("Any", 25), do_not_clear=True, justification='left', key='calc')],
            [sg.ReadFormButton("CLR"), sg.ReadFormButton('DEL'), sg.ReadFormButton('/',  ), sg.ReadFormButton('*',  )],
            [sg.ReadFormButton("7"), sg.ReadFormButton("8"), sg.ReadFormButton("9"), sg.ReadFormButton("-")],
            [sg.ReadFormButton("4"), sg.ReadFormButton("5"), sg.ReadFormButton("6"), sg.ReadFormButton("+")],
            [sg.ReadFormButton("1"), sg.ReadFormButton("2"), sg.ReadFormButton("3"), sg.ReadFormButton("=")],
            [sg.ReadFormButton("."), sg.ReadFormButton("0"), sg.ReadFormButton("("), sg.ReadFormButton(")")]]

form = sg.FlexForm('Calculator', default_button_element_size=(7,2), auto_size_buttons=False, grab_anywhere=False)
form.Layout(layout)

number = ''
countnum = 0
while True:
    button = form.Read()[0]
    if button is "CLR":
        number = ''
    elif button is "DEL":
        number = number[:-1]
    elif button in '1234567890.+-*/()':
        if button in '1234567890.':
            if 7 > countnum >= 0:
                number += button
                countnum += 1
        else:
            number += button
            countnum = 0
    elif button in '=':
        if ')' not in number and '(' in number:
            number = ''
            number += 'ERROR'

        elif '(' not in number and ')' in number:
            number = ''
            number += 'ERROR'

        elif number[-1] == '+' or number[-1] == '-' or number[-1] == '*' or number[-1] == '/':
            number = ''
            number += 'ERROR'

        elif number[-1] == '0' and number[-2] == '/':
            number = ''
            number += 'ERROR'

        else:
            equals = eval(''.join(number))
            number = ''
            number += str(equals)

    form.FindElement('calc').Update(number)