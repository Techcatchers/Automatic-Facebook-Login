from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

driver = webdriver.Chrome(r'C:\Users\Rishabh-Pc\Downloads\chromedriver')

driver.get("https://facebook.com/")
wait = WebDriverWait(driver, 600)

userpass = []

with open(r'D:\Web Development and Programming\CS50\Final Project\Automated\credentials.txt') as f:
    for line in f:
        name = (line.rstrip('\n'))
        userpass.append(name)
    try:

        inp_xpath = "//input[@id='email']"
        input_box = wait.until(EC.presence_of_element_located((
            By.XPATH, inp_xpath)))
        input_box.send_keys(userpass[0] + Keys.TAB)

        inpass_xpath = "//input[@id='pass']"
        input_box = wait.until(EC.presence_of_element_located((
            By.XPATH, inpass_xpath)))
        input_box.send_keys(userpass[1] + Keys.ENTER)
        try:
            time.sleep(1)
            keyboard.press(Key.esc)
            keyboard.release(Key.esc)
        except:
            print("Escape Error")
        print("Logged in")
    except:
        print("error")
