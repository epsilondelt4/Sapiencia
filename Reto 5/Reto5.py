# CarlosAndresArbeláezAlzate,JuanFernandoHurtadoVasquez,AlejandroAlbertoMontesRamirez_Reto4.py
# Reto 4
# Calculadora científica
# Integrantes equipo: Tigres Naranjas
# Carlos Andres Arbeláez Alzate     
# Juan Fernando Hurtado Vasquez     
# Alejandro Alberto Montes Ramirez

from os import system
import math 
import statistics
import json


Menu={1:'Agregar',2:'Buscar ',3:'Modificar',4:'Cancelación de materia',5:'Resultados por estudiante', 6:'Salir'}



textMenu='Menu principal\n'   
for i in Menu:
    if i==0:
        textMenu=textMenu+Menu[i]+'\n'        
    else:
        textMenu=textMenu+str(i)+'.'+Menu[i]+'\n'
textMenu=textMenu+'Elija una opción: ' 


def menu():
    validarOpcion(textMenu,Menu)
    globals()[Menu[Opcion][0]+str(Opcion)]()

# Agregar: se debe pedir al usuario que ingrese todos los datos del estudiante 
# (se pueden crear todos los estudiantes que se quiera agregar).
def A1(): #Agregar estudiante
    datosAux={}
    identificacion=""
    with open('datosEstudiantes.json','r',encoding='utf-8') as file:
        # if json_validator('datosEstudiantes.json')==True:
        datosAux=json.load(file)
        print(datosAux)     
    identificacion=input('Ingrese el documento de identidad: ')
    datosAux[identificacion]=  {
    'Identificación':identificacion,
    'Nombre':input('Ingrese los nombres y apellidos del estudiante: ')
    # 'Correo':input('Ingrese el correo electrónico: '),
    # 'Teléfono':input('Ingrese el número de teléfono: '),
    # 'Fecha de nacimiento':input('Ingrese la fecha de nacimiento dd/mm/aaaa: '),
    # 'Nota 1':input('Ingrese la nota 1: '),
    # 'Nota 2':input('Ingrese la nota 2: '),
    # 'Nota 3':input('Ingrese la nota 3: '),
    # 'Nota 4':input('Ingrese la nota 4: ')
    }
    with open('datosEstudiantes.json','w',encoding='utf-8') as file:
        json.dump(datosAux,file,indent=4,ensure_ascii=False)
        
  
    
    

    

def validarOpcion(texto,dicc):
    global Opcion
    Opcion=''
    while(Opcion==''):
        try:
            Opcion = int(input(f'{texto}'))
            if 1 <=Opcion  and Opcion <= len(dicc):
                break
            else:
                Opcion=""
                system(f"cls")
                print(f'Error, introduce un número entero entre 1 y {len(dicc)}')
        except ValueError:
            system(f"cls")
            print(f'Error, introduce un número entero entre 1 y {len(dicc)}')
    return Opcion

def validarEntrada(varName):    
    valor=''
    while(valor==''):
        try:
            valor = float(input(f'Ingrese el valor de {varName}: '))
            break
        except ValueError:
            system(f"cls")
            print(f"Error, introduce un número")
    return valor

def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError: #as error:
        print(f'El archivo esta vacio') #invalid json: %s" % error)
        # print("invalid json: %s" % error)
        return False
menu()
# for i in Datos:
#     print(str(i)+':'+str(Datos[i]))
    
# for key, value in Datos.items():
#     print(key,':',value)

# for key in Datos.keys():
#     print(key,':',Datos[key][0])
