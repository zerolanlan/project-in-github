
from selenium import webdriver ##驱动
import time ##强制性等待
def get_liuyanban(qq,pwd): ##加载驱动（下面这个）
    driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    driver.get('http://user.qzone.qq.com/{}/334'.format(qq))
    print(qq+'的空间留言板')
    try:
        driver.find_element_by_id('login_div') 
        a = True
    except:
        a = False
    if a==True:
        driver.switch_to.frame('login_frame')##跳到子框架
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys(qq)
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys(pwd)
        driver.find_element_by_id('login_button').click()
        driver.implicitly_wait(10)
    try:
        driver.find_element_by_id('QM_OwnerInfo_ModifyIcon')
        b = True
        print('可以访问')
    except:
        b=False
        print('没有访问权限或则网络错误，请重试')

    if b==True:
        driver.find_element_by_id('dialog_button_1').click()
        driver.implicitly_wait(5)
        print('开始加载')
        driver.switch_to.frame('app_canvas_frame')
        num = driver.find_element_by_id('cnt')
        x = int(num.text)
        y=x//10+1
        for i in range(y):
            time.sleep(3)
            names = driver.find_elements_by_xpath('//*[@class="username"]/a')#找出所有符合xpath的a标签
            ments = driver.find_elements_by_class_name('cont')##留言内容
            print('第%s页留言'%(i+1))
            for name,ment in zip(names,ments):##zip将姓名和留言内容进行打包循环
                data = {  
                    '留言人':name.text,
                    '留言内容':ment.text
                }
            print(data)
            page_down = driver.find_element_by_xpath('//*[@id="pager_bottom"]/div/p[1]/a[2]')#找到下一页标签
            page_down.click()##翻页操作
            time.sleep(3)##强制等待3秒
    print('OK')
    print("=======完成=======")
    # driver.close()
    # driver.quit()
if __name__=='__main__':
     # qq=input("请输入qq号:")
     # mm=input("请输入密码:")

     get_liuyanban("1583143041","mqj1730292041")
