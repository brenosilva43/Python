import os
import xlsxwriter
import datetime
from selenium import webdriver

# Open a file
path = "./breno"
dirs = os.listdir( path )


count=0
lista1 = []
lista2 = []
# This would print all the files and directories
for file in dirs:
    file = file.split('.')
    x = file[1]
    y = file[0]
    if x == 'pdf':
        lista1.append(x)
        lista2.append(y)
        count+=1


row=0
col=0
for i in lista2:

    workbook = xlsxwriter.Workbook('./breno/'+str(i)+'.xlsx')
    worksheet = workbook.add_worksheet()

    row=0

    worksheet.write_row(row, 0, ['Arquivo'])
    worksheet.write_row(row, 1, [i])


    row +=1

    worksheet.write_row(row, 0, ['Tecnico'])
    worksheet.write_row(row, 1, ['Operacional'])
    worksheet.write_row(row, 2, ['Negocio'])



    row+=1

    worksheet.write_row(row, 0, ['Tipo do Arquivo'])
    worksheet.write_row(row, 1, ['Separador CSV'])
    worksheet.write_row(row, 2, ['Data de Captura'])
    worksheet.write_row(row, 3, ['Fonte'])
    worksheet.write_row(row, 4, ['Classificação 5 estrelas'])
    worksheet.write_row(row, 5, ['Descrição'])
    worksheet.write_row(row, 6, ['Vertical'])

    row+=1

    worksheet.write_row(row,col,['pdf'])
    worksheet.write_row(row, col + 2, ['{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())])
    worksheet.write_row(row,col+3, ['Inserir Fonte'])
    worksheet.write_row(row,col+4,[1])
    worksheet.write_row(row, col + 5, ['Inserir Descricao'])
    worksheet.write_row(row, col + 6, ['Inserir Vertical'])



print(count)
print(lista1)
print(lista2)




#if file[1] == 'pdf':
 #   print('Todos sao pedf')





























