from time import sleep
from Config.config import TestData
from Pages.CompleteProcessPage import CompleteProcess
from Tests.test_base import BaseTest

class Test_CompleteProcess(BaseTest):

    def test_complete_process(self):
        global rate
        self.completeprocess = CompleteProcess(self.driver, TestData.BASE_URL)
        self.completeprocess.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.completeprocess.click_on_load_entry()
        self.completeprocess.fill_load_information(TestData.CUSTOMER, TestData.EQUIPMENT_TYPE, TestData.WEIGTH, TestData.COMMODITY, TestData.COMMENT)
        self.completeprocess.click_on_shipping()
        self.completeprocess.auto_fill_shipping_information(TestData.ORIGIN1, TestData.DESTINATION1)
        self.completeprocess.click_on_save()
        self.completeprocess.click_on_quote()
        self.completeprocess.save_quote()
        self.completeprocess.truck_cost_process('Quote made from automation test')
        self.completeprocess.click_on_sales_markup()
        self.completeprocess.search_quote()
        self.completeprocess.click_on_quote_sales()
        self.completeprocess.rate_process()
        self.completeprocess.click_on_quotes_history()
        self.completeprocess.search_quote_on_history()
        self.completeprocess.click_on_quote_history()
        self.completeprocess.click_on_won()
    
    def test_chack_quote_on_capacity(self):
        self.completeprocess = CompleteProcess(self.driver, TestData.URL_CAPACITY)
        self.completeprocess.open_capacity_and_login(TestData.USER_NAME_CAPACITY, TestData.PASSWORD_CAPACITY)
        self.completeprocess.verify_rate_on_capacity()
        sleep(3)