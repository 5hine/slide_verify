from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

import re
from selenium.webdriver.common.by import By
from selenium .webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os

# options = webdriver.FirefoxOptions()
# options.add_argument('excludeSwitches')
# options.add_experimental_option('excludeSwitches', ['enable-automation'])

#print(os.path())
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
chromedriver_path = "C:/Users/lanyu/AppData/Local/Programs/Python/Python37/Scripts/chromedriver.exe"
browser = webdriver.Chrome(options=options)
browser.set_window_size(1440, 900)
try:
    browser.get("https://login.tmall.com/")
    #str = browser.page_source
    time.sleep(1)
    browser.switch_to.frame("J_loginIframe")
    wait = WebDriverWait(browser, 10)
    # with open('1.txt', 'wb')as f:         #将页面内容保存到文本，方便查找
    #     f.write(str.encode())
    #print(browser.page_source)
    pwd_btn = browser.find_element_by_id("J_Quick2Static")
    # browser.find_elements_by_xpath('//*[@class="forget-pwd J_Quick2Static"]')    #id = nc_1_n1z
    pwd_btn.click()
    time.sleep(3)
    input_username_btn = browser.find_element_by_id("TPL_username_1")
    input_username_btn.send_keys("1")
    input_password = browser.find_element_by_id("TPL_password_1")
    input_password.click()

    slider = browser.find_element_by_id("nc_1_n1z")
    # 通过测试滑块 知道 滑块移动的left 为 258px 时，到达最右边\

    # 按住滑块
    ActionChains(browser).click_and_hold(slider).perform()
    # 拖动
    track = (i for i in range(248))

    # for x in track:
    #     ActionChains(browser).move_by_offset(xoffset=x, yoffset=0).perform()
    ActionChains(browser).drag_and_drop_by_offset(slider, 280.123, 0).perform()
    time.sleep(0.2123)
    #ActionChains(browser).drag_and_drop_by_offset(slider, offset, 0).perform()

    # 释放
    ActionChains(browser).click_and_hold().release().perform()
    #resule = browser.find_elements_by_class_name("nc-lang-cnt").text

except Exception:
    raise
finally:
    pass
    #browser.close()
