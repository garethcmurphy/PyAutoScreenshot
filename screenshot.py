#!/usr/bin/env python3
from selenium import webdriver
import time

import json

with open('brightconfig.json') as f:
    data = json.load(f)

browser = webdriver.Chrome()
browser.get("https://scicatapi.esss.dk/visualize")
browser.save_screenshot("visualize.png")
browser.get("https://scicatapi.esss.dk/modeldiagram")
browser.save_screenshot("modeldiagram.png")

browser.get("https://scicat.esss.dk/login")
browser.save_screenshot("login.png")
username = browser.find_element_by_id("emailInput")
password = browser.find_element_by_id("pwdInput")

username.send_keys(data["username"])
password.send_keys(data["password"])

element = browser.find_element_by_id("login-btn").click()
time.sleep(10)
browser.save_screenshot("dashboard.png")

browser.quit()
