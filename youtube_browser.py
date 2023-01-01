from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import lib
from lib import *

class browser_test:
    
    driver =''
    start_url="https://www.youtube.com/"

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        #self.chrome_options.add_argument("--incognito")

    def main(self):
        try:
            #import pdb;pdb.set_trace()
            driver=webdriver.Chrome(chrome_options=self.chrome_options)
            browser_obj=common_lib().browser_open(driver,self.start_url)
            print ("site:", browser_obj.title)
            print("site_url:", browser_obj.current_url)
            search=common_lib().find_element_by_name(browser_obj,"search_query")
            search.send_keys("kal ho na ho sad song")
            #import pdb;pdb.set_trace()
            browser_obj.implicitly_wait(10)
            searchbox=common_lib().find_element_by_id(browser_obj,"search-icon-legacy")
            searchbox.click()
            select_song=common_lib().find_element_by_xpath(browser_obj,'//a[@href="/watch?v=g0eO74UmRBs"]')
            # time.sleep(3)
            select_song.click()
        except Exception as e:
            print ("error:",type(e))
            common_lib().browser_close(browser_obj)        

browser_test().main()

class textboxes_manipulation_data:

    driver =''
    start_url="https://www.formsite.com/"

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        #self.chrome_options.add_argument("--incognito")

    def main(self):
        try:
            #import pdb;pdb.set_trace()
            driver=webdriver.Chrome(chrome_options=self.chrome_options)
            browser_obj=common_lib().browser_open(driver,self.start_url)
            print ("site:", browser_obj.title)
            print("site_url:", browser_obj.current_url)
            wait=WebDriverWait(browser_obj,5)
            search_signup=wait.until(EC.element_to_be_clickable(By.XPATH,'//a[@title="Sign up free"]'))
            search_signup.click
            #simport pdb;pdb.set_trace()
            browser_obj.implicitly_wait(10)

            searchbox_user=common_lib().find_element_by_name(browser_obj,"UserId").send_keys("Saayan123@")
            searchbox_passwd=common_lib().find_element_by_name(browser_obj,"Password1").send_keys("Don9891das@")
            searchbox_email=common_lib().find_element_by_name(browser_obj,"UserEmail").send_keys("saayan8981@gmail.com")
            time.sleep(2)            
            submit_click=common_lib().find_element_by_xpath(browser_obj,'//div[@class="auth-form__group"]/button[@type="submit"]').click()
            
        except Exception as e:
            print ("error:",type(e))
            common_lib().browser_close(browser_obj)


#stextboxes_manipulation_data().main()