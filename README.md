# TFG Code
Este codigo se lleva a cabo con el fin de estudiar las datos obtenidos al realizar varios ejercicios de las cuales se obtiene la velocidad y la aceleración para muestrear los datos. 
El objetivo es buscar una forma mas facil de detectar si un niño tiene alguna enfermedad neurológica como TEA y TDAH.

## Estructura de clases
### MainApp:
  Es la clase principal, donde se controla el fujo de la aplicación.
### VisualizerFactory:
  Define como va a ser la salida de los datos.
### DataAnalyzer:
  Realiza operaciones adicionales sobre los datos.
### DataProcessor:
  Calcula la vleocidad y aceleración con los datos pasados.
### DataFilter:
  Filtros usados para eliminar el ruido de las gráficas. De momento solo se aplica el de paso bajo.
### DataLoader:
  Lee los datos.
### PlotPdf:
  La salida del programa se hace en un pdf.
### PlotFigure:
  La salida del programa es en una figura.
