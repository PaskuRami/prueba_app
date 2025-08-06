import sqlite3 as sql

def createDB():
    try:
        conn = sql.connect("database.db")
        conn.commit()
        conn.close()
        print(f"Base de datos creada")
    except sql.Error as e:
        print(f"Error al crear la base de datos: {e}")

def createTable():
    conn = sql.connect("database.db")
    cursor = conn.cursor()
    users_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        );"""
    roles_table = """
            CREATE TABLE IF NOT EXISTS roles(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                role_name TEXT UNIQUE NOT NULL);        
            """
    
    cursor.execute(users_table)
    cursor.execute(roles_table)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    #createDB()
    createTable()