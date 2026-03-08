from fastapi import FastAPI
from utils import generar_guid
from models import CursoDTO, AlumnoDTO, ActualizarCursosAlumnoDTO   

app = FastAPI()


# Diccionario para almacenar los cursos en memoria,
# con el id del curso como clave y el objeto con el
# ID y el nombre del curso como valor.
#
# Ejemplo de cómo se vería el diccionario de cursos en memoria:
#
# [ 
#   "3b060499-60f7-45f2-96b9-87a59e0fcdb6": {
#     "id": "3b060499-60f7-45f2-96b9-87a59e0fcdb6",
#     "nombre": "Introducción a Python"
#   },
#   "d9c8e5a1-2b3f-4c6a-9e7d-8f1a2b3c4d5e": {
#     "id": "d9c8e5a1-2b3f-4c6a-9e7d-8f1a2b3c4d5e",
#     "nombre": "Introducción a JavaScript"
#   }
# ]
#
cursos_en_memoria = {} 
alumnos_en_memoria = {}
# Ahora el de alumnos con un diccionario igual, pero ahora va a tener un arreglo
# de cursos inscritos, por ejemplo:
#
# alumnos_en_memoria = {
#   "a1b2c3d4-e5f6-7g89-0a1b-2c3d4e5f6g7": {
#     "id": "a1b2c3d4-e5f6-7g89-0a1b-2c3d4e5f6g7",
#     "nombre": "Fabián",
#     "cursos_inscritos": [
#       "3b060499-60f7-45f2-96b9-87a59e0fcdb6",
#       "d9c8e5a1-2b3f-4c6a-9e7d-8f1a2b3c4d5e"
#     ]
#   },
#   "h1i2j3k4-l5m6-7n89-0o1p-2q3r4s5t6u7": {
#     "id": "h1i2j3k4-l5m6-7n89-0o1p-2q3r4s5t6u7",
#     "nombre": "Samuel",
#     "cursos_inscritos": [
#       "3b060499-60f7-45f2-96b9-87a59e0fcdb6"
#     ]
#   }
# }

###########################################
#                 Cursos                 #
###########################################

@app.post("/v1/curso")
def crear_curso(curso: CursoDTO):
    id_generado = generar_guid()
    cursos_en_memoria[id_generado] = {"id": id_generado, "nombre": curso.nombre}
    return cursos_en_memoria[id_generado]


@app.get("/v1/curso")
def get_cursos():
    n_cursos = len(cursos_en_memoria)
    return list(cursos_en_memoria.values())  

@app.get("/v1/curso/{id_curso}")
def get_curso(id_curso: str):
    if id_curso in cursos_en_memoria:
        return cursos_en_memoria[id_curso]
    else:
        return {"error": "Curso no encontrado"}
###########################################
#                 Alumnos                 #
###########################################

@app.post("/v1/alumno")
def crear_alumno(nombre_alumno: str, cursos_inscritos: list[str]):
    id_generado = generar_guid()
    alumnos_en_memoria[id_generado] = {"id": id_generado,
                                       "nombre": nombre_alumno,
                                       "cursos_inscritos": cursos_inscritos}
    return alumnos_en_memoria[id_generado]


@app.get("/v1/alumno")
def get_all_alumnos(alumno: AlumnoDTO):
    id_generado = generar_guid()
    alumnos_en_memoria[id_generado] = {"id": id_generado,
                                       "nombre": alumno.nombre,
                                       "cursos_inscritos": alumno.cursos_inscritos}
    return alumnos_en_memoria[id_generado]
    
    
@app.get("/v1/alumno/{id_alumno}")
def get_alumno(id_alumno: str):
    if id_alumno in alumnos_en_memoria:
        return alumnos_en_memoria[id_alumno]
    else:
        return {"error": "Alumno no encontrado"}    
@app.get("/v1/alumnos")
def get_alumnos():
    n_alumnos = len(alumnos_en_memoria)
    return list(alumnos_en_memoria.values())
    
@app.patch("/v1/alumno/{id_alumno}")
def inscribir_alumno(id_alumno: str, id_curso: str):
    alumno = alumnos_en_memoria.get(id_alumno)
    if alumno:
        if id_curso in cursos_en_memoria:
            if id_curso not in alumno["cursos_inscritos"]:
                alumno["cursos_inscritos"].append(id_curso)
                return {"message": "Alumno inscrito al curso exitosamente"}
            else:
                return {"error": "Alumno ya está inscrito en este curso"}
        else:
            return {"error": "Curso no encontrado"}
    else:
        return {"error": "Alumno no encontrado"}