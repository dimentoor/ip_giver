# import pandas as pd
import open_save
import converter

if __name__ == '__main__':
    path = "/Users/dmitrybaraboshkin/PycharmProjects/ip_giver/input_info/logfile"
    save_path = "/Users/dmitrybaraboshkin/PycharmProjects/ip_giver/output_info/test_excel.xlsx"

    test_list = open_save.FileLoader(path)
    test_list = test_list.read_file()  # list file

    work_df = converter.Converter(test_list)
    work_df.convert_df()
    converted_df = work_df.convert_cols()
    # work_df.new_df()

    save_df = open_save.FileDumper(save_path, 'test', converted_df)
    save_df = save_df.write_file()
