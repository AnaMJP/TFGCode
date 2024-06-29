import numpy as np
import scipy.integrate as integrate
from DataLoader import DataLoader
from DataFilter import DataFilter

class DataProcessor:

    def __init__(self, cutoff_frequency=0.95, fs=10.0):
        self.t = []
        self.A1 = []
        self.A2 = []
        self.A3 = []
        self.g = []

        self.filtered_A1 = []
        self.filtered_A2 = []
        self.filtered_A3 = []
        self.filtered_A = []
        self.A = []

        self.loader = DataLoader()
        self.filter = DataFilter(cutoff_frequency, fs)


    def process_file_data(self, file_name):
        data = self.loader.load_data(file_name)
        self.t = data[:, 0] - data[0, 0]
        self.A1 = np.abs(data[:, 1])
        self.A2 = np.abs(data[:, 2])
        self.A3 = np.abs(data[:, 3])
        self.g = data[:, 8]

        self.filtered_A1 = self.filter.butter_lowpass_filter(self.A1)
        self.filtered_A2 = self.filter.butter_lowpass_filter(self.A2)
        self.filtered_A3 = self.filter.butter_lowpass_filter(self.A3)


    def calculate_velocity(self, file_name):
        self.process_file_data(file_name)
        Vx = integrate.cumtrapz(self.A1, self.t, initial=0)
        Vy = integrate.cumtrapz(self.A2, self.t, initial=0)
        Vz = integrate.cumtrapz(self.A3, self.t, initial=0)
        filtered_Vx = integrate.cumtrapz(self.filtered_A1, self.t, initial=0)
        filtered_Vy = integrate.cumtrapz(self.filtered_A2, self.t, initial=0)
        filtered_Vz = integrate.cumtrapz(self.filtered_A3, self.t, initial=0)

        Vx -= np.mean(Vx)
        Vy -= np.mean(Vy)
        Vz -= np.mean(Vz)

        Vt = np.sqrt((np.diff(Vx) / np.diff(self.t)) ** 2 + (np.diff(Vy) / np.diff(self.t)) ** 2 + (np.diff(Vz) / np.diff(self.t)) ** 2)


        filtered_Vt = np.sqrt((np.diff(filtered_Vx) / np.diff(self.t)) ** 2 + (np.diff(filtered_Vy) / np.diff(self.t)) ** 2 + (
                    np.diff(filtered_Vz) / np.diff(self.t)) ** 2)

        return self.t, Vt, filtered_Vt

    def calculate_acceleration(self, file_name):
        self.process_file_data(file_name)
        self.A = self.A1 + self.A2 + self.A3
        self.filtered_A = self.filtered_A1 + self.filtered_A2 + self.filtered_A3

        return self.t, self.A, self.filtered_A


