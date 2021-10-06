import os, logging, sys, csv

class lib(object):
    
    #--------------------  log module --------------------------
    def create_log(self, log_file):
        try:
            if os.getcwd() + log_file:
                os.remove(os.getcwd() + log_file)
        except FileNotFoundError:
            pass         
        logger = logging.getLogger()
        logging.basicConfig(filename=os.getcwd() + log_file,format=[],filemode='w')
        logger.setLevel(logging.INFO)
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)
        return logger
    
    #TODO: creating file for writing
    def create_csv(self,result_sheet):
        if (os.path.isfile(os.getcwd()+result_sheet)):
            os.remove(os.getcwd()+result_sheet)
        #csv.register_dialect('excel',lineterminator = '\n',skipinitialspace=True,escapechar='')
        output_file = open(os.getcwd() + result_sheet, "w")
        return output_file