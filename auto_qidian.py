from appium  import  webdriver
import time
#这是pc的appium的本机地址和端口，不可变
from appium.webdriver.common.touch_action import TouchAction

server = "http://localhost:4723/wd/hub"
#这是要打开的手机和起点app的各项信息
param ={
  "deviceName": "21a39b110408",
  "platformName": "Android",
  "platformVersion": "10",
  "appPackage": "com.qidian.QDReader",
  "appActivity": "com.qidian.QDReader.ui.activity.MainGroupActivity"
}
#把各项数据给了手机驱动
driver = webdriver.Remote(server,param)

time.sleep(3)

TouchAction(driver).tap(x=729, y=1376).perform()
time.sleep(3)
TouchAction(driver).tap(x=122, y=333).perform()
time.sleep(10)
TouchAction(driver).tap(x=533, y=1653).perform()
time.sleep(5)
TouchAction(driver).tap(x=814, y=2123).perform()

while True:
  time.sleep(3)
  TouchAction(driver).tap(x=1050, y=1000).perform()
  time.sleep(3)
  TouchAction(driver).tap(x=1050, y=166).perform()
  time.sleep(3)
  TouchAction(driver).tap(x=1050, y=166).perform()


