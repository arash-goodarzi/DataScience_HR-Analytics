"""
Created on Tue Jan 25 10:10:36 2022

@author: arash

Step 1: Remove duplicate or irrelevant observations. Remove unwanted observations from your dataset, including duplicate observations or irrelevant observations. ...
Step 2: Fix structural errors. ...
Step 3: Filter unwanted outliers. ...
Step 4: Handle missing data. ...

"""

import numpy as np
import pandas as pd

############################
# constants
title_enum = [
    "data scientist",
    "data science",
    "machine learning engineer",
    "machine learning",
    "machine learning scientist",
    "applications architect",
    "enterprise architect",
    "data architect",
    "infrastructure architect",
    "data engineer",
    "data software engineer",
    "data developer",
    "business intelligence",
    "statistician",
    "data analyst",
    "data support analyst",
    "data visualization analyst",
    "analytics",
    "data analytics analyst",
    "data analytics",
    "analyst",
    "bi analyst",
    "data specialist",
    "marketing scientist",
    "business intelligence analyst",
    "business analyst",
    "data modeler",
    "data steward",
    "data catalog",
    "decision science",
    "scientific software developer"
]

position_enum = ["Manager", "Senior", "Co-op", "Head of Enterprise", "Lead", "Fellowship", "Consultant"]

company_size_enum = ["1 to 50 Employees", "51 to 200 Employees", "201 to 500 Employees", "501 to 1000 Employees",
                     "1001 to 5000 Employees", "5001 to 10000 Employees", "10000+ Employees"]

company_size_dict = {"1 to 50 Employees": 25, "51 to 200 Employees": 100, "201 to 500 Employees": 350,
                     "501 to 1000 Employees": 750, "1001 to 5000 Employees": 3000, "5001 to 10000 Employees": 7500,
                     "10000+ Employees": 10000}

industries_enum = [
    "accounting & legal",
    "aerospace & defense",
    "agriculture & forestry",
    "arts, entertainment & recreation",
    "biotech & pharmaceuticals",
    "business services",
    "construction, repair & maintenance",
    "consumer services",
    "education",
    "finance",
    "government",
    "health care",
    "information technology",
    "insurance",
    "manufacturing",
    "media",
    "non-profit",
    "oil, gas, energy & utilities",
    "real estate",
    "restaurants, bars & food services",
    "retail",
    "telecommunications",
    "transportation & logistics",
    "travel & tourism",
]


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
            return True, item
    # Decision Science

    return False, np.nan

def find_item_enum_txt_sector(enum, txt):
    """return (bool,item)
    it return tuple that shows item is found or not
    and shows what is it
    """

    enum = [i.lower() for i in enum]
    txt = txt.lower()

    for item in enum:
        if item in txt:
            return True, item
    # Decision Science

    return False, 'Unknown / Non-Applicable'

def find_item_enum_txt_title(enum, txt):
    """return (bool,item)
    it return tuple that shows item is found or not
    and shows what is it
    """
    # https://www.northeastern.edu/graduate/blog/data-science-careers-shaping-our-future/
    # 1. Data Scientist
    # Average Salary: $139,840
    #
    # Typical Job Requirements: Find, clean, and organize data for companies. Data scientists will need to be able to analyze large amounts of complex raw and processed information to find patterns that will benefit an organization and help drive strategic business decisions. Compared to data analysts, data scientists are much more technical.
    #
    # Learn more: What Does a Data Scientist Do?
    #
    # 2. Machine Learning Engineer
    # Average Salary: $114,826
    #
    # Typical Job Requirements: Machine learning engineers create data funnels and deliver software solutions. They typically need strong statistics and programming skills, as well as a knowledge of software engineering. In addition to designing and building machine learning systems, they are also responsible for running tests and experiments to monitor the performance and functionality of such systems.
    #
    # 3. Machine Learning Scientist
    # Average Salary: $114,121
    #
    # Typical Job Requirements: Research new data approaches and algorithms to be used in adaptive systems including supervised, unsupervised, and deep learning techniques. Machine learning scientists often go by titles like Research Scientist or Research Engineer.
    #
    # 4. Applications Architect
    # Average Salary: $113,757
    #
    # Typical Job Requirements: Track the behavior of applications used within a business and how they interact with each other and with users. Applications architects are focused on designing the architecture of applications as well, including building components like user interface and infrastructure.
    #
    # 5. Enterprise Architect
    # Average Salary: $110,663
    #
    # Typical Job Requirements: An enterprise architect is responsible for aligning an organization’s strategy with the technology needed to execute its objectives. To do so, they must have a complete understanding of the business and its technology needs in order to design the systems architecture required to meet those needs.
    #
    # 6. Data Architect
    # Average Salary: $108,278
    #
    # Typical Job Requirements: Ensure data solutions are built for performance and design analytics applications for multiple platforms. In addition to creating new database systems, data architects often find ways to improve the performance and functionality of existing systems, as well as working to provide access to database administrators and analysts.
    #
    # 7. Infrastructure Architect
    # Average Salary: $107,309
    #
    # Typical Job Requirements: Oversee that all business systems are working optimally and can support the development of new technologies and system requirements. A similar job title is Cloud Infrastructure Architect, which oversees a company’s cloud computing strategy.
    #
    # 8. Data Engineer
    # Average Salary: $102,864
    #
    # Typical Job Requirements: Perform batch processing or real-time processing on gathered and stored data. Data engineers are also responsible for building and maintaining data pipelines which create a robust and interconnected data ecosystem within an organization, making information accessible for data scientists.
    #
    # 9. Business Intelligence (BI) Developer
    # Average Salary: $81,514
    #
    # Typical Job Requirements: BI developers design and develop strategies to assist business users in quickly finding the information they need to make better business decisions. Extremely data-savvy, they use BI tools or develop custom BI analytic applications to facilitate the end-users’ understanding of their systems.
    #
    # 10. Statistician
    # Average Salary: $76,884
    #
    # Typical Job Requirements: Statisticians work to collect, analyze, and interpret data in order to identify trends and relationships which can be used to inform organizational decision-making. Additionally, the daily responsibilities of statisticians often include design data collection processes, communicating findings to stakeholders, and advising organizational strategy.
    #
    # Learn More: What Do Statisticians Do?
    #
    # 11. Data Analyst
    # Average Salary: $62, 453
    #
    # Typical Job Requirements: Transform and manipulate large data sets to suit the desired analysis for companies. For many companies, this role can also include tracking web analytics and analyzing A/B testing. Data analysts also aid in the decision-making process by preparing reports for organizational leaders which effectively communicate trends and insights gleaned from their analysis.
    #
    # Learn More: What Does a Data Analyst Do?
    # 1
    # Data Scientist
    # Data Science
    # 2
    # Machine Learning Engineer
    # 3
    # Machine Learning Scientist
    # Machine Learning
    # 4
    # Applications Architect
    # 5
    # Enterprise Architect
    # 6
    # Data Architect
    # 7
    # Infrastructure Architect
    # 8
    # Data Engineer
    # Data Software Engineer
    # Data Developer
    # 9
    # Business Intelligence
    # 10
    # Statistician
    # 11
    # Data Analyst
    # Data Support Analyst
    # Data Visualization Analyst
    # Analytics
    # Data Analytics Analyst
    # Data Analytics
    # Analyst
    # BI Analyst
    # Marketing Scientist
    # Business Intelligence Analyst
    # Business Analyst
    # Data Modeler
    # Data Steward
    # Data Catalog
    # Decision Science
    # Scientific Software Developer
    # Data Specialist

    enum = [i.lower() for i in enum]
    txt = txt.lower()

    if 'data science' in txt:
        # machine learning
        # machine learning scientist
        txt = 'data scientist'

    if ('machine learning' in txt) and not ('machine learning engineer' in txt):
        # Data Scientist
        # Data Science
        txt = 'machine learning scientist'

    if ('data software engineer' in txt) or ('data developer' in txt):
        # data engineer
        # data software engineer
        # data developer
        txt = 'data engineer'

    if ('analytics' in txt) or ('data specialist' in txt) or ('analyst' in txt) \
            or ('marketing scientist' in txt) or ('data modeler' in txt) or ('data steward' in txt) \
            or ('data catalog' in txt) or ('decision science' in txt) or ('scientific software developer' in txt):
        txt = 'data analyst'

    for item in enum:
        if item in txt:
            return True, item
    # Decision Science

    return False, np.nan


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

def clean_data_extract_fields(path_in, path_out):
    df = pd.read_csv(path_in)

    df.dropna(subset=["salary", "job_id"], inplace=True)
    df = df.drop_duplicates(subset=['job_id'], keep='first')

    df = df[[c for c in df.columns if c.lower()[:7] != 'unnamed']]

    df["title"] = df["job_title"].apply(lambda x: find_item_enum_txt_title(title_enum, x)[1])
    df["position"] = df["job_title"].apply(lambda x: find_item_enum_txt(position_enum, x)[1]).replace(to_replace=np.nan,
                                                                                                      value="employee")

    df["company_sector"] = df["company_sector"].replace(np.nan, 'Unknown / Non-Applicable').apply(lambda x: find_item_enum_txt_sector(industries_enum, x)[1]).replace(
        to_replace=np.nan,
        value="employee")

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

    # replace null value with empty string
    df['desc'] = df['desc'].fillna("")

    df.drop(['desc_txt', 'desc_list', 'descriptions_txt', 'descriptions_list'], axis=1, inplace=True)

    df['pros'] = df['pros'].apply(
        lambda x: x.replace("[", "").replace("]", "").replace(",", "").replace("'", "").replace("\"", ""))
    df['cons'] = df['cons'].apply(
        lambda x: x.replace("[", "").replace("]", "").replace(",", "").replace("'", "").replace("\"", ""))

    df['salary_estimate'] = df['salary_estimate'].apply(
        lambda x: x.replace('.', '').replace('(', '').replace(')', '').replace(':', ''))

    df["avg_employees"] = df["company_size"].replace('Unknown', np.nan).replace(np.nan,
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

##### List of operations

# clean_data_extract_fields(r'D:\project\DataScience_HR Analytics\data\data.csv',
#                                        r'D:\project\DataScience_HR Analytics\data\data_clean.csv')
