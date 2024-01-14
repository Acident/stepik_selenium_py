from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

timeout = 5
link = "https://SunInJuly.github.io/execute_script.html"

valueId = "input_value"
ansId = "answer"
checkId = "robotCheckbox"
radioId = "robotsRule"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.execute_script("document.querySelector('footer').remove()")

    browser.find_element(By.ID, radioId).click()
    browser.find_element(By.ID, checkId).click()

    value = int(browser.find_element(By.ID, valueId).text)
    browser.find_element(By.ID, ansId).send_keys(calc(value))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(timeout)
    # закрываем браузер после всех манипуляций
    browser.quit()
