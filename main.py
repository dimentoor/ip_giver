# import pandas as pd
import os
import time
import open_save
import converter
import urls

start_time = time.time()

if __name__ == '__main__':

    test_list = open_save.FileLoader(urls.input_path)

    # list of file names
    file_names = test_list.open_folder()
    # open file and write content into list using split. got list
    for file in range(len(file_names)):
        print(file_names[file])
        loader_obj = open_save.FileLoader(file_names[file])
        loader_obj_fix = loader_obj.read_file()

        work_df = converter.Converter(loader_obj_fix)
        work_df.use_all_functions()
        if file + 1 == len(file_names):
            print('---------')
            work_df.group_ip()
            work_df.save_result(urls.save_path + '/' + '{}_{}'.format('test', 'test.xlsx'))

    print("--- %s seconds ---" % (time.time() - start_time))
