import matplotlib.pyplot as plt
import os
import numpy as np
from DataAnalyzer import DataAnalyzer
from DataProcessor import DataProcessor

class PlotFigure:
    def __init__(self):
        self.acc_fig = None
        self.acc_axs = None
        self.vel_fig = None
        self.vel_axs = None
        self.analyzer = DataAnalyzer()
        self.processor = DataProcessor()

    def show_plots(self, files):
        first_files_per_folder = {}
        for file in files:
            folder = os.path.dirname(file)
            if folder not in first_files_per_folder:
                first_files_per_folder[folder] = file
        files = list(first_files_per_folder.values())[:8]

        n_files = len(files)
        self.create_acc_subplots(n_files // 2 + 1, 2, '')
        self.create_vel_subplots(n_files // 2 + 1, 2, '')
        idx = 0
        for file_name in files:
            self.process_file_subplot("../Organizados2/Sano/female\8\\23000049_8_F\D_C_23000049_L_child__1_119_LPM_2024_03_06_12_50_03_T1_1.csv", idx)
            idx += 1
        self.show()

    def create_acc_subplots(self, nrows, ncols, suptitle):
        self.acc_fig, self.acc_axs = plt.subplots(nrows, ncols, figsize=(15, nrows * 6))
        self.acc_fig.suptitle(suptitle, fontsize=18)
        return self.acc_axs

    def create_vel_subplots(self, nrows, ncols, suptitle):
        self.vel_fig, self.vel_axs = plt.subplots(nrows, ncols, figsize=(15, nrows * 6))
        self.vel_fig.suptitle(suptitle, fontsize=18)
        return self.vel_axs

    def process_file_subplot(self, file_name, idx):
        t, A, filtered_A = self.processor.calculate_acceleration(file_name)

        inicio, fin = self.analyzer.cut_data_max_value(filtered_A, t)
        row, col = divmod(idx, 2)
        self.plot_data(t, filtered_A, A, "", start=inicio, end=fin, ax=self.acc_axs[row, col])

        peak_indices = self.analyzer.show_peaks(A[inicio:fin])
        self.acc_axs[row, col].plot(t[inicio:fin][peak_indices], A[inicio:fin][peak_indices], 'ro',
                                            markersize=5)

        t, Vt, filtered_Vt = self.processor.calculate_velocity(file_name)

        self.plot_velocity(t[:-1], filtered_Vt, Vt, "", start=inicio, end=fin,
                                   ax=self.vel_axs[row, col])

    def plot_data(self, t, filtered_A, A, title, start=None, end=None, ax=None):
        ax.plot(t, A, 'g', label='Aceleración sin filtro')
        #ax.plot(t, filtered_A, 'b', label='Aceleración con filtro')

        #ax.plot(t, g, 'b', label='Aceleracion gravitacional')
        ax.grid(True)
        ax.set_xlabel('Tiempo (s)', fontsize=18)
        ax.set_ylabel('Aceleración (m/s$^2$)', fontsize=18)
        ax.set_title(title)
        ax.legend(fontsize=12)

        if start is not None and end is not None:
            ax.plot(t[start:end],A[start:end], 'r', label='Aceleración (Cortada)')
            #ax.plot(t[start:end], g[start:end], 'y', label='Aceleracion gravitacional (Cortada)')
            ax.legend(fontsize=12)

    def plot_velocity(self, t, filtered_Vt, Vt, title, start=None, end=None, ax=None):
        ax.plot(t, Vt * 100, 'g', label='Velocidad sin filtro')
        #ax.plot(t, filtered_Vt * 100, 'b', label='Velocidad con filtro')

        ax.grid(True)
        ax.set_title(title)
        ax.set_xlabel('Tiempo (s)', fontsize=18)
        ax.set_ylabel('Velocidad (m/s)', fontsize=18)
        ax.legend(fontsize=12)

        if start is not None and end is not None:
             ax.plot(t[start:end], Vt[start:end] * 100, 'r', label='Velocidad (Cortada)')
             ax.legend(fontsize=12)
             peak_indices = self.analyzer.show_peaks(Vt[start:end])
             ax.plot(t[start:end][peak_indices], Vt[start:end][peak_indices]*100, 'ro', markersize=5)

    def show(self):
        if self.acc_fig is not None:
            self.acc_fig.tight_layout(rect=[0, 0.03, 1, 0.95])
            self.acc_fig.subplots_adjust(hspace=0.6)
        if self.vel_fig is not None:
            self.vel_fig.tight_layout(rect=[0, 0.03, 1, 0.95])
            self.vel_fig.subplots_adjust(hspace=0.6)
        plt.show()