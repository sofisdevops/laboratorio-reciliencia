from flask import Flask
import time

app = Flask(__name__)
@app.route('/navegador', methods=['GET'])
def navegador():
    return "Pagina de navegador", 200

@app.route('/comprador', methods=['POST'])
def comprador():
    time.sleep(2)
    
    return "Pagina del comprador", 200

if __name__ == '__main__':
    app.run(port=8089, debug=True)