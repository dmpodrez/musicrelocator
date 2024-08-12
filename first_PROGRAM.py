import csv
from yandex_music import Client
import time
import random

# Вставьте ваш токен API Яндекс Музыки
token = 'y0_AgAAAAAcWjaBAAG8XgAAAAELxOZFAAATELKDXPZBI5WZgiM7XL3rYmOXdw'
client = Client(token).init()

# Имя плейлиста, в который будут добавлены треки
playlist_name = 'Imported Playlist'

# Создание плейлиста
playlist = client.users_playlists_create(title=playlist_name)
playlist_id = playlist.kind

# Функция для добавления треков в плейлист
def add_tracks_to_playlist(client, playlist_id, tracks):
    for track in tracks:
        print(f"Ищу трек: {track}")  # Отладочная информация
        search_results = client.search(track)
        if search_results.tracks:
            track_info = search_results.tracks.results[0]
            track_id = track_info.id
            album_id = track_info.albums[0].id
            print(f"Добавляю трек: {track} с ID: {track_id} и Album ID: {album_id}")  # Отладочная информация

            try:
                # Получение актуальной ревизии плейлиста перед добавлением трека
                playlists = client.users_playlists_list()
                for playlist in playlists:
                    if playlist.kind == playlist_id:
                        revision = playlist.revision
                        break
                
                client.users_playlists_insert_track(playlist_id, track_id, album_id, revision=revision)
                print(f"Трек {track} успешно добавлен.")
            except Exception as e:
                print(f"Ошибка при добавлении трека {track}: {e}")
        else:
            print(f"Трек не найден: {track}")  # Отладочная информация

        # Задержка перед добавлением следующего трека
        delay = random.randint(5, 10)
        print(f"Задержка {delay} секунд перед добавлением следующего трека...")
        time.sleep(delay)

# Чтение нового CSV файла и добавление треков в список
tracks = []
with open('playlist.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовок
    for row in reader:
        track_name = row[0]
        artist_name = row[1]
        tracks.append(f'{track_name} {artist_name}')

# Добавление треков в плейлист
add_tracks_to_playlist(client, playlist_id, tracks)
