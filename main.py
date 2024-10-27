import pandas as pd
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

    print("Test")

    # geo_data = pd.read_csv(urls.path_csv)
    #
    # # print(geo_data)
    #
    # # sort
    # geo_data_rus = geo_data[geo_data['country_name'] == "Russia"]
    # # columns_name
    # geo_data_unique = geo_data.nunique()
    # test_df = geo_data_rus[['prefix', 'city_name', 'country_name',
    #                         'registered_country_name']]
    #                         # 'traits_is_anonymous_proxy', 'traits_is_satellite_provider']]
    #
    # # print(geo_data_unique)
    #
    # print(test_df)
