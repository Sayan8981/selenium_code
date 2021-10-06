"""writer: Saayan"""

import datetime, os, json, pandas as pd, openpyxl, selenium, pathlib, shutil, arrow
from datetime import timedelta, datetime
from dateutil.parser import parse
from selenium import webdriver
from twilio.rest import Client
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from common_lib import coupons
from common_lib import page_sales
from common_lib import brand_stores
from common_lib import brand_stores_pages
from common_lib import search_term_impression_share_pages

home_url = 'https://sellercentral.amazon.com/'
week = str(eval(datetime.now().strftime("%U"))-1)
print ("\n Started......................week-%s.....\n"%week)

list_number = ["01,","02,", "03,", "04,", "05,", "06,", "07,", "08,", "09,"]

if datetime.now().strftime('%#m') != '10':
    cm = datetime.now().strftime('%#m').strip('0')
else:
    cm = datetime.now().strftime('%#m')    
cd = (datetime.now() + timedelta(days = -1)).strftime('%#d')
cy = datetime.now().strftime('%#y')
homedir = os.path.expanduser("~")
download_path = homedir + '/Downloads'
#download_path = os.getcwd() + '/downloads_file'
# try:
#    shutil.rmtree(download_path)
# except Exception:
#     pass    
# os.makedirs(os.getcwd() + '/downloads_file', exist_ok=True)

opt = Options()
opt.add_experimental_option('debuggerAddress', 'localhost:8080')
opt.add_argument('--start-maximized')
# opt.add_experimental_option("prefs", {
#         "download.default_directory": download_path,
#         "download.prompt_for_download": False,
#         "download.directory_upgrade": True,
#         "safebrowsing.enabled": True
#         })

#login part -----------------------------------------------
driver = webdriver.Chrome(options=opt)
# driver.get(home_url)
# driver.find_element_by_xpath("//strong[text()='Log in']").click()  # click on Log-in button
# driver.find_element_by_xpath("//input[@id='ap_email']").send_keys("d8adriven.tech@gmail.com")  # enter email
# driver.find_element_by_xpath("//input[@id='ap_password']").send_keys("kpDh2BgWvF9!_GRPt")  # enter password
# driver.find_element_by_xpath("//input[@id='signInSubmit']").click()  # click on Sign-in button
# try:
#     driver.find_element_by_xpath("//input[@id='auth-send-code']").click()  # click on Sign-in button
# except Exception:
#     pass    
# account_sid = 'AC83bba69163877afd1051191dcb1f7be9'
# auth_token = 'd9c228857fa9cd056b4093eab16499cf'
# client = Client(account_sid, auth_token)
# messages = client.messages.list(limit=1)
# lsid = []
# for record in messages:
#     lsid.append(record.sid)
# osid = lsid[0]
# message = client.messages(sid=osid).fetch()
# print(message.sid)
# mbody = message.body
# print(mbody)
# otp = mbody[:6]
# print(otp)

# driver.find_element_by_xpath("//input[@id='auth-mfa-otpcode']").send_keys(otp)  # enter the otp
# driver.find_element_by_xpath("//input[@id='auth-signin-button']").click()  # click on Sign-in
# driver.implicitly_wait(10)
# --------------------------------------------------------------------------------------------------------------
def get_from_week_date(year, week_number):
    first_day = arrow.get(f'{str(year)}-W{str(week_number).zfill(2)}-1').to('US/Pacific')
    last_day = first_day + timedelta(days=7)
    last_day = last_day.format('YYYY-MM-DD')
    parsed_last_day = parse(last_day).date()
    last_day_str = str(parsed_last_day)
    return last_day_str 

current_year = datetime.now().strftime("%Y")
to_date = datetime.strptime(get_from_week_date(int(current_year), int(week)),'%Y-%m-%d') - timedelta(days=1)
from_date = to_date - timedelta(days = 6)
search_term_impression_from_date = to_date - timedelta(days = 20)

'''To get all the company names in a list'''
def get_all_the_company_names():
    select_partner = driver.find_element_by_xpath("//button[@class='dropdown-button']")
    a = ActionChains(driver)
    a.move_to_element(select_partner).perform()  # mouse hover on partner select
    driver.find_element_by_xpath("//button[@class='see-all-btn']").click()  # click on See All button
    all_company = driver.find_elements_by_xpath("(//div[@class='picker-item-column'])[1]//button//div//div")
    listall_company = []
    for company in all_company:
        listall_company.append(company.text)
    return listall_company    

# with open(os.getcwd() + "/all_dates.json") as js:
#     data = json.load(js)

oc = ['Agit Global', '1985 Games', 'NACH HOME', 'Resolut Brand', "Earth's Natural Alternative", 'CleanWell, LLC',
      'PL360', 'Brazi Bites Official Store', "Willie's Remedy", 'dropps', 'Nitropics INC', 'Trukid', 'Armor Concepts',
      "Eliot's Adult Nut Butters", 'Whole Hemp Health', 'xofetti', 'Original Workspace Countertop Support Shelf Bracke',
      "Fisherman's World", 'SweatBlock Store', 'KINeSYS Sunscreen', 'STARDUST Spill Products, LLC',
      'MD Complete Skincare', 'SweatBlock AU', 'Revvies', 'Conscious Step', 'Ricks Roasters Coffee Company',
      'Eagle River Trading', 'Consumer Safety Technology LLC', 'DB Fan Gear', 'Simple Wishes, LLC', 'EyeLine Golf',
      'ALZ3F7KPB27ZO', 'VZ Grips', 'Revival Care', 'Mr. Freddy Bunkers', 'Kind Lips', 'JR Chemical Coatings/Wash Safe',
      'C & I Collectables']

search_term_impression_share_keyword = ["Sponsored Brands", "Sponsored Products"]

store_shrt = {'Agit Global': 'AG', '1985 Games': '1985', 'NACH HOME': 'NAC', 'Resolut Brand': 'WGS',
              "Earth's Natural Alternative": 'ENA', 'CleanWell, LLC': 'CLW', 'PL360': None,
              'Brazi Bites Official Store': 'BB',
              "Willie's Remedy": 'WR', 'dropps': 'DR', 'Nitropics INC': 'NT', 'Trukid': 'TK', 'Armor Concepts': 'AC',
              "Eliot's Adult Nut Butters": None, 'Whole Hemp Health': None, 'xofetti': 'XO',
              'Original Workspace Countertop Support Shelf Bracke': 'OG',
              "Fisherman's World": 'FW', 'SweatBlock Store': 'SB', 'KINeSYS Sunscreen': 'KN',
              'STARDUST Spill Products, LLC': 'SSP', 'MD Complete Skincare': 'MD', 'SweatBlock AU': 'MD',
              'Revvies': 'RV',
              'Conscious Step': 'CS', 'Ricks Roasters Coffee Company': 'RR', 'Eagle River Trading': 'CM',
              'Consumer Safety Technology LLC': 'IN', 'DB Fan Gear': 'DNB', 'Simple Wishes, LLC': 'SW',
              'EyeLine Golf': 'EG', 'Mylec Inc.': 'MY', 'VZ Grips': 'VZ', 'Revival Care': None,
              'Mr. Freddy Bunkers': 'HG', 'Kind Lips': 'KL', 'JR Chemical Coatings/Wash Safe': 'WS',
              'C & I Collectables': 'CI', 'Grace Farms Foods': 'GF', 'Icon Office Environments': 'IO','ebestsale-com': 'JCU'}
 