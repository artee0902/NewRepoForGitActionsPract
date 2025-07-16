from pages.base_page import BasePage
from playwright.sync_api import expect

class TrainBookingPage(BasePage):
    def select_origin(self, origin):
        self.page.click("#ctl00_mainContent_ddl_originStation1_CTXT")
        self.page.wait_for_selector("a[value='BLR']")
        self.page.locator("a[value='BLR']").click()

    def select_destination(self, destination):
        self.page.wait_for_selector("a[value='MAA']")
        self.page.locator("a[value='MAA']").click()

    def click_search(self):
        self.page.click("#ctl00_mainContent_btn_FindFlights")
