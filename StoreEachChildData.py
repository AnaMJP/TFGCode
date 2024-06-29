import os
import shutil


def organizar_archivos(origen, destino):
    if not os.path.exists(destino):
        os.makedirs(destino)

    for files in os.listdir(origen):
        partes = files.split('_')
        sitio = partes[1]
        codigo  = partes[5]
        sano = '0000_' + sitio if partes[2] == "0" else '1000_' + sitio
        edad = partes[3]
        edad = str(int(edad)//12)
        sexo = "M" if partes[4] == "0" else "F"

        destino_ejercicios = codigo + "_" + edad + "_" + sexo

        destino_final = os.path.join(destino, sano, destino_ejercicios)

        if not os.path.exists(destino_final):
            os.makedirs(destino_final)

        shutil.move(os.path.join(origen, files), destino_final)

        print(f"Archivo {files} organizado correctamente en {destino_final}")


# Ejemplo de uso
origen = 'C:/Users/anam0/Desktop/TFT/Datos_Guarderia'
destino = 'C:/Users/anam0/Desktop/TFT/Codigo/Organizados4'
organizar_archivos(origen, destino)
