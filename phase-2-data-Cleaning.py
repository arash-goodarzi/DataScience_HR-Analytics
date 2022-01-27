"""
Created on Tue Jan 25 10:10:36 2022

@author: arash goodarzi

Step 1: Remove duplicate or irrelevant observations. Remove unwanted observations from your dataset, including duplicate observations or irrelevant observations. ...
Step 2: Fix structural errors. ...
Step 3: Filter unwanted outliers. ...
Step 4: Handle missing data. ...

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

def clean_data_remove_duplicate_irrelevant(path_in, path_out):
    df = pd.read_csv(path_in)

    df.dropna(subset=["salary", "job_id"], inplace=True)
    df = df.drop_duplicates(subset=['job_id'], keep='first')

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


def clean_data_enrich_data_description(path_in, path_out):
    df = pd.read_csv(path_in)

    # =============================================================================
    #  rerange columns
    #
    # ['company_name', 'city', 'state', 'rate',
    #         'title', 'position', 'avg_salary','job_age',
    #          'company_size', 'company_type', 'company_sector','company_size_number', 'company_founded', 'company_industry',
    #          'pros', 'cons','desc',
    #          'per_hour', 'remote_work', 'salary_estimate']
    # =============================================================================

    df = df[['company_name', 'city', 'state', 'rate',
             'title', 'position', 'avg_salary', 'job_age',
             'company_size', 'company_type', 'company_sector', 'company_size_number', 'company_founded',
             'company_industry',
             'pros', 'cons', 'desc',
             'per_hour', 'remote_work', 'salary_estimate']]

    df['ms_office'] = df['desc'].replace(np.nan, '').apply(lambda x: 'ms office' in x.lower())
    df['r'] = df['desc'].replace(np.nan, '').apply(lambda x: 'r' in x.lower())
    df['oracle'] = df['desc'].replace(np.nan, '').apply(lambda x: 'oracle' in x.lower())
    df['logstash'] = df['desc'].replace(np.nan, '').apply(lambda x: 'logstash' in x.lower())
    df['matlab'] = df['desc'].replace(np.nan, '').apply(lambda x: 'matlab' in x.lower())
    df['looker'] = df['desc'].replace(np.nan, '').apply(lambda x: 'looker' in x.lower())
    df['k-means'] = df['desc'].replace(np.nan, '').apply(lambda x: 'k-means' in x.lower())
    df['airflow'] = df['desc'].replace(np.nan, '').apply(lambda x: 'airflow' in x.lower())
    df['splunk'] = df['desc'].replace(np.nan, '').apply(lambda x: 'splunk' in x.lower())
    df['trifacta'] = df['desc'].replace(np.nan, '').apply(lambda x: 'trifacta' in x.lower())
    df['linear_regression'] = df['desc'].replace(np.nan, '').apply(lambda x: 'linear regression' in x.lower())
    df['sql'] = df['desc'].replace(np.nan, '').apply(lambda x: 'sql' in x.lower())
    df['apache_airflow'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache airflow' in x.lower())
    df['apache_kafka'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache kafka' in x.lower())
    df['concurrency'] = df['desc'].replace(np.nan, '').apply(lambda x: 'concurrency' in x.lower())
    df['datarobot'] = df['desc'].replace(np.nan, '').apply(lambda x: 'datarobot' in x.lower())
    df['apache_sqoop'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache sqoop' in x.lower())
    df['appdynamics'] = df['desc'].replace(np.nan, '').apply(lambda x: 'appdynamics' in x.lower())
    df['kanban'] = df['desc'].replace(np.nan, '').apply(lambda x: 'kanban' in x.lower())
    df['cyclotron'] = df['desc'].replace(np.nan, '').apply(lambda x: 'cyclotron' in x.lower())
    df['redash'] = df['desc'].replace(np.nan, '').apply(lambda x: 'redash' in x.lower())
    df['shell_scripting'] = df['desc'].replace(np.nan, '').apply(lambda x: 'shell scripting' in x.lower())
    df['cython'] = df['desc'].replace(np.nan, '').apply(lambda x: 'cython' in x.lower())
    df['storm'] = df['desc'].replace(np.nan, '').apply(lambda x: 'storm' in x.lower())
    df['apache_camel'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache camel' in x.lower())
    df['amazon_redshift'] = df['desc'].replace(np.nan, '').apply(lambda x: 'amazon redshift' in x.lower())
    df['prometheus'] = df['desc'].replace(np.nan, '').apply(lambda x: 'prometheus' in x.lower())
    df['aws'] = df['desc'].replace(np.nan, '').apply(lambda x: 'aws' in x.lower())
    df['julia'] = df['desc'].replace(np.nan, '').apply(lambda x: 'julia' in x.lower())
    df['tableau'] = df['desc'].replace(np.nan, '').apply(lambda x: 'tableau' in x.lower())
    df['apache_mahout'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache mahout' in x.lower())
    df['openrefine'] = df['desc'].replace(np.nan, '').apply(lambda x: 'openrefine' in x.lower())
    df['package_vs_module'] = df['desc'].replace(np.nan, '').apply(lambda x: 'package vs module' in x.lower())
    df['decision_tree'] = df['desc'].replace(np.nan, '').apply(lambda x: 'decision tree' in x.lower())
    df['apache_hbase'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache hbase' in x.lower())
    df['elasticsearch'] = df['desc'].replace(np.nan, '').apply(lambda x: 'elasticsearch' in x.lower())
    df['graphite'] = df['desc'].replace(np.nan, '').apply(lambda x: 'graphite' in x.lower())
    df['apache_hadoop'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache hadoop' in x.lower())
    df['cassandra'] = df['desc'].replace(np.nan, '').apply(lambda x: 'cassandra' in x.lower())
    df['powerbi'] = df['desc'].replace(np.nan, '').apply(lambda x: 'powerbi' in x.lower())
    df['nlp'] = df['desc'].replace(np.nan, '').apply(lambda x: 'nlp' in x.lower())
    df['apache_ambari'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache ambari' in x.lower())
    df['fivetran'] = df['desc'].replace(np.nan, '').apply(lambda x: 'fivetran' in x.lower())
    df['scala'] = df['desc'].replace(np.nan, '').apply(lambda x: 'scala' in x.lower())
    df['sap'] = df['desc'].replace(np.nan, '').apply(lambda x: 'sap' in x.lower())
    df['tensorflow'] = df['desc'].replace(np.nan, '').apply(lambda x: 'tensorflow' in x.lower())
    df['influxdb'] = df['desc'].replace(np.nan, '').apply(lambda x: 'influxdb' in x.lower())
    df['apache_zookeeper'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache zookeeper' in x.lower())
    df['beats'] = df['desc'].replace(np.nan, '').apply(lambda x: 'beats' in x.lower())
    df['java'] = df['desc'].replace(np.nan, '').apply(lambda x: 'java' in x.lower())
    df['apache_flink'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache flink' in x.lower())
    df['bigml'] = df['desc'].replace(np.nan, '').apply(lambda x: 'bigml' in x.lower())
    df['zabbix'] = df['desc'].replace(np.nan, '').apply(lambda x: 'zabbix' in x.lower())
    df['dimensionality_reduction'] = df['desc'].replace(np.nan, '').apply(
        lambda x: 'dimensionality reduction' in x.lower())
    df['minitab'] = df['desc'].replace(np.nan, '').apply(lambda x: 'minitab' in x.lower())
    df['excel'] = df['desc'].replace(np.nan, '').apply(lambda x: 'excel' in x.lower())
    df['great_expectations'] = df['desc'].replace(np.nan, '').apply(lambda x: 'great_expectations' in x.lower())
    df['datacleaner'] = df['desc'].replace(np.nan, '').apply(lambda x: 'datacleaner' in x.lower())
    df['apache_solr'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache solr' in x.lower())
    df['svm'] = df['desc'].replace(np.nan, '').apply(lambda x: 'svm' in x.lower())
    df['hevo'] = df['desc'].replace(np.nan, '').apply(lambda x: 'hevo' in x.lower())
    df['mongodb'] = df['desc'].replace(np.nan, '').apply(lambda x: 'mongodb' in x.lower())
    df['naive_bayes'] = df['desc'].replace(np.nan, '').apply(lambda x: 'naive bayes' in x.lower())
    df['kibana'] = df['desc'].replace(np.nan, '').apply(lambda x: 'kibana' in x.lower())
    df['turbonomic'] = df['desc'].replace(np.nan, '').apply(lambda x: 'turbonomic' in x.lower())
    df['_atlas.ti'] = df['desc'].replace(np.nan, '').apply(lambda x: ' atlas.ti' in x.lower())
    df['stitch'] = df['desc'].replace(np.nan, '').apply(lambda x: 'stitch' in x.lower())
    df['hpcc'] = df['desc'].replace(np.nan, '').apply(lambda x: 'hpcc' in x.lower())
    df['qlikview'] = df['desc'].replace(np.nan, '').apply(lambda x: 'qlikview' in x.lower())
    df['freeboard'] = df['desc'].replace(np.nan, '').apply(lambda x: 'freeboard' in x.lower())
    df['pandas'] = df['desc'].replace(np.nan, '').apply(lambda x: 'pandas' in x.lower())
    df['dashboardfox'] = df['desc'].replace(np.nan, '').apply(lambda x: 'dashboardfox' in x.lower())
    df['pentaho'] = df['desc'].replace(np.nan, '').apply(lambda x: 'pentaho' in x.lower())
    df['ado'] = df['desc'].replace(np.nan, '').apply(lambda x: 'ado' in x.lower())
    df['postgresql'] = df['desc'].replace(np.nan, '').apply(lambda x: 'postgresql' in x.lower())
    df['gradient_boosting_algorithm_and_adaboosting'] = df['desc'].replace(np.nan, '').apply(
        lambda x: 'gradient boosting algorithm and adaboosting' in x.lower())
    df['big_query'] = df['desc'].replace(np.nan, '').apply(lambda x: 'big query' in x.lower())
    df['klipfolio'] = df['desc'].replace(np.nan, '').apply(lambda x: 'klipfolio' in x.lower())
    df['random_forest'] = df['desc'].replace(np.nan, '').apply(lambda x: 'random forest' in x.lower())
    df['stats_iq'] = df['desc'].replace(np.nan, '').apply(lambda x: 'stats iq' in x.lower())
    df['metaclasses'] = df['desc'].replace(np.nan, '').apply(lambda x: 'metaclasses' in x.lower())
    df['apache_nifi'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache nifi' in x.lower())
    df['sas'] = df['desc'].replace(np.nan, '').apply(lambda x: 'sas' in x.lower())
    df['apache_drill'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache drill' in x.lower())
    df['apache_hive'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache hive' in x.lower())
    df['presto'] = df['desc'].replace(np.nan, '').apply(lambda x: 'presto' in x.lower())
    df['logistic_regression'] = df['desc'].replace(np.nan, '').apply(lambda x: 'logistic regression' in x.lower())
    df['jenkins'] = df['desc'].replace(np.nan, '').apply(lambda x: 'jenkins' in x.lower())
    df['akka'] = df['desc'].replace(np.nan, '').apply(lambda x: 'akka' in x.lower())
    df['google_analytics'] = df['desc'].replace(np.nan, '').apply(lambda x: 'google analytics' in x.lower())
    df['python'] = df['desc'].replace(np.nan, '').apply(lambda x: 'python' in x.lower())
    df['scrum'] = df['desc'].replace(np.nan, '').apply(lambda x: 'scrum' in x.lower())
    df['bigquery'] = df['desc'].replace(np.nan, '').apply(lambda x: 'bigquery' in x.lower())
    df['apache_spark'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache spark' in x.lower())
    df['agile'] = df['desc'].replace(np.nan, '').apply(lambda x: 'agile' in x.lower())
    df['apache_streamsets'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache streamsets' in x.lower())
    df['dynatrace'] = df['desc'].replace(np.nan, '').apply(lambda x: 'dynatrace' in x.lower())
    df['apache_lucerne'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache lucerne' in x.lower())
    df['grafana'] = df['desc'].replace(np.nan, '').apply(lambda x: 'grafana' in x.lower())
    df['datadog'] = df['desc'].replace(np.nan, '').apply(lambda x: 'datadog' in x.lower())
    df['knime'] = df['desc'].replace(np.nan, '').apply(lambda x: 'knime' in x.lower())
    df['apache_oozie'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache oozie' in x.lower())
    df['knn'] = df['desc'].replace(np.nan, '').apply(lambda x: 'knn' in x.lower())
    df['rapidminer'] = df['desc'].replace(np.nan, '').apply(lambda x: 'rapidminer' in x.lower())
    df['netdata'] = df['desc'].replace(np.nan, '').apply(lambda x: 'netdata' in x.lower())
    df['apache_flume'] = df['desc'].replace(np.nan, '').apply(lambda x: 'apache flume' in x.lower())
    df['instana'] = df['desc'].replace(np.nan, '').apply(lambda x: 'instana' in x.lower())
    df['couchdb'] = df['desc'].replace(np.nan, '').apply(lambda x: 'couchdb' in x.lower())
    df['snowflake'] = df['desc'].replace(np.nan, '').apply(lambda x: 'snowflake' in x.lower())
    df['async.io'] = df['desc'].replace(np.nan, '').apply(lambda x: 'async.io' in x.lower())
    df['spss'] = df['desc'].replace(np.nan, '').apply(lambda x: 'spss' in x.lower())
    df['microstrategy'] = df['desc'].replace(np.nan, '').apply(lambda x: 'microstrategy' in x.lower())

    # =============================================================================
    # list of variables that will be monitored
    # "sas",
    # "apache_hadoop",
    # "tableau",
    # "tensorflow",
    # "bigml",
    # "knime",
    # "rapidminer",
    # "excel",
    # "apache_flink",
    # "powerbi",
    # "datarobot",
    # "apache_spark",
    # "mongodb",
    # "python",
    # "trifacta",
    # "minitab",
    # "r",
    # "apache_kafka",
    # "qlikview",
    # "microstrategy",
    # "google_analytics",
    # "julia",
    # "spss",
    # "matlab",
    # "ado",
    # "ms_office",
    # "agile",
    # "kanban",
    # "scrum",
    # "sap",
    # "oracle",
    # "excel",
    # "apache_streamsets",
    # "apache_nifi",
    # "amazon_redshift",
    # "big_query",
    # "apache_hive",
    # "snowflake",
    # "redash",
    # "presto",
    # "looker",
    # "fivetran",
    # "great_expectations",
    # "stitch",
    # "splunk",
    # "hevo",
    # "apache_zookeeper",
    # "apache_oozie",
    # "apache_flume",
    # "apache_sqoop",
    # "sql",
    # "apache_mahout",
    # "apache_hbase",
    # "apache_drill",
    # "apache_solr",
    # "apache_lucerne",
    # "apache_ambari",
    # "postgresql",
    # "elasticsearch",
    # "jenkins",
    # "atlas.ti",
    # "hpcc",
    # "storm",
    # "cassandra",
    # "stats_iq",
    # "couchdb",
    # "pentaho",
    # "openrefine",
    # "rapidminer",
    # "datacleaner",
    # "grafana",
    # "datadog",
    # "dynatrace",
    # "appdynamics",
    # "kibana",
    # "influxdb",
    # "cyclotron",
    # "graphite",
    # "prometheus",
    # "netdata",
    # "turbonomic",
    # "freeboard",
    # "dashboardfox",
    # "instana",
    # "zabbix",
    # "klipfolio",
    # "aws",
    # "shell_scripting",
    # "java",
    # "scala",
    # "logstash",
    # "beats",
    # "akka",
    # "amazon_redshift",
    # "bigquery",
    # "tableau",
    # "looker",
    # "airflow",
    # "apache_streamsets",
    # "apache_airflow",
    # "apache_nifi",
    # "apache_camel",
    # "snowflake",
    # "redash",
    # "presto",
    # "rapidminer",
    # "async.io",
    # "metaclasses",
    # "concurrency",
    # "package_vs_module",
    # "cython",
    # "pandas",
    # "nlp",
    # "linear_regression",
    # "logistic_regression",
    # "decision_tree",
    # "svm",
    # "naive_bayes",
    # "knn",
    # "k-means",
    # "random_forest",
    # "dimensionality_reduction",
    # "gradient_boosting"
    # "adaboosting"
    # "numpy"
    #
    # =============================================================================

    # =============================================================================
    # def create_item_for_scraping(list_of_variables):
    #     list_of_variables = set([item.lower() for item in list_of_variables])
    #     for item in list_of_variables:
    #         item_with_dash = item.replace(" ", "_")
    #         print(f"df['{item_with_dash}'] = df['desc'].replace(np.nan, '').apply(lambda x: '{item}' in x.lower())")
    #
    #
    # =============================================================================

    df.to_csv(path_out, index=False)


# List of operations

# clean_data_remove_duplicate_irrelevant(r'D:\project\DataScience_HR Analytics\data\integrated_data.csv',
#                                        r'D:\project\DataScience_HR Analytics\data\integrated_data_clean.csv')

clean_data_enrich_data_description(r'D:\project\DataScience_HR Analytics\data\integrated_data_clean.csv',
                                   r'D:\project\DataScience_HR Analytics\data\integrated_data_clean_enrich.csv')

