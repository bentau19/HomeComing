from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import sheetClass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import undetected_chromedriver as uc
# browser = uc.Chrome(driver_executable_path='C:\\Users\\bentau\Desktop\chromedriver-win64/chromedriver')
#
# url = 'https://apps.education.gov.il/mdbnet/'
# browser.get(url)
# input()
# url = 'https://apps.education.gov.il/MdbNet/MdbNihulMSShvuitMeudkanNew.aspx'
# browser.get(url)
# input()
# browser.close()
options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Chrome(options=options)
# sheet = sheetClass.Sheet()
print("site is Running")
driver.get("https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li")
input()
button = driver.find_element(By.CSS_SELECTOR, '//*[@id="references-menu"]/li[2]/a/div[2]/div')
button.click()
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul#ulBirthYear a[data-value='2002']")))
element.click()
input()
# driver.get("https://apps.education.gov.il/mdbnet/")
# print("היכנס ולחץ אנטר")
# input()
# button = driver.find_element(By.CLASS_NAME, u"infoDismiss")
# driver.implicitly_wait(10)
# ActionChains(driver).move_to_element(button).click(button).perform()
# button = driver.find_element(By.ID, "cmdLoginOfkit")
# button.click()
# driver.find_element(By.XPATH,'/html/body/form/div[3]/div/div[1]/div[3]/div[1]/div[2]/div/ul/li[1]/ul/li[1]/ul/li[1]/a').click()
# input()
# print(driver.title)

driver.quit()