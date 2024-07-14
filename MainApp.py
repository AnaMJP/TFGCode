from VisualizerFactory import *
from FilesOrganizer import FilesOrganizer


class MainApp:
    def __init__(self, directories, output_format='fig', algorithm="peaks_count", measure="velocity", yTitle=""):
        self.directories = directories
        self.output_format = output_format
        self.algorithm = algorithm
        self.measure = measure
        self.yTitle = yTitle

        self.plotter = VisualizerFactory.create_visualizer(output_format)
        self.filesOrganizer = FilesOrganizer(directories)

    def run(self):
        files_SanoFemale, files_NoSanoFemale, files_SanoMale, files_NoSanoMale = self.filesOrganizer.organize_by_gender()
        if self.output_format == 'fig':
            self.plotter.show_plots(files_NoSanoMale)
        elif self.output_format == 'set':
            self.plotter.show_plots_set(files_SanoFemale)
        elif self.output_format == 'boxplot':
            self.plotter.peaks_count_boxplot(self.algorithm, self.measure, self.yTitle, files_SanoFemale, files_NoSanoFemale, files_SanoMale, files_NoSanoMale)


"""
output_format:
    * fig
    * boxplot
    * set
Algorithms:
Parámetro a aplicar para ver las diferencias
    * peaks_count: Numero de picos
    * peaks_count_per_seconds: Numero de picos por tiempo de ejecucion
    * duration_counts: tiempo total de ejecución
    * time_to_max_peak: tiempo desde que se empieza al pico mas alto
    * max_peak_value: valor del pico mas alto
    
Measure: 
Medida usada para calcular
    * Acceleration
    * Velocity
"""
if __name__ == "__main__":
    app = MainApp(directories=['../Organizados2/Sano/female', '../Organizados2/No_Sano/female',
                               '../Organizados2/Sano/male', '../Organizados2/No_Sano/male'], output_format='boxplot', algorithm="max_peak_value", measure="Acceleration", yTitle="Valor del pico mas alto")
    app.run()

