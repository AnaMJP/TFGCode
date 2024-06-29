from PlotFigure import PlotFigure
from PlotBoxPlot import PlotBoxPlot
class VisualizerFactory:
    @staticmethod
    def create_visualizer(output_format):
        if output_format == 'fig':
            return PlotFigure()
        elif output_format == 'boxplot':
            return PlotBoxPlot()
        else:
            return