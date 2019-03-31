from selenium import webdriver
import time
import os

def block_user(uname, pwd, profile_link):

    browser = webdriver.Chrome()

    url = "https://www.facebook.com/"

    browser.get(url)

    username = browser.find_element_by_css_selector("input[name='email']")
    username.send_keys(uname)

    password = browser.find_element_by_css_selector("input[name='pass']")
    password.send_keys(pwd)

    browser.find_element_by_css_selector("input[aria-label='Log In']").click()

    time.sleep(1)

    user = os.path.basename(profile_link)

    browser.get("https://www.facebook.com/settings?tab=blocking")

    time.sleep(2)

    block_user = browser.find_element_by_css_selector("input[aria-label='Add name or email']")
    block_user.send_keys(user)

    browser.find_element_by_css_selector("input[value='Block']").click()

    time.sleep(2)

    browser.find_element_by_css_selector("input[value='Block']").click()

    time.sleep(1)
