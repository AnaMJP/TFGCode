import numpy as np

class DataLoader:
    def load_data(self, file_path):
        return np.loadtxt(file_path, delimiter=',')