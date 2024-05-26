import numpy as np

class DataAnalyzer:
    def find_peaks(self, data):
        peaks = (np.roll(data, 1) < data) & (np.roll(data, -1) < data)
        return peaks.sum()

    def show_peaks(self, data):
        peaks = (np.roll(data, 1) < data) & (np.roll(data, -1) < data)
        peak_indexs = np.where(peaks)[0]
        return peak_indexs

    def cut_data(self, filtered_A, t):
        indice_maximo = np.where(filtered_A == filtered_A.max())[0][0]
        inicio = fin = 0
        for i, valor in enumerate(filtered_A[:indice_maximo][::-1]):
            if -1 <= valor <= 1:
                inicio = indice_maximo - i
                break
        for i, valor in enumerate(filtered_A[indice_maximo:]):
            if -1 <= valor <= 1:
                fin = indice_maximo + i + 20
                break
        return inicio, fin