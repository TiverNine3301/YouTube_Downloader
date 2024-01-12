from pytube import YouTube, Playlist

def download_video(link, quality='high'):
    try:
        video = YouTube(link)
        
        if quality == 'high':
            selected_stream = video.streams.get_highest_resolution()
        elif quality == 'low':
            selected_stream = video.streams.get_lowest_resolution()
        else:
            print("Неверный выбор качества. Выбрано максимальное качество.")
            selected_stream = video.streams.get_highest_resolution()
        
        print(f"Загрузка видео: {video.title}...")
        selected_stream.download()
        print("Загрузка завершена.")
        
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

def download_playlist(playlist_url, quality='high'):
    try:
        playlist = Playlist(playlist_url)
        for video_url in playlist.video_urls:
            print(f"Загружается видео из плейлиста: {video_url}...")
            download_video(video_url, quality)
        
        print("Загрузка плейлиста завершена.")
        
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")

if __name__ == "__main__":
    way = input("Что вы хотите скачать (Плейлист или видео)?\n")

    if way.lower() == 'плейлист':
        playlist_url = input("Введите ссылку на плейлист: ")
        quality = input("Выберите качество видео (high/low): ")
        download_playlist(playlist_url, quality)

    elif way.lower() == 'видео':
        link = input("Введите ссылку на видео: ")
        quality = input("Выберите качество видео (high/low): ")
        download_video(link, quality)
