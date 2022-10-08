import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
def yahooNio():
    '''
    automation for downloding Nio stack history yahoo finace
    '''
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1200")

    # Accepting downloads without GUI
    options.add_experimental_option("prefs", {
    "download.default_directory": r"/Users/temesgenalemayehu/Downloads",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing_for_trusted_sources_enabled": False,
    "safebrowsing.enabled": False
    })
    driver = webdriver.Chrome('/Users/temesgenalemayehu/Downloads/chromedriver', options = options)
    driver.get("https://www.google.com")
    # time.sleep(1)
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@class='gLFyf gsfi']"))
        ).send_keys("yahoo finance", Keys.ENTER)
    # driver.find_element(By.XPATH, "//input[@class='gLFyf gsfi']").send_keys("yahoo finance", Keys.ENTER)
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='tF2Cxc']"))
        ).click()
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="yfin-usr-qry"]'))
        ).send_keys("NIO", Keys.ENTER)
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, 
        '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[7]/div/div/section/div/ul/li[6]/a/span'))
        ).click()
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, 
        '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a/span'))
        ).click()

    time.sleep(1)

yahooNio()