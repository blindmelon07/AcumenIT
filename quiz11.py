# ... existing imports ...import quiz10 as q10
import csv
import json

from datetime import datetime
import quiz10 as q10


q10.TOKEN
def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump({"tracks": data}, f, indent=4)  # Wrap in dictionary for better structure

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Number', 'Track', 'Artists', 'Album', 'Duration (sec)', 'Popularity'])
        for idx, track in enumerate(data, 1):
            writer.writerow([
                idx,
                track['name'],
                ', '.join(artist['name'] for artist in track['artists']),
                track['album']['name'],
                track['duration_ms'] // 1000,
                track['popularity']
            ])

if __name__ == '__main__':
    try:
        top_tracks = q10.get_top_tracks()
        
        # Generate timestamp for unique filenames
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = f"top_tracks_{timestamp}"
        
        save_to_json(top_tracks, f'{base_name}.json')
        save_to_csv(top_tracks, f'{base_name}.csv')
        print(f"Data saved to {base_name}.json and {base_name}.csv")
        
    except Exception as err:  # Broaden exception catch
        print(f"Error: {err}")