from __init__ import *

def page_sales(*, from_date='YYYY/MM/DD', to_date='YYYY/MM/DD'):  # DONE
    from __init__ import driver
    driver.find_element_by_xpath("//a[contains(text(),'FEEDBACK')]/following-sibling::div[@id='hmd2f-exit']").click() #close feedback option
    sleep(2)
    driver.find_element_by_xpath("(//a[contains(text(),'Business Reports')])").click()  # click on Business Reports
    sleep(3)
    driver.find_element_by_xpath("//div/p[text()='By ASIN']//following::span[text()='Detail Page Sales and Traffic']").click()   # click on Detail Page Sales and Traffic
    sleep(1)
    current_url = driver.current_url + f'&fromDate={from_date}&toDate={to_date}'
    sleep(1)
    driver.get(current_url)
    driver.refresh()
    sleep(2)
    driver.find_element_by_xpath('//kat-button[@label="Download (.csv)"]').click()  # click on Download csv
    sleep(3)
    driver.find_element_by_xpath("//div[@id='sc-logo-asset']").click()  # click on Amazon seller central to come back to homepage

def brand_stores(*, start_date, end_date):  # DONE
    from __init__ import driver
    stores = driver.find_element_by_xpath("//div[@class='sc-footer-sitemap-row']/h4[contains(text(),'Stores')]") # go to store 
    act = ActionChains(driver)
    act.move_to_element(stores).perform()  # mouse hover on Stores
    driver.find_element_by_xpath("(//a[contains(text(),'Manage Stores')])[1]").click() # click on manage stores
    sleep(4)
    driver.find_element_by_xpath("//a[contains(text(),'See insights')]").click()  # click on See insights
    current_url = driver.current_url
    sleep(1)
    driver.get(current_url + f'&startDate={start_date}&endDate={end_date}')
    sleep(1)
    driver.find_element_by_xpath("//button[@data-test-id='show-export-modal-button']").click()  # click on Export
    sleep(1)
    driver.find_element_by_xpath("//input[@id='exportModal-date']").click()  # click on Date
    sleep(1)
    driver.find_element_by_xpath("(//button[text()='Export'])[2]").click()  # click on Export
    sleep(1)
    driver.find_element_by_xpath("//button[@aria-label='More tools']").click()  # click on Amazon seller central to come back to homepage
    sleep(2)
    driver.find_element_by_xpath("//a[text()='Seller Central']").click()  # click on Amazon seller central to come back to homepage
    

def brand_stores_pages(*, start_date, end_date):  # DONE
    from __init__ import driver
    stores = driver.find_element_by_xpath("//div[@class='sc-footer-sitemap-row']/h4[contains(text(),'Stores')]") # go to store 
    act = ActionChains(driver)
    act.move_to_element(stores).perform()  # mouse hover on Stores
    driver.find_element_by_xpath("(//a[contains(text(),'Manage Stores')])[1]").click() # click on manage stores
    sleep(4)
    driver.find_element_by_xpath("//a[contains(text(),'See insights')]").click()  # click on See insights
    sleep(4)
    driver.find_element_by_xpath("//a[text()='Pages']").click()  # click on Pages
    current_url = driver.current_url
    sleep(1)
    driver.get(current_url + f'&startDate={start_date}&endDate={end_date}')
    sleep(1)
    driver.find_element_by_xpath("//button[@data-test-id='show-export-modal-button']").click()  # click on Export
    sleep(1)
    driver.find_element_by_xpath("//div[text()='Live pages']").click()  # click on Live pages
    sleep(1)
    driver.find_element_by_xpath("(//button[text()='Export'])[2]").click()  # click on Export
    sleep(1)
    driver.find_element_by_xpath("//button[@aria-label='More tools']").click()  # click on Amazon seller central to come back to homepage
    sleep(2)
    driver.find_element_by_xpath("//a[text()='Seller Central']").click()  # click on Amazon seller central to come back to homepage

def coupons():
    from __init__ import driver
    advertising = driver.find_element_by_xpath("//div[@class='sc-footer-sitemap-row']/h4[contains(text(),'Advertising')]")
    ac = ActionChains(driver)
    ac.move_to_element(advertising).perform()  # Mouse hover on Advertising
    driver.find_element_by_xpath("//a[contains(text(),'Coupons')]").click()  # click on Coupons
    driver.find_element_by_xpath("//input[@id='allCoupons']").click()  # click on All checkbox
    return 1

def search_term_impression_share_pages(search_term_keyword, from_date, to_date):  # DONE
    from __init__ import driver, ActionChains, sleep
    driver.find_element_by_xpath("//button[@aria-label='Measurement & Reporting']").click()  # Hover over the logo to get Posts link
    sleep(1)
    driver.find_element_by_xpath("//a[text()='Reports']").click()  # click on Reports
    sleep(1)  
    driver.find_element_by_xpath("//a/button[text()='Create report']").click()  # click on Posts
    sleep(1)  
    driver.find_element_by_xpath("//div//span[text()='%s']"%search_term_keyword).click()  # click on Posts
    sleep(1)
    driver.find_element_by_xpath("//button[@aria-haspopup='listbox']").click()
    sleep(1)
    driver.find_element_by_xpath("//button[text()='Search Term Impression Share']").click()
    sleep(1)
    driver.find_element_by_xpath("//input[@value='day']").click()
    sleep(1)
    driver.find_element_by_xpath("//button[text()='Last 30 days']").click()
    sleep(1)
    driver.find_element_by_xpath("//tr/td[contains(@aria-label,'%s')]"%from_date).click()
    sleep(1)
    driver.find_element_by_xpath("//tr/td[contains(@aria-label,'%s')]"%to_date).click()
    sleep(1)
    driver.find_element_by_xpath("//button[text()= 'Save']").click()
    sleep(2)
    driver.find_element_by_xpath("//span/button[text()= 'Run report']").click()
 




