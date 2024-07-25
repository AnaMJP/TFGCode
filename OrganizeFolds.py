import os
import shutil


def organizar_archivos(origen, destino):
    if not os.path.exists(destino):
        os.makedirs(destino)

    for directorio in os.listdir(origen):
        directorio_path = os.path.join(origen, directorio)
        flagSano = False
        print(directorio_path)
        if directorio_path.split("\\")[-1].startswith('0'):
            flagSano = True
            print("Sano " + directorio_path)

        # Iterar sobre los archivos en el directorio de origen
        for files in os.listdir(directorio_path):
            partes = files.split('_')
            edad = partes[1]
            sexo = partes[2]


            estado_sano = 'Sano' if flagSano else 'No_Sano'

            destino_sexo = 'male' if sexo == 'M' else 'female'

            destino_final = os.path.join(destino, estado_sano, destino_sexo, edad)

            if not os.path.exists(destino_final):
                os.makedirs(destino_final)

            shutil.move(os.path.join(directorio_path, files), destino_final)

            print(f"Archivo {files} organizado correctamente en {destino_final}")


# Ejemplo de uso
origen = 'C:/Users/anam0/Desktop/TFT/Codigo/Organizados4'
destino = 'C:/Users/anam0/Desktop/TFT/Organizados2'
organizar_archivos(origen, destino)
