from scipy.signal import butter, lfilter

class DataFilter:
    def __init__(self, cutoff=0.8, fs=10.0, order=6):
        self.cutoff = cutoff
        self.fs = fs
        self.order = order

    def butter_lowpass(self):
        return butter(self.order, self.cutoff, fs=self.fs, btype='low', analog=False)

    def butter_lowpass_filter(self, data):
        b, a = self.butter_lowpass()
        return lfilter(b, a, data)
