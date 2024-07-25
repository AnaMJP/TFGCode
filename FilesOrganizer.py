import os
from DataAnalyzer import DataAnalyzer
class FilesOrganizer:

    def __init__(self, directories):
        self.analyzer = DataAnalyzer()
        self.directories = directories
    def organize_by_gender(self):
        files_SanoFemale = []
        files_NoSanoFemale = []
        files_SanoMale = []
        files_NoSanoMale = []
        for directory in self.directories:
            for subdir, _, file_names in os.walk(directory):
                for file_name in file_names:
                    if directory == '../Organizados/Sano/female':
                        files_SanoFemale.append(os.path.join(subdir, file_name))
                    elif directory == '../Organizados/No_Sano/female':
                        files_NoSanoFemale.append(os.path.join(subdir, file_name))
                    elif directory == '../Organizados/Sano/male':
                        files_SanoMale.append(os.path.join(subdir, file_name))
                    elif directory == '../Organizados/No_Sano/male':
                        files_NoSanoMale.append(os.path.join(subdir, file_name))

        filtered_files_SanoFemale = [file for file in files_SanoFemale if "_L_" in file and self.analyzer.max_value(file)]
        filtered_files_NoSanoFemale = [file for file in files_NoSanoFemale if
                                       "_L_" in file and self.analyzer.max_value(file)]
        filtered_files_SanoMale = [file for file in files_SanoMale if "_L_" in file and self.analyzer.max_value(file)]
        filtered_files_NoSanoMale = [file for file in files_NoSanoMale if "_L_" in file and self.analyzer.max_value(file)]

        return filtered_files_SanoFemale, filtered_files_NoSanoFemale, filtered_files_SanoMale, filtered_files_NoSanoMale