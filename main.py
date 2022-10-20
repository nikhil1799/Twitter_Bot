from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
PROMISED_DOWN = 1500
PROMISED_UP = 940
CHROME_DRIVER_PATH = Service('/Users/nikhilpatel/Local Files/chromedriver')
TWITTER_EMAIL = '@PatelDummy'
TWITTER_PASSWORD = 'w3M9&f3i+WQ7%DF'


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=driver_path)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        accept_button = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        accept_button.click()

        time.sleep(50)
        download = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        upload = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        return download, upload

    def tweet_at_provider(self, upload, download):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        email = self.driver.find_element(By.NAME,'text')
        email.send_keys('PatelDummy')
        time.sleep(2)
        email.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.NAME,
                                            'password')
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(7)
        tweet_compose = self.driver.find_element(By.CSS_SELECTOR,'.DraftEditor-editorContainer div')
        tweet = f"Hey @Bell, why is my internet speed {download} down and {upload} up when I pay for {PROMISED_DOWN} down and {PROMISED_UP} up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)
        tweet_button = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
download, upload = bot.get_internet_speed()
bot.tweet_at_provider(upload, download)




