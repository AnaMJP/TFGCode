class AlgorithmFactory:
    @staticmethod
    def create_algorithm(algorithm_type, diagnose):
        if algorithm_type == "peaks_count":
            return PeaksCountAlgorithm(diagnose)
        if algorithm_type == "peaks_count_per_seconds":
            return PeaksCountPerSecondsAlgorithm(diagnose)
        elif algorithm_type == "duration_counts":
            return DurationCountsAlgorithm(diagnose)
        elif algorithm_type == "time_to_max_peak":
            return TimeToMaxPeak(diagnose)
        elif algorithm_type == "max_peak_value":
            return MaxPeakValue(diagnose)
        else:
            raise ValueError(f"Tipo de algoritmo no válido: {algorithm_type}")

class PeaksCountAlgorithm:
    def __init__(self, diagnose):
        self.diagnose = diagnose
    def execute(self, measure, files_SanoFemale, files_NoSanoFemale, files_SanoMale, files_NoSanoMale):
        counts_SanoFemale = self.diagnose.get_peak_counts(files_SanoFemale, measure)
        counts_NoSanoFemale = self.diagnose.get_peak_counts(files_NoSanoFemale, measure)
        counts_SanoMale = self.diagnose.get_peak_counts(files_SanoMale, measure)
        counts_NoSanoMale = self.diagnose.get_peak_counts(files_NoSanoMale, measure)
        ylim = 50
        return counts_SanoFemale, counts_NoSanoFemale, counts_SanoMale, counts_NoSanoMale, ylim
class PeaksCountPerSecondsAlgorithm:
    def __init__(self, diagnose):
        self.diagnose = diagnose
    def execute(self, measure, files_SanoFemale, files_NoSanoFemale, files_SanoMale, files_NoSanoMale):
        counts_SanoFemale = self.diagnose.get_peak_counts_per_seconds(files_SanoFemale, measure)
        counts_NoSanoFemale = self.diagnose.get_peak_counts_per_seconds(files_NoSanoFemale, measure)
        counts_SanoMale = self.diagnose.get_peak_counts_per_seconds(files_SanoMale, measure)
        counts_NoSanoMale = self.diagnose.get_peak_counts_per_seconds(files_NoSanoMale, measure)
        ylim = 50
        return counts_SanoFemale, counts_NoSanoFemale, counts_SanoMale, counts_NoSanoMale, ylim

class DurationCountsAlgorithm:
    def __init__(self, diagnose):
        self.diagnose = diagnose
    def execute(self, measure, files_SanoFemale, files_NoSanoFemale, files_SanoMale, files_NoSanoMale):
        counts_SanoFemale = self.diagnose.get_duration_per_age_group(files_SanoFemale)
        counts_NoSanoFemale = self.diagnose.get_duration_per_age_group(files_NoSanoFemale)
        counts_SanoMale = self.diagnose.get_duration_per_age_group(files_SanoMale)
        counts_NoSanoMale = self.diagnose.get_duration_per_age_group(files_NoSanoMale)
        ylim = 2
        return counts_SanoFemale, counts_NoSanoFemale, counts_SanoMale, counts_NoSanoMale, ylim

class TimeToMaxPeak:
    def __init__(self, diagnose):
        self.diagnose = diagnose
    def execute(self, measure, files_SanoFemale, files_NoSanoFemale, files_SanoMale, files_NoSanoMale):
        counts_SanoFemale = self.diagnose.time_from_start_to_maxPeak(files_SanoFemale, measure)
        counts_NoSanoFemale = self.diagnose.time_from_start_to_maxPeak(files_NoSanoFemale, measure)
        counts_SanoMale = self.diagnose.time_from_start_to_maxPeak(files_SanoMale, measure)
        counts_NoSanoMale = self.diagnose.time_from_start_to_maxPeak(files_NoSanoMale, measure)
        ylim = 3
        return counts_SanoFemale, counts_NoSanoFemale, counts_SanoMale, counts_NoSanoMale, ylim

class MaxPeakValue:
    def __init__(self, diagnose):
        self.diagnose = diagnose
    def execute(self, measure, files_SanoFemale, files_NoSanoFemale, files_SanoMale, files_NoSanoMale):
        counts_SanoFemale = self.diagnose.maxPeak_value(files_SanoFemale, measure)
        counts_NoSanoFemale = self.diagnose.maxPeak_value(files_NoSanoFemale, measure)
        counts_SanoMale = self.diagnose.maxPeak_value(files_SanoMale, measure)
        counts_NoSanoMale = self.diagnose.maxPeak_value(files_NoSanoMale, measure)
        ylim = 30
        return counts_SanoFemale, counts_NoSanoFemale, counts_SanoMale, counts_NoSanoMale, ylim


