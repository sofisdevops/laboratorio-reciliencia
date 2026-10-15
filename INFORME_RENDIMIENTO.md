
## TABLA COMPARATIVA DE RESULTADOS

| **Fase** | **Servidor** / **Arquitectura** | **Límite CPU** | **Usuarios Concurrentes** | **RPS Logrados** | **Latencia P95** (ms) | % **Failures** |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Fase 1** | Flask Dev (app.run) | 0.20 Cores | 50 | 32.9 | 10 | 100% |
| **Fase 2** | Gunicorn (4 workers) | 0.20 Cores | 50 | 3.3 | 19000 | 0% |
| **Fase 3** | Nginx + 3 Réplicas | 0.20 c/u | 150 | 6.1 | 82000 | 4% |

## CAPTURA DE PANTALLA

![alt text](image.png)

## ANALISIS TECNICO

En nuestras pruebas de laboratorio nos dimos cuenta de que el servidor uniproceso de Flask (app.run) de la Fase 1 colapsa por completo con un 100% de fallos al recibir 50 usuarios concurrentes bajo el apretado límite de 0.20 Cores. En cambio, cuando implementamos una arquitectura multiproceso con **Gunicorn** o un sistema con **Nginx** y réplicas (como en la Fase 3), logramos manejar mucha más concurrencia —llegando a soportar hasta 150 usuarios— porque las peticiones ya no se quedan atrapadas en una sola fila esperando a que un único hilo procese todo secuencialmente.   

Esto sucede técnicamente porque el balanceador de carga y los múltiples workers reparten las solicitudes de manera distribuida entre varios procesos independientes. Así, a pesar de tener exactamente las mismas restricciones físicas de hardware, la CPU se aprovecha mejor y se evita el bloqueo total: si una petición se demora o satura un proceso, los demás siguen respondiendo tráfico, logrando una resiliencia muy superior y evitando el desastre del 100% de errores que tuvimos en el servidor de desarrollo. 

========
