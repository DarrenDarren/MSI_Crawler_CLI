import paths_helper as paths_helper

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOpts
from selenium.webdriver.chrome.service import Service

import platform

class BrowserHelper:
    
    def __init__(self):
        
        # if on windows, the browser driver should end with .exe
        # driver_filename = platform.system() == "Windows" ? "chromedriver.exe" : "chromedriver"
        driver_filename = "chromedriver.exe" if platform.system() == "Windows" else  "chromedriver"
        print("driver_filename: %s" % driver_filename) 
        options = webdriver.ChromeOptions()
        prefs = {
            'profile.default_content_setting_values' :
                {
                    'notifications' : 2
                }
        }
        options.add_experimental_option('prefs',prefs)
        
        self.driver = webdriver.Chrome(
            service=Service(paths_helper.DRIVER_PATH / driver_filename),
            options=options
        )

    def get_driver(self):
        return self.driver
    
    def open_page(self, url):
        self.driver.get(url)
    
    def get_element_with_xpath(self, xpath: str):
        element = self.driver.find_element(By.XPATH, xpath)
        return element

    def get_element_with_id(self, id: str):
        element = self.driver.find_element(By.ID, id)
        return element

    def click_element(self,element):
        element.click()