import os
from time import sleep
from __init__ import *
from page_sales_report import *
from brand_store_report import *
from brand_store_pages_report import *
from coupons_final import *
from date_validation import *
from date_validation2 import *
from search_term_impression_share_report import *
from advertising_posts_reports import *

#company names
#list_company = ['1985 Games', 'Ricks Roasters Coffee Company','Mylec Inc.', 'Grace Farms Foods', 'Icon Office Environments',]
list_company = ['Mylec Inc.', 'Grace Farms Foods', 'Icon Office Environments','1985 Games', 'STARDUST Spill Products, LLC', 'ebestsale-com']
#list_company = ['Grace Farms Foods']
for company in list_company:
    sleep(30)
    page_sales_report(company)
    sleep(30)
    brand_store_reports(company)
    sleep(30)
    brand_store_pages_reports(company)
    sleep(30)
    get_coupons(company)
    sleep(30)
    date_v(company)
    sleep(30)
    date_validation2(company)
    sleep(30)
    for keyword in search_term_impression_share_keyword:
        search_term_impression_share(keyword, company)
        sleep(10)
    sleep(30)
    advertising_posts_(company)
    sleep(3)
    #driver.close()
            
print("\n Finished..... \n Thanks for using Automation \n Saayan Das")
