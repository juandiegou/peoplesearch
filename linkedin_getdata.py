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

def check_element(criterio,id):
	return WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(criterio,id))

def check_elements(criterio,id):
	return WebDriverWait(driver, timeout=50).until(lambda d: d.find_elements(criterio,id))

if(sys.platform.startswith('linux')):
    driver = webdriver.Firefox(executable_path='./geckodriver')
else:
  driver = webdriver.Firefox(executable_path='.\\chromedriver') 
  #driver = webdriver.Chrome(executable_path='.\\chromedriver.exe')

driver.get('https://co.linkedin.com/')
t.sleep(3)
check_element(By.XPATH,"//a[@href='https://www.linkedin.com/pub/dir/+/+?trk=guest_homepage-basic_guest_nav_menu_people']").click()

check_element(By.NAME,"firstName").send_keys('Benito')
check_element(By.NAME,"lastName").send_keys('Camelas')
t.sleep(1)
check_element(By.CLASS_NAME,"base-search-bar__submit-btn").click()

