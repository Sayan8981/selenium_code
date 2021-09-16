from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time, os, sys
from datetime import datetime
sys.path.insert(0,'%s/common_lib'%("/".join(os.getcwd().split('/')[0:6])))
from lib import lib

class prod_test(lib):
    
    driver =''
    start_url="https://www.d8adriven.io/accounts/login"
    login_admin_user = 'saayan@reckonsys.com'
    login_admin_passwd = 'Test?1234'
    company_lookup_list = [{"SC": ["Brazi Bites", "Grace Farms Foods"]},{"VC": ["JC Toys", "Harry’s"]},{"SC & VC": ["Reynolds","Cleanwell"]}]

    def __init__(self):
        self.retry = 0
        self.company_type = ''
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("detach", True)
        #self.chrome_options.add_argument("--incognito")
        
    def cleanup(self):
        self.company_type = ''    
        
    def login_prod(self, browser):
        self.username_input = browser.find_element_by_xpath('//div[label[text()= "Email"]]/input').send_keys(self.login_admin_user)
        self.passwd_input = browser.find_element_by_xpath('//div[label[text()= "Password"]]/div/input').send_keys(self.login_admin_passwd)
        self.click_login = browser.find_element_by_xpath('//button[@class="btn"][text()="Login"]').click()
        self.logger.info("\n logged user : %s"%self.login_admin_user)
        
    def clear_account_dropdown_search(self, browser):
        self.click_account_dropdown = browser.find_element_by_xpath('//div[@class="account-switcher d-flex-space-center"]')
        actionchain = ActionChains(browser)
        actionchain.move_to_element(self.click_account_dropdown)
        self.click_search = browser.find_element_by_xpath('//input[@placeholder="Search"]')
        actionchain.click(on_element = self.click_search).send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE).perform()
        self.mouse_unhover = browser.find_element_by_xpath('//div[@class="brand-logo"]').click()            
        
    def account_switcher_dropdown(self, browser, company_name):
        time.sleep(10)
        self.click_account_dropdown = browser.find_element_by_xpath('//div[@class="account-switcher d-flex-space-center"]')
        actionchain = ActionChains(browser)
        actionchain.move_to_element(self.click_account_dropdown)
        self.click_search = browser.find_element_by_xpath('//input[@placeholder="Search"]')
        actionchain.click(on_element = self.click_search).send_keys(company_name)
        time.sleep(2)
        actionchain.move_to_element(browser.find_element_by_xpath('//div/ul[@class="company-nav"]'))
        actionchain.click(on_element=browser.find_element_by_xpath('//div/ul[@class="company-nav"]/li[text()="%s"]'%company_name)).perform()
        self.mouse_unhover = browser.find_element_by_xpath('//div[@class="brand-logo"]').click()
        
    def check_hybrid_company(self, browser):
        try:
            self.type_list = browser.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Vendor Central"]')
            if self.type_list.text == 'Vendor Central':
                return "hybrid"    
        except Exception as error:
            return "non-hybrid"
        
    def switch_to_parent_tab(self, browser):
        browser.close()
        browser.switch_to.window(browser.window_handles[0])
        time.sleep(10)
                
    def check_overview_dashboard(self, browser, keys):
        self.click_on_overview_dashboard = browser.find_element_by_xpath('//div[contains(text(),"Overview Dashboard")]').click()
        time.sleep(10)
        if len(browser.window_handles) > 1:
            self.switch_to_parent_tab(browser)   
            time.sleep(10)
            if self.company_type == "hybrid" and keys == "VC":
                browser.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Vendor Central"]').click()
        return browser.find_element_by_xpath('//p[contains(text(),"Weekly ASIN Monitor")]').is_displayed()
    
    def check_executive_summary(self, browser, keys):
        self.click_on_executive_summary = browser.find_element_by_xpath('//div[contains(text(),"Executive Summary")]').click()
        time.sleep(10)
        if len(browser.window_handles) > 1:
            self.switch_to_parent_tab(browser)
            time.sleep(10)
            if self.company_type == "hybrid" and keys == "VC":
                browser.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Vendor Central"]').click()
        return browser.find_element_by_xpath('//button[contains(text(),"View Change Log")]').is_displayed() 
    
    def click_on_business_report(self, browser):
        browser.find_element_by_xpath('//div[contains(text(),"Business Reports")]').click()
        
    def click_on_sales(self,browser):
        browser.find_element_by_xpath('//div[contains(text(),"Sales")]').click()    
       
    def click_on_marketing(self,browser):
        browser.find_element_by_xpath('//div[contains(text(),"Marketing")]').click()
     
    def click_on_finance(self,browser):
        browser.find_element_by_xpath('//div[contains(text(),"Finance")]').click()
        
    def click_on_operations(self,browser):
        browser.find_element_by_xpath('//div[contains(text(),"Operations")]').click() 
        
    def click_on_project_portal(self, browser):
        browser.find_element_by_xpath('//div[contains(text(),"Project Portal")]').click()  
        
    def click_on_settings(self, browser):
        browser.find_element_by_xpath('//div[contains(text(),"Settings")]').click()     
        
    def click_on_client_files(self,browser):
        browser.find_element_by_xpath('//div[contains(text(),"Client Files")]').click()
      
    def click_on_admin(self, browser):
        browser.find_element_by_xpath('//div[contains(text(),"Admin")]').click()  
        
    def click_on_technology_help(self, browser):
        browser.find_element_by_xpath('//p[contains(text(),"Technology Help")]').click() 
        
    def click_on_amazon_help(self,browser):
        browser.find_element_by_xpath('//p[contains(text(),"Amazon Help")]').click()     
        
    def check_PBI_reports(self, browser, report_name, keys):
        self.click_on_reports = browser.find_element_by_xpath('//div[contains(text(),"%s")]'%report_name).click()
        if len(browser.window_handles) > 1:
            self.switch_to_parent_tab(browser)
            time.sleep(10)
            if self.company_type == "hybrid" and keys == "VC":
                browser.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Vendor Central"]').click()
            self.click_businees_report = self.click_on_business_report(browser)
            if report_name == "Gross & Net Revenue" or report_name == "Geography Breakdown" or report_name == "Revenue Breakdown" or report_name == "ASIN Deep Dive" or report_name == "Purchase Order Revenue" or report_name == "Consumer Order Revenue":
                try:
                    time.sleep(10)
                    self.click_sales = self.click_on_sales(browser)
                except Exception as error:
                    self.retry += 1
                    if self.retry <= 5:
                        browser.refresh()
                        time.sleep(15)
                        self.click_businees_report = self.click_on_business_report(browser)
                        self.click_sales = self.click_on_sales(browser)
                        self.check_PBI_reports(browser, report_name, keys)
                    else:
                        self.retry = 0               
            elif report_name == "Category Rank" or report_name == "Customer Engagement" or report_name == "Advertising":
                try:
                    time.sleep(10)
                    self.click_marketing = self.click_on_marketing(browser)
                except Exception as error:
                    self.retry += 1
                    if self.retry <= 5:
                        browser.refresh()
                        time.sleep(15)
                        self.click_businees_report = self.click_on_business_report(browser)
                        self.click_marketing = self.click_on_marketing(browser)
                        self.check_PBI_reports(browser, report_name, keys)
                    else:
                        self.retry = 0  
            elif report_name == "Supply Chain Preformance" or report_name == "Geography Breakdown" or report_name == "Inventory and Forecast":
                try:
                    time.sleep(10)
                    self.click_operations = self.click_on_operations(browser)
                except Exception as error:
                    self.retry += 1
                    if self.retry <= 5:
                        browser.refresh()
                        time.sleep(15)
                        self.click_businees_report = self.click_on_business_report(browser)
                        self.click_marketing = self.click_on_operations(browser)
                        self.check_PBI_reports(browser, report_name, keys)
                    else:
                        self.retry = 0
            elif report_name == "Projections":
                try:
                    time.sleep(10)
                    self.click_finance = self.click_on_finance(browser)
                except Exception as error:
                    self.retry += 1
                    if self.retry <= 5:
                        browser.refresh()
                        time.sleep(15)
                        self.click_businees_report = self.click_on_business_report(browser)
                        self.click_marketing = self.click_on_finance(browser)
                        self.check_PBI_reports(browser, report_name, keys)
                    else:
                        self.retry = 0                             
        time.sleep(10)
        try:
            if browser.find_element_by_xpath('//p[contains(text(),"Coming Soon")]') or browser.find_element_by_xpath('//h4[contains(text(),"Cannot load model")]'):
                return False
        except Exception:
            return True  
        
    def check_sales_report_sc(self, driver, company, keys):
        #Test Gross & Net revenue
        self.status_gross_net_revenue = self.check_PBI_reports(driver, "Gross & Net Revenue", keys)  
        if self.status_gross_net_revenue == True:
            self.logger.info ("\n Test Sales report |Gross & Net Revenue| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:          
            self.logger.info ("\n Test Sales report |Gross & Net Revenue| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))  
        time.sleep(10)
        #Test Geography Breakdown
        self.status_geography_breakdown = self.check_PBI_reports(driver, "Geography Breakdown", keys)  
        if self.status_geography_breakdown == True:
            self.logger.info ("\n Test Sales report |Geography Breakdown| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:          
            self.logger.info ("\n Test Sales report |Geography Breakdown| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))        
        time.sleep(10)
        #Test Revenue Breakdown
        self.status_revenue_breakdown = self.check_PBI_reports(driver, "Revenue Breakdown", keys)  
        if self.status_revenue_breakdown == True:
            self.logger.info ("\n Test Sales report |Revenue Breakdown| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:          
            self.logger.info ("\n Test Sales report |Revenue Breakdown| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))        
        time.sleep(10)
        #Test ASIN Deep Dive
        self.status_asin_deep_dive = self.check_PBI_reports(driver, "ASIN Deep Dive", keys)  
        if self.status_asin_deep_dive == True:
            self.logger.info ("\n Test Sales report |ASIN Deep Dive| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:          
            self.logger.info ("\n Test Sales report |ASIN Deep Dive| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))        
        time.sleep(10)  
        self.click_sales = self.click_on_sales(driver)  
        
    def check_sales_report_vc(self, driver, company, keys):
        #Test Purchase Order Revenue
        self.status_purchase_order_revenue = self.check_PBI_reports(driver, "Purchase Order Revenue", keys)  
        if self.status_purchase_order_revenue == True:
            self.logger.info ("\n Test Sales report |Purchase Order Revenue| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:          
            self.logger.info ("\n Test Sales report |Purchase Order Revenue| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))  
        time.sleep(10)
        #Test Geography Breakdown
        self.status_consumer_order_revenue = self.check_PBI_reports(driver, "Consumer Order Revenue", keys)  
        if self.status_consumer_order_revenue == True:
            self.logger.info ("\n Test Sales report |Consumer Order Revenue| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:          
            self.logger.info ("\n Test Sales report |Consumer Order Revenue| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))        
        time.sleep(10)
        #Test Revenue Breakdown
        self.status_revenue_breakdown = self.check_PBI_reports(driver, "Revenue Breakdown", keys)  
        if self.status_revenue_breakdown == True:
            self.logger.info ("\n Test Sales report |Revenue Breakdown| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:          
            self.logger.info ("\n Test Sales report |Revenue Breakdown| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))        
        time.sleep(10)
        #Test ASIN Deep Dive
        self.status_geography_breakdown = self.check_PBI_reports(driver, "Geography Breakdown", keys)  
        if self.status_geography_breakdown == True:
            self.logger.info ("\n Test Sales report |Geography Breakdown| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:          
            self.logger.info ("\n Test Sales report |Geography Breakdown| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))        
        time.sleep(10)  
        #Test ASIN Deep Dive
        self.status_asin_deep_dive = self.check_PBI_reports(driver, "ASIN Deep Dive", keys)  
        if self.status_asin_deep_dive == True:
            self.logger.info ("\n Test Sales report |ASIN Deep Dive| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:          
            self.logger.info ("\n Test Sales report |ASIN Deep Dive| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))  
        self.click_sales = self.click_on_sales(driver)
                
    def check_marketing_report(self, driver, company, keys):
        #Test Category Rank
        self.status_category_rank = self.check_PBI_reports(driver, "Category Rank", keys)  
        if self.status_category_rank == True:
            self.logger.info ("\n Test Marketing report |Category Rank| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:          
            self.logger.info ("\n Test Marketing report |Category Rank| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))  
        time.sleep(10)
        #Test Customer Engagement
        self.status_customer_engagement = self.check_PBI_reports(driver, "Customer Engagement", keys)  
        if self.status_customer_engagement == True:
            self.logger.info ("\n Test Marketing report |Customer Engagement| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:          
            self.logger.info ("\n Test Marketing report |Customer Engagement| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))        
        time.sleep(10)
        #Test Advertising
        self.status_advertising = self.check_PBI_reports(driver, "Advertising", keys)  
        if self.status_advertising == True:
            self.logger.info ("\n Test Marketing report |Advertising| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:          
            self.logger.info ("\n Test Marketing report |Advertising| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))        
        time.sleep(10)
        self.click_marketing = self.click_on_marketing(driver)
        
    def check_operations_report(self, driver, company, keys):
        #Test Supply Chain Preformance
        self.status_supply_chain_preformance = self.check_PBI_reports(driver, "Supply Chain Preformance", keys)  
        if self.status_supply_chain_preformance == True:
            self.logger.info ("\n Test Operations report |Supply Chain Preformance| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:          
            self.logger.info ("\n Test Operations report |Supply Chain Preformance| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))  
        time.sleep(10)
        #Test Geography Breakdown
        self.status_geography_breakdown = self.check_PBI_reports(driver, "Geography Breakdown", keys)  
        if self.status_geography_breakdown == True:
            self.logger.info ("\n Test Operations report |Geography Breakdown| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:          
            self.logger.info ("\n Test Operations report |Geography Breakdown| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))        
        time.sleep(10)
        #Test Advertising
        try:
            self.status_inventory_and_forecast = self.check_PBI_reports(driver, "Inventory and Forecast", keys)  
        except Exception:
            self.click_operations = self.click_on_operations(driver)
            time.sleep(10)
            self.status_inventory_and_forecast = self.check_PBI_reports(driver, "Inventory and Forecast", keys)
        if self.status_inventory_and_forecast == True:
            self.logger.info ("\n Test Operations report |Inventory and Forecast| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:          
            self.logger.info ("\n Test Operations report |Inventory and Forecast| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))        
        time.sleep(10)
        self.click_operations = self.click_on_operations(driver)
        
    def check_finance_report(self, driver, company, keys):
        #Test Projections
        self.status_projections = self.check_PBI_reports(driver, "Projections", keys)  
        if self.status_projections == True:
            self.logger.info ("\n Test Finance report |Projections| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:          
            self.logger.info ("\n Test Finance report |Projections| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))  
        time.sleep(10)
        self.click_finance = self.click_on_finance(driver)
        
    def check_project_portal_options(self, driver, option, keys):
        driver.find_element_by_xpath('//div[contains(text(),"%s")]'%option).click()
        if len(driver.window_handles) > 1:
            self.switch_to_parent_tab(driver)
            time.sleep(10)
            if self.company_type == "hybrid" and keys == "VC":
                driver.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Vendor Central"]').click()
            self.click_project_portal = self.click_on_project_portal(driver)
            try:
                time.sleep(10)
                self.click_option = driver.find_element_by_xpath('//div[contains(text(),"%s")]'%option).click()
                self.switch_to_parent_tab(driver)
                time.sleep(10)
                if self.company_type == "hybrid" and keys == "VC":
                    driver.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Vendor Central"]').click()
                self.click_project_portal = self.click_on_project_portal(driver)
            except Exception as error:
                self.retry += 1
                if self.retry <= 5:
                    driver.refresh()
                    time.sleep(15)
                    self.check_project_portal_options(driver, option, keys)                      
                else:
                    self.retry = 0 
        time.sleep(10)             
        if option == "Detail View":            
            return driver.find_element_by_xpath('//a[contains(text(),"Projects in Progress")]').is_displayed()        
        elif option == "Budget Approval":
            return driver.find_element_by_xpath('//a[contains(text(),"Topics in Progress")]').is_displayed() 
        elif option == "Content Audit":
            return driver.find_element_by_xpath('//div[contains(text(),"ASIN")]').is_displayed()
        elif option == "Inventory Recommendation":
            return driver.find_element_by_xpath('//div[contains(text(),"ASIN")]').is_displayed()     
           
    def check_on_project_portal(self, driver, company, keys):
        self.status_detail_view = self.check_project_portal_options(driver, "Detail View", keys)
        if self.status_detail_view == True:
            self.logger.info("\n Test Project Portal |Detail View| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:
            self.logger.info("\n Test Project Portal |Detail View| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))
        time.sleep(10)    
        self.status_budget_approval = self.check_project_portal_options(driver, "Budget Approval", keys)
        if self.status_budget_approval == True:
            self.logger.info("\n Test Project Portal |Budget Approval| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:
            self.logger.info("\n Test Project Portal |Budget Approval| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))
        time.sleep(10)    
        self.status_content_audit = self.check_project_portal_options(driver, "Content Audit", keys)
        if self.status_content_audit == True:
            self.logger.info("\n Test Project Portal |Content Audit| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:
            self.logger.info("\n Test Project Portal |Content Audit| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))        
        time.sleep(10)    
        if keys == "SC":
            self.status_inventory_recommendation = self.check_project_portal_options(driver, "Inventory Recommendation", keys)
            if self.status_inventory_recommendation == True:
                self.logger.info("\n Test Project Portal |Inventory Recommendation| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
            else:
                self.logger.info("\n Test Project Portal |Inventory Recommendation| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))   
        self.click_project_portal = self.click_on_project_portal(driver)         
                
    def check_setting_options(self, driver, option, keys):
        driver.find_element_by_xpath('//div[contains(text(),"%s")]'%option).click()
        if len(driver.window_handles) > 1:
            self.switch_to_parent_tab(driver)
            time.sleep(10)
            if self.company_type == "hybrid" and keys == "VC":
                driver.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Vendor Central"]')
            self.click_setting = self.click_on_settings(driver)
            try:
                time.sleep(10)
                self.click_option = driver.find_element_by_xpath('//div[contains(text(),"%s")]'%option).click()
                self.switch_to_parent_tab(driver)
                time.sleep(10)
                if self.company_type == "hybrid" and keys == "VC":
                    driver.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Vendor Central"]').click()
                self.click_setting = self.click_on_settings(driver)
            except Exception as error:
                self.retry += 1
                if self.retry <= 5:
                    driver.refresh()
                    time.sleep(15)
                    self.check_setting_options(driver, option, keys)                      
                else:
                    self.retry = 0 
        time.sleep(10)             
        if option == "Custom Catalog Labeling" or option == "Manage Products":            
            try:
                return driver.find_element_by_xpath('//div[contains(text(),"ASIN")]').is_displayed()
            except Exception:
                return driver.find_element_by_xpath('//button[contains(text(),"Upload CSV")]').is_displayed()        
        elif option == "Strategic Inputs":
            return driver.find_element_by_xpath('//p[contains(text(),"Total Weeks of cover")]').is_displayed() 
                            
    def check_on_settings(self, driver, company, keys):
        self.status_custom_catalog_labeling = self.check_setting_options(driver, "Custom Catalog Labeling", keys)
        if self.status_custom_catalog_labeling == True:
            self.logger.info("\n Test Project Portal |Custom Catalog Labeling| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:
            self.logger.info("\n Test Settings |Custom Catalog Labeling| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))
        time.sleep(10)
        self.status_strategic_inputs = self.check_setting_options(driver, "Strategic Inputs", keys)
        if self.status_strategic_inputs == True:
            self.logger.info("\n Test Settings |Strategic Inputs| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:
            self.logger.info("\n Test Settings |Strategic Inputs| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))
        time.sleep(10)
        self.status_manage_products = self.check_setting_options(driver, "Manage Products", keys)
        if self.status_manage_products == True:
            self.logger.info("\n Test Settings |Manage Products| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:
            self.logger.info("\n Test Settings |Manage Products| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))
        self.click_settings = self.click_on_settings(driver)    
                    
    def verify_client_files_element(self,driver, keys):
        self.click_client_files = self.click_on_client_files(driver)
        if len(driver.window_handles) > 1:
            self.switch_to_parent_tab(driver)
            time.sleep(10)
            if self.company_type == "hybrid" and keys == "VC":
                driver.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Vendor Central"]').click()
        time.sleep(10)    
        try:
            return driver.find_element_by_xpath('//div[contains(text(),"File Name")]').is_displayed()
        except Exception:
            return driver.find_element_by_xpath('//button[contains(text(),"Add File")]').is_displayed()            
        
    def check_on_client_files(self, driver, company, keys):
        self.status_client_files = self.verify_client_files_element(driver, keys)
        if self.status_client_files == True:
            self.logger.info("\n Test |client_files| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:
            self.logger.info("\n Test |client_files| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))
                        
    def check_admin_options(self, driver, option, keys):
        driver.find_element_by_xpath('//div[contains(text(),"%s")]'%option).click()
        if len(driver.window_handles) > 1:
            self.switch_to_parent_tab(driver)
            time.sleep(10)
            if self.company_type == "hybrid" and keys == "VC":
                driver.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Vendor Central"]').click()
            self.click_admin = self.click_on_admin(driver)
            try:
                time.sleep(10)
                self.click_option = driver.find_element_by_xpath('//div[contains(text(),"%s")]'%option).click()
                self.switch_to_parent_tab(driver)
                time.sleep(10)
                if self.company_type == "hybrid" and keys == "VC":
                    driver.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Vendor Central"]').click()
                self.click_admin = self.click_on_admin(driver)
            except Exception as error:
                self.retry += 1
                if self.retry <= 5:
                    driver.refresh()
                    time.sleep(15)
                    self.check_admin_options(driver, option, keys)                      
                else:
                    self.retry = 0 
        time.sleep(10)             
        if option == "Manage Users":            
            try:
                return driver.find_element_by_xpath('//div[contains(text(),"Name")]').is_displayed()
            except Exception:
                return driver.find_element_by_xpath('//button[contains(text(),"Add User")]').is_displayed()
        elif option == "Amazon Reports":
            try:
                return driver.find_element_by_xpath('//div[contains(text(),"File Name")]').is_displayed()
            except Exception:
                return driver.find_element_by_xpath('//button[contains(text(),"(See Results)")]').is_displayed()
                            
    def check_on_admin(self, driver, company, keys):
        self.status_manage_users = self.check_admin_options(driver, "Manage Users", keys)
        if self.status_manage_users == True:
            self.logger.info("\n Test Admin |Manage Users| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:
            self.logger.info("\n Test Admin |Manage Users| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))
        time.sleep(10)    
        self.status_amazon_reports = self.check_admin_options(driver, "Amazon Reports", keys)
        if self.status_amazon_reports == True:
            self.logger.info("\n Test Admin |Amazon Reports| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:
            self.logger.info("\n Test Admin |Amazon Reports| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))
        self.click_admin = self.click_on_admin(driver)    
                      
    def validate_support_ticket_form(self,driver):
        self.result = "Fail"
        if driver.find_element_by_xpath('//label[contains(text(),"Name")]').is_displayed() == True:
            self.result = "Pass"
        if driver.find_element_by_xpath('//label[contains(text(),"Company Name")]').is_displayed() == True:
            self.result = "Pass"
        if driver.find_element_by_xpath('//label[contains(text(),"Email address")]').is_displayed() == True:
            self.result = "Pass"
        if driver.find_element_by_xpath('//label[contains(text(),"Subject")]').is_displayed() == True:        
            self.result = "Pass"
        if driver.find_element_by_xpath('//label[contains(text(),"Please describe your issue with as much detail as possible.")]').is_displayed() == True:        
            self.result = "Pass"
        if driver.find_element_by_xpath('//div[@role="button"][contains(text(),"Submit")]').is_displayed() == True:        
            self.result = "Pass"        
        return self.result    
                          
    def verify_technology_help_element(self, driver, keys):
        self.click_technology_help = self.click_on_technology_help(driver)
        if len(driver.window_handles) > 1:
            self.switch_to_parent_tab(driver)
            time.sleep(10)
            if self.company_type == "hybrid" and keys == "VC":
                driver.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Vendor Central"]').click()
        time.sleep(10)  
        try:
            if driver.find_element_by_xpath('//a[contains(text(),"Create Support Ticket")]').is_displayed() == True:
                driver.find_element_by_xpath('//a[contains(text(),"Create Support Ticket")]').click()
                if len(driver.window_handles) > 1:
                    driver.switch_to.window(driver.window_handles[1])
                    time.sleep(10)
                    self.validate = self.validate_support_ticket_form(driver)
                    if self.validate == "Pass":
                        self.switch_to_parent_tab(driver) 
                        time.sleep(10)
                        if self.company_type == "hybrid" and keys == "VC":
                            driver.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Vendor Central"]').click()
                        return True
                    else:
                        self.switch_to_parent_tab(driver) 
                        time.sleep(10)
                        if self.company_type == "hybrid" and keys == "VC":
                            driver.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Vendor Central"]').click()
                        return False
            else:
                return False                       
        except Exception:
            return False
                         
    def check_on_technology_help(self, driver, company, keys):
        self.status_technology_help = self.verify_technology_help_element(driver, keys)
        if self.status_technology_help == True:
            self.logger.info("\n Test |Technology_Help| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:
            self.logger.info("\n Test |Technology_Help| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys)) 
                
    def verify_amazon_help(self, driver, keys):
        self.click_amazon_help = self.click_on_amazon_help(driver)
        self.switch_iframe = driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        if len(driver.window_handles) > 1:
            self.switch_to_parent_tab(driver)
            time.sleep(10)
            if self.company_type == "hybrid" and keys == "VC":
                driver.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Vendor Central"]').click()
        time.sleep(10)    
        return driver.find_element_by_xpath('//div[contains(text(),"%s")]'%(datetime.now().strftime("%B %Y"))).is_displayed()
                            
    def check_on_amazon_help(self, driver, company, keys):
        self.status_amazon_help = self.verify_amazon_help(driver, keys)
        if self.status_technology_help == True:
            self.logger.info("\n Test |Amazon_Help| <Pass> %s, Type: %s, %s"%(company, self.company_type, keys))
        else:
            self.logger.info("\n Test |Amazon_Help| <Fail> %s, Type: %s, %s"%(company, self.company_type, keys))
        time.sleep(10)
        driver.switch_to.default_content()
        time.sleep(10)
        self.close_amazon_help = driver.find_element_by_xpath('//div[@class="calendly-popup-close"]').click()    
                            
    def prod_verification(self, driver, company, keys):
        #Test overview_dashboard 
        self.status_overview_dashboard = self.check_overview_dashboard(driver, keys)
        if self.status_overview_dashboard == True:
            self.logger.info ("\n Test |overview dashboard| <Pass> %s , type: %s, %s"%(company, self.company_type, keys))
        else:
            self.logger.info ("\n Test |overview dashboard| <Fail> %s , type: %s, %s"%(company, self.company_type, keys))  
        time.sleep(10)      
        #Test executive_summary
        self.status_executive_summary = self.check_executive_summary(driver, keys) 
        if self.status_executive_summary == True:
            self.logger.info ("\n Test |executive summary| <Pass> %s, type: %s, %s"%(company,self.company_type, keys))   
        else:
            self.logger.info ("\n Test executive summary <Fail> %s, type: %s, %s"%(company,self.company_type, keys))
        time.sleep(10)
        #Test businees_report 
        self.click_businees_report = self.click_on_business_report(driver)  
        time.sleep(10)
        #Test Sales
        self.click_sales = self.click_on_sales(driver) 
        time.sleep(10)
        if keys == "SC":
            self.check_sales_report_sc(driver, company, keys)
        elif keys == "VC":    
            self.check_sales_report_vc(driver, company, keys)
        time.sleep(10)
        #Test Marketing
        self.click_marketing = self.click_on_marketing(driver)
        time.sleep(10)
        self.check_marketing_report(driver, company, keys)
        time.sleep(10) 
        #Test Operations
        self.click_operations = self.click_on_operations(driver)
        time.sleep(10)
        self.check_operations_report(driver, company, keys)
        time.sleep(10)
        #Test Finance
        self.click_finance = self.click_on_finance(driver)
        time.sleep(10)
        self.check_finance_report(driver, company, keys)
        time.sleep(10)
        #Collapse businees_report 
        self.click_businees_report = self.click_on_business_report(driver)
        time.sleep(10)
        #Test Project Portal
        self.click_project_portal = self.click_on_project_portal(driver)
        time.sleep(10)
        self.check_project_portal = self.check_on_project_portal(driver, company, keys)
        time.sleep(10)
        #test settings
        self.click_settings = self.click_on_settings(driver)
        time.sleep(10)
        self.check_settings = self.check_on_settings(driver, company, keys)
        time.sleep(10)
        #Test Client files
        self.check_client_files = self.check_on_client_files(driver, company, keys)
        time.sleep(10)
        #Test Admin
        self.click_admin = self.click_on_admin(driver)
        time.sleep(10)
        self.check_admin = self.check_on_admin(driver, company, keys)
        time.sleep(10)
        #Test Technology Help
        self.check_technology_help = self.check_on_technology_help(driver, company, keys)
        time.sleep(10)
        #Test Amazon Help
        self.check_amazon_help = self.check_on_amazon_help(driver, company, keys)
        #Clear the dropdown search area
        self.clear_account_dropdown_search(driver)            
                 
    def main(self):
        self.logger = self.create_log('/reports/Prod_Test_Report_%s.txt'%datetime.now().strftime('%y-%m-%d'))
        try:
            self.driver = webdriver.Chrome(options=self.chrome_options)
            self.driver.set_window_size(1900,1200)
            self.browser_obj = self.driver.get(self.start_url)
            time.sleep(10)
            self.login_prod(self.driver)
            time.sleep(10)
            for company_type in self.company_lookup_list:
                for keys in company_type.keys():
                    if keys == "SC":
                        for company in company_type[keys]:
                            self.cleanup()
                            self.account_switcher_dropdown(self.driver, company)
                            self.company_type = self.check_hybrid_company(self.driver)
                            time.sleep(10)
                            if self.company_type == "non-hybrid":
                                #self.prod_verification(self.driver, company, keys)
                                pass
                            self.clear_account_dropdown_search(self.driver)  
                    elif keys == "VC":
                        for company in company_type[keys]:
                            self.cleanup()
                            self.account_switcher_dropdown(self.driver, company)
                            self.company_type = self.check_hybrid_company(self.driver)
                            time.sleep(10)
                            if self.company_type == "non-hybrid":
                                #self.prod_verification(self.driver, company, keys)
                                pass
                            self.clear_account_dropdown_search(self.driver)  
                    elif keys == "SC & VC":
                        for company in company_type[keys]:
                            self.cleanup()
                            self.account_switcher_dropdown(self.driver, company)
                            self.company_type = self.check_hybrid_company(self.driver)
                            time.sleep(10)
                            if self.company_type == "hybrid":
                                if self.driver.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Seller Central"]').is_displayed():
                                    self.driver.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Seller Central"]').click()
                                    self.prod_verification(self.driver, company, "SC")
                                time.sleep(20)    
                                if self.driver.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Vendor Central"]').is_displayed():
                                    self.driver.find_element_by_xpath('//div[@class="button-wrapper"]/button[text()=" Vendor Central"]').click()
                                    self.prod_verification(self.driver, company, "VC") 
                            self.clear_account_dropdown_search(self.driver)                                 
            time.sleep(25)
            self.driver.close() 
            self.logger.info("\n Report generated , please refer in reports folder for current date.")   
        except Exception as error:
            self.logger.info (error)
            
if __name__ == '__main__':
    prod_test().main()