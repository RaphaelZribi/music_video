import requests
import json


api_key = 'AIzaSyDK5Fjp3r91iQzNW-jaoVeuTszPIA98jJ0'
channel_id = 'UCPVhZsC2od1xjGhgEc2NEPQ'
api_url = 'https://www.googleapis.com/youtube/v3/search?key={}&channelId={}&part=snippet,id&order=date&maxResults={}'.format(api_key, channel_id, 20)

def get_videos(api_url):
	videos = requests.get(api_url).json()
	print(videos)


get_videos(api_url)