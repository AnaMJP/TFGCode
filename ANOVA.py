import numpy as np
import pandas as pd
import scipy.stats as stats
class ANOVA:

    def perform_anova_on_peak_counts(self, peak_counts_cases):
        all_ages = sorted(
            set().union(*[peak_counts.keys() for peak_counts in peak_counts_cases]))  # Obtener todas las edades únicas

        for age_group in all_ages:
            all_data = []
            all_labels = []

            for case_num, peak_counts in enumerate(peak_counts_cases, start=1):
                if age_group in peak_counts:
                    all_data.extend(peak_counts[age_group])
                    all_labels.extend([f'Case{case_num}'] * len(peak_counts[age_group]))

            df = pd.DataFrame({'count': all_data, 'case': all_labels})

            f_value, p_value = stats.f_oneway(
                df[df['case'] == 'Case1']['count'],
                df[df['case'] == 'Case2']['count'],
            )

            print(f"Edad {age_group} - P-Value: {p_value}", end=" ")

            # Si hay diferencias significativas, realizar la prueba de Tukey
            if p_value < 0.05:
                print("Hay diferencias significativas entre los grupos de edad.")
            else:
                print("No hay diferencias significativas entre los casos.")

