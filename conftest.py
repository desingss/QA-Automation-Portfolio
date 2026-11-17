import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Используем Edge, так как с Chrome у тебя были траблы
    browser = webdriver.Edge()
    browser.maximize_window()
    yield browser
    browser.quit()