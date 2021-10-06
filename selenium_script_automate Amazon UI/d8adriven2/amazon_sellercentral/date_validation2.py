from __init__ import *

def date_validation2(company_name):
    try:
        wb = openpyxl.load_workbook(download_path + '/' + company_name + '/' + company_name + '.xlsx')
        sh = wb.active
        sh.delete_cols(2, 1)
        wb.save(download_path + '/' + company_name + '/' + company_name + '.xlsx')
        sleep(1)
        maxrow = sh.max_row
        l = 1
        while l <= maxrow:
            v = sh.cell(row=l, column=3).value
            if v == 'Delete':
                sh.delete_rows(l, 1)
                wb.save(download_path + '/' + company_name + '/' + company_name + '.xlsx')
                l -= 1
            else:
                l += 1
        sleep(2)        
        os.rename(download_path + '/' + company_name + '/' + company_name + '.xlsx', download_path + '/' + company_name + '/' + 'Advertising_Coupons_%s'%week + '.xlsx')
        read_file = pd.read_excel (download_path + '/' + company_name + '/' + 'Advertising_Coupons_%s'%week + '.xlsx')  
        read_file.to_csv (download_path + '/' + company_name + '/' + 'Advertising_Coupons_%s'%week + '.csv',index = None, header=True)      
    except Exception:
        pass
    
    print ("\n finished process from date validation2 file %s"%str(company_name))    