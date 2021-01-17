<https://www.pedco.uncoma.edu.ar/enrol/index.php?id=2052>

discord

opcion 0: crear un canal por cuatrimestre con subchat de cada materia.
    - muchos canales con pocas materias.
    - el usuario tiene que navegar entre los canales.

opción 1: crear un canal por año con subchat de cada materia, dividido por cuatrimestre (categoría).

opción 2: crear un canal por año con subchat de cada materia

telegram

opción 0: enviarle a cada chat (por cada estudiante).
    - sobrecarga de envio

opción 1: armar canales para cada materia +100.
    - satura al estudiante con muchos canales.

opción 2: armar canales para cada cuatrimestre (anterior/4 aprox).
    - el estudiante va a recibir notificaciones que no le interesa.
    - pseudo-solución: buscador de telgram por palabra clave.

opción 3: armar canales para cada año (>15 canales).
    - el estudiante va a recibir notificaciones que no le interesa.

# FUNCIONAMIENTO BASICO

```
- logearse
- recorrer y notificar
    - recorrer pagina de materia
    - filtrar novedades
    - notificar telegram y discord de materia
- dormir una hora y repetir

- actualizar usuarios relevantes (profesores, tutores, etc.). debe realizarse cada cierto tiempo.
```

# LOGEARSE
requerimiento:
    - usuario (válido)
    - contraseña
    - url-login

# RECORRER PAGINA DE MATERIA
requerimiento previo:
    - estar logeado
requerimiento:
    - url de la materia
descripción:
    - recolectar todas las url

# FILTRAR NOVEDADES
requerimiento:
    - url recolectas
    - url guardadas
descripción:
    - compara con las guardadas quedandose con las no guardadas (url novedaes)
    - las identifica y las envia.

# NOTIFICACIÓN
- requerimientos
    - mensaje
    -
