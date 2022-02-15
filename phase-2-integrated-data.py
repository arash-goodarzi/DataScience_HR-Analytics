"""
Created on Tue Jan 23 11:42:16 2022

@author: arash

"""




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

    # destination path
    destination_path = r'.\data\bucket.csv'
    df_result.to_csv(destination_path, index=False)


def append_data_achieve(new_file, source_file):
    df1 = pd.read_csv(new_file)
    df2 = pd.read_csv(source_file)
    df = pd.concat([df2, df1])

    df = df.drop_duplicates(subset=['job_id'], keep='first')
    # df = df[[c for c in df.columns if c.lower()[:7] != 'unnamed']]

    df.to_csv(source_file, index=False)

##### List of operations

# create_one_csv_from_csv_folder(r"D:\project\glassdoor-data-data-science\2022-02-13-09-37-08")
# append_data_achieve(r'.\data\bucket.csv', r'.\data\data.csv')
