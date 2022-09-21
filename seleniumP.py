import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
def yahooNio():
    '''
    automation for downloding Nio stack history yahoo finace
    '''
    driver = webdriver.Chrome('/Users/temesgenalemayehu/Downloads/chromedriver')
    driver.get("https://www.google.com")
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@class='gLFyf gsfi']").send_keys("yahoo finance", Keys.ENTER)

    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@class='tF2Cxc']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="yfin-usr-qry"]').send_keys("NIO", Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[7]/div/div/section/div/ul/li[6]/a/span').click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a/span').click()
    time.sleep(3)


yahooNio()

