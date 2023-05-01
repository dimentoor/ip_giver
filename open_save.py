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
    def __init__(self, path, sheet_name, df):
        self.path = path
        self.sheet_name = sheet_name
        self.df = df

    def write_file(self):
        with pd.ExcelWriter(self.path) as writer:
            self.df.to_excel(writer, sheet_name='test')
            print("Wrote to {}.".format(self.path))

    # def save_result(self, filename):
    #     dict_samples = {"unique_sample": self.unique,
    #                     "users_sample": self.users,
    #                     "black_list_sample": self.black_list,
    #                     "threat_types_sample": self.threat_types,
    #                     "types_sample": self.types}
    #     self.writefile(filename, dict_samples)

    # def writefile(self, filename, samples: dict):
    #     with pd.ExcelWriter(filename) as writer:
    #         for sample_name, sample in samples.items():
    #             sample.to_excel(writer, sheet_name=sample_name)
