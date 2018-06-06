#!/usr/bin/env python3
from selenium import webdriver
import time

import json


class GetScreenshot:
    def __init__(self):
        self.catamel_url = "https://scicatapi.esss.dk/"
        self.catanie_url = "https://scicat.esss.dk/"

    def get_screenshot(self):
        with open('brightconfig.json') as f:
            data = json.load(f)

        browser = webdriver.Chrome()
        browser.get(self.catamel_url + "visualize")
        browser.save_screenshot("visualize.png")
        browser.get(self.catamel_url + "modeldiagram")
        browser.save_screenshot("modeldiagram.png")

        browser.get(self.catanie_url + "login")
        browser.save_screenshot("login.png")
        username = browser.find_element_by_id("emailInput")
        password = browser.find_element_by_id("pwdInput")

        username.send_keys(data["username"])
        password.send_keys(data["password"])

        browser.find_element_by_id("login-btn").click()
        time.sleep(3)
        browser.save_screenshot("dashboard.png")

        browser.quit()


if __name__ == '__main__':
    g = GetScreenshot()
    g.get_screenshot()
