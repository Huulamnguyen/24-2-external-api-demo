import requests

term = "Madonna"

# GET REQUEST
res = requests.get(
    'https://itunes.apple.com/search', params={'term': term, 'limit': 5})

# Retrieve data from the GET request, convert data dictionary to JSON format
data = res.json()

for result in data['results']:
    print("Track Name:", result['trackName'])
    print("Collection Name:", result['collectionName'])


data = {
    'username': 'chickenz',
    'tweets': [
        'hello!', 'goodbye!', 'bock bock!', {
            'id': 1,  'text': 'my first tweet!'}
    ]
}
# MOST COMMON FORMAT IS JSON
requests.post('https://en27bnye2btkl.x.pipedream.net', json=data)
