from Config.config import TestData
from Pages.EditDeletePage import EditDeletePage
from Tests.test_base import BaseTest

class Test_EditDeleteQuote(BaseTest):

    def test_delete_quote(self):
        self.deletequote = EditDeletePage(self.driver)
        self.deletequote.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.deletequote.verify_quote()
        self.deletequote.click_on_quote()
        self.deletequote.click_and_delete()
        self.deletequote.confirm_delete()
    
    def test_edit_quote(self):
        self.editquote = EditDeletePage(self.driver)
        self.editquote.click_on_quote()
        quote1 = self.editquote.get_all_info_quote_from_dashboard()
        self.editquote.click_and_update()
        self.editquote.fill_load_information(TestData.CUSTOMER, TestData.EQUIPMENT_TYPE, TestData.WEIGTH, TestData.COMMODITY, 'Quote edited from automation test')
        self.editquote.click_on_shipping()
        self.editquote.auto_fill_shipping_information(TestData.ORIGIN1, TestData.DESTINATION1)
        quote2 = self.editquote.get_all_info_quote_from_dashboard()
        assert quote1 != quote2
