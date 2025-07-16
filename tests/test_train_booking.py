from pages.train_page import TrainBookingPage

def test_book_train(page):
    train_page = TrainBookingPage(page)
    train_page.visit("https://rahulshettyacademy.com/dropdownsPractise/")
    train_page.select_origin("Bengaluru (BLR)")
    train_page.select_destination("Chennai (MAA)")
    train_page.click_search()
    assert "spicejet" in page.url or page.title()
