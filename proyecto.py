import sqlite3

conexion = sqlite3.connect("base_de_datos.db")
cursor = conexion.cursor()




def elige_una_opcion():
  while True:
    print("\n---Menu de CRUD---")
    print("1.Opción 1:Create")
    print("2.Opción 2:Read")
    print("3.Opción 3:Update")
    print("4.Opción 4:Delete")
    print("-----------------")

    elige_una_opcion=input("Que opcion quieres elegir: ")

    if elige_una_opcion=="1":
        create()
#Añado cambios
     

def create():
    
    print("Insertando datos, porfavor espere.")


    cursor.execute('''
    INSERT INTO Equipo (id_equipo, nombre, posicion, liga) VALUES (?,?,?,?)
    ''', (4, 'Betis', '5º', 'Española'))

    Equipo = [
    (1, 'Barça', '1º', 'Española'),
    (2, 'Real Madrid', '2º', 'Española'),
    (3, 'PSG', '1º', 'Ligue 1')
    ]
    cursor.executemany('''
    INSERT INTO Equipo (id_equipo, nombre, posicion, liga) VALUES (?,?,?,?)
    ''',Equipo)

    conexion.commit()
    conexion.close()                                       

elige_una_opcion()