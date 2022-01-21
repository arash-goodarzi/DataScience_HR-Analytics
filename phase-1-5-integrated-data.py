import pandas as pd
import os


def create_one_csv_from_csv_folder(abs_path_folder):
    # loop through the directory
    all_files = [os.path.join(abs_path_folder, i) for i in os.listdir(abs_path_folder)]

    # create one dataframe
    df_result = pd.concat(map(pd.read_csv, all_files), ignore_index=True)

    df_result.to_csv('.\\data\\integrated_data' + '.csv')


create_one_csv_from_csv_folder(r"D:\project\glassdoor-data-data-science\2022-01-19-10-55-23")
df = pd.read_csv(".\data\integrated_data.csv")

print(df)
