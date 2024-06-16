import os
import numpy as np
from DataLoader import DataLoader
from DataFilter import DataFilter
from DataProcessor import DataProcessor
from DataAnalyzer import DataAnalyzer
from VisualizerFactory import *

class MainApp:
    def __init__(self, directory, output_format='pdf', output_path='output.pdf', cutoff_frequency=0.95, fs=10.0):
        self.directory = directory
        self.output_format = output_format
        self.output_path = output_path
        self.cutoff_frequency = cutoff_frequency
        self.fs = fs
        self.amplitudes = []

        self.loader = DataLoader()
        self.filter = DataFilter(cutoff_frequency, fs)
        self.processor = DataProcessor()
        self.analyzer = DataAnalyzer()
        self.plotter = VisualizerFactory.create_visualizer(output_format, output_path)

    def run(self):
        files = []
        for subdir, _, file_names in os.walk(self.directory):
            for file_name in file_names:
                files.append(os.path.join(subdir, file_name))

        #filtered_files = [file for file in files if "_L_" in file and self.analyzer.max_value(file)]

        #solo el primero de cada niño


        first_files_per_folder = {}
        for file in files:
            if "_L_" in file and self.analyzer.max_value(file):
                folder = os.path.dirname(file)
                if folder not in first_files_per_folder:
                    first_files_per_folder[folder] = file
        filtered_files = list(first_files_per_folder.values())[:8]



        if self.output_format == 'pdf':
            for file_name in filtered_files:
                self.process_file(file_name)
            self.plotter.close()
        elif self.output_format == 'fig':
            n_files = len(filtered_files)
            self.plotter.create_acc_subplots(n_files // 2, 2, '')
            self.plotter.create_vel_subplots(n_files // 2, 2, '')
            idx = 0
            for file_name in filtered_files:
                self.process_file_subplot(file_name, idx)
                idx += 1
            self.plotter.show()
        elif self.output_format == 'boxplot':
            peak_counts = self.get_peak_counts(files)
            self.plotter.plot_data(peak_counts, 'Número de Picos por Edad')

    def process_file(self, file_name):
        data = self.loader.load_data(file_name)
        t = data[:, 0] - data[0, 0]
        A1 = np.abs(data[:, 1])
        A2 = np.abs(data[:, 2])
        A3 = np.abs(data[:, 3])
        g = data[:, 8]

        filtered_A1 = self.filter.butter_lowpass_filter(A1)
        filtered_A2 = self.filter.butter_lowpass_filter(A2)
        filtered_A3 = self.filter.butter_lowpass_filter(A3)
        filtered_A = self.processor.calculate_acceleration(t, filtered_A1, filtered_A2, filtered_A3)


        start, end = self.analyzer.cut_data_max_value(filtered_A, t)
        self.plotter.plot_data(t, filtered_A, g, "Aceleración\n" + file_name, start=start, end=end)

        Vx, Vy, Vz = self.processor.calculate_velocity(t, filtered_A1, filtered_A2, filtered_A3)
        Vt = np.sqrt((np.diff(Vx) / np.diff(t)) ** 2 + (np.diff(Vy) / np.diff(t)) ** 2 + (np.diff(Vz) / np.diff(t)) ** 2)
        start, end = self.analyzer.cut_data_max_value(Vt, t)
        self.plotter.plot_velocity(t[:-1], Vt, "Velocidad\n" + file_name, start=start, end=end)

    def process_file_subplot(self, file_name, idx):
        data = self.loader.load_data(file_name)
        file_name = file_name.split("\\")[-1].split("_")[2]
        t = data[:, 0] - data[0, 0]
        A1 = np.abs(data[:, 1])
        A2 = np.abs(data[:, 2])
        A3 = np.abs(data[:, 3])
        g = data[:, 8]

        filtered_A1 = self.filter.butter_lowpass_filter(A1)
        filtered_A2 = self.filter.butter_lowpass_filter(A2)
        filtered_A3 = self.filter.butter_lowpass_filter(A3)
        filtered_A = self.processor.calculate_acceleration(t, filtered_A1, filtered_A2, filtered_A3)
        A = self.processor.calculate_acceleration(t, A1, A2, A3)


        inicio, fin = self.analyzer.cut_data_max_value(filtered_A, t)
        row, col = divmod(idx, 2)
        self.plotter.plot_data(t, filtered_A, A, g, "", start=inicio, end=fin, ax=self.plotter.acc_axs[row, col])

        peak_indices = self.analyzer.show_peaks(A[inicio:fin])
        #self.plotter.acc_axs[row, col].plot(t[inicio:fin][peak_indices], A[inicio:fin][peak_indices], 'ro', markersize=5)

        Vx, Vy, Vz = self.processor.calculate_velocity(t, A1, A2, A3)
        Vt = np.sqrt((np.diff(Vx) / np.diff(t)) ** 2 + (np.diff(Vy) / np.diff(t)) ** 2 + (np.diff(Vz) / np.diff(t)) ** 2)

        filtered_Vx, filtered_Vy, filtered_Vz = self.processor.calculate_velocity(t, filtered_A1, filtered_A2, filtered_A3)
        filtered_Vt = np.sqrt((np.diff(filtered_Vx) / np.diff(t)) ** 2 + (np.diff(filtered_Vy) / np.diff(t)) ** 2 + (np.diff(filtered_Vz) / np.diff(t)) ** 2)

        self.plotter.plot_velocity(t[:-1], filtered_Vt, Vt,  "", start=inicio, end=fin, ax=self.plotter.vel_axs[row, col])

    def extract_age_from_filename(self, file_name):
        age = os.path.basename(os.path.dirname(os.path.dirname(file_name)))
        return age

    def get_peak_counts(self, files):
        peak_counts = {}
        for file_name in files:
            if "_L_" in file_name:
                data = self.loader.load_data(file_name)
                A1 = np.abs(data[:, 1])
                A2 = np.abs(data[:, 2])
                A3 = np.abs(data[:, 3])
                t = data[:, 0] - data[0, 0]

                filtered_A1 = self.filter.butter_lowpass_filter(np.abs(data[:, 1]))
                filtered_A2 = self.filter.butter_lowpass_filter(np.abs(data[:, 2]))
                filtered_A3 = self.filter.butter_lowpass_filter(np.abs(data[:, 3]))
                filtered_A = self.processor.calculate_acceleration(t, filtered_A1, filtered_A2, filtered_A3)

                inicio, fin = self.analyzer.cut_data_min_max_values(filtered_A, t)
                age = self.extract_age_from_filename(file_name)
                num_peaks = self.analyzer.find_peaks(filtered_A[inicio:fin])

                if age not in peak_counts:
                    peak_counts[age] = []
                peak_counts[age].append(num_peaks)

        return peak_counts

if __name__ == "__main__":
    app = MainApp(directory='../Organizados2/Sano/female', output_format='fig', output_path='../pruebas/grafica_NoSanos_female_conjunto5.pdf')
    app.run()

