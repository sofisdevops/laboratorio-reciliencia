
______

# Respuesta de preguntas (Ejercicio 2)

## Diagnostico de la reaccion en cadena (Cascading Failure)

### ¿Por qué el healthcheck de Docker empieza a fallar si la ruta /health solo hace un return "OK" instantáneo?

#### 

## Bucle Infinito

### Cuando la Réplica 1 se marca como unhealthy y se reinicia, ¿qué ocurre con el tráfico que estaba atendiendo? ¿A dónde lo envía Nginx?

####

### ¿Por qué el reinicio de una réplica provoca que las 3 réplicas sobrevivientes se caigan inmediatamente después?

####

## Propuesta de Solución Lógica (Sin aumentar CPU a la máquina)

### ¿Qué parámetro o tipo de trabajador (worker class) permitiría atender peticiones lentas de E/S o tiempo de espera sin bloquear el hilo principal del healthcheck?

####

### Reconfiguren interval, timeout y retries en el docker-compose.yml de forma coherente con el tiempo de respuesta real de la aplicación.

______

