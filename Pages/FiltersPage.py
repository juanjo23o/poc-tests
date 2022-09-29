from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
from time import sleep

class FiltersPage(BasePage):

    """By locators"""
    EMAIL = (By.ID, "loginFormEmailInput")
    PASSWORD = (By.ID, "loginFormPasswordInput")
    LOGIN_BUTTON = (By.XPATH , "//span[text()='Login']")

    """Filter Locators"""
    QUOTE_ID = (By.NAME, "load_id")
    BUTTON_LENS = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]")
    EQUIPMENT_TYPE = (By.XPATH, "//input[@placeholder='Equipment Type']")
    COMMODITY = (By.XPATH, "//input[@placeholder='Commodity']")
    CUSTOMER = (By.XPATH, "//input[@placeholder='Customer']")
    SEARCH = (By.XPATH, "//input[@placeholder='Search']")
    ORIGIN = (By.XPATH, "//input[@placeholder='Origin']")
    DATE1 = (By.XPATH, "//input[@placeholder='Pick up Date']")
    DESTINATION = (By.XPATH, "//input[@placeholder='Destination']")
    DATE2 = (By.XPATH, "//input[@placeholder='Drop off Date']")
    RADIUS_FROM = (By.XPATH, "//input[@placeholder='From']")
    RADIUS_DISTANCE = (By.XPATH, "//input[@placeholder='Distance']")
    BUTTON_CLEAR = (By.XPATH, "//span[text()='Clear']")
    BUTTON_SEARCH = (By.XPATH, "//span[text()='Search']")

    """Info quote dashboard"""
    QUOTE = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]")
    QUOTE_ID_DASHBOARD = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/p[2]")
    SHIPPER_CITY_DASHBOARD = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/p[1]")
    O_ARRIVE_DATE_DASHBOARD = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/p[1]")
    RECEIVER_CITY_DASHBOARD = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/p[1]")
    D_ARRIVE_DATE_DASHBOARD = (By. XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/p[1]")
    EQUIPMENT_TYPE_DASHBOARD = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/p[1]")
    COMMODITY_DASHBOARD = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/p[1]")
    CUSTOMER_DASHBOARD = (By.XPATH, "//body/div[8]/div[3]/div[1]/div[2]/div[1]/div[2]/p[2]")
    BUTTON_OK = (By.XPATH, "//body/div[8]/div[3]/div[1]/div[3]/div[1]/div[1]/button[1]")
    BUTTON_EXIT = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]")
    NEXT_CALENDAR = (By.XPATH, "(//button[@class='MuiButtonBase-root MuiIconButton-root MuiPickersCalendarHeader-iconButton'])[2]")
    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page actions for login page"""

    """This is used to login to app"""
    def do_login(self, username, password):
        self.send_keys(self.EMAIL, username)
        self.send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

    def click_on_quote(self):
        self.do_click(self.QUOTE)
    
    def get_all_info_quote_from_dashboard(self):
        global quote_info, next_calendar
        quote_info = {
            "quote_id":self.get_element_text(self.QUOTE_ID_DASHBOARD),
            "origin":self.get_element_text(self.SHIPPER_CITY_DASHBOARD),
            "date1":self.get_element_text_day(self.O_ARRIVE_DATE_DASHBOARD),
            "destination":self.get_element_text(self.RECEIVER_CITY_DASHBOARD),
            "date2":self.get_element_text_day(self.D_ARRIVE_DATE_DASHBOARD),
            "equipment":self.get_element_text(self.EQUIPMENT_TYPE_DASHBOARD),
            "commodity":self.get_element_text(self.COMMODITY_DASHBOARD)
        }
        self.do_click(self.QUOTE_ID_DASHBOARD)
        quote_info["customer"] = self.get_element_text(self.CUSTOMER_DASHBOARD)
        self.do_click(self.BUTTON_OK)
        self.do_click(self.BUTTON_EXIT)
        if quote_info["date2"] == '1':
            next_calendar = True
        else:pass
        return quote_info, next_calendar
    
    def send_info_to_filters_and_verify(self):
        self.send_keys(self.QUOTE_ID, quote_info["quote_id"])
        self.do_click(self.BUTTON_LENS)
        assert self.is_enabled(self.QUOTE) == True
        self.do_click(self.EQUIPMENT_TYPE)
        self.send_keys(self.SEARCH, quote_info["equipment"])
        self.do_click_text(quote_info["equipment"])
        self.do_esc(self.SEARCH)
        self.do_click(self.BUTTON_SEARCH)
        assert self.is_enabled(self.QUOTE) == True
        self.do_click(self.COMMODITY)
        self.send_keys(self.SEARCH, quote_info["commodity"])
        self.do_click_text(quote_info["commodity"])
        self.do_esc(self.SEARCH)
        self.do_click(self.BUTTON_SEARCH)
        assert self.is_enabled(self.QUOTE) == True
        self.do_click(self.CUSTOMER)
        self.send_keys(self.SEARCH, quote_info["customer"])
        self.do_click_text(quote_info["customer"])
        self.do_esc(self.SEARCH)
        self.do_click(self.BUTTON_SEARCH)
        assert self.is_enabled(self.QUOTE) == True
        self.do_click(self.ORIGIN)
        self.send_keys(self.SEARCH, quote_info["origin"])
        self.do_click_text(quote_info["origin"])
        self.do_esc(self.SEARCH)
        self.do_click(self.BUTTON_SEARCH)
        assert self.is_enabled(self.QUOTE) == True
        self.do_click(self.DATE1)
        self.do_click_text_day(quote_info["date1"])
        self.do_esc(self.DATE1)
        self.do_click(self.BUTTON_SEARCH)
        assert self.is_enabled(self.QUOTE) == True
        self.do_click(self.DESTINATION)
        self.send_keys(self.SEARCH, quote_info["destination"])
        self.do_click_text(quote_info["destination"])
        self.do_esc(self.SEARCH)
        self.do_click(self.BUTTON_SEARCH)
        assert self.is_enabled(self.QUOTE) == True
        self.do_click(self.DATE2)
        if next_calendar:
            self.do_click(self.NEXT_CALENDAR)    
            self.do_click_text_day(quote_info["date2"])
        else:
            self.do_click_text_day(quote_info["date2"])
        self.do_esc(self.DATE2)
        self.do_click(self.BUTTON_SEARCH)
        assert self.is_enabled(self.QUOTE) == True





        

    