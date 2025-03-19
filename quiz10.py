#https://github.com/public-apis/public-apis?tab=readme-ov-file
#access a public api using request. present the data to the users
import requests


# Spotify API credentials - REPLACE WITH YOUR OWN
#Ang TOKEN ay parang ID na nagpapatunay na ikaw ay may karapatang humingi ng datos
TOKEN = 'BQDa9E3VfYmlUBClo1IAKicVKS8YFKU0PY2rCkivR1QTfVVePDLl5waFkSEaarIxwwvluu5a7W0qAECAuTDcGpObF1cDICVg_P0sztPRCkdfDmPWIQd_BeLvSMFHI8Mw0b8ECXKC1vLaRq6XRySIdMIt_2SPuP5ngGqMqFN6DozoOYjhFjVtmodJjr7-JHPryoMpp-Jy5z5gLFIffySCbibzOedGUwrk2u5UbtLSw-WvR1aAcFAEvQJjK3ii4fPRv1sDXwQvaeupQvfFH8SgHbwDFoyEjRaZeoImY5pB3IZqwcaRzzbcdmat'
#Ang fetch_web_api ang gumagawa ng lahat ng komunikasyon sa Spotify servers
def fetch_web_api(endpoint, method, body=None):
    url = f'https://api.spotify.com/{endpoint}'
    headers = {'Authorization': f'Bearer {TOKEN}'}
    response = requests.request(method, url, headers=headers, json=body)
    response.raise_for_status()
    return response.json()

def get_top_tracks():
    #- Ang time_range=long_term ay nangangahulugang kukunin ang mga kantang pinakapaborito mo sa mahabang panahon

    # Endpoint reference: https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
    response = fetch_web_api('v1/me/top/tracks?time_range=long_term&limit=5', 'GET')
    return response.get('items', [])

if __name__ == '__main__':
    try:
        top_tracks = get_top_tracks()
        print("Top Tracks:")
        #Ang enumerate(top_tracks, 1) ay naglalagay ng numero sa bawat kanta
        for index, track in enumerate(top_tracks, 1):
            artists = ', '.join(artist['name'] for artist in track['artists'])
            print(f"{index}. {track['name']} by {artists}")
            
    except requests.exceptions.HTTPError as err:
        #Ang try-except block ay parang "safety net" na humahawak ng mga posibleng error
        print(f"API Error: {err}")