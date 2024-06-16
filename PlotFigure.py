import matplotlib.pyplot as plt
from DataAnalyzer import DataAnalyzer

class PlotFigure:
    def __init__(self):
        self.acc_fig = None
        self.acc_axs = None
        self.vel_fig = None
        self.vel_axs = None
        self.analyzer = DataAnalyzer()

    def create_acc_subplots(self, nrows, ncols, suptitle):
        self.acc_fig, self.acc_axs = plt.subplots(nrows, ncols, figsize=(15, nrows * 6))
        self.acc_fig.suptitle(suptitle, fontsize=18)
        return self.acc_axs

    def create_vel_subplots(self, nrows, ncols, suptitle):
        self.vel_fig, self.vel_axs = plt.subplots(nrows, ncols, figsize=(15, nrows * 6))
        self.vel_fig.suptitle(suptitle, fontsize=18)
        return self.vel_axs

    def plot_data(self, t, filtered_A, A, g, title, start=None, end=None, ax=None):
        ax.plot(t, A, 'g', label='Aceleración sin filtro')
        ax.plot(t, filtered_A, 'b', label='Aceleración con filtro')

        #ax.plot(t, g, 'b', label='Aceleracion gravitacional')
        ax.grid(True)
        ax.set_xlabel('Tiempo (s)', fontsize=16)
        ax.set_ylabel('Aceleración (m/s$^2$)', fontsize=16)
        ax.set_title(title)
        ax.legend(fontsize=18)

        if start is not None and end is not None:
            #ax.plot(t[start:end], filtered_A[start:end], 'r', label='Aceleracion (Cortada)')
            #ax.plot(t[start:end], g[start:end], 'y', label='Aceleracion gravitacional (Cortada)')
            ax.legend(fontsize=18)

    def plot_velocity(self, t, filtered_Vt, Vt, title, start=None, end=None, ax=None):
        ax.plot(t, Vt * 100, 'g', label='Velocidad sin filtro')
        ax.plot(t, filtered_Vt * 100, 'b', label='Velocidad con filtro')

        ax.grid(True)
        ax.set_title(title)#
        ax.set_xlabel('Tiempo (s)', fontsize=16)
        ax.set_ylabel('Velocidad (m/s)', fontsize=16)
        ax.legend(fontsize=18)

        if start is not None and end is not None:
             #ax.plot(t[start:end], Vt[start:end] * 100, 'r', label='Velocidad (Cortada)')
             ax.legend(fontsize=18)
             #peak_indices = self.analyzer.show_peaks(Vt[start:end])
             #ax.plot(t[start:end][peak_indices], Vt[start:end][peak_indices]*100, 'ro', markersize=5)

    def show(self):
        if self.acc_fig is not None:
            self.acc_fig.tight_layout(rect=[0, 0.03, 1, 0.95])
            self.acc_fig.subplots_adjust(hspace=0.6)
        if self.vel_fig is not None:
            self.vel_fig.tight_layout(rect=[0, 0.03, 1, 0.95])
            self.vel_fig.subplots_adjust(hspace=0.6)
        plt.show()