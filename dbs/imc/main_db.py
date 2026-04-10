# API fon fastapi para calcular el IMC (Índice de Masa Corporal)
from fastapi import FastAPI
from models import Persona
import sqlite3
app = FastAPI()


# new fucntion to create the database and the table
def crear_base_datos():
    conn = sqlite3.connect('fitnessDB.db')
    cursor = conn.cursor()
    
    # IF NOT EXISTS
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            peso REAL NOT NULL,
            talla REAL NOT NULL, 
            imc REAL NOT NULL
        );
    ''')
    
    conn.commit()
    conn.close()



@app.post("/calculate_imc/")
def calculate_imc(person: Persona):
    # Calcular el IMC
    imc = person.peso / (person.talla ** 2)
    conn = sqlite3.connect('fitnessDB.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO personas (nombre, peso, talla, imc)
        VALUES (?, ?, ?, ?);
    ''', (person.nombre, person.peso, person.talla, imc))
    
    conn.commit()
    conn.close()

@app.get("/get_persona/{id_persona}")
def get_persona(id_persona: int):
    conn = sqlite3.connect('fitnessDB.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM personas WHERE id = ?', (id_persona,))
    persona = cursor.fetchone()

    conn.close()
    if persona:
        return {"id": persona[0], "nombre": persona[1], "peso": persona[2], "talla": persona[3], "imc": persona[4]}
    else:
        return {"error": "Persona no encontrada"}

@app.get("/get_all_personas/")
def get_all_personas():
    conn = sqlite3.connect('fitnessDB.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM personas')
    personas = cursor.fetchall()
    
    conn.close()
    return personas


@app.put("/update_persona/{id_persona}")
def update_persona(id_persona: int, person: Persona):
    conn = sqlite3.connect('fitnessDB.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM personas WHERE id = ?', (id_persona,))
    imc = person.peso / (person.talla ** 2)
    persona = cursor.fetchone()
    if persona:
        cursor.execute('UPDATE personas SET nombre = ?, peso = ?, talla = ?, imc = ? WHERE id = ?', 
                       (person.nombre, person.peso, person.talla, imc, id_persona))
        conn.commit()
        conn.close()
        return {"message": "Persona actualizada"}
    else:
        return {"error": "Persona no encontrada"}
    
@app.delete("/delete_persona/{id_persona}")
def delete_persona(id_persona: int):
    # Eliminar la información de una persona por su ID
    conn = sqlite3.connect('fitnessDB.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM personas WHERE id = ?', (id_persona,))
    res = cursor.fetchone()
    conn.commit()
    conn.close()
    print(res)
    if res is None:
        return {"message": "Persona eliminada"}
    else:
        return {"error": "Persona no encontrada"}       

crear_base_datos()