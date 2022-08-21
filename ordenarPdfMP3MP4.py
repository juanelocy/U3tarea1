'''
ejercicio para ordenar archivos o mover de un lugar a otro de formato .pdf
tambien puede ser .mp3 o .mp4, tambien .docx
Se pueden distintos tipos de documentos 
'''


import os

'''Asignando una direccion de mi ordenador '''
carpetaDescargas = "/Users/CORE i3/Downloads/"

if __name__ == "__main__":
    '''Estructura ciclica con funcion de listdir'''
    for nombreArchivo in os.listdir(carpetaDescargas):
        '''apartando asignaciones para nombre y extension'''
        nombre, extension = os.path.splitext(carpetaDescargas + nombreArchivo)
        
        '''Estrucura if que cumple con buscar todos los archivos con formato .pdf'''
        if extension in [".pdf"]:
            '''Asignando una direccion de mi ordenador a una variable'''
            musicFolder = "/Users/CORE i3/PDFs/"
            '''Llamando a una funcion rename para renombrar a los archivos movidos'''
            os.rename(carpetaDescargas + nombreArchivo, musicFolder + nombreArchivo)
            '''Imprimiendo el nombre de los archivos ya movidos'''
            print(nombre + ": " + extension)