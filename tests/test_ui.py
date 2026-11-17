import pytest
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    wait = WebDriverWait(driver, 10)
    title = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "title")))
    assert title.text == "Products"

def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")
    
    wait = WebDriverWait(driver, 10)
    error = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))
    assert "locked out" in error.text