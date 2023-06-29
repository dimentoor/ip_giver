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
        work_df.save_result(urls.save_path + '/' + '{}_{}'.format(file, 'REZ.xlsx'))

        # threats_objects.append(threats.ThreatsReport(path, urls.th_sheet_name))
        # dynamic_th.all_samples_th(threats_objects)
        # dynamic_th.save_result_th(urls.dsave_path_th)

    print("--- %s seconds ---" % (time.time() - start_time))
