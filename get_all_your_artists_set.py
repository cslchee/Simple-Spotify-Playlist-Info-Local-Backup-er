import json, os


def get_all_your_artists_set() -> set:
    """Goes through your playlists JSON and returns a set of every artist you have saved in a playlist"""
    # Get the newest json file name from this directory
    json_files = [f for f in os.listdir(os.getcwd()) if f.endswith('.json')]
    json_files = [os.path.join(os.getcwd(), f) for f in json_files]
    latest_json = max(json_files, key=os.path.getctime)
    print(f"Reading artists from {latest_json}")

    # Read your data and get a set of all the artists you have music of
    with open(latest_json, 'r') as file:
        data = json.loads(file.read())

    # Get all the artists from every song in every playlist you've created
    tracks = []
    for playlist in data['data']['your_playlists']:
        for track in playlist['tracks']:
            tracks.append(track)
    all_your_artists = set()
    for track in tracks:
        artists = track['artist'].split(", ")
        for artist in artists:
            if artist != '' and artist not in all_your_artists:
                all_your_artists.update(artists)
    return all_your_artists
