import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from datetime import date
import re
import math

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

    # For each block we look for the informations
    for job_elem in job_elems:
        job_titles.append(extract_job_title_indeed(job_elem))
        company_names.append(extract_company_name_indeed(job_elem))
        company_locations.append(extract_company_location_indeed(job_elem))
        extract_dates.append(extract_extract_date())
        job_links.append(extract_job_link_indeed(job_elem))

        try:
            post_dates.append(extract_post_date(job_elem))
        except AttributeError:
            post_dates.append("")


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
    total_pages = math.ceil(int(total_job) / 15)

    return total_pages


# Loop over pages
def extract_all_pages(job, location, job_type):

    # Get hmtl text
    link = f'https://fr.indeed.com/jobs?q={job}&l={location}'
    print(link)
    r = requests.get(link, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    job_elems = soup.findAll("a", class_="tapItem")

    number_pages = extract_number_pages(soup)
    # Loop over pages
    for i in range(0, number_pages * 10, 10):
        extract(job_elems)

    indeed_dictionnary = {
        "Company": company_names,
        "Location": company_locations,
        "Job": job_titles,
        "Extract Date": extract_dates,
        "Post Day": post_dates,
        "Job link": job_links,
    }

    df_extracted = pd.DataFrame(indeed_dictionnary)
    return df_extracted

# https://fr.indeed.com/jobs?q=Data%20Engineer&l=Paris
# https://www.indeed.com/jobs?q=data%20engineer&l=Paris
