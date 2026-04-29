import sqlite3

def conectar():
    connect = sqlite3.connect('base_de_datos.db')
    connect.execute("PRAGMA foreign_keys = ON;")
    return connect

def inicializar_db():
    connect = conectar()
    cursor = connect.cursor()
    # 1. Tabla Equipo
    cursor.execute('''CREATE TABLE IF NOT EXISTS Equipo (
                        id_equipo INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        posicion TEXT,
                        liga TEXT)''')
    # 2. Tabla jugadores
    cursor.execute('''CREATE TABLE IF NOT EXISTS jugadores (
                        id_jugador INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        apellidos TEXT,
                        dorsal INTEGER,
                        goles INTEGER,
                        id_equipo INTEGER,
                        FOREIGN KEY(id_equipo) REFERENCES Equipo(id_equipo) ON DELETE CASCADE)''')
    # 3. Tabla trofeos
    cursor.execute('''CREATE TABLE IF NOT EXISTS trofeos (
                        id_trofeos INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        numero_de_trofeos INTEGER,
                        id_equipo INTEGER,
                        FOREIGN KEY(id_equipo) REFERENCES Equipo(id_equipo) ON DELETE CASCADE)''') 
   
    connect.commit()
    connect.close()
# Insertamos los datos iniciales de las tablas
def insertar_datos_iniciales():
    connect = conectar()
    cursor = connect.cursor()
    try:
        # Comprobamos si la tabla está vacía
        cursor.execute("SELECT COUNT(*) FROM Equipo")
        conteo = cursor.fetchone()[0]
        
        if conteo == 0:
            equipos = [(1, 'Barça', '1º', 'Española'), (2, 'Real Madrid', '2º', 'Española'), (3, 'PSG', '1º', 'Ligue 1')]
            cursor.executemany("INSERT INTO Equipo VALUES (?, ?, ?, ?)", equipos)
            
            jugadores = [(1, 'Pedri', 'Gonzalez', 8, 30, 1), (2, 'Vinicius', 'Junior', 7, 300, 2), (3, 'Fabian', 'Ruiz', 8, 115, 3)]
            cursor.executemany("INSERT INTO jugadores VALUES (?, ?, ?, ?, ?, ?)", jugadores)
            
            trofeos = [(1, 'Liga Española', 28, 2), (2, 'Champions', 15, 2), (3, 'Champions', 1, 3)]
            cursor.executemany("INSERT INTO trofeos VALUES (?, ?, ?, ?)", trofeos)
            
            connect.commit() # Guardamos los datos insertados
            print(">>> Datos del Real Madrid y otros equipos cargados.")
    except Exception as e:
        print(f"Error al insertar: {e}")
    finally:
        connect.close()
# Se leen los datos de las tablas para saber su contenido.
def leer_datos(tabla):
    connect = conectar()
    cursor = connect.cursor()
    try:
        cursor.execute(f"SELECT * FROM {tabla}")
        filas = cursor.fetchall()
        
        print(f"\n--- DATOS DE {tabla.upper()} ---")
        if not filas:
            print("No hay datos en esta tabla.")
        else:
            for fila in filas:
                print(" | ".join(map(str, fila)))
    finally:
        connect.close()

# --- OPERACIONES CRUD ---

def crear_jugador(nombre, apellidos, dorsal, goles, id_equipo):
    connect = conectar()
    connect.execute("INSERT INTO jugadores (nombre, apellidos, dorsal, goles, id_equipo) VALUES (?,?,?,?,?)", (nombre, apellidos, dorsal, goles, id_equipo))
    connect.commit()
    connect.close()
    print("Jugador guardado.")

def actualizar_goles(id_jugador, goles):
    connect = conectar()
    connect.execute("UPDATE jugadores SET goles = ? WHERE id_jugador = ?", (goles, id_jugador))
    connect.commit()
    connect.close()
    print("Goles actualizados.")

def eliminar_jugador(id_jugador):
    connect = conectar()
    connect.execute("DELETE FROM jugadores WHERE id_jugador = ?", (id_jugador,))
    connect.commit()
    connect.close()
    print("Jugador eliminado.")
    
# --- MENÚ ---

def menu():
    inicializar_db()
    insertar_datos_iniciales() # Nos aseguramos de que se mantengan los datos iniciales
    while True:
        print("\n=== TABLAS DE FÚTBOL ===")
        print("1. Ver Equipos\n2. Ver Jugadores\n3. Ver Trofeos\n4. Añadir Jugador\n5. Actualizar Goles\n6. Eliminar Jugador\n7. Salir")
        op = input("Selecciona: ")
        
        if op == "1": leer_datos("Equipo")
        elif op == "2": leer_datos("jugadores")
        elif op == "3": leer_datos("trofeos")
        elif op == "4":
            nombre = input("Nombre: "); apellidos = input("Apellidos: "); dorsal = int(input("Dorsal: ")); goles = int(input("Goles: ")); id_equipo = int(input("ID Equipo: "))
            crear_jugador(nombre, apellidos, dorsal, goles, id_equipo)
        elif op == "5":
            id_jugador = int(input("ID Jugador: ")); goles_nuevos = int(input("Nuevos goles: "))
            actualizar_goles(id_jugador, goles_nuevos)
        elif op == "6":
            id_jugador = int(input("ID Jugador: "))
            eliminar_jugador(id_jugador)
        elif op in ["7", "salir"]: break

if __name__=="__main__":
    menu()