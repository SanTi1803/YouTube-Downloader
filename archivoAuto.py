import os, shutil

def descarga():
    path = r"Tenes que colocar la ruta en donde pusiste este proyecto"

    view_files = os.listdir(path)

    folder_names = ['descargas']
    for loop in range(1):
        if not os.path.exists(path + folder_names[loop]):
        # print((path + folder_names[loop]))
            os.makedirs(path + folder_names[loop])


    for file in view_files:
        if ".mp4" in file and not os.path.exists(path + "descargas/" + file):
            shutil.move(path + file, path + "descargas/" + file)

descarga()