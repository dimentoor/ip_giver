import pandas as pd


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
        print(self.df)
        return self.df

    def new_df(self):
        self.cut_df = pd.DataFrame(data=self.df[['cs-method', 'cs-username', 'c-ip']])
        print(self.cut_df)
        pass

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

    def save_result(self):
        pass
        # object of  file dumper
