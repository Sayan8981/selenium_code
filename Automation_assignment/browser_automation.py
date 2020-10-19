from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait,Select
import time

class common_lib:

    def browser_open(self,driver,request_url):       
        driver.get(request_url)
        driver.set_window_size(1800,900)
        return driver

    def find_element_by_name(self,browser,name):
        search_query=browser.find_element_by_name(name)
        return search_query   
    
    def find_element_by_id(self,browser,id):
        search_query=browser.find_element_by_id(id)
        return search_query

    def find_element_by_link_text(self,browser,link):
        search_query=browser.find_element_by_link_text(link)
        return search_query  

    def find_element_by_xpath(self,browser,xpath):
        search_query=browser.find_element_by_xpath(xpath)
        return search_query

    def find_element_by_class(self,browser,class_name):
        search_query=browser.find_elements(By.CLASS_NAME,class_name)
        return search_query 

    def find_elements_by_tag_name(self,browser,tag_name):
        search_query=browser.find_elements_by_tag_name(tag_name)                
        return search_query

    def scroll_down_page_till_end(self,browser):
        return browser.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def scroll_down_by_element(self,browser,element_to_scroll):
        return browser.execute_script("arguments[0].scrollIntoView();",element_to_scroll)        

    def browser_close(self,browser):
        browser.close()

#main class for automation:
class browser_automation_test(common_lib):
    
    driver =''
    product_count = 0
    count = 0
    product_links_list = []
    start_url = "https://www.flipkart.com/"

    #initialization
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        self.search_box_name = "q"
        self.search_box_query = "Titan Watches"
        self.brand_name = "Titan"
        self.product_link_class_name = "_2W-UZw"

    def default_xpath_locators(self):
        self.close_btn_xpath_name = '//button[@class="_2AkmmA _29YdH8"]'                    
        self.search_btn_xpath = '//*[@type="submit"]'
        self.category_xpath = '//a[@title="Wrist Watches"]'
        self.element_upto_scroll_xpath = '//a/span[contains(text(),"Next")]'
        self.product_detail_xpath = '//div[contains(text(),"Product Details")]'
        self.read_more_btn_xpath = '//*[contains(text(),"Read More")]'
        self.product_detals_xpath_scolled = '//div[contains(text(),"Product Details")]'
        self.product_description_xpath = '//div[@class="_2GNeiG"]'
                        
    # method for scroll down page upto certain elemnet    
    def scrolling_action(self, browser,element_xpath):
        try:
            # scroll by element
            element_to_scroll=self.find_element_by_xpath(browser,element_xpath)
            self.scroll_down_by_element(browser,element_to_scroll)
        except Exception as e:
            print ("error in scrolling_action:",type(e))
            self.browser_close(browser)        
     
    # method for categories_selection    
    def categories_selection(self, browser):
        select_category = self.find_element_by_xpath(browser, self.category_xpath).click()
        print ("\n Category selected: %s"%self.category_xpath.strip("//a"))
        return select_category
    
    # method for brand selection
    def brand_selection(self, browser):
        select_brand = self.find_element_by_xpath(browser, '//div[contains(text(),"%s")]'%self.brand_name).click()
        print ("\n Brand name selected: %s"%self.brand_name)
        return select_brand
    
    def get_all_product_link(self, browser):
        get_all_product_link = self.find_element_by_class(browser,self.product_link_class_name)
        for link in get_all_product_link:
            self.product_links_list.append(link.get_attribute('href'))
        return self.product_links_list
    
    # method to print all the N number products 
    def get_print_all_product_list(self, browser):
        watches_list = self.find_elements_by_tag_name(browser, 'a')
        for list_ in watches_list:
            if "Titan" in list_.get_attribute('title'):
                self.product_count += 1
                print ("\n")
                if self.product_count ==1:
                    print ({"Product_number":'{}{}'.format(str(self.product_count),"st Product"),"Product": list_.get_attribute('title').encode('utf-8')})
                elif self.product_count == 2:
                    print ({"Product_number":'{}{}'.format(str(self.product_count),"nd Product"),"Product": list_.get_attribute('title').encode('utf-8')})         
                elif self.product_count == 3:
                    print ({"Product_number":'{}{}'.format(str(self.product_count),"rd Product"),"Product": list_.get_attribute('title').encode('utf-8')})                                   
                else:
                    print ({"Product_number":'{}{}'.format(str(self.product_count),"th Product"),"Product": list_.get_attribute('title').encode('utf-8')})   
                    
    def open_window(self, browser, browser_link):
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[1])
        browser.get(browser_link)
        new_browser_window = browser
        return new_browser_window
    
    # method to print all product description from first page:
    def get_print_all_product_description(self, browser, navigate_product_link):
        child_window = ''
        product_array_details = []
        self.count += 1        
        child_window = self.open_window(browser, navigate_product_link)
        print("\n")
        if "Online Shopping India" not in child_window.title:
            print (child_window.title, "Product_number:",self.count)
            product_details = self.find_element_by_xpath(child_window, self.product_detail_xpath).click()
            try:
                read_more_button = self.find_element_by_xpath(child_window, self.read_more_btn_xpath).click()
            except Exception as error:
                pass    
            self.scrolling_action(child_window, self.product_detals_xpath_scolled)                
            product_description_xpath = self.find_element_by_xpath(child_window, self.product_description_xpath)
            product_element = self.find_element_by_class(product_description_xpath, 'row')
            product_array_details.append({"Product_name":child_window.title})
            for element in product_element:
                product_array_details.append(element.text.encode('utf-8').replace("\n",':'))
            print ("\n")
            print (product_array_details)    
            time.sleep(10)
            child_window.close()
            browser.switch_to.window(browser.window_handles[0])        
                
    def main(self):
        try:
            self.default_xpath_locators()
            self.driver = webdriver.Chrome(chrome_options = self.chrome_options)
            browser_obj = self.browser_open(self.driver, self.start_url)
            print ("site:", browser_obj.title)
            print("site_url:", browser_obj.current_url)
            browser_obj.implicitly_wait(10)            
            close_btn = self.find_element_by_xpath(browser_obj, self.close_btn_xpath_name)
            close_btn.click()      
            time.sleep(3)              
            search_box = self.find_element_by_name(browser_obj, self.search_box_name)
            search_box.send_keys(self.search_box_query)
            browser_obj.implicitly_wait(10)
            search_btn = self.find_element_by_xpath(browser_obj, self.search_btn_xpath)
            search_btn.click()
            time.sleep(3)
            category_select = self.categories_selection(browser_obj)
            brand_select = self.brand_selection(browser_obj)
            time.sleep(4)
            check_all_product = self.get_print_all_product_list(browser_obj)
            get_product_link = self.get_all_product_link(browser_obj)
            for link in get_product_link:
                self.get_print_all_product_description(browser_obj, link)
            print ("\n All product details crawled and Existing the main page .........................")
            self.scrolling_action(browser_obj,self.element_upto_scroll_xpath)            
            time.sleep(200)            
            self.browser_close(browser_obj)
        except Exception as error:
            print ("error:",type(error))
            self.browser_close(browser_obj)        

if __name__=='__main__':
    browser_automation_test().main()
