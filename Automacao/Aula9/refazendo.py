from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
import time

browser = Edge()

link = "https://page-test-selenium.s3.sa-east-1.amazonaws.com/index.html"

browser.get(link)

add_Element = browser.find_element(By.ID, "addElement")
for i in range(12):
    add_Element.click()

elementTree = browser.find_elements(By.TAG_NAME, "input")
print(len(elementTree))

for element in elementTree:
    element.click()
    print('Clicado')

time(3.0)

browser.quit()