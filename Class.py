from selenium import webdriver
from pyautogui import press
from time import sleep
from datetime import datetime
from winsound import Beep


def beep():
    for i in range(3):
        Beep(440,1000)


def classs(link):
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:\\Users\\Zein Zebib\\AppData\\Local\\Google\\Chrome\\User Data")
    driver=webdriver.Chrome(executable_path='C:\\Users\Zein Zebib\Documents\Python Stuff\Online Automation\chromedriver',
    chrome_options=options)
    driver.get(str(link))
    sleep(3)
    press('left')
    press('enter')
    sleep(5)
    press('enter')
    driver.close()

l=input("Enter Your class link: ")
start=str(input("Enter your class start time:\nEx:09:00 :  "))

while True:
    now= datetime.now()
    t=now.strftime('%H:%M')
    if t==start:
        beep()
        classs(l)
        break
