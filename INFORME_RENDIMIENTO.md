
## TABLA COMPARATIVA DE RESULTADOS

| Fase | Servidor / Arquitectura | Límite CPU | Usuarios Concurrentes | RPS Logrados | Latencia P95 (ms) | % Errores |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Fase 1** | Flask Dev (app.run) | 0.20 Cores | 50 | | | |
| **Fase 2** | Gunicorn (4 workers) | 0.20 Cores | 100 | | | |
| **Fase 3** | Nginx + 3 Réplicas | 0.20 c/u | 150 | | | |

## CAPTURA DE PANTALLA

## ANALISIS TECNICO
###¿Por qué un servidor multiproceso con balanceador de carga logra responder más tráfico usando las mismas restricciones de hardware que un servidor uniproceso?
