import matplotlib.pyplot as plt

class PlotFigure:
    def __init__(self):
        self.acc_fig = None
        self.acc_axs = None
        self.vel_fig = None
        self.vel_axs = None

    def create_acc_subplots(self, nrows, ncols, suptitle):
        self.acc_fig, self.acc_axs = plt.subplots(nrows, ncols, figsize=(15, nrows * 6))
        self.acc_fig.suptitle(suptitle, fontsize=16)
        return self.acc_axs

    def create_vel_subplots(self, nrows, ncols, suptitle):
        self.vel_fig, self.vel_axs = plt.subplots(nrows, ncols, figsize=(15, nrows * 6))
        self.vel_fig.suptitle(suptitle, fontsize=16)
        return self.vel_axs

    def plot_data(self, t, filtered_A, g, title, start=None, end=None, ax=None):
        ax.plot(t, filtered_A, 'g', label='Aceleracion')
        ax.plot(t, g, 'b', label='Aceleracion gravitacional')
        ax.grid(True)
        ax.set_title(title)
        ax.legend()

        if start is not None and end is not None:
            ax.plot(t[start:end], filtered_A[start:end], 'g', label='Aceleracion (Cortada)')
            ax.plot(t[start:end], g[start:end], 'b', label='Aceleracion gravitacional (Cortada)')
            ax.legend()

    def plot_velocity(self, t, Vt, title, start=None, end=None, ax=None):
        ax.plot(t, Vt * 100, label='Velocidad')
        ax.grid(True)
        ax.set_title(title)
        ax.legend()

        if start is not None and end is not None:
            ax.plot(t[start:end], Vt[start:end] * 100, 'r', label='Velocidad (Cortada)')
            ax.legend()

    def show(self):
        if self.acc_fig is not None:
            self.acc_fig.tight_layout(rect=[0, 0.03, 1, 0.95])
        if self.vel_fig is not None:
            self.vel_fig.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()