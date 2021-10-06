# ***** this report script will run on sunday as script will select last 7 days instead of last week or date range ( should be after 12 PM IST time , script to run)
from __init__ import *

'''To get all the Posts Report'''
def advertising_posts_(company):
    fromdate = from_date.strftime("%B %d, %Y")
    todate = to_date.strftime("%B %d, %Y")
    try:
        reports = driver.find_element_by_xpath("//div[@class='sc-footer-sitemap-row']/h4[contains(text(),'Reports')]")
        sleep(5)
        act = ActionChains(driver)
        act.move_to_element(reports).perform()  # mouse hover on Report
        driver.find_element_by_xpath("//a[contains(text(),'FEEDBACK')]/following-sibling::div[@id='hmd2f-exit']").click() # close feedback option
        sleep(3)
        driver.find_element_by_xpath("//a[contains(text(),'Advertising Reports')]").click()  # click on Advertising Report
        sleep(3)
        driver.find_element_by_xpath("//button[@aria-label='More tools']").click()   # Hover over the logo to get Posts link
        sleep(1)
        driver.find_element_by_xpath("//a[text()='Posts']").click()  # click on Posts
    except Exception:
        pass    
    sleep(1)
    driver.find_element_by_xpath("//div[@id='publisher:navigation:profile-dropdown']//span//p").click()  # hover to select company
    all_company = driver.find_elements_by_xpath("//ul//li")
    list_company = []
    for i in all_company:
        list_company.append(i.text)
    sleep(1)
    os.makedirs(download_path + '/' + company, exist_ok=True)
    driver.find_element_by_xpath(
        "//div[@id='publisher:navigation:profile-dropdown']//span//p").click()  # hover to select company
    for company_name in list_company:   
        if company_name != 'Manage profiles' and (company_name == company or company_name.lower() in company.lower()):
            driver.find_element_by_xpath("//div[@id='publisher:navigation:profile-dropdown']//span//p").click()
            try:
                sleep(1)
                driver.find_element_by_xpath(f'//ul//li[text()="{company_name}"]').click()
                sleep(1)
                try:
                    sleep(2)
                    driver.find_element_by_xpath("//button[@id='publisher:author-detail-page:unifiedDataTable:dateRangeFilter:openContainer']").click()  # click on Date Range
                    sleep(3)
                    for number in list_number:
                        if number in fromdate:
                            fromdate = fromdate.replace(number, number.strip('0'))
                        if number in todate:
                            todate = todate.replace(number, number.strip('0'))
                    while True:
                        try:              
                            sleep(3)      
                            driver.find_element_by_xpath("//tr/td[contains(@aria-label,'%s')]"%str(fromdate)).click()
                            sleep(3)
                            driver.find_element_by_xpath("//tr/td[contains(@aria-label,'%s')]"%str(todate)).click()
                            driver.find_element_by_xpath("//button[text()= 'Apply']").click()
                            break
                        except Exception:
                            driver.find_element_by_xpath("//button[@aria-label='Move forward to switch to the next month.']").click()         
                    sleep(3)
                    driver.find_element_by_xpath("//button/span[text()= 'Export']").click()
                    sleep(3)
                    hover_to_company = driver.find_element_by_xpath(
                    "//div[@id='publisher:navigation:profile-dropdown']//span//p")
                    driver.execute_script("arguments[0].scrollIntoView();", hover_to_company)
                    sleep(1)
                except Exception as e:
                    f = open(download_path + '/' + company + "/PostsTextFile.txt", "a")
                    f.write(company + '\n' + str(e))
                    f.close()
                    sleep(1)
                    hover_to_company = driver.find_element_by_xpath(
                        "//div[@id='publisher:navigation:profile-dropdown']//span//p")
                    driver.execute_script("arguments[0].scrollIntoView();", hover_to_company)
                    sleep(1)
                sleep(3) 
                for filename in os.listdir(download_path):
                    if filename.startswith("Posts_"):
                        os.rename(download_path + '/' + filename, download_path + '/' + company + '/' + store_shrt[company] + ' ' + 'Posts_%s'%week + '.xlsx')  
                        read_file = pd.read_excel (download_path + '/' + company + '/' + store_shrt[company] + ' ' + 'Posts_%s'%week + '.xlsx')
                        read_file.to_csv (download_path + '/' + company + '/' + store_shrt[company] + ' ' + 'Posts_%s'%week + '.csv',index = None, header=True)      
            except Exception as e:
                pass         
    driver.get(home_url)         
    sleep(5)           
    print ("\n finished process from advertising posts reports file.............%s"%str(company))                

