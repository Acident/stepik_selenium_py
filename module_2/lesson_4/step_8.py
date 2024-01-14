from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
firstBtnId = "book"
secondBtnId = "solve"
valueId = "input_value"
ansId = "answer"
timeout = 13


try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstBtn = WebDriverWait(browser, timeout).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    browser.find_element(By.ID, firstBtnId).click()

    value = int(WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((By.ID, valueId))
        ).text)
    browser.find_element(By.ID, ansId).send_keys(calc(value))

    secondBtn = WebDriverWait(browser, timeout).until(
            EC.element_to_be_clickable((By.ID, secondBtnId))
        )
    secondBtn.click()
finally:
    time.sleep(15)
    browser.quit()
