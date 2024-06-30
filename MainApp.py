from VisualizerFactory import *
from FilesOrganizer import FilesOrganizer


class MainApp:
    def __init__(self, directories, output_format='fig'):
        self.directories = directories
        self.output_format = output_format
        self.amplitudes = []

        self.plotter = VisualizerFactory.create_visualizer(output_format)
        self.filesOrganizer = FilesOrganizer(directories)

    def run(self):
        files_SanoFemale, files_NoSanoFemale, files_SanoMale, files_NoSanoMale = self.filesOrganizer.organize_by_gender()
        if self.output_format == 'fig':
            self.plotter.show_plots(files_NoSanoFemale)

        elif self.output_format == 'boxplot':
            self.plotter.peaks_count_boxplot("duration_counts", files_SanoFemale, files_NoSanoFemale, files_SanoMale, files_NoSanoMale)

if __name__ == "__main__":
    app = MainApp(directories=['../Organizados2/Sano/female', '../Organizados2/No_Sano/female',
                               '../Organizados2/Sano/male', '../Organizados2/No_Sano/male'], output_format='boxplot')
    app.run()

