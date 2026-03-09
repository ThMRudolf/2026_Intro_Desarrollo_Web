from pydantic import BaseModel
from typing import List

# Clase DTO (Data Transfer Object) para representar un
# objeto de Curso para cuando se van a mandar datos a 
# un endpoint.
class CursoDTO(BaseModel):
    nombre: str
    
    
class AlumnoDTO(BaseModel):
    nombre: str
    cursos_inscritos: List[str]


class ActualizarCursosAlumnoDTO(BaseModel):
    cursos_inscritos: List[str]