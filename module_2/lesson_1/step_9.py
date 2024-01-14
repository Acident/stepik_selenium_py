from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x))))) #ln(abs(12*sin(x)))


timeout = 50
link = "http://suninjuly.github.io/get_attribute.html"

value1 = "robotCheckbox"
value2 = "robotsRule"
value3 = "answer"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elX = browser.find_element(By.ID, "treasure")
    x = elX.get_attribute("valuex")
    answer = browser.find_element(By.ID, value3)
    answer.send_keys(calc(x))

    checkBox = browser.find_element(By.ID, value1)
    checkBox.click()
    radio = browser.find_element(By.ID, value2)
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(timeout)
    # закрываем браузер после всех манипуляций
    browser.quit()
