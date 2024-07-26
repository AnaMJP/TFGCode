import os
from DataProcessor import DataProcessor


class FileOrganizer:
    def __init__(self, directories):
        self.directories = directories
        self.age_data = {}
        self.processor = DataProcessor()

    def max_value(self, file):
        t, A, filtered_A = self.processor.calculate_acceleration(file)
        if A.max() * 10 <= 50 or t.max() < 2.9:
            return False
        return True

    def organize_files(self):
        for directory in self.directories:
            for subdir, dirs, _ in os.walk(directory):
                for dir_name in dirs:
                    child_path = os.path.join(subdir, dir_name)
                    for child_subdir, child_dirs, _ in os.walk(child_path):
                        for child_dir_name in child_dirs:
                            child_dir = os.path.join(child_subdir, child_dir_name)
                            #print(f'Processing directory: {child_dir}')
                            age = child_dir_name.split('_')[1]
                            if age not in self.age_data:
                                self.age_data[age] = {'children': 0, 'files': 0}

                            valid_files = 0
                            for file_name in os.listdir(child_dir):
                                if "_L_" in file_name and self.max_value(os.path.join(child_dir, file_name)):
                                    valid_files += 1

                            if valid_files > 0: #solo se cuenta al niño si tiene datos válidos
                                self.age_data[age]['children'] += 1
                                self.age_data[age]['files'] += valid_files

                        break

    def get_results(self):
        return self.age_data


directories = [
    '../Organizados/No_Sano/male'
]

organizer = FileOrganizer(directories)
organizer.organize_files()
results = organizer.get_results()

for age, counts in results.items():
    print(f'Edad: {age}')
    print(f'  Niños: {counts["children"]}')
    print(f'  Total excels: {counts["files"]}')
