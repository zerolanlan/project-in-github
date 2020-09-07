from selenium import webdriver
import time
def get liuyanban(qq,pwd):
    driver = webdriver.Chrome(executable_path="C:\Users\文岚清\AppData\Local\Google\Chrome\Application\chromedriver.exe")
    driver.get('https://users.qzone.qq.com/{}/334'.format(qq))
    print(qq+'的空间留言板')
    try:
        driver.find_element_by_id('login_div')
        a = True
    except:
        a = False
    if a == True:
        driver.swith_to.frame('llogin_frame')
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys(qq)
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys(pwd)
        driver.find_element_by_id('login_button').click()
        driver.implicitly_wait(3)
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
        b = True
        print('可以访问')
    except：
        b = False
        print('没有访问权限或者网络错误，请重试')

    if b == True:
        driver.find_element_by_id('dialog_button_1').click()
        dr   iver.implicitly_wait(5)
        print('开始加载')
        driver.switch_to.frame('app_canvas_frame')

        num = driver.find_element_by_id('cnt')
        x = int(num.text)
        y = x // 10
        for i in range(y):
            

