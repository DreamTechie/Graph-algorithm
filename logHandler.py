'''log handler'''
import config


#later log_handler class can be used to handle multi-threading or multi - instances log writing
class log_handler:

    #global log_pointer

    #defult constructer def __init__(self):
    # def __init__(self):
    #     log_pointer = 'Null'

    def write_to_log_file(self):

        f_log_name = config.log_file
        log_pointer = open(f_log_name, 'a+')
        print(config.log_bucket)

        #log_pointer.write(config.log_bucket)
        log_pointer.close()
        config.log_bucket = ''
        return