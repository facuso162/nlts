# NLTS - New Lines to Spaces

import pyperclip
from os import system

while True:
    system("cls")
    inputText = pyperclip.paste()
    resultText = inputText.replace("\r\n", " ")
    pyperclip.copy(resultText)
    print('Resultado\n\n', resultText)
    exit = input("\nPara transformar otro texto, toque cualquier tecla. Para salir ingrese e:\t")
    if (exit.upper() == 'E'):
        print('\nHasta la proxima!\n')
        break