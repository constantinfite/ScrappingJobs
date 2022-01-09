import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import date
import re
import math
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

job_titles = []
company_names = []
company_locations = []
extract_dates = []
post_dates = []
job_links = []
is_consulted = []


def extract(job_elems):
    # For each job card we look for the informations
    for job_elem in job_elems:

        try:
            job_titles.append(extract_job_title_indeed(job_elem))
            company_names.append(extract_company_name_indeed(job_elem))
            company_locations.append(extract_company_location_indeed(job_elem))
            extract_dates.append(extract_extract_date())
            job_links.append(extract_job_link_indeed(job_elem))
            post_dates.append(extract_post_date(job_elem))

        except AttributeError:
            print("------------ Block -------------")
            break


def extract_job_title_indeed(element):
    title = element.find("span", class_=None).text.replace("\n", "")

    return title


def extract_company_location_indeed(element):
    location = element.find("div", class_="companyLocation").text.replace("\n", "")
    return location


def extract_company_name_indeed(element):
    company = element.find("span", class_="companyName").text.replace("\n", "")

    return company


def extract_extract_date():
    return date.today().strftime('%Y-%m-%d')


def extract_post_date(element):
    post_date = element.find("span", class_="date").text.replace("\n", "")
    return post_date


def extract_job_link_indeed(element):
    link = "https://www.indeed.com" + element.get('href')
    return link


def extract_number_pages(soup):
    raw_total_number_jobs = soup.find("div", class_="searchCountContainer").text
    raw_total_number_jobs = raw_total_number_jobs.replace(" ", "")
    regex = r"((\d+ )?\d+) emplois"
    total_job_array = re.findall(regex, raw_total_number_jobs)
    total_job = total_job_array[0][0]
    print("total_job", total_job)
    total_pages = math.ceil(int(total_job) / 15)
    print("total pages", total_pages)

    return total_pages


# Loop over pages
def extract_all_pages(job, location, job_type):
    url = f'https://fr.indeed.com/jobs?q={job}&l={location}&jt={job_type}&start=0'
    print(url)
    c = 0
    while True:
        r = requests.get(url, headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        job_elems = soup.findAll("a", class_="tapItem")
        # Extract array of cards
        extract(job_elems)

        # If next button exist change url to the next url page
        try:

            url = "https://fr.indeed.com" + soup.find('a', {'aria-label': 'Suivant'}).get('href')
            c += 1
            print("Page number :", url)
            #time.sleep(10)
        except AttributeError:
            break

    extract_number_pages(soup)

    indeed_dictionnary = {
        "Company": company_names,
        "Location": company_locations,
        "Job": job_titles,
        "Extract Date": extract_dates,
        "Post Day": post_dates,
        "Job link": job_links,
    }

    df_extracted = pd.DataFrame(indeed_dictionnary)
    print("Size of extracted df", df_extracted.shape)
    return df_extracted
