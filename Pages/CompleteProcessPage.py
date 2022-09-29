from time import sleep
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData

class CompleteProcess(BasePage):

    """By locators"""

    EMAIL = (By.XPATH, "//input[@id='loginFormEmailInput']")
    PASSWORD = (By.ID, "loginFormPasswordInput")
    LOGIN_BUTTON = (By.XPATH , "//span[text()='Login']")

    EMAIL_CAPACITY = (By.XPATH, "//input[@placeholder='Email']")
    PASSWORD_CAPACITY = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON_CAPACITY = (By.XPATH, "//div[text()='Login']")

    CLICK_ON_LOAD = (By.XPATH, "//div[text()='Load']")
    LOAD_ENTRY_BUTTON = (By.XPATH, "//span[text()='+ Load Entry']")
    DIV_MODAL = "//div[@role='dialog']"
    CUSTOMER = (By.XPATH, f"{DIV_MODAL}//input[@placeholder='Customer']")
    CLICK_ON_CUSTOMER = (By.XPATH, "(//p[@title='EDGE LOGISTICS LLC'])[2]")
    EQUIPMENT_TYPE = (By.XPATH, f"{DIV_MODAL}//input[@placeholder='Equipment Type']")
    CLICK_ON_EQ = (By.XPATH, "//body/div[@id='simple-popover']/div[3]//p[contains(text(), 'Auto Hauler')]")
    WEIGTH = (By.NAME, "weight")
    COMMODITY = (By.XPATH, f"{DIV_MODAL}//input[@placeholder='Commodity']")
    CLICK_ON_COMMODITY = (By.XPATH, "(//p[@title='Liquid Fertilizer'])[1]")
    COMMENT = (By.NAME, "special_requirements")
    SEARCH = (By.XPATH, "//input[@placeholder='Search']")

    CLICK_ON_QUOTE = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]")
    CLICK_ON_QUOTE2 = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]")
    SHIPPING_BUTTON = (By.XPATH, "//div[text()='Shipping']")

    SHIPPER_CITY = (By.XPATH, "//input[@placeholder='Shipper City']")
    CLICK_ON_SCITY = (By.XPATH, "//p[text()=' Bakerhill, AL - (USA)']")
    ZIP_CODE1 = (By.XPATH, "(//input[@placeholder='Zip Code'])[1]")
    O_ARRIVE_DATE = (By.XPATH, "(//input[@placeholder='Arrive Early Date'])[1]")

    RECEIVER_CITY = (By.XPATH, "//input[@placeholder='Receiver City']")
    CLICK_ON_RCITY = (By.XPATH, "//p[text()=' Birmingham, IA - (USA)']")
    ZIP_CODE2 = (By.NAME, "destination.zip_code")
    D_ARRIVE_DATE = (By.XPATH, "(//input[@placeholder='Arrive Early Date'])[2]")
    NEXT_CALENDAR = (By.XPATH, "(//button[@class='MuiButtonBase-root MuiIconButton-root MuiPickersCalendarHeader-iconButton'])[2]")

    CLICK_ON_RCITY2 = (By.XPATH, "//p[text()=' New York, FL - (USA)']")
    CLICK_ON_DCITY2 = (By.XPATH, "//p[text()=' Washington Hill, AL - (USA)']")

    BUTTON_SAVE = (By.XPATH, "//span[text()='Save']")
    BUTTON_OK = (By.XPATH, "//span[text()='ok']")

    TRUCK_COST = (By.XPATH, "//span[contains(text(), 'Truck cost')]")
    COST = (By.XPATH, "//input[@placeholder='Cost']")
    EXPIRATION_DATE = (By.XPATH, "//input[@placeholder='Expiration Date']")
    COMMENT_COST = (By.XPATH, "//textarea[@name='comment_truck_cost']")
    BUTTON_SUBMIT = (By.XPATH, "//span[contains(text(), 'Submit')]")

    QUOTE_ID = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/p[2]")
    BUTTON_LENS = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]/div[1]/*[1]")
    BUTTON_LENS2 = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]")
    SALES_MARKUP = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/button[2]")
    SEARCH_FIELD = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
    SEARCH_FIELD2 = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]")
    BUTTON_EXIT = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]")

    BUTTON_RATE = (By.XPATH, "//span[text()='Rate']")
    RATE_FIELD = (By.XPATH, "//input[@name='rate']")

    QUOTES_HISTORY = (By.XPATH, "//p[text()='Quotes History']")
    CLICK_ON_QUOTE3 = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]")

    QUOTE_INFORMATION = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]")
    BUTTON_WON = (By.XPATH, "//body/div[@id='simple-menu']/div[3]/ul[1]/li[1]")

    """Constructor of the page class"""
    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)

    """This is used to login to app"""
    def do_login(self, username, password):
        self.send_keys(self.EMAIL, username)
        self.send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
    
    def click_on_load_entry(self):
        self.do_click(self.LOAD_ENTRY_BUTTON)
    
    def click_on_shipping(self):
        self.do_click(self.SHIPPING_BUTTON)

    def fill_load_information(self, customer, equipment, weigth, commodity, comment):
        self.do_click(self.CUSTOMER)
        self.send_keys(self.SEARCH, customer)
        self.do_click(self.CLICK_ON_CUSTOMER)
        self.do_click(self.EQUIPMENT_TYPE)
        self.send_keys(self.SEARCH, equipment)
        self.do_click(self.CLICK_ON_EQ)
        self.send_keys(self.WEIGTH, weigth)
        self.do_click(self.COMMODITY)
        self.send_keys(self.SEARCH, commodity)
        self.do_click(self.CLICK_ON_COMMODITY)
        self.send_keys(self.COMMENT, comment)

    def auto_fill_shipping_information(self, shipper_city, receiver_city):
        self.do_click(self.SHIPPER_CITY)
        self.send_keys(self.SEARCH, shipper_city)
        self.do_click(self.CLICK_ON_SCITY)
        self.do_click(self.O_ARRIVE_DATE)
        actual_day = self.get_current_day()
        ORIGIN_DAY = (By.XPATH, f"//button[@tabindex='0']//p[text()='{actual_day}']")
        self.do_click(ORIGIN_DAY)
        self.do_click(self.D_ARRIVE_DATE)
        if int(actual_day) >= 26:
            self.do_click(self.NEXT_CALENDAR)
            dest_day = 1
            DEST_DAY_LOCATOR = (By.XPATH, f"//button[@tabindex='0']//p[text()='{str(dest_day)}']")
            self.do_click(DEST_DAY_LOCATOR)
        else:
            dest_day = int(actual_day) + 5
            DEST_DAY_LOCATOR = (By.XPATH, f"//button[@tabindex='0']//p[text()='{str(dest_day)}']")
            self.do_click(DEST_DAY_LOCATOR)
        self.do_click(self.RECEIVER_CITY)
        self.send_keys(self.SEARCH, receiver_city)
        self.do_click(self.CLICK_ON_RCITY)

    def click_on_save(self):
        self.do_click(self.BUTTON_SAVE)

    def click_on_ok(self):
        self.do_click(self.BUTTON_OK)

    def click_on_quote(self):
        self.do_click(self.CLICK_ON_QUOTE)
    
    def click_on_quote_sales(self):
        self.do_click(self.CLICK_ON_QUOTE2)
    
    def click_on_quote_history(self):
        self.do_click(self.CLICK_ON_QUOTE3)

    def truck_cost_process(self, comment):
        self.do_click(self.TRUCK_COST)
        cost = self.generate_random_int(300, 900)
        self.send_keys(self.COST, cost)
        self.do_click(self.EXPIRATION_DATE)
        actual_day = self.get_current_day()
        ORIGIN_DAY = (By.XPATH, f"//button[@tabindex='0']//p[text()='{actual_day}']")
        self.do_click(ORIGIN_DAY)
        self.send_keys(self.COMMENT_COST, comment)
        self.do_click(self.BUTTON_SUBMIT)
    
    def save_quote(self):
        global quote_id
        quote_id = self.get_element_text(self.QUOTE_ID)

    def click_on_sales_markup(self):
        self.do_click(self.SALES_MARKUP)

    def search_quote(self):
        self.do_click(self.SEARCH_FIELD)
        self.send_keys(self.SEARCH_FIELD, quote_id)
        self.do_click(self.BUTTON_LENS)

    def rate_process(self):
        global RATE_FROM_CAPACITY
        self.do_click(self.BUTTON_RATE)
        rate = self.generate_random_int(300, 900)
        RATE_FROM_CAPACITY = (By.XPATH, f"//div[@class='css-1dbjc4n r-1awozwy r-lgvlli r-18u37iz r-1wtj0ep r-iyfy8q']//div[contains(text(), '{rate}')]")
        self.send_keys(self.RATE_FIELD, rate)
        self.do_click(self.BUTTON_SUBMIT)

    def click_on_quotes_history(self):
        self.do_click(self.QUOTES_HISTORY)

    def search_quote_on_history(self):
        self.do_click(self.SEARCH_FIELD2)
        self.send_keys(self.SEARCH_FIELD2, quote_id)
        self.do_click(self.BUTTON_LENS2)

    def click_on_won(self):
        self.do_click(self.QUOTE_INFORMATION)
        self.do_click(self.BUTTON_WON)


    def open_capacity_and_login(self, user, password):
        self.send_keys(self.EMAIL_CAPACITY, user)
        self.send_keys(self.PASSWORD_CAPACITY, password)
        self.do_click(self.LOGIN_BUTTON_CAPACITY)

    def verify_rate_on_capacity(self):
        rate_on_capacity = self.get_element_text(RATE_FROM_CAPACITY)
        assert rate_on_capacity