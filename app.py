from flask import Flask
import time
import requests

app = Flask(__name__)

@app.route("/comprar", methods=["POST"])
def procesar_compra():

    try:

        time.sleep(4)

        return {"status": "Aprobado", "transaccion_id": 9942}, 200
    
    except Exception as e:

        app.logger.error(f"Fallo en pasarela de pagos: {str(e)}")

        return {"error": "Servicio no disponible"}, 500