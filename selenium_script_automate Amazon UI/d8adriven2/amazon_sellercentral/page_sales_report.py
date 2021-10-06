from __init__ import * 
from __init__ import get_all_the_company_names, get_from_week_date

def page_sales_report(company_name):
    os.makedirs(download_path + '/' + company_name, exist_ok=True)
    sleep(5)
    select_partner = driver.find_element_by_xpath("//button[@class='dropdown-button']")
    actionchain = ActionChains(driver)
    actionchain.move_to_element(select_partner).perform()  # mouse hover on partner select
    sleep(5)
    driver.find_element_by_xpath("//button[@class='see-all-btn']").click()  # click on See All button
    sleep(5)
    driver.find_element_by_xpath(f'(//div[@class="picker-item-column"])[1]//button//div//div[text()="{company_name}"]').click()
    sleep(5)
    try:
        driver.find_element_by_xpath("//div[text()='United States']").click()
        sleep(5)
        driver.find_element_by_xpath("//button[contains(text(),'Select Account')]").click()  # Click on Select Account button
        sleep(5)
    except Exception as e:
        f = open(download_path + '/' + company_name + "/PageSalesFile.txt", "a")
        f.write(company_name + '\n' + str(e))
        f.close()
        sleep(1)
        pass
    try:
        sleep(1)
        page_sales(from_date=from_date.strftime("%Y-%m-%d"), to_date=to_date.strftime("%Y-%m-%d"))
    except Exception as e:
        f = open(download_path + '/' + company_name + "/PageSalesFile.txt", "a")
        f.write(company_name + '\n' + str(e))
        f.close()
        sleep(3)
        pass
    try:
        if company_name.find('/'):
            mname = company_name.split('/')
            old_file = os.path.join(download_path,
                                    "BusinessReport-" + cm + '-' + cd + '-' + cy + ".csv")
            sleep(3)
            new_file = os.path.join(download_path + '/' + company_name,
                                    "Business Reports_By ASIN_Detail Page Sales and Traffic" + '_' + week + ".csv")
            sleep(2)
            os.rename(old_file, new_file)
            sleep(3)
        else:
            sleep(1)
            old_file = os.path.join(download_path,
                                    "BusinessReport-" + cm + '-' + cd + '-' + cy + ".csv")
            sleep(3)
            new_file = os.path.join(download_path + '/' + company_name,
                                "Business Reports_By ASIN_Detail Page Sales and Traffic" + '_' + week + ".csv")
            sleep(2)

            os.rename(old_file, new_file)
            sleep(3)
    except Exception as e:
        pass        
    print ("\n Finished process from page sales report %s"%str(company_name))
    #driver.find_element_by_xpath("//div[@id='sc-logo-asset']").click()  # click on Amazon seller central to come back to homepage

