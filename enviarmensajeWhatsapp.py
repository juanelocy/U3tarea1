'''
Programa para enviar mensajes a travez de la plataforma Whatsapp Web
--------------
funcionalidad:
    Enviar mensajes por Whatsapp introduciendo el numero de la persona con el codigo de cada pais
'''

import pyautogui as pg, webbrowser as web , time as tn

'''Ingreso o pedir datos de manera dinamica'''
numeroTelefono=input("Ingrese el numero de telefono: ")
mensaje=input("Ingrese el mensaje: ")
'''Funcion que permite abrir en el navegador predeterminado el Whatsapp Web agregando el numero de telefono'''
web.open("https://web.whatsapp.com/send?phone=+" + numeroTelefono)
'''Funcion sleep que funciona como tiempo para enviar el mensaje o un delay mejor dicho'''
tn.sleep(8)
'''Funcion write que permite escribir el mensaje o lo que uno quiera mandar hacia el destinatario'''
pg.write(mensaje)
'''Funcion press para darle enter o enviar el mensaje sin necesidad de que el usuario le de enter'''
pg.press("enter")


'''
El siguiente codigo es para enviar mensajes de manera ciclica
dentro del range se pone la cantidad de mensaje que se decea enviar
'''
'''for i in range(500):
    pg.write(mensaje)
    pg.press("enter")
    pass'''