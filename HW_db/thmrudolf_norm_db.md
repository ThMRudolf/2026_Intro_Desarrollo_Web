# Normalización de bases de datos

## 1. Introducción

En clase hablamos sobre la normalización de bases de datos y vimos ejemplos donde una tabla mal organizada puede generar problemas. La idea central es: una base de datos no debe guardar información repetida sin necesidad, porque eso después causa errores, inconsistencias y consultas más difíciles de mantener.

El artículo de IBM explica la normalización como un proceso de diseño. No es solamente “separar tablas”. Es organizar los datos de forma lógica para que cada dato esté en el lugar correcto y se pueda relacionar con otros datos mediante claves primarias y claves foráneas.

En mi opinión, esto conecta directamente con lo visto en clase, porque trabajamos cómo las tablas se relacionan entre sí y por qué necesitamos claves para mantener ordenada la información.

------------------------------------------------------------------------

## 2. Ideas principales del artículo

El artículo resalta varios puntos importantes.

1.) La normalización ayuda a reducir la redundancia. Esto significa evitar que el mismo dato aparezca repetido en muchas partes de la base de datos. Por ejemplo, si en una tabla de alumnos guardo el nombre del estado en cada alumno, estoy repitiendo el mismo dato muchas veces. Es mejor tener una tabla separada de estados y relacionarla con los alumnos mediante una clave.

2.) La normalización mejora la integridad de los datos. Esto quiere decir que la información es más confiable. Si un dato se actualiza en un solo lugar, hay menos riesgo de que existan versiones diferentes del mismo dato.

3.) La normalización ayuda a evitar anomalías. El artículo menciona tres tipos importantes:

-   anomalías de inserción,
-   anomalías de actualización,
-   anomalías de eliminación.

Estas anomalías aparecen cuando una tabla está mal diseñada. Por ejemplo, si borro un registro y con eso pierdo información que todavía necesitaba, entonces el diseño de la tabla no era correcto.

4.) El artículo explica que existen formas normales. Las formas normales son reglas para organizar mejor las tablas. La primera forma normal busca evitar grupos repetidos o valores múltiples dentro de una sola celda. La segunda y tercera forma normal van más lejos y revisan si los atributos dependen correctamente de la clave.

## 3. Relación con lo visto en clase

En clase vimos que una base de datos relacional organiza la información en tablas. Cada tabla tiene filas y columnas. También vimos que una clave primaria identifica de forma única cada registro, mientras que una clave foránea permite relacionar una tabla con otra.

Esto es exactamente lo que se necesita para normalizar.

Por ejemplo, en la presentación vimos relaciones 1-1, 1-N y N-M. Estas relaciones ayudan a decidir cómo separar la información.

Una relación 1-N aparece cuando un registro de una tabla puede estar relacionado con muchos registros de otra. Por ejemplo:

-   un estado puede tener muchos alumnos,
-   una persona puede tener varios perros,
-   un cliente puede hacer muchos pedidos.

En estos casos, no conviene repetir toda la información del estado, persona o cliente en cada registro. Lo correcto es usar una clave foránea.

También vimos relaciones N-M, como alumnos y cursos. Un alumno puede estar inscrito en varios cursos y un curso puede tener varios alumnos. En este caso no es sufuciente con poner una clave foránea directa. Se necesita una tabla intermedia, por ejemplo `Inscripcion`.

Esto se relaciona claramente con la normalización porque la tabla intermedia evita guardar listas dentro de una celda o repetir columnas como `curso1`, `curso2`, `curso3`. Ese tipo de diseño es práctico al inicio, pero malo para una base de datos real.

------------------------------------------------------------------------

## 4. Ejemplo de una tabla mal diseñada

Supongamos que tenemos la siguiente tabla:

| alumno_id | alumno_nombre | curso_1        | curso_2 | profesor_1 | profesor_2 |
|-----------|---------------|----------------|---------|------------|------------|
| 1         | Ana López     | Bases de Datos | React   | Adrian     | Laura      |
| 2         | Carlos Pérez  | Bases de Datos | Python  | Adrian     | Mario      |

Esta tabla tiene varios problemas.

1.) hay columnas repetidas: `curso_1`, `curso_2`, `profesor_1`, `profesor_2`. Eso no es un buen diseño. ¿Qué pasa si un alumno toma tres cursos? ¿Agregamos `curso_3`? ¿Y si toma siete? La tabla no escala.

2.) Se repite información. El curso “Bases de Datos” aparece varias veces, igual que el profesor “Adrian”. Si después cambia el nombre del curso o se quiere corregir el nombre del profesor, habría que modificar muchas filas.

3.) Se mezclan varias entidades en una sola tabla: alumnos, cursos y profesores. Eso hace que la tabla sea más difícil de mantener.

------------------------------------------------------------------------

## 5. Propuesta de normalización

Una mejor opción sería separar la información en varias tablas.

### Tabla `Alumno`

| alumno_id | nombre       |
|-----------|--------------|
| 1         | Ana López    |
| 2         | Carlos Pérez |

### Tabla `Profesor`

| profesor_id | nombre |
|-------------|--------|
| 1           | Adrian |
| 2           | Laura  |
| 3           | Mario  |

### Tabla `Curso`

| curso_id | nombre         | profesor_id |
|----------|----------------|-------------|
| 1        | Bases de Datos | 1           |
| 2        | React          | 2           |
| 3        | Python         | 3           |

### Tabla `Inscripcion`

| alumno_id | curso_id |
|-----------|----------|
| 1         | 1        |
| 1         | 2        |
| 2         | 1        |
| 2         | 3        |

Con este diseño, cada tabla tiene una función clara.

La tabla `Alumno` guarda alumnos.\
La tabla `Profesor` guarda profesores.\
La tabla `Curso` guarda cursos.\
La tabla `Inscripcion` conecta alumnos con cursos.

Este diseño es más limpio. También permite hacer consultas con `JOIN` para volver a juntar la información cuando sea necesario. Es decir, separar la información no significa perderla. Significa organizarla mejor.

------------------------------------------------------------------------

## 6. Reflexión crítica

La normalización es útil porque ordena la información, reduce errores y hace que la base de datos sea más consistente. También obliga a pensar mejor el diseño antes de empezar a guardar datos.

Pero tampoco hay que verla como una receta automática. Normalizar demasiado puede hacer que una base de datos tenga muchas tablas y que las consultas sean más complejas. En algunos casos se necesitan muchos `JOINs`, y eso puede afectar el rendimiento si no se diseña bien.

Por eso, la normalización no debe aplicarse de forma mecánica. Hay que entender el problema. La pregunta correcta no es “¿cuántas tablas puedo crear?”, sino “¿qué información pertenece realmente junta y qué información debe separarse?”.

En resumen, normalizar significa diseñar con orden. Una base de datos bien normalizada no solamente guarda datos. También evita problemas futuros.

------------------------------------------------------------------------

## 8. Conclusión

El artículo de IBM complementa bien lo visto en clase. IBM explica la lógica general de la normalización: reducir redundancia, evitar anomalías y mejorar la integridad de los datos. En clase vimos las herramientas prácticas para lograrlo: tablas, claves primarias, claves foráneas, relaciones entre tablas y `JOINs`.

La idea principal que me queda es esta: una base de datos bien diseñada no depende de meter todo en una sola tabla. Depende de separar correctamente la información y relacionarla de forma clara.

Normalizar no es complicar por complicar. Es poner orden antes de que el desorden se vuelva un problema.
