from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.common.keys import Keys



import time

class twitterBot:
    def __init__(self, name, phone, comment):
        self.name = name
        self.phone = phone
        self.comment = comment
        cap = DesiredCapabilities().FIREFOX
        cap["marionette"] = False

        self.bot = webdriver.Chrome('/Users/abbosjonkudratov/Downloads/chromedriver')




    def login(self):
        bot = self.bot
        bot.get('http://grantkorea.uz/')



        time.sleep(2)
        name = bot.find_element_by_name('name')
        phone= bot.find_element_by_name('phone')
        comment = bot.find_element_by_name('comment')


        comment.clear()
        name.clear()
        phone.clear()

        name.send_keys(self.name)
        phone.send_keys(self.phone)
        comment.send_keys(self.comment)
        time.sleep(2)
        submit = bot.find_element_by_id('submit')
        submit.send_keys(Keys.RETURN)




credentials = ['Cornellio U.D.', '661700000', 'hello world']
smth = twitterBot(credentials[0],credentials[1],credentials[2])
smth.login()

