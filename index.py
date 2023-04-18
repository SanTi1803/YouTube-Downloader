# import el paquete
from pytube import YouTube
import archivoAuto

url = 'Tu URL va acá'
mi_video = YouTube(url)

print("Imagen del video")
# Obtener la imagen del video
print(mi_video.thumbnail_url)

print("Descargar video")
# Obtener todas las resoluciones del video 
for stream in mi_video.streams:
    print(stream)

#Seleccionar el video con más resolución
my_video = mi_video.streams.get_highest_resolution()

# O seleccionar la resolución que viene por defecto
# my_video = my_video.streams.first()

# Descargar el video
descarga = my_video.download()

# Crear y guardar en la carpeta Descargas
archivoAuto.descarga()