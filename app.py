import os
from pytube import YouTube
from moviepy.editor import *
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining

    percentage = (bytes_downloaded / total_size) * 100
    print(f"%{round(percentage, 2)} indirildi.", end="\r")


def video_indir(link, kayit_yolu):
    yt = YouTube(link, on_progress_callback=on_progress)
    ys = yt.streams.get_highest_resolution()  # en yüksek çözünürlükteki videoyu seçer
    print("Video indiriliyor...")
    ys.download(kayit_yolu)
    print("Video başarıyla indirildi!")

def video_to_mp3(video_dosyasi, mp3_dosyasi):
    video = VideoFileClip(video_dosyasi)
    video.audio.write_audiofile(mp3_dosyasi)
    video.audio.close()
    video.close()

def main():
    print("Video indirmek için 1'e basın, MP3 dönüştürmek için 2'ye basın.")
    secim = input("Seçiminizi yapın (1/2): ")

    if secim == "1":
        link = input("YouTube video linkini girin: ")
        kayit_yolu = os.getcwd()  # Geçerli çalışma dizinine kaydedilir
        video_indir(link, kayit_yolu)
    elif secim == "2":
        video_dosyasi = input("MP3'e dönüştürülecek video dosyasının yolunu girin (örn: video.mp4): ")
        mp3_dosyasi = input("Çıktı olarak kaydedilecek MP3 dosyasının adını girin (örn: cikis.mp3): ")
        video_to_mp3(video_dosyasi, mp3_dosyasi)
    else:
        print("Geçersiz seçim!")

if __name__ == "__main__":
    main()