from flask import Flask, render_template, request
import requests

API_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/"

# You should keep your API key a secret (I'm keeping it here so you can run this app)
key = 'Y1lMPcQPvKhNs9dGdGOyPIrt680ohwBG'

app = Flask(__name__)


# Define seperate function to get lat and lng
def get_coords(address):

    # MAKE GET REQUEST
    res = requests.get(f"{API_BASE_URL}/address",
                       params={'key': key, 'location':  address})

    # GET DATA
    data = res.json()

    # RETIEVE WANTED INFORMATION
    lat = data["results"][0]['locations'][0]['latLng']['lat']
    lng = data["results"][0]['locations'][0]['latLng']['lng']
    coords = {'lat': lat, 'lng': lng}

    return coords


@app.route('/')
def show_address_form():
    return render_template("address_form.html")


@app.route('/geocode')
def get_location():
    address = request.args["address"]
    coords = get_coords(address)
    return render_template('address_form.html', coords=coords)
