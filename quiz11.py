import requests

TOKEN = "BQDa9E3VfYmlUBClo1IAKicVKS8YFKU0PY2rCkivR1QTfVVePDLl5waFkSEaarIxwwvluu5a7W0qAECAuTDcGpObF1cDICVg_P0sztPRCkdfDmPWIQd_BeLvSMFHI8Mw0b8ECXKC1vLaRq6XRySIdMIt_2SPuP5ngGqMqFN6DozoOYjhFjVtmodJjr7"
def fetch_web_api(endpoint, method, body=None):
    url = f'https://api.spotify.com/{endpoint}'
    headers = {'Authorization': f'Bearer {TOKEN}'}
    response = requests.request(method, url, headers=headers, json=body)
    response.raise_for_status()
    return response.json()

def get_top_tracks():
    # Endpoint reference: https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
    response = fetch_web_api('v1/me/top/tracks?time_range=long_term&limit=5', 'GET')
    return response.get('items', [])