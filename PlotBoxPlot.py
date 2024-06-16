import matplotlib.pyplot as plt
import numpy as np


class PlotBoxPlot:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 8))

    def plot_data(self, peak_counts, title):
        sorted_ages = sorted(peak_counts.keys(), key=int)  # Ordenar edades de menor a mayor
        data = [peak_counts[age] for age in sorted_ages]

        # Mostrar el boxplot con medias
        boxplot = self.ax.boxplot(data)

        self.ax.set_xticklabels(sorted_ages, fontsize=13)
        self.ax.set_title(title)
        self.ax.set_xlabel('Age', fontsize=14)
        self.ax.set_ylabel('Number of Peaks', fontsize=14)
        self.ax.set_ylim(top=100, bottom=0)

        # Calcular y mostrar los valores de la media, mediana y el número de archivos sobre cada boxplot
        means = [np.mean(peak_counts[age]) for age in sorted_ages]
        medians = [np.median(peak_counts[age]) for age in sorted_ages]
        file_counts = [len(peak_counts[age]) for age in sorted_ages]

        for mean, median, count, xpos in zip(means, medians, file_counts, range(1, len(sorted_ages) + 1)):
            self.ax.text(xpos, median, f' {median:.2f}', ha='center', va='top', color='orange')
            self.ax.text(xpos, self.ax.get_ylim()[0] + 0.1, f'n={count}', ha='center', va='bottom', fontsize=12, color='blue')

        plt.tight_layout()
        plt.show()

    def close(self):
        plt.close(self.fig)
