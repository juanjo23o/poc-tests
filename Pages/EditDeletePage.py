from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData

class EditDeletePage(BasePage):

    """By locators"""
    EMAIL = (By.ID, "loginFormEmailInput")
    PASSWORD = (By.ID, "loginFormPasswordInput")
    LOGIN_BUTTON = (By.XPATH , "//span[text()='Login']")

    """"""
    CLICK_ON_LOAD = (By.XPATH, "//div[text()='Load']")
    LOAD_ENTRY_BUTTON = (By.XPATH, "//span[text()='+ Load Entry']")
    DIV_MODAL = "//div[@role='dialog']"
    CUSTOMER = (By.XPATH, f"{DIV_MODAL}//input[@placeholder='Customer']")
    CLICK_ON_CUSTOMER = (By.XPATH, "(//p[@title='EDGE LOGISTICS LLC'])[2]")
    EQUIPMENT_TYPE = (By.XPATH, f"{DIV_MODAL}//input[@placeholder='Equipment Type']")
    CLICK_ON_EQ = (By.XPATH, "//body/div[@id='simple-popover']/div[3]//p[contains(text(), 'Auto Hauler')]")
    CLEAR_EQ = (By.XPATH, "/html[1]/body[1]/div[8]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]")
    CLEAR_COMMODITY = (By.XPATH, "//body/div[8]/div[3]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]")
    WEIGTH = (By.NAME, "weight")
    COMMODITY = (By.XPATH, f"{DIV_MODAL}//input[@placeholder='Commodity']")
    CLICK_ON_COMMODITY = (By.XPATH, "//body/div[@id='simple-popover']/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]")
    COMMENT = (By.NAME, "special_requirements")
    SEARCH = (By.XPATH, "//input[@placeholder='Search']")
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

    """Info quote dashboard"""
    SEARCH_FIELD = (By.NAME, "load_id")
    BUTTON_LENS = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/button[1]")
    QUOTE_ID = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/p[2]")
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
    BUTTON_DOTS = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]")
    BUTTON_EDIT = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]")
    BUTTON_UPDATE = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]")
    BUTTON_DELETE = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]")
    BUTTON_CONFIRM = (By.XPATH, "//span[contains(text(),'Confirm')]")

    UPDATE_ACTION = (By.XPATH, "//span[text()='Update']")

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

    def click_and_update(self):
        self.do_click(self.BUTTON_DOTS)
        self.do_click(self.BUTTON_UPDATE)

    def click_and_delete(self):
        self.do_click(self.BUTTON_DOTS)
        self.do_click(self.BUTTON_DELETE)

    def verify_quote(self):
        quote_id = self.get_element_text(self.QUOTE_ID)
        self.send_keys(self.SEARCH_FIELD, quote_id)
        self.do_click(self.BUTTON_LENS)

    def confirm_delete(self):
        self.do_click(self.BUTTON_CONFIRM)
    
    def do_clear_eq(self):
        self.do_click(self.CLEAR_FIELD_EQ)
        self.do_click(self.CLEAR_FIELD_COMMODITY)

    def get_all_info_quote_from_dashboard(self):
        global quote_info
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
        # self.do_click(self.BUTTON_EXIT)
        return quote_info

    def click_on_shipping(self):
        self.do_click(self.SHIPPING_BUTTON)

    def fill_load_information(self, customer, equipment, weigth, commodity, comment):
        self.do_click(self.CUSTOMER)
        self.send_keys(self.SEARCH, customer)
        self.do_click(self.CLICK_ON_CUSTOMER)
        self.do_click(self.CLEAR_EQ)
        self.do_click(self.EQUIPMENT_TYPE)
        self.send_keys(self.SEARCH, equipment)
        self.do_click(self.CLICK_ON_EQ)
        self.do_clear(self.WEIGTH)
        self.send_keys(self.WEIGTH, weigth)
        self.do_click(self.CLEAR_COMMODITY)
        self.do_click(self.COMMODITY)
        self.send_keys(self.SEARCH, commodity)
        self.do_click(self.CLICK_ON_COMMODITY)
        self.do_clear(self.COMMENT)
        self.send_keys(self.COMMENT, comment)

    def auto_fill_shipping_information(self, shipper_city, receiver_city):
        self.do_click(self.SHIPPER_CITY)
        self.send_keys(self.SEARCH, shipper_city)
        self.do_click(self.CLICK_ON_SCITY)
        actual_day = self.get_current_day()
        ORIGIN_DAY = (By.XPATH, f"//button[@tabindex='0']//p[text()='{actual_day}']")
        if int(actual_day) > 26:
            self.do_click(self.D_ARRIVE_DATE)
            self.do_click(self.NEXT_CALENDAR)
            # dest_day = int(actual_day) + 5
            DEST_DAY_LOCATOR = (By.XPATH, f"//p[text()='1']")
            self.do_click(DEST_DAY_LOCATOR)
        else:
            self.do_click(self.D_ARRIVE_DATE)
            dest_day = int(actual_day) + 5
            DEST_DAY_LOCATOR = (By.XPATH, f"//p[text()='{str(dest_day)}']")
            self.do_click(DEST_DAY_LOCATOR)
        self.do_click(self.O_ARRIVE_DATE)
        self.do_click(ORIGIN_DAY)
        self.do_click(self.RECEIVER_CITY)
        self.send_keys(self.SEARCH, receiver_city)
        self.do_click(self.CLICK_ON_RCITY)
        self.do_click(self.UPDATE_ACTION)
    
