from pages.base_page import BasePage
from playwright.sync_api import expect

class FlightBookingPage(BasePage):
    def select_origin(self, origin):
        self.page.click("#ctl00_mainContent_ddl_originStation1_CTXT")
        self.page.wait_for_selector("a[value='BLR']")  # Wait for options to be visible
        self.page.locator("a[value='BLR']").click()

    def select_destination(self, destination):
        self.page.wait_for_selector("a[value='MAA']")
        self.page.locator("a[value='MAA']").click()

    def select_round_trip(self):
        self.page.locator("#ctl00_mainContent_rbtnl_Trip_1").check()

    def click_search(self):
        self.page.click("#ctl00_mainContent_btn_FindFlights")
