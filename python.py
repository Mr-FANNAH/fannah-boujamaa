from flask import Flask, jsonify, request
from geopy.geocoders import Nominatim

app = Flask(__name__)
geolocator = Nominatim(user_agent="geospatial_app")

@app.route('/')
def index():
    return 'Bienvenue sur l\'application web service géospatial !'

@app.route('/geocode', methods=['GET'])
def geocode():
    address = request.args.get('address')
    if not address:
        return jsonify({"error": "Adresse manquante"}), 400

    location = geolocator.geocode(address)
    if location:
        result = {
            "address URL ==>" : location.address,
            "latitude Y ==>": location.latitude,
            "longitude X ==>": location.longitude
        }
        return jsonify(result)
    else:
        return jsonify({"error": "Adresse non trouvée"}), 404

if __name__ == '__main__':
    app.run(debug=True)


 # http://localhost:5000/geocode?address=
