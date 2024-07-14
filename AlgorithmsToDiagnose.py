import os
import numpy as np
from DataProcessor import DataProcessor
from DataAnalyzer import DataAnalyzer
class AlgorithmsToDiagnose:

    def __init__(self):
        self.analyzer = DataAnalyzer()
        self.processor = DataProcessor()

    def get_peak_counts(self, files, measure):
        peak_counts= {}
        for file in files:
            t, A, filtered_A = self.processor.calculate_acceleration(file)
            t, Vt, filtered_Vt = self.processor.calculate_velocity(file)

            start, end = self.analyzer.cut_data_max_value(filtered_A, t)
            age = self.extract_age_from_filename(file)
            age_group = (int(age) // 4) * 4

            if age_group >= 18:
                continue

            if measure == "Velocity":
                num_peaks = self.analyzer.find_peaks(Vt[start:end])
            elif measure == "Acceleration":
                num_peaks = self.analyzer.find_peaks(A[start:end])
            else:
                raise ValueError("Medida no válida. Debe ser 'Acceleration' o 'Velocity'.")

            if age_group not in peak_counts:
                peak_counts[age_group] = []
            peak_counts[age_group].append(num_peaks)

        return peak_counts
    def get_peak_counts_per_seconds(self, files, measure):
        peak_counts_per_second = {}
        for file in files:
            t, A, filtered_A = self.processor.calculate_acceleration(file)
            t, Vt, filtered_Vt = self.processor.calculate_velocity(file)

            start, end = self.analyzer.cut_data_max_value(filtered_A, t)
            age = self.extract_age_from_filename(file)
            age_group = (int(age) // 4) * 4

            if age_group >= 18:
                continue

            if measure == "Velocity":
                num_peaks = self.analyzer.find_peaks(Vt[start:end])
            elif measure == "Acceleration":
                num_peaks = self.analyzer.find_peaks(A[start:end])
            else:
                raise ValueError("Medida no válida. Debe ser 'Acceleration' o 'Velocity'.")

            duration = t[end] - t[start]
            peaks_per_second = num_peaks / duration

            if age_group not in peak_counts_per_second:
                peak_counts_per_second[age_group] = []
            peak_counts_per_second[age_group].append(peaks_per_second)

        return peak_counts_per_second

    def extract_age_from_filename(self, file_name):
        age = os.path.basename(os.path.dirname(os.path.dirname(file_name)))
        return age

    def get_duration_per_age_group(self, files):
        duration_per_age_group = {}
        for file in files:
            t, A, filtered_A = self.processor.calculate_acceleration(file)
            t, Vt, filtered_Vt = self.processor.calculate_velocity(file)

            start, end = self.analyzer.cut_data_max_value(filtered_A, t)
            age = self.extract_age_from_filename(file)
            age_group = (int(age) // 4) * 4

            if age_group >= 18:
                continue

            duration = t[end] - t[start]

            if age_group not in duration_per_age_group:
                duration_per_age_group[age_group] = []
            duration_per_age_group[age_group].append(duration)

        return duration_per_age_group

    def time_from_start_to_maxPeak(self, files, measure):
        time_to_max_peak = {}
        for file in files:
            t, A, filtered_A = self.processor.calculate_acceleration(file)
            t, Vt, filtered_Vt = self.processor.calculate_velocity(file)

            start, end = self.analyzer.cut_data_max_value(filtered_A, t)
            age = self.extract_age_from_filename(file)
            age_group = (int(age) // 4) * 4
            try:
                if measure == "Velocity":
                    indice_maximo = np.where(Vt[start:end] == Vt[start:end].max())[0][0]
                elif measure == "Acceleration":
                    indice_maximo = np.where(A[start:end] == A[start:end].max())[0][0]
                else:
                    raise ValueError("Medida no válida. Debe ser 'Acceleration' o 'Velocity'.")
            except:
                print(f'Falló al analizar: {file}')

            time_to_peak = np.abs(t[indice_maximo] - t[start])

            if age_group not in time_to_max_peak:
                time_to_max_peak[age_group] = []
            time_to_max_peak[age_group].append(time_to_peak)

        return time_to_max_peak

    def maxPeak_value(self, files, measure):
        time_to_max_peak = {}
        for file in files:
            t, A, filtered_A = self.processor.calculate_acceleration(file)
            t, Vt, filtered_Vt = self.processor.calculate_velocity(file)

            start, end = self.analyzer.cut_data_max_value(filtered_A, t)
            age = self.extract_age_from_filename(file)
            age_group = (int(age) // 4) * 4
            try:
                if measure == "Velocity":
                    indice_maximo = Vt[start:end].max()
                elif measure == "Acceleration":
                    indice_maximo = A[start:end].max()
                else:
                    raise ValueError("Medida no válida. Debe ser 'Acceleration' o 'Velocity'.")
            except:
                print(f'Falló al analizar: {file}')


            if age_group not in time_to_max_peak:
                time_to_max_peak[age_group] = []
            time_to_max_peak[age_group].append(indice_maximo)

        return time_to_max_peak


