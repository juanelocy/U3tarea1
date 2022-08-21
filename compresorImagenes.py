'''
Programa para comprimir el peso de las imagenes
'''

from PIL import Image
import os


'''asginando a variables unas direcciones que se localizan en mi computador'''
carpetaDescargas = "/Users/CORE i3/Downloads/"
carpetaImagenes = "/Users/CORE i3/Pictures/"

if __name__ == "__main__":
    '''Estructura ciclica For'''
    for nombreArchivo in os.listdir(carpetaDescargas):
        '''apartando asignaciones para nombre y extension'''
        nombre, extension = os.path.splitext(carpetaDescargas + nombreArchivo)

        '''Condicion valida para formatos .jpg, .jpeg y .png'''
        if extension in [".jpg", ".jpeg", ".png"]:
            '''instanciacion con varibales en concatenacion'''
            imagen = Image.open(carpetaDescargas + nombreArchivo)
            '''Utilizando metodo save para añadir un nombre compresado_ al pricipio de cada imagen '''
            '''Con optimizacion de forma boolean y calidad de imagen 60'''
            imagen.save(carpetaImagenes + "compresado_"+nombreArchivo, optimize=True, quality=60)
            '''Utilizacion de metodo para eliminar las imagenes originales de la carpeta de descargas'''
            os.remove(carpetaDescargas + nombreArchivo)
            '''Impresion y muestra del nombre de las imgenes que se van comprimiendo'''
            print(nombre + ": " + extension)