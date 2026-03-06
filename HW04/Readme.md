**sessionStorage** es una API de almacenamiento web nativa de JavaScript que permite guardar pares clave-valor en el navegador, accesibles solo mientras la pestaña o ventana siga abierta. Los datos sobreviven a recargas, pero se eliminan al cerrar la pestaña. Es ideal para datos temporales de sesión (<https://ed.team/blog/que-es-y-como-utilizar-localstorage-y-sessionstorage>).

**Métodos Principales**:

*Guardar/Actualizar*: sessionStorage.setItem('clave', 'valor').

*Recuperar*: sessionStorage.getItem('clave').

*Eliminar*: sessionStorage.removeItem('clave').

*Lim*

*piar todo*: sessionStorage.clear()

Los datos en sessionStorage siempre se guardan como cadenas de texto (strings) (<https://mosaic.uoc.edu/2014/02/11/web-storage/#>:\~:text=Un%20detalle%20que%20hay%20que%20tener%20en,contenido%20a%20almacenar%20no%20sea%20de%20texto.). \|Feature \|LocalStorage \| SessionStorage \|Lifetime \| Permanent until cleared \| Clears on tab close \|Scope \|Across browser tabs \|Only same tab\| \|Size \|5–10 MB \|About 5 MB\|

| Feature  | LocalStorage            | SessionStorage      |
|----------|-------------------------|---------------------|
| Lifetime | Permanent until cleared | Clears on tab close |
| Scope    | Across browser tabs     | Only same tab       |
| Size     | 5–10 MB                 | About 5 MB          |
