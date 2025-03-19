#read the generated json and csv file from quiz11
import json
import csv
import quiz11 as q11

def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data['tracks']  
    # Access the "tracks" key from quiz11's structure

def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return list(reader)

if __name__ == '__main__':
    try:
        filename = input("Enter filename to read (e.g. top_tracks_20240315_123456.json/csv): ")
        
        if filename.endswith('.json'):
            data = read_json(filename)
            print("\nJSON Data:")
            for track in data:
                print(f"{track['name']} by {', '.join(artist['name'] for artist in track['artists'])}")
                
        elif filename.endswith('.csv'):
            data = read_csv(filename)
            print("\nCSV Data:")
            for row in data:
                print(f"{row['Number']}. {row['Track']} by {row['Artists']}")
                
        else:
            print("Invalid file type. Please use .json or .csv")
            
    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except Exception as e:
        print(f"Error: {str(e)}")