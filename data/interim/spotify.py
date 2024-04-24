import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import datetime
import time
from sqlalchemy import create_engine
from apscheduler.schedulers.background import BackgroundScheduler

def get_db_engine():
    username = 'admin'
    password = 'Analyt1cs'
    hostname = 'spotifystreamdb.czwo24egittv.us-east-2.rds.amazonaws.com'
    database = 'spotify'
    return create_engine(f'mysql+mysqlconnector://{username}:{password}@{hostname}/{database}', echo=False)

def manage_api_calls(request_count, start_time):
    if request_count >= 80:
        elapsed_time = time.time() - start_time
        if elapsed_time < 30:
            time.sleep(30 - elapsed_time)
        start_time = time.time()
        request_count = 0
    return request_count, start_time

def fetch_artists_data(artist_ids, spotify):
    artists_data = []
    request_count = 0
    start_time = time.time()
    for artist_id in artist_ids:
        request_count, start_time = manage_api_calls(request_count, start_time)
        try:
            artist_info = spotify.artist(artist_id)
            artists_data.append({
                'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'name': artist_info['name'],
                'followers': artist_info['followers']['total'],
                'uri': artist_info['uri'],
                'popularity': artist_info['popularity'],
                'genres': ', '.join(artist_info['genres'])
            })
        except Exception as e:
            artists_data.append({
                'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'name': None,
                'followers': None,
                'uri': None,
                'popularity': None,
                'genres': None
            })
        request_count += 1
    return artists_data

def fetch_album_data(artist_ids, spotify):
    album_data = []
    request_count = 0
    start_time = time.time()
    for artist_id in artist_ids:
        request_count, start_time = manage_api_calls(request_count, start_time)
        try:
            albums = spotify.artist_albums(artist_id, limit=50)
            for album in albums['items']:
                album_data.append({
                    'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'Artist ID': artist_id,
                    'Album ID': album['id'],
                    'Album Name': album['name'],
                    'release_date': album['release_date'],
                    'total_tracks': album['total_tracks']
                })
        except Exception as e:
            print(f"Failed to fetch albums for artist ID {artist_id}: {e}")
        request_count += 1
    return album_data

def fetch_audio_features(artist_ids, spotify):
    audio_features_data = []
    request_count = 0
    start_time = time.time()
    for artist_id in artist_ids:
        request_count, start_time = manage_api_calls(request_count, start_time)
        try:
            top_tracks = spotify.artist_top_tracks(artist_id)
            track_ids = [track['id'] for track in top_tracks['tracks']]
            audio_features = spotify.audio_features(track_ids)
            for feature, track_id in zip(audio_features, track_ids):
                if feature:
                    audio_features_data.append({
                        'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        'track_id': track_id,
                        'danceability': feature['danceability'],
                        'energy': feature['energy'],
                        'key': feature['key'],
                        'loudness': feature['loudness'],
                        'mode': feature['mode'],
                        'speechiness': feature['speechiness'],
                        'acousticness': feature['acousticness'],
                        'instrumentalness': feature['instrumentalness'],
                        'liveness': feature['liveness'],
                        'valence': feature['valence'],
                        'tempo': feature['tempo']
                    })
        except Exception as e:
            print(f"Failed to fetch audio features for artist ID {artist_id}: {e}")
        request_count += 1
    return audio_features_data

def feed_data_to_aws(data, table_name):
    engine = get_db_engine()
    df = pd.DataFrame(data)
    try:
        df.to_sql(table_name, con=engine, if_exists='append', index=False)
    except Exception as e:
        print(f"Failed to feed data into AWS RDS: {e}")

def execute_data_operations():
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='ac04d37a2c594ed0a650ea64ba73206c',
                                                                              client_secret='1e7516fc12d146f88e754a0cb8711a77'))
    artist_ids = pd.read_csv('./pop_artists_info.csv')['uri'].str.split(':').apply(lambda x: x[-1]).tolist()
    artist_data = fetch_artists_data(artist_ids, spotify)
    feed_data_to_aws(artist_data, 'artists_new')
    album_data = fetch_album_data(artist_ids, spotify)
    feed_data_to_aws(album_data, 'albums_new')
    audio_features_data = fetch_audio_features(artist_ids, spotify)
    feed_data_to_aws(audio_features_data, 'audio_features_new')

def schedule_jobs():
    scheduler = BackgroundScheduler()
    scheduler.add_job(execute_data_operations, 'date', run_date=datetime.datetime.now() + datetime.timedelta(seconds=10))
    scheduler.add_job(execute_data_operations, 'cron', hour=0, minute=0, second=0, start_date=datetime.datetime.now().date() + datetime.timedelta(days=1))
    scheduler.start(paused=False)

if __name__ == '__main__':
    schedule_jobs()
