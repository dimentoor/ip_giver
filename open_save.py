import pandas as pd


class FileLoader:
    def __init__(self, path):
        self.path = path
        self.list = list()

    # open and read file
    def read_file(self):
        with open(self.path, 'r+') as input_file:
            for line in input_file:
                # print(line.readline())
                self.list.append(line.split())
                # print(self.list)
        print("Read {}.".format(self.path))
        # print(self.list)
        return self.list


class FileDumper:
    def __init__(self, path):
        self.path = path

    @staticmethod
    def write_file(path, elist: dict):
        with pd.ExcelWriter(path) as writer:
            for list_name, df in elist.items():
                df.to_excel(writer, sheet_name=list_name)
        print("Wrote to {}.".format, path)

