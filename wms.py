from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from urllib3.connectionpool import log
import time

# To try to turn off selenium logs
LOGGER.setLevel(logging.WARNING)
log.setLevel(logging.WARNING)

#xpaths
search_button_p = "/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]"
chat_button_p = "/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]"
last_message_p = "/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/div[3]/div/div[2]/div[3]/div[last()]/div/div/div/div[1]/div/span[1]/span"
path = "chromdriverpath"

def configure(chrome_path, profile, buffer):
    options = webdriver.ChromeOptions()
    options.add_argument("user-data-dir=C:/Users/<user>/AppData/Local/Google/Chrome/User Data")
    options.add_argument("profile-directory=" + profile)
    driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=options)
    driver.get("https://web.whatsapp.com")
    time.sleep(buffer)
    return driver
    

def send_message(driver, target, message):
    search_button = driver.find_element_by_xpath(search_button_p)
    search_button.click()
    search_button.send_keys(target + "\n")
    chat_button = driver.find_element_by_xpath(chat_button_p)
    chat_button.send_keys(message + "\n")

def read_last(driver, target):
    search_button = driver.find_element_by_xpath(search_button_p)
    search_button.click()
    search_button.send_keys(target + "\n")
    time.sleep(5)
    last_message = driver.find_element_by_xpath(last_message_p)
    message = last_message.text
    return message

if __name__ == "__main__":
    messenger = configure(path, "Default", 5)
    target = input("who do you want to send the message to?\n")
    print("reading last message:")
    lm = read_last(messenger, target)
    print(lm)
    respone = input("what reply do you want to send?\n")
    send_message(messenger, target, respone)

