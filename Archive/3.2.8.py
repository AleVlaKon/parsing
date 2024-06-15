import requests

response = requests.get(url='https://parsinger.ru/video_downloads/videoplayback.mp4', stream=True)

# Если надо загрузить видео одним куском
with open('videoplayback2.mp4', 'wb') as file:
    file.write(response.content)

# Если большой файл, то видео можно загрузить по частям
with open('videoplayback.mp4', 'wb') as video:
    for piece in response.iter_content(chunk_size=100000):
        video.write(piece)

