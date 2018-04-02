# coding:utf-8
import selenium
import selenium.webdriver
import time,random,json
from lxml import etree
import requests
from pyquery import PyQuery as pq
from concurrent.futures import ProcessPoolExecutor
from selenium.webdriver.common.action_chains import ActionChains
base_heads = {
    'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
}

def rank(doc,num):
    for i in range(num):
        # 控制滚动条下滑，x为向右滚动的像素
        doc.execute_script("window.scrollBy(0,300)")
        time.sleep(1)
    return doc
def login_home():
    # keys = ['小桔', '贵州', '矿石', '广州', '科技', '网络']
    user_agent = "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);"
    # 火狐浏览器设置
    # fp = selenium.webdriver.FirefoxProfile()
    # fp.set_preference("general.useragent.override", user_agent)
    # driver = selenium.webdriver.Firefox(firefox_profile=fp)
    options = selenium.webdriver.ChromeOptions()
    # 设置中文
    options.add_argument('lang=zh_CN.UTF-8')
    # 更换头部
    options.add_argument("User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0);")
    # options.add_argument('accept="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"')
    # options.add_argument('accept-encoding="gzip, deflate"')
    # options.add_argument('accept-language="zh-CN,zh;q=0.9"')
    # options.add_argument('cache-control="max-age=0"')
    # options.add_argument('connection="keep-alive"')
    # options.add_argument('host="www.qichacha.com"')
    # options.add_argument('cache-control="max-age=0"')
    # options.add_argument('referer="http://www.qichacha.com/"')
    # options.add_argument('upgrade-insecure-requests="1"')

    driver = selenium.webdriver.Chrome(chrome_options=options)
    # driver.set_window_size(1000,800)
    driver.get("http://www.qichacha.com/user_login")
    time.sleep(2)

    user = driver.find_element_by_id("nameNormal")
    password = driver.find_element_by_id("pwdNormal")
    submit = driver.find_element_by_xpath("//*[@id='user_login_normal']/button")
    user.clear();
    time.sleep(1)
    user_key = '13924379750'
    for k in user_key:
        user.send_keys(k)
    time.sleep(2)

    password.clear()
    time.sleep(2)
    pwd_key='cdsire0124'
    for k in pwd_key:
        password.send_keys(k)
    time.sleep(2)

    # 拖动验证码元素
    dragger = driver.find_element_by_id('nc_1_n1z')
    action = ActionChains(driver)
    #action.drag_and_drop_by_offset(dragger,309,0).perform()
    offset = 308/5
    action.click_and_hold(dragger).perform()
    for i in range(5):
        try:
            action.move_by_offset(offset, 0).perform()
            time.sleep(3)
        except Exception as e:
            print(e)
    time.sleep(10)  #等待输入验证码
    submit.click()
    time.sleep(3)   #等待页面加载
    print(driver.current_url)
    # cookies = driver.get_cookies()
    # cookie = {}
    # for item in cookies:
    #     cookie[item.get('name')] = item.get('value')
    # with open('cookies.txt', 'w') as f1:
    #     f1.write(json.dumps(cookie))  # 写入转换为字符串的字典
    # driver = rank(driver,4)
    # driver.find_element_by_xpath("//*[@id='area']/ul/li[6]/a/a[@href='/g_GD']").click()

    # for i in range(200):
    #     searchkey = driver.find_element_by_xpath("//*[@id='searchkey']")
    #     print(searchkey)
    #     searchkey.clear()
    #     searchkey.send_keys(random.choice(keys))
    #     time.sleep(random.random()+1)
    #     if 'search-list' not in str(driver.page_source):
    #         print(driver.page_source)
        # submit = driver.find_element_by_id('V3_Search_bt').click()
        # time.sleep(random.random())
        # driver.back()

    # print('跳转...')
    # time.sleep(2)
    # windows = driver.window_handles
    # driver.switch_to.window(windows[-1])
    # driver = rank(driver,4)  # 下滚动
    #
    # doc = pq(driver.page_source)
    # links = [i.attr('href') for i in doc('a.list-group-item clearfix').items()]
    # print(links)
    # return driver
if __name__ == '__main__':
    login_home()