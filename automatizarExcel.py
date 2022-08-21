from openpyxl import Workbook
from openpyxl.styles import Font
import time 

book=Workbook()
hoja1=book.active

hoja1['A1']='Id'
hoja1['A1'].font=Font(color='FF0000', bold=True)
hoja1['B1']='Nombres'
hoja1['B1'].font=Font(color='FF0000', bold=True)
hoja1['C1']='Apellidos'
hoja1['C1'].font=Font(color='FF0000', bold=True)
hoja1['D1']='Numero de telefono'
hoja1.merge_cells('D1:E1')
hoja1['D1'].font=Font(color='FF0000', bold=True)
hoja1['F1']='Fecha'
fecha=time.strftime('%x')
hoja1['F2'] = fecha


hoja2=book.create_sheet('Hoja 2')
hoja2['A1']='Creacion de Segunda hoja'

book.save('ExcelDePrueba.xlsx')