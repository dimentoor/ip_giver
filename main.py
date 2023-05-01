# import pandas as pd
import open_save
import converter
import urls

if __name__ == '__main__':

    test_list = open_save.FileLoader(urls.path)
    test_list = test_list.read_file()  # list file

    work_df = converter.Converter(test_list)
    work_df.all_samples_threats()
    work_df.save_result(urls.save_path)

    # work_df.convert_df()
    # converted_df = work_df.convert_cols()
    #
    # save_df = open_save.FileDumper(urls.save_path, 'test', converted_df)
    # save_df = save_df.write_file()
