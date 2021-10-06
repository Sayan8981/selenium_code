from __init__ import *

week = str(eval(datetime.now().strftime("%U"))-1)

'''To get the search_term_impression_share Report'''
def search_term_impression_share(search_term_keyword, company):
    sleep(1)
    fromdate = search_term_impression_from_date.strftime("%B %d, %Y")
    todate = to_date.strftime("%B %d, %Y")
    for number in list_number:
        if number in fromdate:
            fromdate = fromdate.replace(number, number.strip('0'))
        if number in todate:
            todate = todate.replace(number, number.strip('0'))

    os.makedirs(download_path + '/' + company.strip('.'), exist_ok=True)
    sleep(5)
    select_partner = driver.find_element_by_xpath("//button[@class='dropdown-button']")
    sleep(5)
    actionchain = ActionChains(driver)
    actionchain.move_to_element(select_partner).perform()  # mouse hover on partner select
    driver.find_element_by_xpath("//button[@class='see-all-btn']").click()  # click on See All button
    sleep(5)
    driver.find_element_by_xpath(f'(//div[@class="picker-item-column"])[1]//button//div//div[text()="{company}"]').click()
    sleep(5)
    try:
        driver.find_element_by_xpath("//div[text()='United States']").click()
        sleep(5)
        driver.find_element_by_xpath(
            "//button[contains(text(),'Select Account')]").click()  # Click on Select Account button
        sleep(5)
        reports = driver.find_element_by_xpath("//div[@class='sc-footer-sitemap-row']/h4[contains(text(),'Reports')]")
        act = ActionChains(driver)
        act.move_to_element(reports).perform()  # mouse hover on Report
        sleep(5)
        driver.find_element_by_xpath("//a[contains(text(),'FEEDBACK')]/following-sibling::div[@id='hmd2f-exit']").click() # close feedback option
        sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'Advertising Reports')]").click()  # click on Advertising Report
        sleep(3)
        try:
            search_term_impression_share_pages(search_term_keyword, fromdate, todate)
            sleep(2)
            while True:
                if any([h1 for h1 in driver.find_elements_by_xpath('//a[@id="sspa-reports:report-settings-page:-download-button"]')]):
                    break
                else:
                    driver.refresh()
                    sleep(5)
            sleep(5)        
            driver.find_element_by_xpath('//a[@id="sspa-reports:report-settings-page:-download-button"]').click() 
            sleep(3)
            if search_term_keyword == 'Sponsored Brands':
                if os.path.exists(download_path + '/Sponsored Brands Search Term Impression Share report.csv'):
                    os.rename(download_path + '/Sponsored Brands Search Term Impression Share report.csv', download_path + '/' + company + '/%s SB Search Term Impression Share_%s.csv'%(store_shrt[company],week))
            else:
                if os.path.exists(download_path + '/Sponsored Products Search Term Impression Share report.csv'):
                    os.rename(download_path + '/Sponsored Products Search Term Impression Share report.csv', download_path + '/' + company + '/%s SP Search Term Impression Share_%s.csv'%(store_shrt[company],week))
            sleep(5)        
            driver.find_element_by_xpath("//button[@aria-label='More tools']").click()  # click on Amazon seller central to come back to homepage
            sleep(5)
            driver.find_element_by_xpath("//a[text()='Seller Central']").click()  # click on Amazon seller central to come back to homepage
        except Exception as e:
            f = open(download_path + '/' + company.strip(".") + "/search_term_impression_error.txt", "a")
            f.write(company + '\n' + str(e))
            f.close()
            driver.find_element_by_xpath("//span/button[text()='Cancel']").click()  # when keyword not there 
            sleep(2)
            driver.find_element_by_xpath("//button[@aria-label='More tools']").click()  # click on Amazon seller central to come back to homepage
            sleep(2)
            driver.find_element_by_xpath("//a[text()='Seller Central']").click()  # click on Amazon seller central to come back to homepage
            pass 
    except Exception as e:
        f = open(download_path + '/' + company.strip(".") + "/search_term_impression_error.txt", "a")
        f.write(company + '\n' + str(e))
        f.close()
        sleep(1)
        pass
    print ("\n finished process from %s search_term_impression_share reports file.............%s"%(search_term_keyword,str(company)))                