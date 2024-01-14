from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

timeout = 50
link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    for elms in browser.find_elements(By.CSS_SELECTOR, ".form-control"):
        elms.send_keys("ABJФИО")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    filePath = os.path.join(current_dir, 'empty.txt')

    browser.find_element(By.ID, "file").send_keys(filePath)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(timeout)
    # закрываем браузер после всех манипуляций
    browser.quit()
