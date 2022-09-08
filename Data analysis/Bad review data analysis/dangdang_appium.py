import time
import random
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC


def main():
    # 设置驱动配置
    server = 'http://localhost:4723/wd/hub'
    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'STF_AL00',
        'appPackage': 'com.dangdang.buy2',
        'appActivity': 'com.dangdang.buy2.StartupActivity'
    }
    driver = webdriver.Remote(server, desired_caps)
    # 这里获取一下手机屏幕实际大小,可以为设置滑动参数做参考
    size = driver.get_window_size()
    print(size)
    wait = WebDriverWait(driver, 60)
    # 因为要叫我切换地区，选择取消
    button_1 = wait.until(EC.presence_of_element_located((By.ID, 'com.dangdang.buy2:id/left_bt')))
    button_1.click()
    # 点击图书榜按钮
    button_2 = wait.until(EC.presence_of_element_located((By.ID, 'com.dangdang.buy2:id/index_icon_iv0')))
    button_2.click()
    # 点击图书「活着」区域块
    button_3 = wait.until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.ListView/android.widget.LinearLayout[2]')))
    button_3.click()
    # 点击评论区域块
    button_4 = wait.until(EC.presence_of_element_located((By.ID, 'com.dangdang.buy2:id/product_component_book_score_ll')))
    button_4.click()
    time.sleep(5)
    # 点击差评按钮
    button_5 = wait.until(EC.presence_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[6]/android.widget.TextView')))
    button_5.click()
    # 向下滑动,y轴参数我随便选的,向上滑就对了
    while True:
        TouchAction(driver).press(x=515, y=1247).move_to(x=515, y=1026).release().perform()
        time.sleep(float(random.randint(5, 10)))


if __name__ == '__main__':
    main()
