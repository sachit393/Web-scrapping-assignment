import selenium
import pyautogui
import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
list=[]
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get('https://codeforces.com/problemset')
contest_no=(input("enter contest no "))
os.mkdir(fr'C:\Users\hp\PycharmProjects\web scrapping\{contest_no}')
listch=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R']
for i in listch:
    try:

            element=driver.find_element_by_link_text(contest_no+i)
            list.append(element)
            os.mkdir(rf'C:\Users\hp\PycharmProjects\web scrapping\{contest_no}\{i}')
            element.click()
            inputlist = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "input")))

            outputlist = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "output")))

            length=len(inputlist)
            for k in range(0,length):
                    f = open(rf'C:\Users\hp\PycharmProjects\web scrapping\{contest_no}\{i}\input{k}.txt', 'w')
                    g = open(rf'C:\Users\hp\PycharmProjects\web scrapping\{contest_no}\{i}\output{k}.txt', 'w')
                    output_data=outputlist[k].text
                    input_data=inputlist[k].text
                    f.write(input_data)
                    g.write(output_data)
            sleep(2)
            driver.get_screenshot_as_file(rf'C:\Users\hp\PycharmProjects\web scrapping\{contest_no}\{i}\problem.png')

            driver.back()
    except:
        j=0



