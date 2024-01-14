from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

timeout = 50
link = "https://suninjuly.github.io/selects1.html"

num1Id = "num1"
num2Id = "num2"
selectId ="dropdown"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, num1Id).text
    num2 = browser.find_element(By.ID, num2Id).text

    searchedNum = str(int(num1) + int(num2))

    select = Select(browser.find_element(By.ID, selectId))
    select.select_by_visible_text(searchedNum)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(timeout)
    # закрываем браузер после всех манипуляций
    browser.quit()
