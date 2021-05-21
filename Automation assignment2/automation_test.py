from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time, logging, datetime, os, sys
from selenium.webdriver.support.ui import WebDriverWait,Select


class common_module(object):

    def browser_open(self,driver,request_url):       
        driver.get(request_url)
        driver.set_window_size(1800,900)
        return driver

    def create_log(self,log_file):
        self.logger = logging.getLogger()
        logging.basicConfig(filename=log_file,format=[],filemode='w')
        self.logger.setLevel(logging.DEBUG)
        stream_handler = logging.StreamHandler(sys.stdout)
        self.logger.addHandler(stream_handler)
        return self.logger 

    def scroll_down_by_element(self,browser,element_to_scroll):
        return browser.execute_script("arguments[0].scrollIntoView();",element_to_scroll)    

    def browser_close(self,browser):
        browser.close()   


class automation_test(common_module):

    driver =''
    logger = ''
    retry_count = 0
    start_url = "https://demo.sath.com/"

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.chrome_options.add_argument("start-maximized")
        self.chrome_options.add_argument("disable-infobars")
        self.chrome_options.add_argument("--disable-extensions")
        #org_name to input
        self.input_org_name = "Testing"
        #Login using credentials:
        self.username = "qatest"
        self.password = "YEae@WHHs8yFC?z1"
        self.click_request = 'Request Access'
        self.select_tab = 'Applications'
        self.searched_apps = 'G Suite'

    def searching_apps_details(self,browser_obj,search_tab):
        self.search_apps = browser_obj.find_element_by_xpath('//p[@class="descriptive-content-bold"][contains(text(), " %s ")]'%self.searched_apps)
        self.displayed_apps = self.search_apps.is_displayed() 
        try:
            assert self.displayed_apps == True, False 
            if self.displayed_apps == True:
                self.logger.debug ({"The search apps %s is present from %s ="%(self.searched_apps,search_tab) : self.search_apps})
                self.scroll_down_by_element(browser_obj, self.search_apps)
                try:
                    self.apps_logo = browser_obj.find_element_by_xpath('//div//p[@class="descriptive-content-bold"][contains(text(), " %s ")]/preceding::div/img[@class="entity-logo"]'%self.searched_apps)
                    self.displayed_apps_logo = self.apps_logo.is_displayed()                    
                    assert self.displayed_apps_logo == True, False
                    if self.apps_logo.get_attribute('src') and 'https' in self.apps_logo.get_attribute('src'):
                        self.logger.debug ({"Application_logo %s present from %s"%(self.searched_apps,search_tab) : self.apps_logo.get_attribute('src')})
                    else:
                        self.logger.debug ({"Application_logo %s not present %s"%(self.searched_apps,search_tab) : self.apps_logo.get_attribute('src')}) 
                    self.search_keywords = browser_obj.find_element_by_xpath('//p[@class="descriptive-content-bold"][contains(text(), " %s ")]/following-sibling::span'%self.searched_apps).text
                    if 'Company, Productivity, Collaboration' == self.search_keywords:
                        self.logger.debug({"search_keywords present for %s"%self.searched_apps : self.search_keywords})
                    else:
                        self.logger.debug({"search_keywords not present for %s"%self.searched_apps : self.search_keywords})
                    self.description = browser_obj.find_element_by_xpath('//p[@class="descriptive-content-bold"][contains(text(), " %s ")]/following-sibling::div'%self.searched_apps).text
                    if self.description == 'G Suite - Email, Drive, Docs, Sheets, Slides, etc.':
                        self.logger.debug({"Description present for %s"%self.searched_apps : self.description})
                    else:
                        self.logger.debug({"Description not present for %s"%self.searched_apps : self.description})                         
                except Exception as error:
                    self.logger.debug ({"Error": error})                                
                    self.browser_close(browser_obj)
        except Exception as error:
            self.logger.debug ({"Error": error})
            self.logger.debug ({"The search apps %s is present from %s ="%(self.searched_apps,search_tab) : self.search_apps})
            self.browser_close(browser_obj)

    def main(self):
        try:
            self.logger = self.create_log(os.getcwd()+'/logs/log_%s.txt'%datetime.datetime.now().strftime('%d-%m-%Y'))
            self.driver = webdriver.Chrome(chrome_options = self.chrome_options)
            wait = WebDriverWait(self.driver, 200)
            self.browser_obj = self.browser_open(self.driver, self.start_url)
            self.logger.debug ({"Site_Link": self.browser_obj.title})
            self.logger.debug ({"login_url": self.browser_obj.current_url})

            #****************** first page url login button click action ********************
            login_button = self.browser_obj.find_element(By.XPATH, '//div[@class="login-container"]/button[contains(text(),"Login")]')
            time.sleep(10)
            self.scroll_down_by_element(self.browser_obj, login_button)
            time.sleep(10)
            login_button.click()

            #---------------- enter the text 'Testing' and click login again  -----------------------
            input_org_text = self.browser_obj.find_element(By.CLASS_NAME, "org-name-input").send_keys(self.input_org_name) 
            time.sleep(10)
            login_button_after_input = self.browser_obj.find_element(By.XPATH, '//div[@id="login-block"]/form/div/button[contains(text(),"Login")]')
            login_button_after_input.click()
            time.sleep(30)

            #----------------------------  Login using credentials: -------------------------------
            input_username = self.browser_obj.find_element(By.NAME, "username")
            input_username.send_keys(self.username)
            input_password = self.browser_obj.find_element(By.NAME, "password")
            input_password.send_keys(self.password)
            time.sleep(10)
            login_button_after_creds = self.browser_obj.find_element(By.NAME, "login")
            login_button_after_creds.click()

            #***************************  Click on 'Request Access'  ************************************
            wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '%s')]"%self.click_request))).click()

            #---------------- Search for an application named 'GSuite' using Search box -------------------
            wait.until(EC.element_to_be_clickable((By.NAME, "searchKeyword"))).send_keys(self.searched_apps)
            self.browser_obj.find_element(By.XPATH, "//button/span[contains(text(),' Search ')]").click()
            time.sleep(10)
            self.searching_apps_details(self.browser_obj,'Search_Tab')
            time.sleep(20)    

            #-------------------- Search for an application named 'GSuite' using Application Tab  ---------------
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button/div[contains(text(), '%s')]"%self.select_tab))).click()
            time.sleep(30)
            self.searching_apps_details(self.browser_obj,self.select_tab) 

            #////////////////// Closing browser //////////////////
            time.sleep(30)
            self.browser_close(self.browser_obj)
        except Exception as error:
            self.logger.debug ({"Error":error})
            self.browser_close(self.browser_obj)
            if 'WebDriverException' in type(error):
                import pdb;pdb.set_trace()
                if self.retry_count < 5 :
                    self.retry_count += 1
                    self.main()
                else:
                    self.retry_count = 0

if __name__  == '__main__':
    test_obj = automation_test()
    test_obj.main()