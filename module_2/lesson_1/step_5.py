from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


timeout = 50
link = "https://suninjuly.github.io/math.html"

value1 = "[for='robotCheckbox']"
value2 = "[for='robotsRule']"
value3 = "answer"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elX = browser.find_element(By.ID, "input_value")
    x = elX.text
    answer = browser.find_element(By.ID, value3)
    answer.send_keys(calc(x))

    checkBox = browser.find_element(By.CSS_SELECTOR, value1)
    checkBox.click()
    input2 = browser.find_element(By.CSS_SELECTOR, value2)
    input2.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(timeout)
    # закрываем браузер после всех манипуляций
    browser.quit()
