---
editor_options: 
  markdown: 
    wrap: 72
---

# Bases de Datos – Preguntas y Respuestas

## 1. ¿Qué es una transacción? ¿Para qué se usan?

Una transacción es un conjunto de operaciones que se ejecutan como una
unidad lógica.

Objetivo: - Garantizar consistencia de datos

Propiedades (ACID): - Atomicidad: todo o nada - Consistencia: datos
válidos - Aislamiento: sin interferencias - Durabilidad: persistencia
después de COMMIT

Uso: - Operaciones críticas (ej. transferencias)

Comandos: - BEGIN - COMMIT - ROLLBACK

## 2. ¿Cómo puedo evitar que el comando para crear una tabla no falle si es que la tabla ya está creada?

Uso de condición:

sql CREATE TABLE IF NOT EXISTS nombre_tabla (...);

Efecto: No error si la tabla ya existe

Nota: No valida cambios en estructura

## 3. ¿Qué es un trigger o disparador? Da dos ejemplos de cuándo es bueno usarlos.

Un trigger es una acción automática ejecutada por la base de datos ante
un evento.

Eventos típicos: INSERT UPDATE DELETE

Ejemplo 1: Auditoría (registro de cambios)

Ejemplo 2: Validación de datos antes de insertar

Observación: Lógica oculta en la base de datos Puede afectar rendimiento

## 4. ¿Qué es SQL Injection? ¿Qué implicaciones tiene? Busca 3 noticias de talla mundial relacionadas con esto.

Definición:

Inserción de código SQL malicioso mediante inputs

Causa:

Concatenación directa de strings en queries

Implicaciones:

Acceso no autorizado Modificación de datos Eliminación de información
Compromiso del sistema

Casos reales:

TalkTalk (2015): filtración de datos de clientes Sony Pictures (2014):
acceso a información interna Heartland Payment Systems (2008): robo
masivo de tarjetas

Prevención:

Queries parametrizadas Validación de inputs

## 5. ¿Qué es un ORM y qué diferencias existen con escribir sentencias de SQL comunes?

Definición: ORM = Object-Relational Mapping Mapea tablas a objetos

*Diferencias:*

ORM: Alta abstracción Menos control Desarrollo más rápido

SQL: Control total Mejor optimización Mayor complejidad

Observación: ORM no reemplaza SQL Uso combinado recomendado
