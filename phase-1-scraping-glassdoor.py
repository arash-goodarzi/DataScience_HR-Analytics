import datetime
import os

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Constants
PATH = "C:\Program Files (x86)\chromedriver.exe"


# URLSearchParams
def page_glassdoor_scraping_selenium(url):
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
    print('*'*15, " Start the process ", '*'*15)
    print('|company_name|rate|city|state|job_title|salary|salary_estimate|salary_avg|company_size|company_type'
          '|company_sector|company_founded|company_industry|descriptions_txt|descriptions_txt|job_age|pros_txt|cons_txt|')
    for index, element in enumerate(elements):
        driver.implicitly_wait(3)

        try:
            element.click()
        except Exception as ex:
            print(ex)
            continue

        try:
            button_close = driver.find_element(By.XPATH, '//span[@alt="Close"]')
            driver.execute_script("arguments[0].click();", button_close)
        except NoSuchElementException:
            pass
        finally:
            driver.implicitly_wait(8)

        try:
            # Take elements
            company_name_rate = driver.find_element(By.XPATH,
                                                    '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div['
                                                    '1]/div[1]').text
            name_and_rate = company_name_rate.partition('\n')
            company_name = name_and_rate[0].strip()

            remote_work = False
        except NoSuchElementException:
            company_name = ""

        try:
            rate = driver.find_element(By.XPATH, '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div['
                                                 '1]/div[1]/span').text
        except NoSuchElementException:
            rate = -1

        try:
            company_size = driver.find_element(By.XPATH, '//*[@id="EmpBasicInfo"]/div[1]/div/div[1]/span[2]').text
        except NoSuchElementException:
            company_size = -1

        try:
            company_type = driver.find_element(By.XPATH, '//*[@id="EmpBasicInfo"]/div[1]/div/div[3]/span[2]').text
        except NoSuchElementException:
            company_type = ""

        try:
            company_sector = driver.find_element(By.XPATH, '//*[@id="EmpBasicInfo"]/div[1]/div/div[5]/span[2]').text
        except NoSuchElementException:
            company_sector = ""

        try:
            company_founded = driver.find_element(By.XPATH, '//*[@id="EmpBasicInfo"]/div[1]/div/div[2]/span[2]').text
        except NoSuchElementException:
            company_founded = ""

        try:
            company_industry = driver.find_element(By.XPATH, '//*[@id="EmpBasicInfo"]/div[1]/div/div[4]/span[2]').text
        except NoSuchElementException:
            company_industry = ""

        try:
            location = driver.find_element(By.XPATH,
                                           '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
            location = location.split(", ")
        except NoSuchElementException:
            location = ""

        try:
            print(location[0])
            city = location[0]
            if city == 'Remote':
                remote_work = True
                city = ""
        except IndexError:
            city = ""

        try:
            state = location[1]
        except IndexError:
            state = ""

        try:
            job_title = driver.find_element(By.XPATH,
                                            '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]').text
        except NoSuchElementException:
            job_title = ""

        try:
            salary = driver.find_element(By.XPATH, '//*[@id="JDCol"]//span[@data-test="detailSalary"]').text
        except NoSuchElementException:
            salary = ""

        try:
            salary_estimate = driver.find_element(By.XPATH,
                                                  '//*[@id="JDCol"]//span[@data-test="detailSalary"]/span').text
        except NoSuchElementException:
            salary_estimate = ""

        try:
            salary_avg = driver.find_element(By.XPATH, '//span[text() = "yr"]/parent::*').text
        except NoSuchElementException:
            salary_avg = -1

        try:
            pros = driver.find_elements(By.XPATH, '//*[@id="Reviews"]/div/div/div[1]/p')
            pros_txt = [pro.text for pro in pros]
        except NoSuchElementException:
            pros = -1

        try:
            cons = driver.find_elements(By.XPATH, '//*[@id="Reviews"]/div/div/div[2]/p')
            cons_txt = [con.text for con in cons]
        except NoSuchElementException:
            cons = ""

        try:
            descriptions_txt = driver.find_elements(By.XPATH, '//div[@class="jobDescriptionContent desc"]//p')
            descriptions_txt = [desc.text for desc in descriptions_txt]
        except NoSuchElementException:
            descriptions_txt = ""

        try:
            descriptions_list = driver.find_elements(By.XPATH, '//div[@class="jobDescriptionContent desc"]//li')
            descriptions_list = [con.text for con in descriptions_list]
        except NoSuchElementException:
            descriptions_list = ""

        try:
            job_age = job_age_list[index]
        except NoSuchElementException:
            job_age = -1

        #  pre-Cleaning Data
        salary = salary.partition("(")[0].strip()
        salary = salary[salary.find('$'):]
        salary_estimate = salary_estimate.replace('(', '')
        salary_estimate = salary_estimate.replace('est', '')
        salary_estimate = salary_estimate.replace('.', '')
        salary_estimate = salary_estimate.replace(':', '')
        salary_estimate = salary_estimate.replace(')', '').strip()

        # Debugging Propose

        print(
            f'|{company_name}|{rate}|{city}|{state}|{job_title}|{salary}|{salary_estimate}|{salary_avg}|{company_size}|{company_type}|{company_sector}|{company_founded}|{company_industry}|{descriptions_txt}|{descriptions_list}|{job_age}|{pros_txt}|{cons_txt}|')

        # Add result to list
        result.append({
            "company_name": company_name,
            "rate": rate,
            "city": city,
            "state": state,
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

    return pd.DataFrame(result)


def grassdoor_url_generator(n, search_w):
    return 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword=%22'+ search_w +'%22&locT=C&locId=1147401,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0&' + 'p=' + str(n)


def selenium_scraping(from_page_, to_page_, search_word_):

    path = os.getcwd()
    parent_path = os.path.abspath(os.path.join(path, os.pardir))
    path_folder = os.path.join(parent_path, "glassdoor-data-data-science", datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    os.makedirs(path_folder)

    urls = [grassdoor_url_generator(i, search_word_) for i in range(from_page_, to_page_)]
    for inx, url in enumerate(urls):
        df = page_glassdoor_scraping_selenium(url)
        destination = os.path.join(path_folder, str(inx))
        df.to_csv(destination+'.csv')

    print('*'*15, " End the process ", '*'*15)


search_word = 'ِData Science'
from_page = 0
to_page = 30
selenium_scraping(from_page, to_page, search_word)


