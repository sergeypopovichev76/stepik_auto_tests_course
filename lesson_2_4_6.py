# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# broswer = webdriver.Chrome()
# link = 'http://suninjuly.github.io/redirect_accept.html'
# broswer.get(link)
# broswer.find_element(By.ID, 'button').click()


# урок 7

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait2.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text