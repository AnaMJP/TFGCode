import matplotlib.pyplot as plt
import numpy as np
from DataProcessor import DataProcessor
from AlgorithmsToDiagnose import AlgorithmsToDiagnose
from ANOVA import ANOVA
from AlgorithmFactory import *

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

    def plot_comparison_by_age(self, peak_counts_list, titles, ylim, genders):
        plt.close('all')
        for peak_list, title, gender in zip(peak_counts_list, titles, genders):
            ages = sorted(
                set().union(*[peak_counts.keys() for peak_counts in peak_list]))  # Obtener todas las edades únicas
            num_ages = len(ages)
            fig, axs = plt.subplots(1, num_ages, figsize=(20, 10), sharey=True)
            axs = axs.flatten()

            for ax, age in zip(axs, ages):
                data = [peak_counts.get(age, []) for peak_counts in
                        peak_list]

                # Mostrar el boxplot con medias
                boxplot = ax.boxplot(data, patch_artist=True, notch=True, vert=True, showmeans=True)

                ax.set_title(f'{gender}, edad: {age} - {age+4}')
                if ax == axs[0]:
                    ax.set_ylabel('Numero de picos por tiempo ejecución', fontsize=12)
                ax.set_xticklabels(title, rotation=45, ha='right', fontsize=10)
                ax.set_ylim(top=ylim, bottom=0)

                # Calcular y mostrar los valores de la media, mediana y el número de archivos sobre cada boxplot
                means = [np.mean(d) if len(d) > 0 else 0 for d in data]
                medians = [np.median(d) if len(d) > 0 else 0 for d in data]
                file_counts = [len(d) for d in data]

                for mean, median, count, xpos in zip(means, medians, file_counts, range(1, len(title) + 1)):
                    ax.text(xpos, median, f' {median:.2f}', ha='center', va='top', color='orange')
                    ax.text(xpos, ax.get_ylim()[0] + 0.1, f'n={count}', ha='center', va='bottom', fontsize=10, color='blue')

            plt.tight_layout()
            plt.show()
            plt.close(fig)

    def peaks_count_boxplot(self, algorithm, measure, files_SanoFemale, files_NoSanoFemale, files_SanoMale, files_NoSanoMale):
        counts_list = []
        titles = []
        genders = []

        algorithm_execute = AlgorithmFactory.create_algorithm(algorithm, self.diagnose)
        counts_SanoFemale, counts_NoSanoFemale, counts_SanoMale, counts_NoSanoMale, ylim = algorithm_execute.execute(
            measure, files_SanoFemale, files_NoSanoFemale, files_SanoMale, files_NoSanoMale
        )

        peak_counts_list_female = [counts_SanoFemale, counts_NoSanoFemale]
        peak_counts_list_male = [counts_SanoMale, counts_NoSanoMale]

        titles_female = ['Neurotípico', 'Neurodivergente']
        titles_male = ['Neurotípico', 'Neurodivergente']

        if len(peak_counts_list_female[0]) != 0:
            counts_list.append(peak_counts_list_female)
            titles.append(titles_female)
            genders.append('Femenino')

        if len(peak_counts_list_male[0]) != 0:
            counts_list.append(peak_counts_list_male)
            titles.append(titles_male)
            genders.append('Masculino')

        if len(counts_list) != 0:
            self.anova.perform_anova_on_peak_counts(counts_list)
            self.plot_comparison_by_age(counts_list, titles, ylim, genders)
        else:
            print("No data")

    def close(self):
        plt.close(self.fig)




