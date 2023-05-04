import pandas as pd
import open_save


class Converter:
    def __init__(self, file_list):
        self.file_list = file_list
        self.df = pd.DataFrame()
        self.cut_df = pd.DataFrame()  # think that this is incorrect
        self.clear_df = pd.DataFrame()
        self.ip_df = pd.DataFrame()

    # convert list of logs to df (include all columns)
    def convert_df(self):
        count_of_items = 0
        clear_file_list = list()
        for item in self.file_list:
            for item_1 in item:
                count_of_items += 1
            if count_of_items == 14:
                clear_file_list.append(item)
            else:
                print(item)
            count_of_items = 0

        self.df = pd.DataFrame(clear_file_list,
                               columns=['date', 'time', 's-ip', 'cs-method', 'cs-uri-stem', 'cs-uri-query', 's-port',
                                        'cs-username', 'c-ip', 'cs(User-Agent)', 'sc-status',
                                        'sc-substatus', 'sc-win32-status', 'time-taken'])
        # convert columns into correct type
        convert_dict = {'s-port': 'uint',
                        'sc-status': 'uint',
                        'sc-substatus': 'uint',
                        'sc-win32-status': 'uint',
                        'time-taken': 'int64'
                        }
        # df.astype({'col1': 'int32'}).dtypes

        datatypes = self.df.dtypes
        print(datatypes)
        self.df = self.df.astype(convert_dict)
        print("")
        print(datatypes)
        return self.df

    # get df with needed columns
    def new_df(self):
        self.cut_df = pd.DataFrame(data=self.df[['cs-method', 'cs-username', 'c-ip']])
        return self.cut_df

    # delete all requests  except POST
    def del_requests(self):
        cs_method_list = self.df['cs-method'].tolist()
        res_list = []
        for item in cs_method_list:
            if item not in res_list:
                res_list.append(item)
        # print list of all requests
        print(res_list)

        self.clear_df = self.cut_df[self.cut_df['cs-method'] == "POST"]
        return self.clear_df

    #  splits the field c-ip apart
    def ip_sep(self):
        ip_list_sep = list()
        # create dataframe preparing for the next changes
        self.ip_df = pd.DataFrame(self.clear_df, columns=['c-ip'])
        ip_list = self.ip_df['c-ip'].tolist()

        for line in ip_list:
            ip_list_sep.append(line.split('.'))

        self.ip_df = pd.DataFrame(ip_list_sep, columns=['num_1', 'num_2', 'num_3', 'num_4'])
        convert_dict_ip = {'num_1': int,
                           'num_2': int,
                           'num_3': int,
                           'num_4': int,
                           }
        tmp = self.ip_df[self.ip_df['num_1'] != "::1"]  # fix bugs
        self.ip_df = tmp.astype(convert_dict_ip)
        return self.ip_df

    #  use call functions
    def use_all_functions(self):
        self.convert_df()
        # self.new_df()
        # self.del_requests()
        # self.ip_sep()

    # write function execution result into xlsx document in different sheets
    def save_result(self, path):
        save = open_save.FileDumper(path)
        dict_elist = {
            "all_logs": self.df,
            "short_info": self.clear_df,
            "ip in dif cells": self.ip_df
        }
        save.write_file(dict_elist)
