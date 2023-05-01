import pandas as pd
import open_save
import urls


class Converter:
    def __init__(self, file_list):
        self.file_list = file_list
        self.df = pd.DataFrame()
        self.cut_df = pd.DataFrame()

    def convert_df(self):
        self.df = pd.DataFrame(self.file_list,
                               columns=['date', 'time', 's-ip', 'cs-method', 'cs-uri-stem', 'cs-uri-query', 's-port',
                                        'cs-username', 'c-ip', 'cs(User-Agent)', 'sc-status',
                                        'sc-substatus', 'sc-win32-status', 'time-taken'])
        return self.df

    def new_df(self):
        self.cut_df = pd.DataFrame(data=self.df[['cs-method', 'cs-username', 'c-ip']])
        return self.cut_df

    def convert_cols(self):
        # print(self.df)
        convert_dict = {'s-port': int,
                        'sc-status': int,
                        'sc-substatus': int,
                        'sc-win32-status': int,
                        'time-taken': int
                        }

        self.df = self.df.astype(convert_dict)
        return self.df

    def del_requests(self):
        # прочитать и записать в лист
        convert_dict = []
        # удалить строки

    #  coming soon
    def ip_sep(self):
        pass

    # start all functions
    def all_samples_threats(self):
        self.convert_df()
        self.convert_cols()
        self.new_df()

    def save_result(self, path):
        save = open_save.FileDumper(path)
        dict_elist = {"all_logs": self.df,
                      "short_info": self.cut_df}
        save.write_file(path, dict_elist)
        # object of  file dumper
