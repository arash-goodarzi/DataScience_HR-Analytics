"""
Created on Tue Jan 15 18:06:32 2022

@author: arash

"""



import datetime
import os

import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Constants
PATH = "C:\Program Files (x86)\chromedriver.exe"


# URLSearchParams
def page_glassdoor_scraping_selenium(url, indx, job_age_d):
    driver = webdriver.Chrome(service=Service(PATH), options=webdriver.ChromeOptions())
    result = []

    driver.maximize_window()

    driver.get(url)

    try:
        job_age_list_ = driver.find_elements(By.XPATH, '//div[@data-test="job-age"]')
        job_age_list = [day.text for day in job_age_list_]
    except NoSuchElementException:
        job_age_list = []
    elements = driver.find_elements(By.XPATH, '//li[@data-id]')

    # Header table for debugging
    print(f'{"*" * 15}   Start process of page {indx + 1}  {">" * 15}')

    for index, element in enumerate(elements):
        driver.implicitly_wait(5)

        try:
            element.click()
        except Exception as ex:
            continue

        try:
            button_close = driver.find_element(By.XPATH, '//span[@alt="Close"]')
            driver.execute_script("arguments[0].click();", button_close)
        except NoSuchElementException:
            pass
        finally:
            driver.implicitly_wait(3)

        try:
            button_show_me = driver.find_element(By.XPATH, '//*[@id="JobDescriptionContainer"]/div[2]')
            driver.execute_script("arguments[0].click();", button_show_me)
        except NoSuchElementException:
            pass
        finally:
            driver.implicitly_wait(15)

        try:
            # Take elements
            company_name_rate = driver.find_element(By.XPATH,
                                                    '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div['
                                                    '1]/div[1]').text
            name_and_rate = company_name_rate.partition('\n')
            company_name = name_and_rate[0].strip()
            company_name = np.nan if len(str(company_name)) == 0 else company_name

            remote_work = 0
        except NoSuchElementException:
            company_name = np.nan

        try:
            rate = driver.find_element(By.XPATH,
                                       '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div['
                                       '1]/div[1]/span').text
            rate = np.nan if len(str(rate)) == 0 else rate
        except NoSuchElementException:
            rate = np.nan

        try:
            company_size = driver.find_element(By.XPATH, '//*[@id="EmpBasicInfo"]/div[1]/div/div[1]/span[2]').text
            company_size = np.nan if len(str(company_size)) == 0 else company_size
        except NoSuchElementException:
            company_size = np.nan

        try:
            company_type = driver.find_element(By.XPATH, '//*[@id="EmpBasicInfo"]/div[1]/div/div[3]/span[2]').text
            company_type = np.nan if len(str(company_type)) == 0 else company_type
        except NoSuchElementException:
            company_type = np.nan

        try:
            company_sector = driver.find_element(By.XPATH, '//*[@id="EmpBasicInfo"]/div[1]/div/div[5]/span[2]').text
            company_sector = np.nan if len(str(company_sector)) == 0 else company_sector
        except NoSuchElementException:
            company_sector = np.nan

        try:
            company_founded = driver.find_element(By.XPATH,
                                                  '//*[@id="EmpBasicInfo"]/div[1]/div/div[2]/span[2]').text
            company_founded = np.nan if len(str(company_founded)) == 0 else company_founded
        except NoSuchElementException:
            company_founded = np.nan

        try:
            company_industry = driver.find_element(By.XPATH,
                                                   '//*[@id="EmpBasicInfo"]/div[1]/div/div[4]/span[2]').text
            company_industry = np.nan if len(str(company_industry)) == 0 else company_industry
        except NoSuchElementException:
            company_industry = np.nan

        try:
            job_id = driver.find_element(By.XPATH, "//button[@data-job-id]").get_attribute('data-job-id')
        except NoSuchElementException:
            company_industry = np.nan

        try:
            location = driver.find_element(By.XPATH,
                                           '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
            location = location.split(", ")
        except NoSuchElementException:
            location = np.nan

        try:
            city = location[0]
            if city == 'Remote':
                remote_work = 1
                city = np.nan
            city = np.nan if len(str(city)) == 0 else city
        except IndexError:
            city = np.nan
        except :
            city = np.nan

        try:
            state = location[1]
            state = np.nan if len(str(state)) == 0 else state
        except :
            state = np.nan

        try:
            job_title = driver.find_element(By.XPATH,
                                            '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]').text
            job_title = np.nan if len(str(job_title)) == 0 else job_title
        except NoSuchElementException:
            job_title = np.nan

        try:
            salary = driver.find_element(By.XPATH, '//*[@id="JDCol"]//span[@data-test="detailSalary"]').text
            salary = np.nan if len(str(salary)) == 0 else salary
        except NoSuchElementException:
            salary = np.nan

        try:
            salary_estimate = driver.find_element(By.XPATH,
                                                  '//*[@id="JDCol"]//span[@data-test="detailSalary"]/span').text
            salary_estimate = np.nan if len(str(salary_estimate)) == 0 else salary_estimate
        except NoSuchElementException:
            salary_estimate = np.nan

        try:
            salary_avg = driver.find_element(By.XPATH, '//span[text() = "yr"]/parent::*').text
            salary_avg = np.nan if len(salary_avg) == 0 else salary_avg
        except NoSuchElementException:
            salary_avg = np.nan

        try:
            pros = driver.find_elements(By.XPATH, '//*[@id="Reviews"]/div/div/div[1]/p')
            pros_txt = [pro.text for pro in pros if len(pro.text) != 0]
        except NoSuchElementException:
            pros_txt = np.nan

        try:
            cons = driver.find_elements(By.XPATH, '//*[@id="Reviews"]/div/div/div[2]/p')
            cons_txt = [con.text for con in cons if len(con.text) != 0]
        except NoSuchElementException:
            cons_txt = np.nan

        try:
            driver.implicitly_wait(10)
            descriptions_txt = driver.find_elements(By.XPATH,
                                                    '//div[@class="jobDescriptionContent desc"]/descendant-or-self::p')
            descriptions_txt = [desc.text for desc in descriptions_txt if len(desc.text) != 0]
        except NoSuchElementException:
            descriptions_txt = np.nan

        try:
            descriptions_list_ = driver.find_elements(By.XPATH, '//div[@id="JobDescriptionContainer"]//ul/li')
            descriptions_list = [con.text for con in descriptions_list_ if len(con.text) != 0]
        except NoSuchElementException:
            descriptions_list = np.nan

        try:
            job_age = job_age_list[index]
        except NoSuchElementException:
            job_age = np.nan

        if job_age_d == 1:
            job_age = datetime.datetime.now().strftime('%Y-%m-%d')
        elif job_age_d == 2:
            job_age = (datetime.datetime.now() - datetime.timedelta(days=2)).strftime('%Y-%m-%d')
        elif job_age_d == 3:
            job_age = (datetime.datetime.now() - datetime.timedelta(days=3)).strftime('%Y-%m-%d')
        elif job_age_d == 4:
            job_age = (datetime.datetime.now() - datetime.timedelta(days=4)).strftime('%Y-%m-%d')
        elif job_age_d == 5:
            job_age = (datetime.datetime.now() - datetime.timedelta(days=5)).strftime('%Y-%m-%d')
        elif job_age_d == 6:
            job_age = (datetime.datetime.now() - datetime.timedelta(days=6)).strftime('%Y-%m-%d')
        elif job_age_d == 7:
            job_age = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
        elif job_age_d == 14:
            job_age = (datetime.datetime.now() - datetime.timedelta(days=14)).strftime('%Y-%m-%d')
        elif job_age_d == 30:
            job_age = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')

        # Debugging Propose

        print(
            f'{index}|{company_name}|{rate}|{city}|{state}|{job_id}|{job_title}|{salary}|{salary_estimate}|{salary_avg}|{company_size}|{company_type}|{company_sector}|{company_founded}|{company_industry}|{descriptions_txt}|{descriptions_list}|{job_age}|{pros_txt}|{cons_txt}|')

        # Add result to list
        result.append({
            "company_name": company_name,
            "rate": rate,
            "city": city,
            "state": state,
            "job_id": job_id,
            "remote_work": remote_work,
            "job_title": job_title,
            "salary": salary,
            "salary_estimate": salary_estimate,
            "salary_avg": salary_avg,
            "company_size": company_size,
            "company_type": company_type,
            "company_sector": company_sector,
            "company_founded": company_founded,
            "company_industry": company_industry,
            "descriptions_txt": descriptions_txt,
            "descriptions_list": descriptions_list,
            "job_age": job_age,
            "pros": pros_txt,
            "cons": cons_txt
        })
    print(f'{"*" * 15}   End process of page {indx + 1}  {"<" * 15}')
    return pd.DataFrame(result)


def grassdoor_url_generator(n, search_w, job_age_d):
    return 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword=%22' + search_w + '%22&locT=C&locId=1147401,%20CA&jobType=all&fromAge=' + str(
        job_age_d) + '&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0&' + 'p=' + str(
        n)


def selenium_scraping(from_page_, to_page_, search_word_, job_age_):
    # create folder for destination data
    path = os.getcwd()
    parent_path = os.path.abspath(os.path.join(path, os.pardir))
    path_folder = os.path.join(parent_path, "glassdoor-data-data-science",
                               datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    os.makedirs(path_folder)

    # creating of urls
    urls = [grassdoor_url_generator(i, search_word_, job_age_) for i in range(from_page_, to_page_)]

    # get data from each url
    for inx, url in enumerate(urls):
        df = page_glassdoor_scraping_selenium(url, inx, job_age_)
        destination = os.path.join(path_folder, str(inx))
        df.to_csv(destination + '.csv', index=False)

    print('*' * 15, " End the process of saving", '*' * 15)


# Input data #################
search_word = 'ِData Science'
from_page = 1
to_page = 10
job_age = 1  # 1=> last day       3=> last 3 days      -1=> all times
##############################

# adjust inputs
from_page = 1 if from_page < 1 else from_page
to_page = 30 if to_page > 30 else to_page

selenium_scraping(from_page, to_page, search_word, job_age)
