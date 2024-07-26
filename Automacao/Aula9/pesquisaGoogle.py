from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

browser = Edge()

link = "https://www.google.com.br"

browser.get(link)

elementopesquisar = browser.find_element(By.NAME, "q")

elementopesquisar.send_keys("Instituto Joga Junto")
elementopesquisar.send_keys(Keys.ENTER)

result_search = browser.find_elements(By.TAG_NAME, "h3")

check = False

while check == False:
    for link in result_search:
        if link.text == "Instituto Joga Junto":
            link.click()
            check = True


