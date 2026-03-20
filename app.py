from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos simulada de autos (JDM Legends)
autos = [
    {"id": 1, "marca": "Nissan", "modelo": "Skyline GT-R R34", "tipo_combustible": "Gasolina", "precio_usd": 150000},
    {"id": 2, "marca": "Toyota", "modelo": "Supra MK4 (A80)", "tipo_combustible": "Gasolina", "precio_usd": 90000},
    {"id": 3, "marca": "Mazda", "modelo": "RX-7 FD", "tipo_combustible": "Gasolina", "precio_usd": 65000},
    {"id": 4, "marca": "Honda", "modelo": "NSX (NA1)", "tipo_combustible": "Gasolina", "precio_usd": 120000},
    {"id": 5, "marca": "Mitsubishi", "modelo": "Lancer Evolution IX", "tipo_combustible": "Gasolina", "precio_usd": 45000},
    {"id": 6, "marca": "Subaru", "modelo": "Impreza WRX STI 22B", "tipo_combustible": "Gasolina", "precio_usd": 300000}
]

@app.route('/')
def inicio():
    return jsonify({
        "mensaje": "Bienvenido a la API de Autos",
        "endpoints_disponibles": [
            "/autos (GET) - Lista todos los autos",
            "/autos/<id> (GET) - Obtiene un auto por su ID"
        ]
    })

@app.route('/autos', methods=['GET'])
def obtener_autos():
    return jsonify({
        "cantidad": len(autos),
        "autos": autos
    })

@app.route('/autos/<int:auto_id>', methods=['GET'])
def obtener_auto_por_id(auto_id):
    auto = next((a for a in autos if a["id"] == auto_id), None)
    if auto:
        return jsonify(auto)
    return jsonify({"error": "Auto no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
