from selenium import webdriver
import time

def warn_user(username, pwd, handles):
    browser = webdriver.Chrome()

    url = "https://twitter.com/login/error?redirect_after_login=%2F"

    browser.get(url)

    email = browser.find_element_by_class_name("js-username-field")
    email.send_keys(username)

    password = browser.find_element_by_class_name("js-password-field")
    password.send_keys(pwd)

    browser.find_element_by_css_selector("button[type='submit']").click()

    for handle in handles:
        tweet_box = browser.find_element_by_css_selector("div[aria-labelledby='tweet-box-home-timeline-label']")
        tweet_box.send_keys("@" + handle + " this is a warning from a bot, stop this or I will block you")
        time.sleep(1)
        browser.find_element_by_class_name("tweeting-text").click()
        time.sleep(2)

    browser.close()
