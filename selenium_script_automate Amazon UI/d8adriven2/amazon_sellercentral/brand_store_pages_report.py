from __init__ import *
from __init__ import get_all_the_company_names

def brand_store_pages_reports(company_name):
    os.makedirs(download_path + '/' + company_name, exist_ok=True)
    sleep(5)
    select_partner = driver.find_element_by_xpath("//button[@class='dropdown-button']")
    actionchains = ActionChains(driver)
    actionchains.move_to_element(select_partner).perform()  # mouse hover on partner select
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
        f = open(download_path + '/' + company_name + "/BrandStorePagesFile.txt", "a")
        f.write(company_name + '\n')
        f.close()
        sleep(1)
        pass
    try:
        sleep(1)
        brand_stores_pages(start_date=from_date.strftime("%Y%m%d"), end_date=to_date.strftime("%Y%m%d"))
    except Exception as e:
        try:
            f = open(download_path + '/' + company_name + "/BrandStorePagesFile.txt", "a")
            f.write(company_name + '\n' + str(e))
            f.close()
            sleep(1)
            driver.find_element_by_xpath("//button[@aria-label='More tools']").click() # Hover over the logo to get Amazon seller link
            driver.find_element_by_xpath("//a[text()='Seller Central']").click()  # click on Amazon seller central to come back to homepage
        except Exception:
            pass    
    try:
        sleep(2)
        for key, value in store_shrt.items():
            if key == company_name:
                old_file = os.path.join(download_path,
                                        from_date.strftime("%Y%m%d") + '-' + to_date.strftime("%Y%m%d") + '-' + 'livePage' + '.csv')
                sleep(2)
                new_file = os.path.join(download_path + '/' + company_name,
                                        value + " Brand Store Pages" + '_' + week + ".csv")
                sleep(2)
                os.rename(old_file, new_file)
                sleep(2)
    except Exception:
        pass
    print ("\n finished process from Brand store pages report file......%s"%str(company_name))    



