from Config.config import TestData
from Pages.CreateQuotePage import CreateQuotePage
from Tests.test_base import BaseTest

class Test_CreateAndReadQuote(BaseTest):

    def test_create_quote(self):
        global OBJECT_INFO, FULL_INFO_OBJECT
        """Create a quote with a random zip code"""
        self.createQuote = CreateQuotePage(self.driver)
        self.createQuote.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.createQuote.click_on_load_entry()
        self.createQuote.fill_load_information(TestData.CUSTOMER, TestData.EQUIPMENT_TYPE, TestData.WEIGTH, TestData.COMMODITY, TestData.COMMENT)
        self.createQuote.click_on_shipping()
        self.createQuote.fill_shipping_information(TestData.ORIGIN2, TestData.ORIGIN_ZIP_CODE, TestData.DESTINATION2, TestData.DESTINATION_ZIP_CODE)
        self.createQuote.click_on_save()
        self.createQuote.click_on_ok()
        """Create a quote with auto zip code"""
        self.createQuote.click_on_load_entry()
        self.createQuote.fill_load_information(TestData.CUSTOMER, TestData.EQUIPMENT_TYPE, TestData.WEIGTH, TestData.COMMODITY, TestData.COMMENT)
        self.createQuote.click_on_shipping()
        self.createQuote.auto_fill_shipping_information(TestData.ORIGIN1, TestData.DESTINATION1)
        OBJECT_INFO = self.createQuote.get_quote_info()
        FULL_INFO_OBJECT = self.createQuote.get_all_info_quote()
        self.createQuote.click_on_save()


    def test_read_quote(self):
        self.createQuote = CreateQuotePage(self.driver)
        QUOTE_INFO = self.createQuote.get_quote_info_from_dashboard()
        assert OBJECT_INFO == QUOTE_INFO
        self.createQuote.click_on_quote()
        QUOTE_FROM_DASHBOARD = self.createQuote.get_all_info_quote_from_dashboard()
        assert FULL_INFO_OBJECT == QUOTE_FROM_DASHBOARD
