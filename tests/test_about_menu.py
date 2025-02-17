from selenium import webdriver
from time import sleep


def test_about_text():
    driver = webdriver.Chrome(r'C:\Users\Nikki\Downloads\chromedriver.exe')
    driver.get('http://localhost/devops/')
    about_xpath = '//a[text()="About Us"]'
    about_text = 'ABOUT US'
    about_menu = driver.find_element_by_xpath(about_xpath)
    assert about_text == about_menu.text, "text not matching"
    print('expected text is matching')
    about_menu.click()
    print('Opening about page...')

    sleep(5)
    driver.close()
