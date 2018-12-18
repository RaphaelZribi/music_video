import requests
import json

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music_video.settings')
import django
django.setup()
from main_app.models import Playlist, Video


api_key = 'AIzaSyDK5Fjp3r91iQzNW-jaoVeuTszPIA98jJ0'
channel_id = 'UCupvZG-5ko_eiXAupbDfxWw'
playlists_api_url = 'https://www.googleapis.com/youtube/v3/playlists?part=snippet&channelId={}&key={}&maxResults={}'.format(channel_id, api_key, 20)


def get_videos(playlist):
	
	playlist_api_url= 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults={}&playlistId={}&key={}'.format(20, playlist.playlist_id, api_key)
	playlist_json = requests.get(playlist_api_url).json()
	#playlist_items = playlist_json['items']


	for dico in playlist_json['items']:
		video_id =dico['snippet']['resourceId']['videoId']
		title = dico['snippet']['title']
		description= dico['snippet']['description']
		thumbnail = dico['snippet']['thumbnails']['default']['url']
		video = Video.objects.get_or_create(video_id = video_id,
											title = title,
											description = description,
											thumbnail = thumbnail, 
											playlist= playlist)[0]
		


def get_playlists(playlists_api_url):
	playlist_json = requests.get(playlists_api_url).json()
	playlists_items = playlist_json['items']
	play_description = []
	for item in playlists_items: 
		playlist_id = item['id']
		title = item['snippet']['title']
		description= item['snippet']['description']
		thumbnail = item['snippet']['thumbnails']['high']['url']

		playlist = Playlist.objects.get_or_create(playlist_id= playlist_id, 
												  title=title, 
												  description= description,
												  thumbnail=thumbnail)[0]
		
	get_videos(playlist)
		


if __name__ == '__main__':
    print('Staring to populate...')
    get_playlists(playlists_api_url)

    print('Finished populating!')



