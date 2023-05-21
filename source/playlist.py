#!/usr/bin/env python3


from urllib.parse import parse_qs, urlparse


def get_media_id(media_url:str) -> str:
	query = urlparse(media_url)
	match query.hostname:
		case 'youtu.be':
			return query.path[1:]
		case  'www.youtube.com' | 'youtube.com' | 'music.youtube.com':
			if query.path[:7] == '/watch/':
				return query.path.split('/')[1]
			if query.path == '/watch':
				return parse_qs(query.query)['v']
			if query.path[:7] == '/embed/':
				return query.path.split('/')[2]
			if query.path[:3] == '/v/':
				return query.path.split('/')[2]
			if query.path[:8] == '/shorts/':
				return query.path.split('/')[2]
		case _:
			raise Exception("URL could not be parsed.")


def get_playlist_video_ids_array(playlist_filename:str):
	playlist_array = []
	with open(playlist_filename, encoding='UTF-8', errors='ignore') as playlist_file:
		count = 0
		for line in playlist_file:
			count += 1
			print(count)
			try:
				line_media_id = get_media_id(line)
				playlist_array.append(line_media_id)
			except Exception:
				print(f"Error: Likely unable to get info: {line}")
	return playlist_array


