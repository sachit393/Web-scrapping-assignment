import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)

driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(5)
cookie=driver.find_element_by_id("bigCookie")
cookie_count=driver.find_element_by_id("cookies")
actions = ActionChains(driver)
actions.click( cookie)
items= [driver.find_element_by_id("productPrice"+str(i)) for i in range(1,-1,-11)]
for j in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value=int(item.text)
        if value <=count:
            upgrade_actions=ActionChains(driver)
            #upgrade_actions.move_to_element(item)
            upgrade_actions.click(item)
            upgrade_actions.perform()
