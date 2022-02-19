# datosEstudiantes=   {
#   "23456789": {
#     "Identificacion": 23456789,
#     "Nombre": "Carlos Andres Arbelaez Alzate",
#     "Correo": "carlos@udea.edu.co",
#     "Telefono": 604987654321,
#     "Fecha de nacimiento": "01/01/1900",
#     "Nota 1": 3.2,
#     "Nota 2": 5,
#     "Nota 3": 2.9,
#     "Nota 4": 4
#   },
#   "159753346": {
#     "Identificacion": 159753346,
#     "Nombre": "Alejandro Alberto Montes Ramirez",
#     "Correo": "alejandro@udea.edu.co",
#     "Telefono": 604987654323,
#     "Fecha de nacimiento": "01/01/1901",
#     "Nota 1": 4,
#     "Nota 2": 3.3,
#     "Nota 3": 2.8,
#     "Nota 4": 3.5
#   },
#   "852741963": {
#     "Identificacion": 852741963,
#     "Nombre": "Juan Fernando Hurtado Vasquez",
#     "Correo": "juan@udea.edu.co",
#     "Telefono": 604987654322,
#     "Fecha de nacimiento": "01/01/1901",
#     "Nota 1": 4.5,
#     "Nota 2": 3.1,
#     "Nota 3": 2.5,
#     "Nota 4": 3.8
#   }
# }

    # nombres=input('Ingrese los nombres y apellidos del estudiante: ')
    # correo=input('Ingrese el correo electrónico: ')
    # telefono=input('Ingrese el número de teléfono: ')
    # fechaDeNacimiento=input('Ingrese la fecha de nacimiento dd/mm/aaaa: ')
    # nota1=input('Ingrese la nota 1: ')
    # nota2=input('Ingrese la nota 2: ')
    # nota3=input('Ingrese la nota 3: ')
    # nota4=input('Ingrese la nota 4: ')
# import json
# dicc={}
# with open('data.json','r',encoding='utf-8') as file:
#     dicc=json.load(file)
# print(dicc)
# with open('data.json','w',encoding='utf-8') as file:
#     json.dump(dicc,file,indent=4,ensure_ascii=False)
    
dicc={
    "456": {
        "Identificación": "456",
        "Nombre": "4569"
    },
    "789456": {
        "Identificación": "789456",
        "Nombre": "loko"
    },
    "49563": {
        "Identificación": "49563",
        "Nombre": "78lo"
    }
}
for i,j in dicc.items():
    print(i,j)