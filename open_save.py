import pandas as pd
import os


class FileLoader:
    def __init__(self, path):
        self.path = path
        self.list = list()
        self.file_names = list()

    def open_folder(self):
        for filename in os.listdir(self.path):
            print(filename)
            if filename != '.DS_Store':
                f = os.path.join(self.path, filename)
                if os.path.isfile(f):
                    self.file_names.append(f)
        print(self.file_names)
        return self.file_names

    # open and read file
    def read_file(self):
        try:
            with open(self.path, 'r+') as input_file:
                for line in input_file:
                    self.list.append(line.split())
            print("Read {}.".format(self.path))
        except Exception:
            pass
        return self.list


class FileDumper:
    def __init__(self, path):
        self.path = path

    def write_file(self, elist: dict):
        with pd.ExcelWriter(self.path) as writer:
            for list_name, df in elist.items():
                df.to_excel(writer, sheet_name=list_name)
        print("Wrote to {}.".format, self.path)
