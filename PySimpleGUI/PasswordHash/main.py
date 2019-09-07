import PySimpleGUI as sg      
import hashlib      
    
layout = [  [sg.Text('Password'), sg.Input(size=(50,1), key='password')],
            [sg.Text('SHA Hash'), sg.Input('', size=(50,1), key='hash')]]      

window = sg.Window('Hashiranje lozinke', layout, auto_size_text=False, default_element_size=(10,1),      
                    text_justification='r', return_keyboard_events=True, grab_anywhere=False)  

while True:      
    event, values = window.Read()      
    if event is None:      
            exit()      

    password = values['password']        
    password_utf = password.encode('utf-8')      
    sha1hash = hashlib.sha1()      
    sha1hash.update(password_utf)      
    password_hash = sha1hash.hexdigest()      
    window.Element('hash').Update(password_hash)      
