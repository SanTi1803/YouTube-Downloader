# **YouTube Video Downloader**
Esta pequeña intro te dirá como tenés que hacer para descargar cualquier video de YouTube que desees ver.

Estos son los pasos a seguir:
```sh
git clone https://github.com/SanTi1803/YouTube-Downloader.git
cd YouTube-Downloader
python3 -m venv env
source env/bin/activate #Linux
source env/Scripts/activate # Windows
pip install pytube
```

# **Pasos importantes** 

Después de estos pasos quedan 2 más que son muy importante:

<ul>
    <li>Lo primero que tenés que hacer es entrar al archivo "index.py" y poner la URL del video que desees descargar. </<li>
</ul>

<ul>
    <li>Lo segundo que tenés que hacer es entrar al archivo "archivoAuto.py" y en path poner la ruta en donde descargaste este proyecto. EJ: C:/Users/santi/Documents/Example/ </<li>
</ul>

Para hacerlo un poco más propio al proyecto agregue el archivo "archivoAuto.py" que básicamente te crea una carpeta llamada descargas y pone el video descargado. Si la carpeta "descargas" ya está creada, el video se pondrá automáticamente en esa carpeta.


# **Requisitos Previos**
```sh
- Python
