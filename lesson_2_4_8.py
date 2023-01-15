from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser.get(link)

button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))

browser.find_element(By.ID, 'book').click()

num = browser.find_element(By.ID, 'input_value').text
result = math.log(abs(12 * math.sin(int(num))))
select = browser.find_element(By.ID, 'answer')
select.send_keys(str(result))
browser.find_element(By.ID, 'solve').click()

time.sleep(40)
