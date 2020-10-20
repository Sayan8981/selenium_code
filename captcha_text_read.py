from pytesseract import image_to_string 
from PIL import Image 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from lib import *

class read_captcha_text:
    
    driver = ''
    start_url = 'https://esearchigr.maharashtra.gov.in/portal/esearchlogin.aspx'
    
    def  __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        
    def get_captcha_text(self, location, size): 
        #import pdb;pdb.set_trace()
        im = Image.open('screenshot1.png')     
        left = location['x']    
        top = location['y']    
        right = location['x'] + size['width']    
        bottom = location['y'] + size['height']
        im = im.crop((left, top, right, bottom))
        im.save('screenshot.png')
        captcha_text = image_to_string(Image.open('screenshot.png'))    
        return captcha_text
                  
    def main(self):
        try:
            self.driver = webdriver.Chrome(chrome_options = self.chrome_options)
            browser_obj = common_lib().browser_open(self.driver, self.start_url)    
            print ("site:", browser_obj.title)
            print("site_url:", browser_obj.current_url)
            #import pdb;pdb.set_trace()
            element = common_lib().find_element_by_xpath(browser_obj, '//*[@class="style3"]/img') # find part of the page you want image of
            location = element.location
            size = element.size
            self.driver.save_screenshot('screenshot1.png')
            user_id = common_lib().find_element_by_name(browser_obj,'txtUserid')
            user_id.clear()    
            user_id.send_keys('Saayan')    
            password = common_lib().find_element_by_name(browser_obj,'txtPswd')
            password.clear()    
            password.send_keys('Saayan@123')    
            captcha = common_lib().find_element_by_name(browser_obj,'txtcaptcha')
            captcha.clear()    
            captcha_text = self.get_captcha_text(location, size)
            captcha.send_keys(captcha_text)    
            # driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
            #common_lib().browser_close(browser_obj)
        except Exception as Error:
            common_lib().browser_close(browser_obj)
                 
        
        
if __name__ == "__main__":
    read_captcha_text().main()                                
        
        