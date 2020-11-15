import requests


# IMPORTANT: SHOULD KEEP API KEY SECRETLY FROM THE FILE WHEN API REQUIRES CREDIT CARD
key = 'Y1lMPcQPvKhNs9dGdGOyPIrt680ohwBG'

response = requests.get('http://open.mapquestapi.com/geocoding/v1/address',
                        params={'key': key, 'location': '115 atlantic ave hempstead ny 11550'})
