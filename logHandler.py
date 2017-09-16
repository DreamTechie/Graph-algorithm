'''log handler'''
import config

class log_handler:

    #log_pointer = 'Null'

    #defult constructer def __init__(self):
    def __init__(self):
        log_pointer = 'Null'

    def give_me_a_log_pointer(self):

        f_log_name = config.log_file
        log_pointer = open(f_log_name, 'a+')
        return log_pointer