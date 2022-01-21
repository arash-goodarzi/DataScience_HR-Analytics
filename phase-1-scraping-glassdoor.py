import os
import datetime
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Constants
PATH = "C:\Program Files (x86)\chromedriver.exe"


# URLSearchParams
def pageGlassDoorScraping(url):
    driver = webdriver.Chrome(service=Service(PATH), options=webdriver.ChromeOptions())
    result = []

    driver.maximize_window()
    driver.get(url)

    elements = driver.find_elements(By.XPATH, '//li[@data-id]')

    # Header table for debugging
    print('*'*15, " Start the process ", '*'*15)
    print('|company_name|rate|city|state|job_title|salary|salary_estimate|salary_avg|company_size|company_type'
          '|company_sector|company_founded|company_industry|pros_txt|cons_txt|')
    for index, element in enumerate(elements):
        driver.implicitly_wait(2)

        try:
            element.click()
        except Exception as ex:
            print(ex)
            continue

        try:
            driver.find_element(By.XPATH, '//span[@alt="Close"]').click()
        except NoSuchElementException:
            pass
        finally:
            driver.implicitly_wait(7)

        # Take elements
        company_name_rate = driver.find_element(By.XPATH,
                                                  '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div['
                                                  '1]/div[1]').text
        name_and_rate = company_name_rate.partition('\n')
        company_name = name_and_rate[0].strip()

        remote_work = False

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
            company_type = -1

        try:
            company_sector = driver.find_element(By.XPATH, '//*[@id="EmpBasicInfo"]/div[1]/div/div[5]/span[2]').text
        except NoSuchElementException:
            company_sector = -1

        try:
            company_founded = driver.find_element(By.XPATH, '//*[@id="EmpBasicInfo"]/div[1]/div/div[2]/span[2]').text
        except NoSuchElementException:
            company_founded = -1
        try:
            company_industry = driver.find_element(By.XPATH, '//*[@id="EmpBasicInfo"]/div[1]/div/div[4]/span[2]').text
        except NoSuchElementException:
            company_industry = -1

        try:
            location = driver.find_element(By.XPATH,
                                           '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[3]').text
            location = location.split(", ")
        except NoSuchElementException:
            location = -1

        try:
            city = location[0]
            if city == 'Remote':
                remote_work = True
                city = -1
        except IndexError:
            city = -1
        try:
            state = location[1]
        except IndexError:
            state = -1

        try:
            job_title = driver.find_element(By.XPATH,
                                            '//*[@id="JDCol"]/div/article/div/div[1]/div/div/div[1]/div[3]/div[1]/div[2]').text
        except NoSuchElementException:
            job_title = -1

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
            cons = -1

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
            f'|{company_name}|{rate}|{city}|{state}|{job_title}|{salary}|{salary_estimate}|{salary_avg}|{company_size}|{company_type}|{company_sector}|{company_founded}|{company_industry}|{pros_txt}|{cons_txt}|')

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
            "pros": pros_txt,
            "cons": cons_txt
        })

    return pd.DataFrame(result)


def grassdoorUrlGenerator(n, searchWord):
    return 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword=%22'+ searchWord +'%22&locT=C&locId=1147401,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0&' + 'p=' + str(n)


def mainScraping(n, searchWord):

    path = os.getcwd()
    parent_path = os.path.abspath(os.path.join(path, os.pardir))
    path_folder = os.path.join(parent_path, "glassdoor-data-data-science", datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    os.makedirs(path_folder)

    urls = [grassdoorUrlGenerator(i, searchWord) for i in range(1, n+1)]
    for inx, url in enumerate(urls):
        df = pageGlassDoorScraping(url)
        destination = os.path.join(path_folder, str(inx))
        df.to_csv(destination+'.csv')

    print('*'*15, " End the process ", '*'*15)


searchWord = 'ِData Science'
mainScraping(1, searchWord)
