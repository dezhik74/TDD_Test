import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_home_page(driver, live_server):
    driver.get(live_server.url)
    assert driver
    assert 'ToDo App' == driver.title
    h1 = driver.find_element(By.TAG_NAME, 'h1')
    assert h1.text == 'Текущие дела'
    input1 = driver.find_element(By.ID, 'add_todo')
    assert input1.get_attribute('placeholder') == 'Какое дело планируем...'

