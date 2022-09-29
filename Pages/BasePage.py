import random
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By

"""This class is the parent of all pages"""
"""it contains all the generic methods and utilities for all the pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        driver.maximize_window()

    def close_browser(self):
        self.driver.close()

    def refresh_browser(self):
        self.driver.refresh()

    def open_new_tab(self, tab):
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(tab)

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
        sleep(1)

    def do_click_text(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//body/div[@id='simple-popover']/div[3]/div[1]/div[3]//p[contains(text(),'{by_locator}')]"))).click()

    def do_click_text_day(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//button[@tabindex='0']//p[text()='{by_locator}']"))).click()

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
    
    def do_clear(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.CONTROL + "a")
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.DELETE)

    def do_esc(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.ESCAPE)


    def get_value(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element_ = element.get_attribute("value")
        return element_.split('-')[0].strip()
    
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_element_text_day(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element_ = element.text
        return element_.split('/')[1].replace('0','')
    
    def get_commodity_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        element_ = element.get_attribute("value")
        return element_.split(',')[0]
    
    def get_zipcode_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text.split(' ')[2]

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
    
    def get_current_day(self):
        today = date.today()
        d1 = today.strftime("%d/%m/%Y")
        day = d1.split('/')[0]
        return day
    
    def generate_random_int(self, range1, range2):
        n = random.randint(range1, range2)
        return n