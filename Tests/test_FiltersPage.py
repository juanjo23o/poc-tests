from Config.config import TestData
from Pages.FiltersPage import FiltersPage
from Tests.test_base import BaseTest

class Test_Filters(BaseTest):

    def test_get_all_info(self):
        self.filter = FiltersPage(self.driver)
        self.filter.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.filter.click_on_quote()
        self.filter.get_all_info_quote_from_dashboard()
        self.filter.send_info_to_filters_and_verify()
        