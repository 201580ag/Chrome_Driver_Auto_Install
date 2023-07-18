from selenium import webdriver
import chromedriver_autoinstaller
import getpass
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
driver_path = f'./{chrome_ver}/chromedriver.exe'
if os.path.exists(driver_path):
    print(f"chromedriver is installed: {driver_path}")
else:
    print(f"Install the chromedriver (version: {chrome_ver})")
    chromedriver_autoinstaller.install(True)

driver = webdriver.Chrome(driver_path)
driver.maximize_window()
driver.get("") # web site
driver.implicitly_wait(3)
