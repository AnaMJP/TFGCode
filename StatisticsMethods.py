import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import shapiro, levene, mannwhitneyu
class StatisticsMethods:

    def check_normality(self, peak_counts_cases):
        for peak_cases in peak_counts_cases:
            all_ages = sorted(
                set().union(*[peak_counts.keys() for peak_counts in peak_cases]))

            for age_group in all_ages:
                for case_num, peak_counts in enumerate(peak_cases, start=1):
                    if age_group in peak_counts:
                        counts = peak_counts[age_group]
                        stat, p = shapiro(counts)
                        print(f'\nShapiro-Wilk test para Case{case_num}, Age group: {age_group}: Statistics={stat}, p-value={p}')
                        if p > 0.05:
                            print('Sample looks Gaussian (fail to reject H0)')
                        else:
                            print('Sample does not look Gaussian (reject H0)')

    def check_homogeneity_of_variance(self, peak_counts_cases):
        for case_num, peak_cases in enumerate(peak_counts_cases, start=1):
            all_ages = sorted(
                set().union(*[peak_counts.keys() for peak_counts in peak_cases]))

            for age_group in all_ages:
                data = [peak_counts[age_group] for peak_counts in peak_cases if age_group in peak_counts]
                if len(data) > 1:
                    stat, p = levene(*data)
                    print(f'\nLevene test para Case {case_num}, Age group: {age_group}: Statistics={stat}, p-value={p}')
                    if p > 0.05:
                        print('Variances are equal (fail to reject H0)')
                    else:
                        print('Variances are not equal (reject H0)')

    def perform_Mann_Whitney_U_tests(self, peak_counts_cases):
        for peak_cases in peak_counts_cases:
            all_ages = sorted(
                set().union(*[peak_counts.keys() for peak_counts in peak_cases]))  # Obtener todas las edades únicas

            for age_group in all_ages:
                all_data = []
                all_labels = []

                for case_num, peak_counts in enumerate(peak_cases, start=1):
                    if age_group in peak_counts:
                        all_data.extend(peak_counts[age_group])
                        all_labels.extend([f'Case{case_num}'] * len(peak_counts[age_group]))

                df = pd.DataFrame({'count': all_data, 'case': all_labels})

                group1 = df[df['case'] == 'Case1']['count']
                group2 = df[df['case'] == 'Case2']['count']

                if len(group1) > 0 and len(group2) > 0:
                    u_statistic, p_value = stats.mannwhitneyu(group1, group2, alternative='two-sided')

                    print(f"Edad {age_group} - P-Value: {p_value}", end=" ")

                    # Verificar si hay diferencias significativas
                    if p_value < 0.05:
                        print("Hay diferencias significativas entre los grupos de edad.")
                    else:
                        print("No hay diferencias significativas entre los casos.")
                else:
                    print(f"Edad {age_group} - No hay suficientes datos para realizar la prueba de Mann-Whitney U.")


