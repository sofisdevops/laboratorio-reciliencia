
______

# Post-Mortem

## Captura de pantalla de Dozzle filtrando el evento de error de Gunicorn (WORKER TIMEOUT)

![alt text](image.png)
## Captura de pantalla del gráfico de latencia de Locust mostrando el momento del fallo.

![alt text](image-4.png)

![alt text](image-1.png)

## Identificación de la Síntoma

### ¿Qué código de estado HTTP devuelve Nginx (nginx-balanceador)?

#### Nos devuelve un 502 al ser un error de Bad Gateway, se debe a que la comunicacion entre nginxs y los contenedores se rompio

### ¿Qué mensaje de error exacto aparece en los logs del Backend (api-backend) cuando las peticiones empiezan a fallar?

#### Nos devuelve un error de timeout porque tenemos un limite de 3 segundos en el gunicorn y al programar un tiempo de espera de 4 segundos en el app.py, el tiempo sobrepasa el tiempo que estipulamos

## Diagnóstico de la Causa Raíz (Análisis SRE) Si el código Python no tiene ninguna sintaxis errónea ni lanza excepciones no capturadas (Tracebacks)

### ¿Por qué Gunicorn está matando los procesos trabajadores (Worker Timeout)?

#### Gunicorn mata los procesos porque la peticion tarda mas tiempo en responder que el limite que habiamos configurado en el parametro, por eso mismo el gunicorn lo toma como un proceso quebfue bloqueado o esta congelado y por eso lo reinicia

### ¿Qué relación existe entre la duración de la simulación (time.sleep(4)) y el parámetro -t 3 de Gunicorn?

#### Tambien pasa porque el endpoint ejecuta un time.sleep(4) pero  gunicorn tiene un timeout  de 3 segundos -t 3. Como la funcion se demora 4 segundos en hacerse, obviamente se va a superar el limite maximo de 3 segundos, causando que gunicorn aborte  antes de que la funcion se retorne en una  respuesta al cliente.

## Efecto Domino en la Arquitectura

### ¿Qué sucede con los 15 usuarios de Locust cuando las 2 réplicas de la API (cada una con solo 2 workers) se quedan sin hilos libres para atender peticiones entrantes?

#### Con solo 2 replicas con 2 workers cada una, el sistema solo podra procesar 4 peticiones, de esta forma si se ingresan 15 usuarios concurrentes, los 4 hilos que hay disponibles se congelan o se bloquean de inmediato por los 4 segundos del time.sleep(4), lo que sucede que las  peticiones restantes se quedan esperando alguna señal o ni siquiera se tomaran en cuenta, haciendo que se agote rapidamente toda la capacidad que le configuramos al sistema.

### ¿Cómo interpreta Nginx la falta de respuesta de los contenedores tras bambalinas?

#### El nginx intenta reenviar las peticiones que van entrando en las replicas del backend como los workers que hay en el gunicorn son eliminados por el timeout por el tiempo de respuesta, la conexion entre nginx y el backend se daña y se rompe haciendo que Nginx lo interprete como una falla del servidor y responde al cliente con  un error 502.

## Propuesta de Solución

### Primer cambio concreto en la configuración

#### Para evitar que nuestros sistemas no colapcen debemos tener en cuenta los tiempos de espera que nosotros configuramos, si en el codigo sobrepasamos estos tiempos, nuestra aplicacion nos va a fallar y para esto deberiamos aumentar el limite de tiempo en el gunicorn 

### Segundo cambio concreto en la configuración

#### Para evitar que nuestras replicas se queden sin hilos libres ante muchisimas solicitudes, deberiamos implementar una clase de trabajador asincrono en gunicorn.

______
