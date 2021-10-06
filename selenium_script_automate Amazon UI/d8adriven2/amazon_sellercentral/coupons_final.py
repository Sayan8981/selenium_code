from __init__ import *
from __init__ import get_all_the_company_names

def get_coupons(company_name):
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
        driver.find_element_by_xpath(
            "//button[contains(text(),'Select Account')]").click()  # Click on Select Account button
        sleep(5)
    except Exception as e:
        f = open(download_path + '/' + company_name + "/CouponsFile.txt", "a")
        f.write(company_name + '\n' + str(e))
        f.close()
        sleep(1)
        pass
    try:
        c = coupons()
    except Exception as e:
        f = open(download_path + '/' + company_name + "/CouponsFile.txt", "a")
        f.write(company_name + '\n' + str(e))
        f.close()
        sleep(1)
        driver.find_element_by_xpath("//div[@id='sc-logo-asset']").click()
    try:
        if c == 1:
            wb = openpyxl.Workbook()
            sheet = wb.active
            sheet.cell(row=1, column=1).value = 'Coupon Title'
            sheet.cell(row=1, column=2).value = 'Actions'
            sheet.cell(row=1, column=3).value = 'Status'
            sheet.cell(row=1, column=4).value = 'Start Date'
            sheet.cell(row=1, column=5).value = 'End Date'
            sheet.cell(row=1, column=6).value = 'Budget'
            sheet.cell(row=1, column=7).value = 'Discount'
            sheet.cell(row=1, column=8).value = 'Spend'
            sheet.cell(row=1, column=9).value = 'Clips'
            sheet.cell(row=1, column=10).value = 'Redeemed'
            sheet.cell(row=1, column=11).value = 'Sales'
            wb.save(download_path + '/' + company_name + '/' + company_name + '.xlsx')
    except:
        pass
    try:
        txt = driver.find_element_by_xpath(
            "//input[@class='a-input-text a-width-small pagedisplay']").get_attribute('value')  # pagination
        l = txt.split('/')
        count = int(l[1])
        page = 1
        rowcount = 0
        while page <= count:
            for i in range(1, 21):
                for j in range(1, 12):
                    ss = driver.find_element_by_xpath(f"//tbody//tr[{i}]//td[{j}]").text
                    workbook = openpyxl.load_workbook(download_path + '/' + company_name + '/' +company_name+'.xlsx')
                    sheet = workbook.active
                    sheet.cell(row=i + rowcount + 1, column=j).value = ss
                    workbook.save(download_path + '/' + company_name + '/' +company_name+'.xlsx')
            page += 1
            driver.find_element_by_xpath("//button[text()='Next']").click()
            rowcount += 20
        try:
            sleep(1)
            work = openpyxl.load_workbook(download_path + '/' + company_name + '/'  + company_name + '.xlsx')
            she = work.active
            she.delete_cols(2,1)
            work.save(download_path + '/' + company_name + '/'  + company_name + '.xlsx')
        except:
            print('y')
            pass
    except:
        pass
    sleep(3)
    driver.find_element_by_xpath("//a[@aria-label='Amazon']").click()  # to go back to home page    
    print ("finished process from coupons_final file .....%s"%str(company_name))    


