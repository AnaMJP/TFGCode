import os
from DataProcessor import DataProcessor
from DataAnalyzer import DataAnalyzer
class AlgorithmsToDiagnose:

    def __init__(self):
        self.analyzer = DataAnalyzer()
        self.processor = DataProcessor()

    def get_peak_counts_per_second(self, files):
        peak_counts_per_second = {}
        for file in files:
            t, A, filtered_A = self.processor.calculate_acceleration(file)

            start, end = self.analyzer.cut_data_max_value(filtered_A, t)
            age = self.extract_age_from_filename(file)
            age_group = (int(age) // 2) * 2

            num_peaks = self.analyzer.find_peaks(A[start:end])

            duration = t[end] - t[start]
            peaks_per_second = num_peaks / duration

            if age_group not in peak_counts_per_second:
                peak_counts_per_second[age_group] = []
            peak_counts_per_second[age_group].append(peaks_per_second)

        return peak_counts_per_second

    def extract_age_from_filename(self, file_name):
        age = os.path.basename(os.path.dirname(os.path.dirname(file_name)))
        return age