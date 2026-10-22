import time
from flask import Flask, request

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK", 200

@app.route("/aplicar-descuento", methods=["POST"])
def aplicar_descuento():

# Simula cálculo pesado de validación de cupones
# Consume tiempo de CPU bloqueando el hilo de Gunicorn

    time.sleep(1.2)
    return {"status": "Descuento aplicado", "descuento": 15}, 200


# === codigo de clase ===

# from flask import Flask
# import time
# import request

# app = Flask(__name__)

# @app.route("/health")
# def health():
#     return "ok", 200

# @app.route("/version")
# def version():
#     return { "version": "2.0.0", "mensaje": "API v2 Operativa, peticion a la actualizacion" }, 200


# @app.route("/comprar", methods=["POST"])
# def procesar_compra():

#     try:

#         time.sleep(4)

#         return {"status": "Aprobado", "transaccion_id": 9942}, 200
    
#     except Exception as e:

#         app.logger.error(f"Fallo en pasarela de pagos: {str(e)}")

#         return {"error": "Servicio no disponible"}, 500