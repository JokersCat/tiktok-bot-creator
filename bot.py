import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip
from time import sleep

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver, 20)
driver.get('https://temp-mail.org/en/')


def login():
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tm-body"]/div[1]/div/div/div[2]/div[1]/form/div[2]/button'))).click()
    temp_mail = pyperclip.paste()


    #send verify email
    driver.switch_to.new_window()
    driver.get('https://www.tiktok.com/signup/phone-or-email/email')
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/form/div[2]/div[1]/div'))).click()  # month
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/form/div[2]/div[1]/ul/li[11]'))).click()  # 11
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/form/div[2]/div[2]/div'))).click()  # day
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/form/div[2]/div[2]/ul/li[4]'))).click()  # 4
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/form/div[2]/div[3]/div'))).click()  # year
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/form/div[2]/div[3]/ul/li[19]'))).click()  # 2003
    wait.until(EC.element_to_be_clickable((By.NAME, 'email'))).send_keys(temp_mail)  # email
    wait.until(EC.element_to_be_clickable((By.NAME, 'password'))).send_keys('Jello@1234')  # password
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]/form/div[4]/div[5]/button'))).click()
    
    
    #get_verification_code
    driver.switch_to.window(driver.window_handles[0])
    #script to get code
    
    
    #input code
    driver.switch_to.window(driver.window_handles[1])
    #script to paste code and submit
    
    
    #sub to account
    #script to sup to specific account


start = int(input('type 1 to start'))
if start == 1:
    account = ('Account you want to bot: ')
    login()
else:
    print('See you next time')
    exit()
