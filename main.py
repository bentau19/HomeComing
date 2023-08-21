import sheetClass
from selenium import webdriver
sheet = sheetClass.Sheet()
driver = webdriver.Chrome()
print("site is Running")
driver.get("https://apps.education.gov.il/MdbNet/Default.aspx")
print("היכנס ולחץ אנטר")
input()
print(driver.title)

driver.quit()