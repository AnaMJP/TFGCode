import matplotlib.pyplot as plt
import os
import re
from DataAnalyzer import DataAnalyzer
from DataProcessor import DataProcessor
from matplotlib.backends.backend_pdf import PdfPages

class ExportFigureAsImage:
    def __init__(self, base_output_dir='output'):
        self.analyzer = DataAnalyzer()
        self.processor = DataProcessor()
        self.base_output_dir = 'C:/Users/anam0/Desktop/TFT/Codigo/DatasetFemaleCompleto'
    def show_plots(self, files_SanoFemale, files_NoSanoFemale, files_SanoMale, files_NoSanoMale):
        all_files = {
            "SanoFemale": files_SanoFemale,
            "NoSanoFemale": files_NoSanoFemale,
        }

        for category, files in all_files.items():
            for file_name in files:
                self.plot_acceleration(file_name)

    def save_all_plots_to_pdf(self, all_files, pdf_file_name):
        with PdfPages(pdf_file_name) as pdf_pages:
            for category, files in all_files.items():
                for file_name in files:
                    self.plot_acceleration(file_name, pdf_pages)

    def plot_acceleration(self, file_name):
        t, A, filtered_A = self.processor.calculate_acceleration(file_name)
        start, end = self.analyzer.cut_data_max_value(filtered_A, t)

        fig = plt.figure(figsize=(10, 6))
        adjusted_x = [x - t[start] for x in t[start:end]]
        plt.plot(adjusted_x, A[start:end], 'r')
        save_dir, name = self.get_save_dir(file_name)
        plt.ylim(0, 100)
        plt.xlim(0, 2)
        plt.axis('off')

        os.makedirs(save_dir, exist_ok=True)
        plt.savefig(os.path.join(save_dir, f'Aceleracion - {name}.png'))
        plt.close()

    def get_save_dir(self, file_name):
        parts = re.split(r'[\\\\/]', file_name)
        save_dir = os.path.join(self.base_output_dir, *parts[-5:-1])
        name = parts[-1]
        return save_dir, name