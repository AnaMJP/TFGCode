from scipy.signal import butter, filtfilt

class DataFilter:
    def __init__(self, cutoff, fs, order=6):
        self.cutoff = cutoff
        self.fs = fs
        self.order = order

    def butter_lowpass(self):
        nyquist = 0.5 * self.fs
        normal_cutoff = self.cutoff / nyquist
        return butter(self.order, normal_cutoff, btype='low', analog=False)

    def butter_lowpass_filter(self, data):
        b, a = self.butter_lowpass()
        return filtfilt(b, a, data)
