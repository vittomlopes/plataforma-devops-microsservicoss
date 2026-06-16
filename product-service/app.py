from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/products")
def products():
    return jsonify([
        {
            "id": 1,
            "nome": "Calculo Numerico"
        }
    ])

@app.route("/user-info")
def user_info():
    try:
        response = requests.get("http://user-service:5000/users")
        return response.json()
    except:
        return {"erro": "user-service indisponivel"}

@app.route("/health")
def health():
    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
