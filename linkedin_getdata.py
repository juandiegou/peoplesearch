import requests
import json
from bs4 import BeautifulSoup as bs #beautifulsoup4==4.8.2
import mechanize #mechanize==0.4.8
import os
import sys
import time as t

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui as pg

keys = ['Georgia Institute of Technology','Engineer','Intel Corporation','gatech','senic','Doctoral Student','Leadership Fellow (Coach)','nano engineering ','chemistry','chemist','engineer','bioengineering','organic engineering']

def check_element(criterio,id):
	return WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(criterio,id))

def check_elements(criterio,id):
	return WebDriverWait(driver, timeout=50).until(lambda d: d.find_elements(criterio,id))

def find_word(text):
    concordance = 0
    for key in keys:
        if(key.lower() in text.lower()):
            concordance += 1
        if(concordance >= 1 and keys[0].lower() in text.lower()):
            print("\nEncontrad@ con prioridad")
            return True
        if(concordance >= 3):
            print("\nEncontrad@ con cantidad")
            return True
    return False

def find_persons(first_name, last_name):
    links_persons = []

    check_element(By.NAME,"firstName").send_keys(first_name)
    check_element(By.NAME,"lastName").send_keys(last_name)
    t.sleep(1)
    check_element(By.CLASS_NAME,"base-search-bar__submit-btn").click()
    t.sleep(1)
    persons = check_elements(By.XPATH,"//section[@class='serp-page__results-list']/child::ul/child::li")

    for p in persons:
        link = p.find_element(By.TAG_NAME,"a")
        if(find_word(link.text)):
            links_persons.append(link.get_attribute('href'))
            print(link.get_attribute('href'))
            print(link.text)

    return links_persons


if(sys.platform.startswith('linux')):
    driver = webdriver.Firefox(executable_path='./geckodriver')
else:
    driver = webdriver.Chrome(executable_path='.\\chromedriver.exe')

driver.get('https://co.linkedin.com/')
t.sleep(3)
check_element(By.XPATH,"//a[@href='https://www.linkedin.com/pub/dir/+/+?trk=guest_homepage-basic_guest_nav_menu_people']").click()

find_persons('Simple', 'Kumar')
