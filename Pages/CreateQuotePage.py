from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData

class CreateQuotePage(BasePage):
    
    """By locators"""

    EMAIL = (By.XPATH, "//input[@id='loginFormEmailInput']")
    PASSWORD = (By.ID, "loginFormPasswordInput")
    LOGIN_BUTTON = (By.XPATH , "//span[text()='Login']")

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

    SHIPPER_CITY_DASHBOARD = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/p[1]")
    O_ARRIVE_DATE_DASHBOARD = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/p[1]")
    RECEIVER_CITY_DASHBOARD = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/p[1]")
    D_ARRIVE_DATE_DASHBOARD = (By. XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[2]/div[1]/p[1]")

    CLICK_ON_QUOTE = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]")

    SCITY = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/p[1]")
    SZIP = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/p[2]")
    ODATE = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/p[1]")
    RCITY = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/p[1]")
    RZIP = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[2]/p[2]")
    DDATE = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/div[1]/div[2]/p[1]")
    EQ = (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/p[1]")
    COMMODITY_QUOTE = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/p[1]")


    """Constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """This is used to login to app"""
    def do_login(self, username, password):
        self.send_keys(self.EMAIL, username)
        self.send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

    def click_on_quote(self):
        self.do_click(self.CLICK_ON_QUOTE)
    
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

    def fill_shipping_information(self, shipper_city, zip_code1, receiver_city, zip_code2):
        self.do_click(self.SHIPPER_CITY)
        self.send_keys(self.SEARCH, shipper_city)
        self.do_click(self.CLICK_ON_RCITY2)
        self.do_clear(self.ZIP_CODE1)
        self.send_keys(self.ZIP_CODE1, zip_code1)
        self.do_click(self.O_ARRIVE_DATE)
        actual_day = self.get_current_day()
        ORIGIN_DAY = (By.XPATH, f"//button[@tabindex='0']//p[text()='{actual_day}']")
        self.do_click(ORIGIN_DAY)
        self.do_click(self.D_ARRIVE_DATE)
        if int(actual_day) > 26:
            self.do_click(self.NEXT_CALENDAR)
            dest_day = int(actual_day) + 5
            DEST_DAY_LOCATOR = (By.XPATH, f"//button[@tabindex='0']//p[text()='1']")
            self.do_click(DEST_DAY_LOCATOR)
        else:
            dest_day = int(actual_day) + 5
            DEST_DAY_LOCATOR = (By.XPATH, f"//button[@tabindex='0']//p[text()='{str(dest_day)}']")
            self.do_click(DEST_DAY_LOCATOR)
        self.do_click(self.RECEIVER_CITY)
        self.send_keys(self.SEARCH, receiver_city)
        self.do_click(self.CLICK_ON_DCITY2)
        self.do_clear(self.ZIP_CODE2)
        self.send_keys(self.ZIP_CODE2, zip_code2)
        
    
    def click_on_save(self):
        self.do_click(self.BUTTON_SAVE)

    def click_on_ok(self):
        self.do_click(self.BUTTON_OK)
    
    def auto_fill_shipping_information(self, shipper_city, receiver_city):
        self.do_click(self.SHIPPER_CITY)
        self.send_keys(self.SEARCH, shipper_city)
        self.do_click(self.CLICK_ON_SCITY)
        self.do_click(self.O_ARRIVE_DATE)
        actual_day = self.get_current_day()
        ORIGIN_DAY = (By.XPATH, f"//button[@tabindex='0']//p[text()='{actual_day}']")
        self.do_click(ORIGIN_DAY)
        self.do_click(self.D_ARRIVE_DATE)
        if int(actual_day) > 26:
            self.do_click(self.NEXT_CALENDAR)
            dest_day = int(actual_day) + 5
            DEST_DAY_LOCATOR = (By.XPATH, f"//button[@tabindex='0']//p[text()='1']")
            self.do_click(DEST_DAY_LOCATOR)
        else:
            dest_day = int(actual_day) + 5
            DEST_DAY_LOCATOR = (By.XPATH, f"//button[@tabindex='0']//p[text()='{str(dest_day)}']")
            self.do_click(DEST_DAY_LOCATOR)
        self.do_click(self.RECEIVER_CITY)
        self.send_keys(self.SEARCH, receiver_city)
        self.do_click(self.CLICK_ON_RCITY)

    def get_quote_info(self):
        quote_object = {
        "shipper_city":self.get_value(self.SHIPPER_CITY),
        "o_arrive_date":self.get_value(self.O_ARRIVE_DATE),
        "receiver_city":self.get_value(self.RECEIVER_CITY),
        "d_arrive_date":self.get_value(self.D_ARRIVE_DATE)
        }
        return quote_object

    def get_quote_info_from_dashboard(self):
        quote_info = {
            "shipper_city":self.get_element_text(self.SHIPPER_CITY_DASHBOARD),
            "o_arrive_date":self.get_element_text(self.O_ARRIVE_DATE_DASHBOARD),
            "receiver_city":self.get_element_text(self.RECEIVER_CITY_DASHBOARD),
            "d_arrive_date":self.get_element_text(self.D_ARRIVE_DATE_DASHBOARD)
        }
        return quote_info
 
    def get_all_info_quote(self):
        quote_object = {
            "shipper_city":self.get_value(self.SHIPPER_CITY),
            "o_arrive_date":self.get_value(self.O_ARRIVE_DATE),
            "receiver_city":self.get_value(self.RECEIVER_CITY),
            "d_arrive_date":self.get_value(self.D_ARRIVE_DATE)
            }
        self.do_click(self.CLICK_ON_LOAD)
        quote_object["equipment"] = self.get_value(self.EQUIPMENT_TYPE)
        quote_object["commodity"] = self.get_commodity_element(self.COMMODITY)
        return quote_object

    def get_all_info_quote_from_dashboard(self):
        quote_info = {
            "shipper_city":self.get_element_text(self.SCITY),
            "o_arrive_date":self.get_element_text(self.ODATE),
            "receiver_city":self.get_element_text(self.RCITY),
            "d_arrive_date":self.get_element_text(self.DDATE),
            "equipment":self.get_element_text(self.EQ),
            "commodity":self.get_element_text(self.COMMODITY_QUOTE)
        }
        return quote_info