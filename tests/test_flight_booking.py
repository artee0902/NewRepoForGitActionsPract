from pages.flight_page import FlightBookingPage

def test_book_flight(page):
    flight_page = FlightBookingPage(page)
    flight_page.visit("https://rahulshettyacademy.com/dropdownsPractise/")
    flight_page.select_origin("Bengaluru (BLR)")
    flight_page.select_destination("Chennai (MAA)")
    flight_page.select_round_trip()
    flight_page.click_search()
    assert "spicejet" in page.url or page.title()
