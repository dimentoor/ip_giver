# import pandas as pd
import open_save
import converter
import urls

if __name__ == '__main__':

    test_list = open_save.FileLoader(urls.input_path)
    # open file and write content into list using split. got list
    test_list = test_list.read_file()

    work_df = converter.Converter(test_list)
    work_df.use_all_functions()
    work_df.save_result(urls.save_path)


