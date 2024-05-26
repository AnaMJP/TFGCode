from PlotPdf import PlotPdf
from PlotFigure import PlotFigure

class VisualizerFactory:
    @staticmethod
    def create_visualizer(output_format, output_path):
        if output_format == 'pdf':
            return PlotPdf(output_path)
        elif output_format == 'fig':
            return PlotFigure()
        else:
            return