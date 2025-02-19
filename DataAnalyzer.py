import numpy as np
from DataLoader import DataLoader
from DataProcessor import DataProcessor

class DataAnalyzer:
    def __init__(self):
        self.loader = DataLoader()
        self.processor = DataProcessor()
    def find_peaks(self, data):
        peaks = (np.roll(data, 1) < data) & (np.roll(data, -1) < data)
        return peaks.sum()

    def show_peaks(self, data):
        peaks = (np.roll(data, 1) < data) & (np.roll(data, -1) < data)
        peak_indexs = np.where(peaks)[0]
        return peak_indexs

    def max_value(self, file):
        t, A, filtered_A = self.processor.calculate_acceleration(file)
        if A.max()*10 <= 50 or t.max() < 2.9:
            return False
        return True
    def cut_data_min_max_values(self, filtered_A, t):
        indice_maximo = np.where(filtered_A == filtered_A.max())[0][0]
        inicio = np.where(filtered_A[:indice_maximo] == filtered_A[:indice_maximo].min())[0][-1]
        fin = np.where(filtered_A == filtered_A[indice_maximo:].min())[0][0]
        return inicio, fin

    def cut_data_max_value(self, filtered_A, t):
        indice_maximo = np.where(filtered_A == filtered_A.max())[0][0]
        inicio = fin = 0
        for i, valor in enumerate(filtered_A[:indice_maximo][::-1]):
            if -1 <= valor <= 1:
                inicio = indice_maximo - i
                break
        for i, valor in enumerate(filtered_A[indice_maximo:]):
            if -1 <= valor <= 1 or (indice_maximo + i) == 299:
                fin = indice_maximo + i
                break


        return inicio, fin