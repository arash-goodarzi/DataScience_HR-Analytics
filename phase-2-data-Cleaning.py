"""
Created on Tue Jan 25 10:10:36 2022

@author: arash goodarzi
"""

import numpy as np
import pandas as pd

############################
# constants
title_enum = ["Data Science", "Data Software Engineer", "Data Software Engineer", "Data Scientist",
              "Data Support Analyst", "Machine Learning Enginee", "Data Analyst", "Data Visualization Analyst",
              "Data Specialist", "Computer Science"]
position_enum = ["Manager", "Senior", "Co-op", "Head of Enterprise", "Lead", "Fellowship", "Consultant"]

company_size_enum = ["1 to 50 Employees", "51 to 200 Employees", "201 to 500 Employees", "501 to 1000 Employees",
                     "1001 to 5000 Employees", "5001 to 10000 Employees", "10000+ Employees"]

company_size_dict = {"1 to 50 Employees": 25, "51 to 200 Employees": 100, "201 to 500 Employees": 350,
                     "501 to 1000 Employees": 750, "1001 to 5000 Employees": 3000, "5001 to 10000 Employees": 7500,
                     "10000+ Employees": 10000}


############################
# General function

def find_item_enum_txt(enum, txt):
    """return (bool,item)
    it return tuple that shows item is found or not
    and shows what is it
    """

    enum = [i.lower() for i in enum]
    txt = txt.lower()

    for item in enum:
        if item in txt:
            return (True, item)
    return (False, np.nan)


def find_items_enum_txt(enum, txt):
    """return []
    it returns array of found elements
    """
    res = []

    enum = [i.lower() for i in enum]
    txt = txt.lower()

    for item in enum:
        if item in txt:
            res.append(item)

    return res


############################
# main function

def clean_data(path_in, path_out):
    df = pd.read_csv(path_in)

    df.dropna(subset=["salary"], inplace=True)
    df = df.drop_duplicates(subset=['company_name', 'job_title'], keep='first')

    df["title"] = df["job_title"].apply(lambda x: find_item_enum_txt(title_enum, x)[1])
    df["position"] = df["job_title"].apply(lambda x: find_item_enum_txt(position_enum, x)[1]).replace(to_replace=np.nan,
                                                                                                      value="developer")

    df["per_hour"] = df["salary"].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
    df["salary"] = df["salary"].apply(
        lambda x: x.replace("(Glassdoor est.)", "").replace("Employer Provided Salary:", "").replace("$", "").replace(
            "K", "").replace("Per Hour", ""))

    df["salary"] = df["salary"].map(lambda x: list(map(int, filter(None, x.split('-')))))

    df[["min", "max"]] = pd.DataFrame(df.salary.tolist(), index=df.index)

    df["max"] = np.where(df["max"].isnull(), df["min"], df["max"])

    df["min"] = np.where(df["per_hour"] == 1, df["min"] * 1.8, df["min"])
    df["max"] = np.where(df["per_hour"] == 1, df["max"] * 1.8, df["max"])
    df["avg_salary"] = (df["min"] + df["max"]) / 2

    df.drop(['salary', 'min', 'max', 'salary_avg'], axis=1, inplace=True)

    df['desc_txt'] = df['descriptions_txt'].apply(
        lambda x: x.replace("[", "").replace("]", "").replace(",", "").replace("'", ""))
    df['desc_list'] = df['descriptions_list'].apply(
        lambda x: x.replace("[", "").replace("]", "").replace(",", "").replace("'", ""))
    df["desc"] = df['desc_txt'] + df['desc_list']

    df.drop(['desc_txt', 'desc_list', 'descriptions_txt', 'descriptions_list'], axis=1, inplace=True)

    df['pros'] = df['pros'].apply(
        lambda x: x.replace("[", "").replace("]", "").replace(",", "").replace("'", "").replace("\"", ""))
    df['cons'] = df['cons'].apply(
        lambda x: x.replace("[", "").replace("]", "").replace(",", "").replace("'", "").replace("\"", ""))

    df['salary_estimate'] = df['salary_estimate'].apply(
        lambda x: x.replace('.', '').replace('(', '').replace(')', '').replace(':', ''))

    df["company_size_number"] = df["company_size"].replace('Unknown', np.nan).replace(np.nan,
                                                                                      '1 to 50 Employees').astype(
        str).apply(lambda x: company_size_dict[x])

    # majority of companies who is not mention the size of their companies they are in small size range.
    #			1 to 50 Employees				small				25
    #			51 to 200 Employees				medium-sized		100
    #			201 to 500 Employees			medium-sized		350
    #			501 to 1000 Employees			large 				750
    #			1001 to 5000 Employees			large 				3000
    #			5001 to 10000 Employees			large				7500
    #			10000+ Employees				large 				10000

    df.to_csv(path_out, index=False)


clean_data(r'D:\project\DataScience_HR Analytics\data\integrated_data.csv',
           r'D:\project\DataScience_HR Analytics\data\integrated_data_clean.csv')


# ToDo
def enrich_data():
    pass
