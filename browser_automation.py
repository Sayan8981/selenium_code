import os
from selenium import webdriver
from selenium.webdriver import ActionChains
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


# switch to frames actions showing here
class goibibo_page_browse:

    driver=''
    start_url="https://www.goibibo.com/"

    class login:

        def __init__(self):
            self.chrome_options = Options()
            self.chrome_options.add_experimental_option("detach", True)
            self.user_authmobile="***************"

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
                    

    def main(self):
        goibibo_page_browse().login().login_()
     

class automation_actions:

    driver=''
    start_url="http://demo.automationtesting.in/Register.html"
              
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.language_opt_array=[]
        self.file_path="/home/*****/****/****.jpg"
        self.firstname='***********'
        self.lastname='****'
        self.address='**********,*******,'
        self.email='***********'
        self.phone='*************'

    def browser_open(self):
        driver=webdriver.Chrome(chrome_options=self.chrome_options)
        browser_obj=common_lib().browser_open(driver,self.start_url)
        return browser_obj

    def window_handle(self):
        try:
            browser_obj=self.browser_open() 
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
            print ("error in window_handle action:",type(e))
            common_lib().browser_close(browser_obj) 

    def scrolling_action(self):
        try:
            browser_obj=self.browser_open()
            browser_obj.implicitly_wait(10)
            time.sleep(10)
            scroll_page=common_lib().scroll_down_page_till_end(browser_obj) 
            # scroll by element
            # element_to_scroll=common_lib().find_element_by_xpath(browser_obj,'//label[@class="col-md-3 col-xs-3 col-sm-3 control-label"][contains(text(),"Gender*")]')
            # scroll_page= common_lib().scroll_down_by_element(browser_obj,element_to_scroll)
        except Exception as e:
            #import pdb;pdb.set_trace()
            print ("error in scrolling_action:",type(e))
            common_lib().browser_close(browser_obj)

    def mouse_hovering(self):
        try:
            browser_obj=self.browser_open()
            browser_obj.implicitly_wait(10)
            first_element_lookup=common_lib().find_element_by_xpath(browser_obj,
                     '//li[@class="dropdown "]/a[contains(text(),"Interactions ")]')        
            sec_element_lookup=common_lib().find_element_by_xpath(browser_obj,
                     '//ul[@class="dropdown-menu"]/li/a[contains(text(),"Drag and Drop ")]')
            third_element_lookup=common_lib().find_element_by_xpath(browser_obj,
                     '//ul[@class="childmenu "]/li/a[contains(text(),"Dynamic ")]')
            action=ActionChains(browser_obj)
            action.move_to_element(first_element_lookup).move_to_element(sec_element_lookup).move_to_element(third_element_lookup).click().perform()
        except Exception as e:
            print ("error in mouse_hovering action:",type(e))
            common_lib().browser_close(browser_obj)

    # filling form action
    def registration(self):
        try:                
            browser_obj=self.browser_open()
            browser_obj.implicitly_wait(10)
            time.sleep(10)
            firstname=common_lib().find_element_by_xpath(browser_obj,
                           '//div/input[@ng-model="FirstName"]').send_keys(self.firstname)            
            lastname=common_lib().find_element_by_xpath(browser_obj,
                           '//div/input[@ng-model="LastName"]').send_keys(self.lastname)
            address=common_lib().find_element_by_xpath(browser_obj,
                           '//div/textarea[@ng-model="Adress"]').send_keys(self.address)
            email=common_lib().find_element_by_xpath(browser_obj,
                           '//div/input[@ng-model="EmailAdress"]').send_keys(self.email)
            phone=common_lib().find_element_by_xpath(browser_obj,
                           '//div/input[@ng-model="Phone"]').send_keys(self.phone)
            print ("Please enter your gender like Male/FeMale:")
            gender=input(str)
            time.sleep(3)

            gender_select=common_lib().find_element_by_xpath(browser_obj,
                                     '//div/label/input[@value="%s"]'%gender).click()

            print ("Please enter your hobies like 'Cricket/Movies/Hockey':")
            hobies=input(str)
            time.sleep(3)
            #import pdb;pdb.set_trace()
            hobies_list=hobies.split("/")
            if len(hobies_list)<=1:
                common_lib().find_element_by_xpath(browser_obj,
                                     '//div/input[@value="%s"]'%hobies_list[0]).click()
            else:
                for entry in hobies_list:
                    common_lib().find_element_by_xpath(browser_obj,
                                     '//div/input[@value="%s"]'%entry).click()
            #import pdb;pdb.set_trace()        
            #to select language actions:
            language_options_parent_element=common_lib().find_element_by_xpath(browser_obj,
                '//div/ul[@class="ui-autocomplete ui-front ui-menu ui-widget ui-widget-content ui-corner-all"]')

            language_options= common_lib().find_elements_by_tag_name(language_options_parent_element,'a')

            for language in language_options:
                self.language_opt_array.append(str(language.get_attribute('text')))
            print("Choose language from the list: ", self.language_opt_array) 
            language_select_input=input(str)   
            #import pdb;pdb.set_trace()
            if language_select_input:
                #click action on box
                language_box_click=common_lib().find_element_by_xpath(browser_obj,
                           '//div[@class="ui-autocomplete-multiselect ui-state-default ui-widget"]').click()
                #scroll action on box
                element_to_scroll=common_lib().scroll_down_by_element(browser_obj,common_lib().find_element_by_xpath(browser_obj,
                                        '//li[@class="ng-scope"]/a[contains(text(),"%s")]'%language_select_input))
                #select action of language
                language_to_select= ActionChains(browser_obj).move_to_element(common_lib().find_element_by_xpath(browser_obj,
                            '//li[@class="ng-scope"]/a[contains(text(),"%s")]'%language_select_input)).click().perform()
            else:
                print ("Please select your language from the list",self.language_opt_array)
            #import pdb;pdb.set_trace()
            #upload file
            upload_file=common_lib().find_element_by_id(browser_obj,"imagesrc").send_keys(self.file_path)    
            time.sleep(10)
            common_lib().browser_close(browser_obj)
        except Exception as e:
            #import pdb;pdb.set_trace()
            print ("error in login action:",type(e))
            common_lib().browser_close(browser_obj)

    def main(self):
        #self.window_handle()
        #self.mouse_hovering()
        #self.scrolling_action()
        self.registration() 

class downloading_files_chrome:

    driver=''
    start_url="http://demo.automationtesting.in/Register.html"

    def __init__(self):
        self.expected_download_dir="/home/saayan-0186/Music"
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)

    def browser_open(self):
        self.chrome_options.add_experimental_option("prefs",
                     {"download.default_directory":self.expected_download_dir})
        driver=webdriver.Chrome(chrome_options=self.chrome_options)
        browser_obj=common_lib().browser_open(driver,self.start_url)
        return browser_obj

    def locate_section_for_download(self):
        try:
            #import pdb;pdb.set_trace()
            browser_obj=self.browser_open()
            locate_parent_element=common_lib().find_element_by_xpath(browser_obj,
                                              '//a[contains(text(),"More")]')    
            locate_child_element=common_lib().find_element_by_xpath(browser_obj,
                                                 '//a[contains(text(),"File Download")]')
            action=ActionChains(browser_obj)
            action.move_to_element(locate_parent_element).move_to_element(locate_child_element).click().perform()
            return browser_obj
        except Exception as e:
            print ("error in locate_element_for_download action:",type(e))
            common_lib().browser_close(browser_obj)

    def downloading_files(self):
        try:
            browser_obj=self.locate_section_for_download()
            time.sleep(15)

            #download text_file
            common_lib().find_element_by_id(browser_obj,"textbox").send_keys("text file to download")
            common_lib().find_element_by_id(browser_obj,"createTxt").click()
            #import pdb;pdb.set_trace()
            common_lib().find_element_by_id(browser_obj,"link-to-download").click()

            #download pdf file
            common_lib().find_element_by_id(browser_obj,"pdfbox").send_keys("pdf file to download")
            common_lib().find_element_by_id(browser_obj,"createPdf").click()
            #import pdb;pdb.set_trace()
            common_lib().find_element_by_id(browser_obj,"pdf-link-to-download").click()             

            time.sleep(25)
            common_lib().browser_close(browser_obj) 
        except Exception as e:
            print ("error in downloading action:",type(e))
            common_lib().browser_close(browser_obj)

    def main(self):
       self.downloading_files() 

class downloading_files_firefox:

    driver=''
    start_url="http://demo.automationtesting.in/Register.html"

    def __init__(self):
        self.expected_download_dir="/home/saayan-0186/Music"
        self.firefox_preference=webdriver.FirefoxProfile()

    def browser_open(self):
        #type of file downloading mentioned here
        self.firefox_preference.set_preference(
                    "browser.helperApps.neverAsk.saveToDisk","text/plain,application/pdf") #Mime type 
        # set pref for download pop up not to show in firefox
        self.firefox_preference.set_preference("browser.download.manager.showWhenStarting",False)
        # set for desired directory to download
        self.firefox_preference.set_preference("browser.download.dir",self.expected_download_dir) 
        self.firefox_preference.set_preference("browser.download.folderList",2)
        self.firefox_preference.set_preference("pdfjs.disabled",True)
        driver=webdriver.Firefox(firefox_profile=self.firefox_preference)
        browser_obj=common_lib().browser_open(driver,self.start_url)
        time.sleep(10)
        return browser_obj

    def locate_section_for_download(self):
        try:
            #import pdb;pdb.set_trace()
            browser_obj=self.browser_open()
            time.sleep(15)
            locate_parent_element=common_lib().find_element_by_xpath(browser_obj,
                                              '//a[contains(text(),"More")]')    
            locate_child_element=common_lib().find_element_by_xpath(browser_obj,
                                                 '//a[contains(text(),"File Download")]')
            action=ActionChains(browser_obj)
            action.move_to_element(locate_parent_element).click().perform()
            time.sleep(4)
            action.move_to_element(locate_child_element).click().perform()
            return browser_obj
        except Exception as e:
            print ("error in locate_element_for_download action:",type(e))
            common_lib().browser_close(browser_obj)

    def downloading_files(self):
        try:
            browser_obj=self.locate_section_for_download()
            time.sleep(20)

            #download text_file
            common_lib().find_element_by_id(browser_obj,"textbox").send_keys("text file to download")
            common_lib().find_element_by_id(browser_obj,"createTxt").click()
            #import pdb;pdb.set_trace()
            common_lib().find_element_by_id(browser_obj,"link-to-download").click()

            #download pdf file
            common_lib().find_element_by_id(browser_obj,"pdfbox").send_keys("pdf file to download")
            common_lib().find_element_by_id(browser_obj,"createPdf").click()
            #import pdb;pdb.set_trace()
            common_lib().find_element_by_id(browser_obj,"pdf-link-to-download").click()             

            time.sleep(25)
            common_lib().browser_close(browser_obj) 
        except Exception as e:
            print ("error in downloading action:",type(e))
            common_lib().browser_close(browser_obj)

    def main(self):
       self.downloading_files()          

class data_driven_test_action:

    def __init__(self):
        pass 

    def read_excel_file(self):
        input_file = '/employee_sheet.xlsx'
        data_sheet=common_lib().excel_file_action(input_file)
        sheet=data_sheet.active
        print (data_sheet.max_row,data_sheet.max_column)

        for row_no in range(1,data_sheet.max_row+1):
            for column_no in range(1,data_sheet.max_column+1):
                print(sheet.cell(row=row_no,column=column_no).value,end="   ")
            print("\n ")

    def write_excel_file(self):
        #import pdb;pdb.set_trace()
        output_file = '/employee_sheet1.xlsx'
        if os.path.isfile(os.getcwd()+output_file):
            os.remove(os.getcwd()+output_file)
        common_lib().create_excel_file(os.getcwd()+output_file)    
        data_sheet=common_lib().excel_file_action(output_file)
        sheet=data_sheet.active
        for row_no in range(1,7):
            for column_no in range(1,6):
                sheet.cell(row=row_no,column=column_no).value="Welcome"

        data_sheet.save(os.getcwd()+output_file)                         

    def main(self):
        #self.read_excel_file()          
        self.write_excel_file()

if __name__=='__main__':
    # browser_test().main()
    # textboxes_manipulation_data().main()
    # goibibo_page_browse().main()
    # automation_actions().main()
    # downloading_files_chrome().main()
    # downloading_files_firefox().main()
    data_driven_test_action().main()
