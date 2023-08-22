from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import sheetClass
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def optionSetter():
    options = Options()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    return options


options = optionSetter()
driver = webdriver.Chrome(options=options)
# sheet = sheetClass.Sheet()
print("site is Running")
driver.get("https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li")

ele = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/header/div/div[2]/nav/ul/li[1]')

action = ActionChains(driver)

action.move_to_element(ele).perform()
driver.find_element(By.XPATH,'//*[@id="references-menu"]/li[2]/a').click()

ele = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/header/div/div[2]/nav/ul/li[2]')
action.move_to_element(ele).perform()
driver.find_element(By.XPATH,'//*[@id="guides-menu"]/li[5]/a').click()
html_list = driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/header/div/div[2]/nav/ul/li[1]')
items = html_list.find_elements(By.TAG_NAME,"li")
for item in items:
    text = item.text
    print (text)
    print("hello")
input()
print("hello")

driver.quit()


