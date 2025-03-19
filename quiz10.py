#https://github.com/public-apis/public-apis?tab=readme-ov-file
#access a public api using request. present the data to the users
import requests


# Spotify API credentials - REPLACE WITH YOUR OWN
#Ang TOKEN ay parang ID na nagpapatunay na ikaw ay may karapatang humingi ng datos

#Ang fetch_web_api ang gumagawa ng lahat ng komunikasyon sa Spotify servers
TOKEN = 'BQDxm6qyk1YRXrm_A6VmROc8htJmxlsnmSayeaaKVj2ZOpwKcgpBaDXUqRM5-bce833firP6E_ybCD44MNNiGlWuY5xnYLI78H6xQ6MVCMCO0tAoCTo2HNrAkaUXBs_riF9EGRZo-MkzQ5SFU2HuMuvnfmiQrljnlY0ZSWPCwG3Sex3b7_4ydBgLWWhQ5eRDrbXjWRt6xR0jcftOa3l68M41tqQ_GnOr7mCSRBKq8MsA3Mhgm66Mc7mvgP2--hkgDL9-0HVLZ4MhkQovRWEQlvvqG8L_acc_N-QQZYXqGLtqJh0X2LdWfkTg';
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