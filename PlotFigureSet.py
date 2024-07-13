import matplotlib.pyplot as plt
import os
from DataAnalyzer import DataAnalyzer
from DataProcessor import DataProcessor


class PlotFigureSet:
    def __init__(self):
        self.analyzer = DataAnalyzer()
        self.processor = DataProcessor()

    def show_plots_set(self, files):
        files_per_folder = {}

        for file in files:
            folder = os.path.dirname(file)
            if folder not in files_per_folder:
                files_per_folder[folder] = []
            files_per_folder[folder].append(file)

        for folder, folder_files in files_per_folder.items():
            self.create_acc_subplots(1, 1, f'Acceleration plots for {folder}')
            self.create_vel_subplots(1, 1, f'Velocity plots for {folder}')

            idx = 0
            for file_name in folder_files:
                self.process_file_subplot(file_name, idx)
                idx += 1

            self.show()

    def create_acc_subplots(self, nrows, ncols, suptitle):
        self.acc_fig, self.acc_axs = plt.subplots(nrows, ncols, figsize=(15, 6))
        self.acc_fig.suptitle(suptitle, fontsize=18)
        return self.acc_axs

    def create_vel_subplots(self, nrows, ncols, suptitle):
        self.vel_fig, self.vel_axs = plt.subplots(nrows, ncols, figsize=(15, 6))
        self.vel_fig.suptitle(suptitle, fontsize=18)
        return self.vel_axs

    def process_file_subplot(self, file_name, idx):
        t, A, filtered_A = self.processor.calculate_acceleration(file_name)
        inicio, fin = self.analyzer.cut_data_max_value(filtered_A, t)

        self.plot_data(t, filtered_A, A, "", start=inicio, end=fin, ax=self.acc_axs)

        peak_indices = self.analyzer.show_peaks(A[inicio:fin])
        self.acc_axs.plot(t[inicio:fin][peak_indices], A[inicio:fin][peak_indices], 'ro', markersize=5)

        t, Vt, filtered_Vt = self.processor.calculate_velocity(file_name)
        self.plot_velocity(t[:-1], filtered_Vt, Vt, "", start=inicio, end=fin, ax=self.vel_axs)

    def plot_data(self, t, filtered_A, A, title, start=None, end=None, ax=None):
        ax.plot(t, A, 'g', label='Aceleración sin filtro')
        ax.grid(True)
        ax.set_xlabel('Tiempo (s)', fontsize=16)
        ax.set_ylabel('Aceleración (m/s$^2$)', fontsize=16)
        ax.set_title(title)
        ax.legend(fontsize=12)

        if start is not None and end is not None:
            ax.plot(t[start:end], A[start:end], 'r', label='Aceleración (Cortada)')
            ax.legend(fontsize=12)

    def plot_velocity(self, t, filtered_Vt, Vt, title, start=None, end=None, ax=None):
        ax.plot(t, Vt * 100, 'g', label='Velocidad sin filtro')
        ax.grid(True)
        ax.set_title(title)
        ax.set_xlabel('Tiempo (s)', fontsize=16)
        ax.set_ylabel('Velocidad (m/s)', fontsize=16)
        ax.legend(fontsize=12)

        if start is not None and end is not None:
            ax.plot(t[start:end], Vt[start:end] * 100, 'r', label='Velocidad (Cortada)')
            ax.legend(fontsize=12)
            peak_indices = self.analyzer.show_peaks(Vt[start:end])
            ax.plot(t[start:end][peak_indices], Vt[start:end][peak_indices] * 100, 'ro', markersize=5)

    def show(self):
        if self.acc_fig is not None:
            self.acc_fig.tight_layout(rect=[0, 0.03, 1, 0.95])
            self.acc_fig.subplots_adjust(hspace=0.6)
        if self.vel_fig is not None:
            self.vel_fig.tight_layout(rect=[0, 0.03, 1, 0.95])
            self.vel_fig.subplots_adjust(hspace=0.6)
        plt.show()
