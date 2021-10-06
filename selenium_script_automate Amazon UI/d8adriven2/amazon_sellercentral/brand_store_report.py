from __init__ import *
from __init__ import get_all_the_company_names

def brand_store_reports(company_name):
    os.makedirs(download_path + '/' + company_name, exist_ok=True)
    select_partner = driver.find_element_by_xpath("//button[@class='dropdown-button']")
    sleep(5)
    actionchain = ActionChains(driver)
    actionchain.move_to_element(select_partner).perform()  # mouse hover on partner select
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
        f = open(download_path + '/' + company_name + "/BrandStoreFile.txt", "a")
        f.write(company_name + '\n' + str(e))
        f.close()
        sleep(1)
        pass
    try:
        sleep(1)
        brand_stores(start_date=from_date.strftime("%Y%m%d"), end_date=to_date.strftime("%Y%m%d"))
    except Exception as e:
        try:
            f = open(download_path + '/' + company_name + "/BrandStoreFile.txt", "a")
            f.write(company_name + '\n' + str(e))
            f.close()
            sleep(1)
            driver.find_element_by_xpath("//button[@aria-label='More tools']").click()  # click on Amazon seller central to come back to homepage
            driver.find_element_by_xpath("//a[text()='Seller Central']").click()  # click on Amazon seller central to come back to homepage
            """******* xpath change here to back to main page"""
        except Exception:
            pass
    try:
        sleep(2)
        for key, value in store_shrt.items():
            if key == company_name:
                sleep(1)
                old_file = os.path.join(download_path,
                                        from_date.strftime("%Y%m%d") + '-' + to_date.strftime("%Y%m%d") + '-' + 'date' + '.csv')
                sleep(2)
                new_file = os.path.join(download_path + '/' + company_name,
                                        value + " Brand Store" + '_' + week + ".csv")
                sleep(2)
                os.rename(old_file, new_file)
                sleep(2)
    except Exception:
        pass
    print ("\n finished process from brand store report file.......%s"%str(company_name))    



