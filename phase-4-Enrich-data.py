# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 08:10:19 2022

@author: arash
"""

import numpy as np
import pandas as pd



def clean_data_enrich_data_description(path_in, path_out):
    df = pd.read_csv(path_in)

    # =============================================================================
    #  rearrange columns
    #
    # df = df[['company_name', 'city', 'state', 'rate',
    #          'title', 'position', 'avg_salary', 'job_age',
    #          'company_type', 'company_sector', 'avg_employees', 'company_founded',
    #          'company_industry',
    #          'pros', 'cons', 'desc',
    #          'per_hour', 'remote_work', 'salary_estimate']]
    # =============================================================================

    df = df[['rate',
             'title', 'position', 'avg_salary',
             'company_type', 'company_sector', 'avg_employees',
             'company_industry',
             'desc',
             'per_hour', 'remote_work', 'salary_estimate']]



    # step 1 extract from desc field


    # fill null desc column to empty string
    df['desc'] = df['desc'].replace(np.nan, '')

    #  apache
    df['apache_airflow'] = df['desc'].apply(lambda x: 'airflow' in x.lower())
    df['apache_kafka'] = df['desc'].apply(lambda x: 'kafka' in x.lower())
    df['apache_camel'] = df['desc'].apply(lambda x: 'camel' in x.lower())
    df['apache_oozie'] = df['desc'].apply(lambda x: 'oozie' in x.lower())
    df['apache_nifi'] = df['desc'].apply(lambda x: 'nifi' in x.lower())
    df['apache_spark'] = df['desc'].apply(lambda x: 'spark' in x.lower())
    df['apache_drill'] = df['desc'].apply(lambda x: 'drill' in x.lower())
    df['apache_hive'] = df['desc'].apply(lambda x: 'hive' in x.lower())
    df['apache_streamsets'] = df['desc'].apply(lambda x: 'streamsets' in x.lower())
    df['apache_flume'] = df['desc'].apply(lambda x: 'flume' in x.lower())
    df['apache_lucerne'] = df['desc'].apply(lambda x: 'lucerne' in x.lower())
    df['apache_hbase'] = df['desc'].apply(lambda x: 'hbase' in x.lower())
    df['apache_hadoop'] = df['desc'].apply(lambda x: 'hadoop' in x.lower())
    df['apache_ambari'] = df['desc'].apply(lambda x: 'ambari' in x.lower())
    df['apache_solr'] = df['desc'].apply(lambda x: 'solr' in x.lower())
    df['apache_flink'] = df['desc'].apply(lambda x: 'flink' in x.lower())
    df['apache_zookeeper'] = df['desc'].apply(lambda x: 'zookeeper' in x.lower())
    df['apache_mahout'] = df['desc'].apply(lambda x: 'mahout' in x.lower())
    df['apache_sqoop'] = df['desc'].apply(lambda x: 'sqoop' in x.lower())

    # Database
    df['bigquery'] = df['desc'].apply(lambda x: 'bigquery' in x.lower())
    df['amazon_redshift'] = df['desc'].apply(lambda x: 'amazon redshift' in x.lower())
    df['kinetica'] = df['desc'].apply(lambda x: 'kinetica' in x.lower())
    df['sql_server'] = df['desc'].apply(lambda x: 'sql server' in x.lower())
    df['oracle'] = df['desc'].apply(lambda x: 'oracle' in x.lower())
    df['vertica'] = df['desc'].apply(lambda x: 'vertica' in x.lower())
    df['mindsdb'] = df['desc'].apply(lambda x: 'mindsdb' in x.lower())
    df['sql'] = df['desc'].apply(lambda x: 'sql' in x.lower())
    df['mongodb'] = df['desc'].apply(lambda x: 'mongodb' in x.lower())

    # language
    df['r'] = df['desc'].apply(lambda x: 'r' in x.lower())
    df['python'] = df['desc'].apply(lambda x: 'python' in x.lower())
    df['scala'] = df['desc'].apply(lambda x: 'scala' in x.lower())
    df['java'] = df['desc'].apply(lambda x: 'java' in x.lower())



    df['ms_office'] = df['desc'].apply(lambda x: 'ms office' in x.lower())


    df['logstash'] = df['desc'].apply(lambda x: 'logstash' in x.lower())

    df['looker'] = df['desc'].apply(lambda x: 'looker' in x.lower())

    df['airflow'] = df['desc'].apply(lambda x: 'airflow' in x.lower())
    df['splunk'] = df['desc'].apply(lambda x: 'splunk' in x.lower())
    df['trifacta'] = df['desc'].apply(lambda x: 'trifacta' in x.lower())

    df['concurrency'] = df['desc'].apply(lambda x: 'concurrency' in x.lower())
    df['datarobot'] = df['desc'].apply(lambda x: 'datarobot' in x.lower())
    df['appdynamics'] = df['desc'].apply(lambda x: 'appdynamics' in x.lower())
    df['kanban'] = df['desc'].apply(lambda x: 'kanban' in x.lower())
    df['cyclotron'] = df['desc'].apply(lambda x: 'cyclotron' in x.lower())
    df['redash'] = df['desc'].apply(lambda x: 'redash' in x.lower())
    df['shell_scripting'] = df['desc'].apply(lambda x: 'shell scripting' in x.lower())
    df['cython'] = df['desc'].apply(lambda x: 'cython' in x.lower())
    df['storm'] = df['desc'].apply(lambda x: 'storm' in x.lower())
    df['prometheus'] = df['desc'].apply(lambda x: 'prometheus' in x.lower())
    df['aws'] = df['desc'].apply(lambda x: 'aws' in x.lower())
    df['julia'] = df['desc'].apply(lambda x: 'julia' in x.lower())
    df['tableau'] = df['desc'].apply(lambda x: 'tableau' in x.lower())
    df['openrefine'] = df['desc'].apply(lambda x: 'openrefine' in x.lower())
    df['package_vs_module'] = df['desc'].apply(lambda x: 'package vs module' in x.lower())

    df['elasticsearch'] = df['desc'].apply(lambda x: 'elasticsearch' in x.lower())
    df['graphite'] = df['desc'].apply(lambda x: 'graphite' in x.lower())
    df['cassandra'] = df['desc'].apply(lambda x: 'cassandra' in x.lower())
    df['powerbi'] = df['desc'].apply(lambda x: 'powerbi' in x.lower())
    df['nlp'] = df['desc'].apply(lambda x: 'nlp' in x.lower())
    df['fivetran'] = df['desc'].apply(lambda x: 'fivetran' in x.lower())
    df['sap'] = df['desc'].apply(lambda x: 'sap' in x.lower())
    df['tensorflow'] = df['desc'].apply(lambda x: 'tensorflow' in x.lower())
    df['influxdb'] = df['desc'].apply(lambda x: 'influxdb' in x.lower())
    df['beats'] = df['desc'].apply(lambda x: 'beats' in x.lower())
    df['bigml'] = df['desc'].apply(lambda x: 'bigml' in x.lower())
    df['zabbix'] = df['desc'].apply(lambda x: 'zabbix' in x.lower())
    df['great_expectations'] = df['desc'].apply(lambda x: 'great_expectations' in x.lower())
    df['datacleaner'] = df['desc'].apply(lambda x: 'datacleaner' in x.lower())
    df['hevo'] = df['desc'].apply(lambda x: 'hevo' in x.lower())
    df['kibana'] = df['desc'].apply(lambda x: 'kibana' in x.lower())
    df['turbonomic'] = df['desc'].apply(lambda x: 'turbonomic' in x.lower())
    df['_atlas.ti'] = df['desc'].apply(lambda x: ' atlas.ti' in x.lower())
    df['stitch'] = df['desc'].apply(lambda x: 'stitch' in x.lower())
    df['hpcc'] = df['desc'].apply(lambda x: 'hpcc' in x.lower())
    df['qlikview'] = df['desc'].apply(lambda x: 'qlikview' in x.lower())
    df['freeboard'] = df['desc'].apply(lambda x: 'freeboard' in x.lower())
    df['pandas'] = df['desc'].apply(lambda x: 'pandas' in x.lower())
    df['dashboardfox'] = df['desc'].apply(lambda x: 'dashboardfox' in x.lower())
    df['pentaho'] = df['desc'].apply(lambda x: 'pentaho' in x.lower())
    df['ado'] = df['desc'].apply(lambda x: 'ado' in x.lower())
    df['postgresql'] = df['desc'].apply(lambda x: 'postgresql' in x.lower())
    df['adaboosting'] = df['desc'].apply(
        lambda x: 'adaboosting' in x.lower())
    df['big_query'] = df['desc'].apply(lambda x: 'big query' in x.lower())
    df['klipfolio'] = df['desc'].apply(lambda x: 'klipfolio' in x.lower())
    df['stats_iq'] = df['desc'].apply(lambda x: 'stats iq' in x.lower())
    df['metaclasses'] = df['desc'].apply(lambda x: 'metaclasses' in x.lower())
    df['presto'] = df['desc'].apply(lambda x: 'presto' in x.lower())
    df['jenkins'] = df['desc'].apply(lambda x: 'jenkins' in x.lower())
    df['akka'] = df['desc'].apply(lambda x: 'akka' in x.lower())
    df['google_analytics'] = df['desc'].apply(lambda x: 'google analytics' in x.lower())
    df['dynatrace'] = df['desc'].apply(lambda x: 'dynatrace' in x.lower())
    df['grafana'] = df['desc'].apply(lambda x: 'grafana' in x.lower())
    df['datadog'] = df['desc'].apply(lambda x: 'datadog' in x.lower())
    df['knime'] = df['desc'].apply(lambda x: 'knime' in x.lower())
    df['rapidminer'] = df['desc'].apply(lambda x: 'rapidminer' in x.lower())
    df['netdata'] = df['desc'].apply(lambda x: 'netdata' in x.lower())
    df['instana'] = df['desc'].apply(lambda x: 'instana' in x.lower())
    df['couchdb'] = df['desc'].apply(lambda x: 'couchdb' in x.lower())
    df['snowflake'] = df['desc'].apply(lambda x: 'snowflake' in x.lower())
    df['async.io'] = df['desc'].apply(lambda x: 'async.io' in x.lower())

    df['microstrategy'] = df['desc'].apply(lambda x: 'microstrategy' in x.lower())

    # management tools
    df['scrum'] = df['desc'].apply(lambda x: 'scrum' in x.lower())
    df['agile'] = df['desc'].apply(lambda x: 'agile' in x.lower())


    # statistical tools
    df['sas'] = df['desc'].apply(lambda x: 'sas' in x.lower())
    df['excel'] = df['desc'].apply(lambda x: 'excel' in x.lower())
    df['matlab'] = df['desc'].apply(lambda x: 'matlab' in x.lower())
    df['spss'] = df['desc'].apply(lambda x: 'spss' in x.lower())
    df['minitab'] = df['desc'].apply(lambda x: 'minitab' in x.lower())

    # Machine Learning Algorithms
    df['linear_regression'] = df['desc'].apply(lambda x: 'linear regression' in x.lower())
    df['logistic_regression'] = df['desc'].apply(lambda x: 'logistic regression' in x.lower())
    df['decision_tree'] = df['desc'].apply(lambda x: 'decision tree' in x.lower())
    df['svm'] = df['desc'].apply(lambda x: 'svm' in x.lower())
    df['naive_bayes'] = df['desc'].apply(lambda x: 'naive bayes' in x.lower())
    df['knn'] = df['desc'].apply(lambda x: 'knn' in x.lower())
    df['k-means'] = df['desc'].apply(lambda x: 'k-means' in x.lower())
    df['random_forest'] = df['desc'].apply(lambda x: 'random forest' in x.lower())
    df['dimensionality_reduction'] = df['desc'].apply(
        lambda x: 'dimensionality reduction' in x.lower())
    df['gradient_boosting'] = df['desc'].apply(
        lambda x: 'gradient boosting' in x.lower())

    df['skills'] = df.iloc[:, -113:].sum(axis=1)

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
    #         print(f"df['{item_with_dash}'] = df['desc'].apply(lambda x: '{item}' in x.lower())")
    #
    #
    # =============================================================================
    
    df.drop(['desc'], axis=1, inplace=True)
    # step 2 drop desc field and get dummies
    # rate
    # title
    # position
    # avg_salary
    # company_type
    # company_sector
    # avg_employees
    # company_industry
    # per_hour
    # remote_work
    # salary_estimate
    df_dum = pd.get_dummies(df)

    df_dum.to_csv(path_out, index=False)


# def clean_data_enrich_data_others(path_in, path_out):
#     # rate
#     # avg_employees
#     # remote_work
#     # salary_estimate
#     # company_type
#     # company_sector
#     # company_industry
#     # title
#     # position
#     # per_hour
#     # avg_salary
#     pass

##### List of operations
clean_data_enrich_data_description(r'D:\project\DataScience_HR Analytics\data\data_clean.csv',
                                   r'D:\project\DataScience_HR Analytics\data\data_clean_enrich.csv')


# clean_data_enrich_data_others(r'D:\project\DataScience_HR Analytics\data\data_clean_enrich.csv',r'D:\project\DataScience_HR Analytics\data\data_clean_enrich_dummies.csv')

