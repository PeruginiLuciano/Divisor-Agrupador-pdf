#Creado por el ing. Luciano Perugini


#Todas estas Librerias vas a necesitar descargarlas o por lo menos la mayoria, podes hacerlo con el comando PIP
from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import time
import shutil
import PyPDF2
from datetime import datetime
#Te defini la fecha y la hora actual, nunbca viene mal, capaz la queres usar para algo y ya la tenes guardada.
FECHA= datetime.today().strftime('%d-%h-%Y')
Hora=time.strftime("%H:%M:%S")


#En la siguiente linea creo algunas rutas donde tengo mis pdf, vos tenes que cambiar las rutas hasta la /0000hoja1.pdf, eso lo tenes que dejar.
#Si creas 3 carpetas en el escritorio podes llamarlas carpeta1 ,2 y 3 y lo unico que vas a tener que cambiar es la ruta hasta ahi,
Carpeta1="C:/Users/Fabio/Desktop/carpeta1/0000Hoja1.pdf"
Carpeta2="C:/Users/Fabio/Desktop/carpeta2/0000Hoja1.pdf"
#En este caso lo mismo cambias todo menos la parte de /PdfFinal.pdf
#Algo importante cuando copies las turas la barra te va a salir al revez es decir \  pero vos las tenes que remplazar por /
final2="C:/Users/Fabio/Desktop/carpeta2/PdfFinal.pdf"
final3="C:/Users/Fabio/Desktop/carpeta3/PdfFinal.pdf"

#Esta funcion es la encargada de unir los pdf cuuando ya esten todos en la carpeta 2
def unirPdf():
    #el siguiente comando se para en la ruta especificada es decir arranca ahi
    os.chdir("C:/Users/Fabio/Desktop/carpeta2")
    i=0
    #el for recorre todos los archivos que hay en el directorio donde estamos parado
    for file in os.listdir():
        #El if es para guardar los 3 pdf en diferentes archivos pdf1, pdf2, pdf3
        if i==0:
            pdf1=open(file,"rb")
        elif i == 1:
            pdf2=open(file,"rb")
        elif i ==2 :
            pdf3=open(file,"rb")
        else:
            print("Listo")
        i=i+1
    #Lo vamos a usar para crear un unico pdf Final
    merger=PyPDF2.PdfFileMerger()
    
    merger.append(pdf1)
    merger.append(pdf2)
    merger.append(pdf3)
    #Se crea el pdf final
    with open("PdfFinal.pdf","wb") as PdfFinal:
        merger.write(PdfFinal)
    pdf1.close()
#Esta funcion es para dividir el primer pdf y sacarle la primera Hoja
def divisor (doc_name):
    #Aca lo lee
    pdf_leido=PdfFileReader(open(doc_name,'rb'))
    
    
    pdf_leidos=PdfFileWriter()
   
    pdf_leidos=PdfFileWriter()
    #Extrae la primer hoja por eso el indice 0
    pdf_leidos.addPage(pdf_leido.getPage(0))
        
        
    #Crea este pdf nuevo con una sola Hoja y le pone de nombre 0000Hoja1, esos 0000 son para que lo tome como la primera hoja del pdf final, ya que lo hace por orden alfabetico
    with open("0000Hoja1"+".pdf",'wb') as file1:
        pdf_leidos.write(file1)
    #Mueve la 0000Hoja1 a la carpeta 2
    shutil.move(Carpeta1,Carpeta2)


#---------Programa Principal---------------
#Abre el directorio en la carpeta1    
os.chdir("C:/Users/Fabio/Desktop/carpeta1")
#Lee todos los archivos que hay, que deberian ser uno solo, el que le vamos a sacar la primer hoja
for file in os.listdir():
    #Lo guarda en la variable scr
    scr=file
    #Llama a la funcion divisor y envia como parametro el archivo pdf
    divisor(scr)
    #Le damos 3 segundos por las dudas
    time.sleep(3)
    #Avisa que termino
    print("Fin")

#Llama a la funcion que une los pdf
unirPdf()
#Le damos 2 segundos
time.sleep(2)
#Mueve el pdf final de la carpeta 2 a la carpeta 3
shutil.move(final2,final3)
#Le damos 3 segundos
time.sleep(3)
#Elimina la 0000Hoja1 que creo 
os.remove("C:/Users/Fabio/Desktop/carpeta2/0000Hoja1.pdf")
#Avisa que es un exito
print("Salio bien")
