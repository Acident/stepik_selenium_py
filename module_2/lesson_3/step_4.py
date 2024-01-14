from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

timeout = 20
link = "http://suninjuly.github.io/alert_accept.html"
valueId = "input_value"
ansId = "answer"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    alert = browser.switch_to.alert
    alert.accept()

    value = int(browser.find_element(By.ID, valueId).text)
    browser.find_element(By.ID, ansId).send_keys(calc(value))

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(timeout)
    # закрываем браузер после всех манипуляций
    browser.quit()
