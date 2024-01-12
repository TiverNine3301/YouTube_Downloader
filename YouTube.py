# https://www.youtube.com/playlist?list=PLgULlLHTSGIQ9BeVZY37fJP50CYc3lkW2

# rm -rf *.Identifier  rm -rf *.ldentifier rm -rf *.identifier

from pytube import YouTube
import yt_dlp

def download_playlist(playlist_url, quality='best'):
    try:
        with yt_dlp.YoutubeDL() as ydl:
            info_dict = ydl.extract_info(playlist_url, download=False)
            for entry in info_dict['entries']:
                video_url = entry['url']
                print(f"Загружается видео: {entry['title']}...")
                try:
                    ydl.download([video_url])
                except yt_dlp.DownloadError as e:
                    # Обрабатываем ошибку загрузки видео и выводим сообщение
                    print(f"Произошла ошибка при загрузке видео: {str(e)}")
                    continue
            print("Загрузка завершена.")

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


def download_video(link, quality = 'High'):
    try:
        video = YouTube(link)
        
        if quality == 'High':
            selected_stream = video.streams.get_highest_resolution()
        elif quality == 'Low':
            selected_stream = video.streams.get_lowest_resolution()
        else:
            print("Неверный выбор качества. Выбрано максимальное качество.")
            selected_stream = video.streams.get_highest_resolution()
        
        print(f"Загрузка видео: {video.title}...")
        selected_stream.download()
        print("Загрузка завершена.")
        
    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")
    
if __name__ == "__main__":
    way = input("Что вы хотите скачать(Плейлист или видео)?\n")
    
    if way == 'Плейлист':
        playlist_url = input("Введите ссылку на плейлист: ")
        quality = input("Выберите качество видео (High/low): ")
        download_playlist(playlist_url, quality)
        
    elif way == 'Видео':
        link = input("Введите ссылку на видео: ")
        quality = input("Введите качество видео(High/Low): ").capitalize()
        download_video(link, quality)
