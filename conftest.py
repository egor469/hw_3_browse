import pytest
from selene import browser, be, have

@pytest.fixture(autouse=True)
def open_browser():
    browser.config.window_height = 1024
    browser.config.window_width = 1024
    browser.open('https://duckduckgo.com')
    yield
    browser.quit()

