import pandas as pd
import os


def create_one_csv_from_csv_folder(abs_path_folder):
    # loop through the directory
    all_files = [os.path.join(abs_path_folder, i) for i in os.listdir(abs_path_folder)]

    # remove empty files
    [os.remove(path) for path in all_files if os.path.getsize(path) == 0]

    # recreate absolute pass after removing empty files
    all_files = [os.path.join(abs_path_folder, i) for i in os.listdir(abs_path_folder)]

    # create one dataframe
    df_result = pd.concat(map(pd.read_csv, all_files), ignore_index=True)

    df_result.to_csv('.\\data\\integrated_data' + '.csv', index=False)


create_one_csv_from_csv_folder(r"D:\project\glassdoor-data-data-science\2022-01-25-10-31-10")
