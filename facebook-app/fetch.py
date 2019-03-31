from selenium import webdriver
import time
import urllib.request as ur
import os

def get_feed(user, pwd, target_username):

    browser = webdriver.Chrome()

    url = "https://www.facebook.com/"

    browser.get(url)

    username = browser.find_element_by_css_selector("input[name='email']")
    username.send_keys(user)

    password = browser.find_element_by_css_selector("input[name='pass']")
    password.send_keys(pwd)

    browser.find_element_by_css_selector("input[aria-label='Log In']").click()

    url = "https://www.facebook.com/notifications"

    browser.get(url)

    time.sleep(1)

    a = browser.find_elements_by_css_selector("a[data-testid='notif_list_item_link']")
    spans = browser.find_elements_by_class_name("_6btd")

    urls = []

    for url in a:
        u = url.get_attribute("href")
        if "comment_mention" in u:
            urls.append(url.get_attribute("href"))


    browser.close()

    browser_list = [webdriver.Chrome() for _ in range(len(urls))]


    im_to_prof = {}

    for i in range(len(urls)):
        browser_list[i].get(urls[i])

        try:
            l = browser_list[i].find_element_by_css_selector("a[data-render-location='group_hoisted']")
        except:
            l = browser_list[i].find_element_by_css_selector("a[data-render-location='permalink']")

        link = l.get_attribute("data-ploi")

        comments = browser_list[i].find_elements_by_css_selector("span[dir='ltr']")
        profile_links = browser_list[i].find_elements_by_class_name("_6qw4")

        comments = [comment.text for comment in comments]
        profile_links = [profile_link.get_attribute('href') for profile_link in profile_links]

        comments_to_links = {}

        for j in range(len(comments)):
            comments_to_links[comments[j]] = profile_links[j]

        for comment in comments:
            if target_username in comment:
                profile_user = comments_to_links[comment]

        im_to_prof[link] = profile_user

        browser_list[i].close()

    return im_to_prof
