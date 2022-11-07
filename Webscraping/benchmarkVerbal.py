from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

MAX_SCORE = 1000
DRIVER_PATH = "C:/Users/arksh/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get("https://humanbenchmark.com/tests/verbal-memory")

options = Options

try:
    #Get Start Button
    eles = WebDriverWait(driver, 3).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "e19owgy710"))
    )
    if len(eles) != 1:
        raise Exception("More than one start buttons")
    start_button = eles[0]
    start_button.click()

    # Get SEEN and NEW
    eles = WebDriverWait(driver, 3).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "e19owgy710"))
    )
    if len(eles) != 2:
        raise Exception("Only 2 (SEEN and NEW) buttons not found ")

    seen_button = eles[0]
    new_button = eles[1]

    all_seen_words = {}
    score = 0
    while score < MAX_SCORE:
        score += 1

        # Get the word
        eles = WebDriverWait(driver, 3).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "word"))
        )
        if len(eles) != 1:
            raise Exception("More than one words found")

        word = eles[0].get_attribute('innerHTML')

        if word not in all_seen_words:
            all_seen_words[word] = True
            new_button.click()
        else:
            seen_button.click()

    time.sleep(3)

except Exception as e:
    print(e)

finally:
    driver.quit()
