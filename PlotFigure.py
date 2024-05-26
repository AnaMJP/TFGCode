import matplotlib.pyplot as plt

class PlotFigure:
    def __init__(self):
        self.fig = None
        self.axs = None

    def create_subplots(self, nrows, ncols, suptitle):
        self.fig, self.axs = plt.subplots(nrows, ncols, figsize=(15, nrows * 6))
        self.fig.suptitle(suptitle, fontsize=16)
        return self.axs

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

    def plot_velocity(self, t, Vt, title, ax=None):
        ax.plot(t, Vt * 100, label='Velocidad')
        ax.grid(True)
        ax.set_title(title)
        ax.legend()

    def show(self):
        plt.tight_layout()
        plt.show()