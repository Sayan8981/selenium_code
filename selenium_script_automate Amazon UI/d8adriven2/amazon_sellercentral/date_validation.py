from __init__ import *

def date_v(company_name):
    count = 2
    f = open(download_path + '/' + company_name + "/Date_Validation.txt", "a")
    f.write(company_name + '\n')
    f.close()
    start_date = []
    end_date = []
    try:
        wb = openpyxl.load_workbook(download_path + '/' + company_name + '/' + company_name + '.xlsx')
        sh = wb.active
        maxrow = sh.max_row
        for row in range(2, maxrow + 1):
            start_date.append(sh.cell(row=row, column=4).value)
        for row in range(2, maxrow + 1):
            end_date.append(sh.cell(row=row, column=5).value)
        print (start_date)    
        print (end_date)    
        sd_date_object = []
        ed_date_object = []
        for i in start_date:
            sd_date_object.append(datetime.strptime(i, "%Y-%m-%d"))
        for j in end_date:
            ed_date_object.append(datetime.strptime(j, "%Y-%m-%d"))

        coupon_activated = datetime.strptime(from_date.strftime("%Y-%m-%d"), "%Y-%m-%d")
        coupon_expires = datetime.strptime(to_date.strftime("%Y-%m-%d"), "%Y-%m-%d")
        z = zip(sd_date_object, ed_date_object)
        for k, v in z:

            if ((coupon_activated >= k and coupon_activated <= v) or
                (coupon_expires >= k and coupon_expires <= v)) or \
                    (coupon_expires >= k and coupon_expires <= v) or \
                    (coupon_expires >= k and coupon_activated >= v):
                f = open(download_path + '/' + company_name + "/Date_Validation.txt", "a")
                f.write('Activated Row' + str(count) + '\n')
                f.close()
                print("Activated Row ", count)
            else:
                sh.cell(row=count, column=4).value = 'Delete'
                wb.save(download_path + '/' + company_name + '/' + company_name+'.xlsx')
                f = open(download_path + '/' + company_name + "/Date_Validation.txt", "a")
                f.write('Delete Row ' + str(count) + '\n')
                f.close()
                print('Delete Row ', count)
            count += 1
    except:
        pass

    print ("\n finished process from date validation file %s"%str(company_name))

