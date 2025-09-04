from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")

    treasure = browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)

    answer = browser.find_element(By.TAG_NAME, "input")
    answer.send_keys(y)
    time.sleep(1)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    time.sleep(1)

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()
    time.sleep(1)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
    time.ctime(1)

finally:
    time.sleep(5)
    browser.quit()
