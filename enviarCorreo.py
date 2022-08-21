'''
Programa para enviar correos a personas 
'''


'''Librerias'''
from email.message import EmailMessage
import ssl
import smtplib

'''Asignando datos'''
emisor="juanchoyasig@gmail.com"
contrasena="eurjhglhlcytrvcn"

'''Pedir datos de manera dinamica'''
receptor=input("Ingrese correo del receptor: ")
asunto = input("Ingrese el Asunto: ")
cuerpo= input("Ingrese informacion o descripcion: ")

'''Instanciamos un clase que viene dentro de una libreria'''
em=EmailMessage()
'''Funciones de EmailMessage que se estan asignado'''
'''Desde donde se envia o el emisor'''
em["From"]=emisor
'''Para quien va dirigido el correo'''
em["To"]=receptor
'''Tipo de descripcion que le quiera dar al destinatario'''
em["Subject"]=asunto
'''Funcion para cumplir un formato que tambien esta la descripcion del correo'''
em.set_content(cuerpo)

'''Seguridad de red'''
contexto=ssl.create_default_context()

'''Para tener una conexion segura mientras se esta realizando este proceso'''
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    '''Funcion Login para el ingreso de sesion del emisor'''
    smtp.login(emisor, contrasena)
    '''Funcion sendmail para enviar el mensaje'''
    smtp.sendmail(emisor,receptor,em.as_string())

'''Impresion por pantalla para saber si el correo se a enviado correctamente'''
print("Se envio el correo exitosamente")
