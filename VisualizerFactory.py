from PlotFigure import PlotFigure
from PlotBoxPlot import PlotBoxPlot
from PlotFigureSet import PlotFigureSet
from ExportFigureAsImage import ExportFigureAsImage
class VisualizerFactory:
    @staticmethod
    def create_visualizer(output_format):
        if output_format == 'fig':
            return PlotFigure()
        elif output_format == 'boxplot':
            return PlotBoxPlot()
        elif output_format == 'set':
            return PlotFigureSet()
        elif output_format == 'ImgFig':
            return ExportFigureAsImage()
        else:
            print("Tipo de representación incorrecto, opciones: fig, set y boxplot.")
            return