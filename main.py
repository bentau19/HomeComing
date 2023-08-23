from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import sheetClass
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.webdriver.remote.remote_connection import LOGGER

def optionSetter():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    return options

def getId(teacher_name):
    driver.get("https://apps.education.gov.il/MdbNet/MdbIturOVHLemosad.aspx")
    # driver.find_element(By.XPATH,'//*[@id="ShemSearch"]').send_keys(teacher_name)
    name=teacher_name.split()
    for i in range(41):
        if(driver.find_element(By.XPATH, '//*[@id="ctl00_Main_grdOvhLemosad"]/tbody/tr['+str(2+i)+']/td[4]').text==name[0] and
                driver.find_element(By.XPATH, '//*[@id="ctl00_Main_grdOvhLemosad"]/tbody/tr['+str(2+i)+']/td[3]').text==name[1]):
            teacher_id = driver.find_element(By.XPATH, '//*[@id="ctl00_Main_grdOvhLemosad"]/tbody/tr['+str(2+i)+']/td[5]').text
            i=42
            print(teacher_id)
    driver.back()
    driver.find_element(By.XPATH, '//*[@id="ctl00_txtZehut"]').clear()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="ctl00_txtZehut"]').send_keys(teacher_id)
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="ctl00_cmdItur"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="ctl00_cmdItur"]').click()
    time.sleep(5)
def getFrontalTime(day):
    return driver.find_element(By.XPATH,'//*[@id="ctl00_Main_ctl01_grdDivuachOut_ctl02_grdDivuachIn_ctl02_lblShaot'+str(day)+'"]').text

def start_program():
    action = ActionChains(driver)
    sheet = sheetClass.Sheet()


    driver.get("https://apps.education.gov.il/mdbnet/")
    print("get into your account and than press enter:")
    input()
    driver.find_element(By.XPATH,'//*[@id="cmdLoginOfkit"]').click()

    # try:
    ele = driver.find_element(By.XPATH,'//*[@id="menubar"]/div[2]/div/ul/li[1]')
    action.move_to_element(ele).perform()
    ele = driver.find_element(By.XPATH,'//*[@id="menubar"]/div[2]/div/ul/li[1]/ul/li[1]')
    action.move_to_element(ele).perform()
    driver.find_element(By.XPATH,'//*[@id="menubar"]/div[2]/div/ul/li[1]/ul/li[1]/ul/li[1]').click()
    counter = 1
    for teacher in sheet.teachers:
        getId(teacher.name)
        for day in teacher.days:
            frontal =getFrontalTime(sheet.date_to_day(day))
            sheet.add_num_to_place(counter, day, frontal)
        counter+=1
    # except  Exception as e:
    #     print(e)
    input()
    print("hello")

    driver.quit()

if __name__=="__main__":
    options = optionSetter()
    LOGGER.setLevel(logging.WARNING)
    driver = webdriver.Chrome(options=options)
    start_program()


