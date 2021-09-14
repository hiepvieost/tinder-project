import selenium
from selenium import webdriver
from selenium.common.exceptions import  NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_drive_path =  "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)

URL = "https://tinder.com/"
EMAIL = "hiepviedeu@gmail.com"
PASSWORD = "jaja23456"

driver.get(URL)
# step1: signin with facebook account
sleep(5)
signin = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
signin.click()
sleep(5)
signin_fb = driver.find_element_by_xpath('//*[@id="c1564682258"]/div/div/div[1]/div/div[3]/span/div[2]/button')
signin_fb.click()
# step2 :switch to fb page to login with your fb acc
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email = driver.find_element_by_id("email")
password = driver.find_element_by_xpath('//*[@id="pass"]')
email.send_keys(EMAIL)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
# switch to your main window
driver.switch_to.window(base_window)
# share location button
sleep(5)
location = driver.find_element_by_xpath('//*[@id="c1564682258"]/div/div/div/div/div[3]/button[1]')
location.click()
enable = driver.find_element_by_xpath('//*[@id="c1564682258"]/div/div/div/div/div[3]/button[1]')
enable.click()

sleep(2)

cookies = driver.find_element_by_xpath('//*[@id="c-690079234"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for _ in range(100):

    try:
        sleep(3)
        print("called")
        like_button = driver.find_element_by_xpath('//*[@id="c-690079234"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_button.click()
    
    except selenium.common.exceptions.NoSuchElementException:
        like_button.click()
    except ElementClickInterceptedException:

            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()



driver.quit()
