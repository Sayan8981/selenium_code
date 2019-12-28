from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait,Select
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

#browser_test().main()

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
            browser_obj.implicitly_wait(10)
            #import pdb;pdb.set_trace()
            time.sleep(2) 
            search_signup=browser_obj.find_element(By.XPATH,'//div[@class="hero__text-wrapper--home"]/a[@title="Sign up free"]')
            search_signup.click()
            #import pdb;pdb.set_trace()
            browser_obj.implicitly_wait(10)

            inputboxes=common_lib().find_element_by_class(browser_obj,"auth-form__text-input")
            print("number of inputboxes:", len(inputboxes))

            inputbox_user=common_lib().find_element_by_name(browser_obj,"UserId").send_keys("Saayan23@")
            inputbox_passwd=common_lib().find_element_by_name(browser_obj,"Password1").send_keys("Don9891das@")
            inputbox_email=common_lib().find_element_by_name(browser_obj,"UserEmail").send_keys("saayan@headrun.com")
            time.sleep(2)            
            submit_click=common_lib().find_element_by_xpath(browser_obj,'//div[@class="auth-form__group"]/button[@type="submit"]').click()
            
        except Exception as e:
            #import pdb;pdb.set_trace()
            print ("error:",type(e))
            common_lib().browser_close(browser_obj)


#textboxes_manipulation_data().main()

# switch to frames actions showing here
class goibibo_page_browse:

    driver=''
    start_url="https://www.goibibo.com/"

    class login:

        def __init__(self):
            self.chrome_options = Options()
            self.chrome_options.add_experimental_option("detach", True)
            self.user_authmobile="8981983244"

        # action for login  
        def login_(self):
            try:
                driver=webdriver.Chrome(chrome_options=self.chrome_options)
                browser_obj=common_lib().browser_open(driver,goibibo_page_browse().start_url)
                main_page = browser_obj.current_window_handle 
                print ("site:", browser_obj.title)
                print("site_url:", browser_obj.current_url)
                browser_obj.implicitly_wait(10)
                time.sleep(2)
                common_lib().find_element_by_id(browser_obj,"get_sign_in").click()
                print (set(browser_obj.window_handles))
                time.sleep(2)   
                iframe_login=common_lib().find_elements_by_tag_name(browser_obj,'iframe')[0]
                browser_obj.switch_to.frame(iframe_login) 
                enter_authmobile=common_lib().find_element_by_id(browser_obj,"authMobile").send_keys(self.user_authmobile)
                click_submit=common_lib().find_element_by_id(browser_obj,"mobileSubmitBtn").click()
                time.sleep(1)
                browser_obj.switch_to.default_content()
                print("enter otp id :")
                user_otp=input(str)
                iframe_otp=common_lib().find_elements_by_tag_name(browser_obj,'iframe')[0]
                browser_obj.switch_to_frame(iframe_otp)
                if user_otp:
                    enter_otp=common_lib().find_element_by_id(browser_obj,"otp_index0").send_keys(user_otp)
                    click_continue=common_lib().find_element_by_id(browser_obj,"authOtpSubmitBtn").click()
                    time.sleep(5)
                    print("login completed!")
                    browser_obj.switch_to.window(main_page)
                else:
                    print("Please enter the otp id!")
                return browser_obj
            except Exception as e:
                #import pdb;pdb.set_trace()
                print ("error in login action:",type(e))
                common_lib().browser_close(browser_obj)
                    

    @staticmethod
    def main():
        #import pdb;pdb.set_trace()
        goibibo_page_browse().login().login_()


#goibibo_page_browse().main()       

# Window handle action here
class window_handler:

    driver=''
    start_url="http://demo.automationtesting.in/Register.html"
              
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        
    def window_handle(self):
        try:
            driver=webdriver.Chrome(chrome_options=self.chrome_options)
            browser_obj=common_lib().browser_open(driver,self.start_url)
            browser_obj.implicitly_wait(10)
            Click_switchto_tag=common_lib().find_element_by_link_text(browser_obj,"SwitchTo").click()
            choose_window_option=common_lib().find_element_by_link_text(browser_obj,"Windows").click()
            #import pdb;pdb.set_trace()
            time.sleep(5)
            choose_click=common_lib().find_element_by_xpath(browser_obj,'//a/button[@class="btn btn-info"]').click()
            print("current window handle:",browser_obj.current_window_handle,"current_window_title:",browser_obj.title)
            print(set(browser_obj.window_handles))
            time.sleep(5)
            for handle in browser_obj.window_handles:
                if handle!=browser_obj.current_window_handle:
                    child_window_handle=handle
            browser_obj.switch_to.window(child_window_handle)
            print("current window handle:",browser_obj.current_window_handle,"current_window_title:",browser_obj.title)        
            #choose Documentation of the current window
            choose_Documentation=common_lib().find_element_by_link_text(browser_obj,"Documentation").click()
            choose_Web_element=common_lib().find_element_by_link_text(browser_obj,"Web").click()
        except Exception as e:
            #import pdb;pdb.set_trace()
            print ("error in login action:",type(e))
            common_lib().browser_close(browser_obj)    

    # filling form action
    def registration(self):                  
        

    def main(self):
        self.window_handle()



window_handler().main()