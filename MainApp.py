import os
import numpy as np
from DataLoader import DataLoader
from DataFilter import DataFilter
from DataProcessor import DataProcessor
from DataAnalyzer import DataAnalyzer
from VisualizerFactory import *

class MainApp:
    def __init__(self, directory, output_format='pdf', output_path='output.pdf', cutoff_frequency=0.8, fs=10.0):
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

        if self.output_format == 'pdf':
            for file_name in files:
                if "_L_" in file_name:
                    self.process_file(file_name)
            self.plotter.close()
        else:
            n_files = len([f for f in files if "_L_" in f])
            self.plotter.create_acc_subplots(n_files // 2 + 1, 2, 'Aceleracion')
            self.plotter.create_vel_subplots(n_files // 2 + 1, 2, 'Velocidad')
            idx = 0
            for file_name in files:
                if "_L_" in file_name:
                    self.process_file_subplot(file_name, idx)
                    idx += 1
            self.plotter.show()

        print(f'Amplitudes: {self.amplitudes}')

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

        start, end = self.analyzer.cut_data(filtered_A, t)
        self.plotter.plot_data(t, filtered_A, g, "Aceleración\n" + file_name, start=start, end=end)

        self.amplitudes.append(filtered_A[start])

        Vx, Vy, Vz = self.processor.calculate_velocity(t, filtered_A1, filtered_A2, filtered_A3)
        Vt = np.sqrt((np.diff(Vx) / np.diff(t)) ** 2 + (np.diff(Vy) / np.diff(t)) ** 2 + (np.diff(Vz) / np.diff(t)) ** 2)
        self.plotter.plot_velocity(t[:-1], Vt, "Velocidad\n" + file_name, start=start, end=end)

    def process_file_subplot(self, file_name, idx):
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

        start, end =  self.analyzer.cut_data(filtered_A, t)
        row, col = divmod(idx, 2)
        self.plotter.plot_data(t, filtered_A, g, file_name, start=start, end=end, ax=self.plotter.acc_axs[row, col])

        Vx, Vy, Vz = self.processor.calculate_velocity(t, filtered_A1, filtered_A2, filtered_A3)
        Vt = np.sqrt((np.diff(Vx) / np.diff(t)) ** 2 + (np.diff(Vy) / np.diff(t)) ** 2 + (np.diff(Vz) / np.diff(t)) ** 2)

        self.plotter.plot_velocity(t[:-1], Vt, file_name, start=start, end=end, ax=self.plotter.vel_axs[row, col])


if __name__ == "__main__":
    app = MainApp(directory='../Organizados/female/3', output_format='pdf', output_path='../pruebas/grafica_NoSanos_female_conjunto5.pdf')
    app.run()

