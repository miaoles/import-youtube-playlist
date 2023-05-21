#!/usr/bin/env python3


from playlist import *
from google_apis import *
from youtube import *

playlist_filename = 'playlist.txt'
client_filename = 'client_secret.json'
playlist_title = 'playlist.txt'
playlist_description = 'Generated Playlist'
playlist_privacy_status = 'unlisted'
playlist_id = None

def main():
	video_ids_array = get_playlist_video_ids_array(playlist_filename)
	video_ids_array.reverse()

	youtube = YouTube(client_filename)
	youtube.init_service()

	response_playlist = youtube.create_playlist(
		playlist_title,
		playlist_description,
		playlist_privacy_status
	)

	playlist_id = response_playlist.get('id')
	playlist_title = response_playlist['snippet']['title']

	video_count = 0
	for video_id in video_ids_array:
		video_count += 1
		request_body = {
			'snippet': {
				'playlistId': playlist_id,
				'resourceId': {
					'kind': 'youtube#video',
					'videoId': video_id
				}
			}
		}
		response = youtube.service.playlistItems().insert(
			part='snippet',
			body=request_body
		).execute()
		video_title = response['snippet']['title']
		print(f'{video_count}: "{video_title}" inserted to "{playlist_title}"')

if __name__ == "__main__":
    main()
