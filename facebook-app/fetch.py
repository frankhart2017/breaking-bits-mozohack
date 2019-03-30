from selenium import webdriver
import time
import urllib.request as ur
import os

def get_feed(user, pwd):

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
    
    urls = []
    
    for url in a:
        u = url.get_attribute("href")
        if "comment_mention" in u:
            urls.append(url.get_attribute("href"))
    
    browser.close()
    
    browser_list = [webdriver.Chrome() for _ in range(len(urls))]
    
    for i in range(len(urls)):
        browser_list[i].get(urls[i])
        
        try:
            l = browser_list[i].find_element_by_css_selector("a[data-render-location='group_hoisted']")
        except:
            l = browser_list[i].find_element_by_css_selector("a[data-render-location='permalink']")
        
        link = l.get_attribute("data-ploi")
        
        filename = "data/" + os.path.basename(link.split("?")[0]) + ".jpg"
        
        ur.urlretrieve(link, filename)
    
        browser_list[i].close()