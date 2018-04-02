# -*- coding: utf-8 -*-
import selenium
import selenium.webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains



driver = selenium.webdriver.Chrome()
driver.get("http://www.qichacha.com/user_login")
time.sleep(10)

user = driver.find_element_by_id("nameNormal")
password = driver.find_element_by_id("pwdNormal")
submit = driver.find_element_by_xpath("//*[@id='user_login_normal']/button")
user.clear();
time.sleep(1)
user.send_keys("13924379750")
time.sleep(2)

password.clear()
time.sleep(2)
password.send_keys("cdsire0124")
time.sleep(5)

# 拖动验证码元素
dragger = driver.find_element_by_id('nc_1_n1z')
action = ActionChains(driver)

#鼠标左键按下不放
action.click_and_hold(dragger).perform()

#平行移动大于解锁的长度的距离
action.drag_and_drop_by_offset(dragger,308, 0).perform()

# 这个延时必须有，在滑动后等待回复原状
time.sleep(8)
# for i in range(10):
#     try:
#         action.move_by_offset(offset, 0).perform()
#         time.sleep(3)
#     except Exception as e:
#         print(e)
submit.click()
time.sleep(3)   #等待页面加载
print(driver.current_url)