import matplotlib.pyplot as plt
import numpy as np
from DataProcessor import DataProcessor
from AlgorithmsToDiagnose import AlgorithmsToDiagnose
from ANOVA import ANOVA

class PlotBoxPlot:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        self.processor = DataProcessor()
        self.diagnose = AlgorithmsToDiagnose()
        self.anova = ANOVA()


    def plot_data(self, peak_counts_list, titles):
        fig, axs = plt.subplots(2, 2, figsize=(15, 10))  # Crear una figura con 2x2 subplots
        axs = axs.flatten()  # Aplanar la matriz de ejes para un acceso más fácil

        for ax, peak_counts, title in zip(axs, peak_counts_list, titles):
            sorted_ages = sorted(peak_counts.keys(), key=int)  # Ordenar edades de menor a mayor
            sorted_ages_label = {f"{age}-{age+1}": age for age in sorted_ages}
            data = [peak_counts[age] for age in sorted_ages]

            # Mostrar el boxplot con medias
            boxplot = ax.boxplot(data)

            ax.set_title(title)
            ax.set_xlabel('Edad', fontsize=12)
            ax.set_ylabel('Numero de picos por tiempo ejecución', fontsize=12)
            ax.set_ylim(top=25, bottom=0)

            # Calcular y mostrar los valores de la media, mediana y el número de archivos sobre cada boxplot
            means = [np.mean(peak_counts[age]) for age in sorted_ages]
            medians = [np.median(peak_counts[age]) for age in sorted_ages]
            file_counts = [len(peak_counts[age]) for age in sorted_ages]

            for mean, median, count, xpos in zip(means, medians, file_counts, range(1, len(sorted_ages) + 1)):
                ax.text(xpos, median, f' {median:.2f}', ha='center', va='top', color='orange')
                ax.text(xpos, ax.get_ylim()[0] + 0.1, f'n={count}', ha='center', va='bottom', fontsize=10, color='blue')

        plt.tight_layout()
        plt.show()
        plt.close(fig)  # Cerrar la figura actual

    def plot_comparison_by_age(self, peak_counts_list, titles):
        ages = sorted(
            set().union(*[peak_counts.keys() for peak_counts in peak_counts_list]))  # Obtener todas las edades únicas
        num_ages = len(ages)
        fig, axs = plt.subplots(1, num_ages, figsize=(20, 10), sharey=True)
        axs = axs.flatten()

        for ax, age in zip(axs, ages):
            data = [peak_counts.get(age, []) for peak_counts in
                    peak_counts_list]

            # Mostrar el boxplot con medias
            boxplot = ax.boxplot(data, patch_artist=True, notch=True, vert=True, showmeans=True)

            ax.set_title(f'Age {age}')
            ax.set_xlabel('Category', fontsize=12)
            if ax == axs[0]:
                ax.set_ylabel('Numero de picos por tiempo ejecución', fontsize=12)
            ax.set_xticklabels(titles, rotation=45, ha='right', fontsize=10)
            ax.set_ylim(top=30, bottom=0)

            # Calcular y mostrar los valores de la media, mediana y el número de archivos sobre cada boxplot
            means = [np.mean(d) if len(d) > 0 else 0 for d in data]
            medians = [np.median(d) if len(d) > 0 else 0 for d in data]
            file_counts = [len(d) for d in data]

            for mean, median, count, xpos in zip(means, medians, file_counts, range(1, len(titles) + 1)):
                ax.text(xpos, median, f' {median:.2f}', ha='center', va='top', color='orange')
                ax.text(xpos, ax.get_ylim()[0] + 0.1, f'n={count}', ha='center', va='bottom', fontsize=10, color='blue')

        plt.tight_layout()
        plt.show()
        plt.close(fig)

    def peaks_count_boxplot(self,files_SanoFemale, files_NoSanoFemale, files_SanoMale, files_NoSanoMale):
        peak_counts_SanoFemale = self.diagnose.get_peak_counts_per_second(files_SanoFemale)
        peak_counts_NoSanoFemale = self.diagnose.get_peak_counts_per_second(files_NoSanoFemale)
        peak_counts_SanoMale = self.diagnose.get_peak_counts_per_second(files_SanoMale)
        peak_counts_NoSanoMale = self.diagnose.get_peak_counts_per_second(files_NoSanoMale)

        peak_counts_list = [peak_counts_SanoFemale, peak_counts_NoSanoFemale, peak_counts_SanoMale, peak_counts_NoSanoMale]
        titles = ['Sano female', 'No sano female', 'Sano male', 'No sano male']

        for index, counts in reversed(list(enumerate(peak_counts_list))):
            if len(counts) == 0:
                peak_counts_list.pop(index)
                titles.pop(index)

        self.anova.perform_anova_on_peak_counts(peak_counts_list)
        self.plot_comparison_by_age(peak_counts_list, titles)

    def close(self):
        plt.close(self.fig)




