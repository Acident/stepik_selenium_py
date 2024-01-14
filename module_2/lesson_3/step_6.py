from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


timeout = 20
link = "http://suninjuly.github.io/redirect_accept.html"
valueId = "input_value"
ansId = "answer"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.switch_to.window(browser.window_handles[1])

    value = int(browser.find_element(By.ID, valueId).text)
    browser.find_element(By.ID, ansId).send_keys(calc(value))
    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(timeout)
    # закрываем браузер после всех манипуляций
    browser.quit()
