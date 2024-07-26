from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
import time

browser = Edge()

def acessPage(link):
    browser.get(link)

def findElement(by, name):
    element = browser.find_element(by, name)
    return element

def fElements(by, name, searched):
    result = browser.find_elements(by, name)
    check = False
    while check == False:
        for link in result:
            if link.text == searched:
                link.click()
                check = True

def sendInfo(por, nome:str, mensagem:str, btnname, btn):
    element = browser.find_element(por, nome)
    element.send_keys(mensagem)
    print('Mensagem inserida.')
    browser.find_element(btn)

acessPage('https://www.google.com.br')

time.sleep(6)

selectedPage = sendInfo(By.NAME, 'q', 'Instituto Joga Junto', By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')