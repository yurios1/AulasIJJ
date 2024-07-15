from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
import time

browser = Edge()

link = "https://page-test-selenium.s3.sa-east-1.amazonaws.com/index.html"

browser.get(link)

btn_add_element = browser.find_element(By.ID, "addElement")

for i in range(10):
    btn_add_element.click()

checkboxes = browser.find_elements(By.TAG_NAME, "input")

for checkbox in checkboxes:
    checkbox.click()

time.sleep(3.0)

browser.quit()
