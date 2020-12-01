'''
Created on Nov 27, 2020

@author: kdeepa
'''

from utilityclasses.constants import Constants as const
from selenium import webdriver
import logging
import os

class WebdriverBase(object):
    '''
    This class contains selenium driver instantiation methods
    '''
    driver = logger = instance = None   
    class DriverProcess:
        '''
        This class contains selenium driver instantiation & logger instantiation methods
        '''
        def __init__(self, name, *args):
            global logger
            logger = logging.getLogger(name)
            logger.setLevel(logging.DEBUG)
              
            if not logger.handlers:
                path = os.getcwd()
                self.filehandler = logging.FileHandler(path + const.log_file_name)
                self.filehandler.setLevel(logging.DEBUG)
                  
                self.streamhandler = logging.StreamHandler()
                self.streamhandler.setLevel(logging.DEBUG)
                  
                formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s :  %(message)s')
                  
                self.filehandler.setFormatter(formatter)
                self.streamhandler.setFormatter(formatter)
                  
                logger.addHandler(self.filehandler)
                logger.addHandler(self.streamhandler) 
                   
       
        def get_logger(self, name): 
            self.__init__(name)                  
            return logger  
#     
    def __init__(self, name, *args):
        global driver, logger
        if WebdriverBase.instance == None:
            WebdriverBase.instance = WebdriverBase.DriverProcess(name)
            path = os.getcwd()
            print(path)
            driver = webdriver.Firefox(executable_path= path + const.win_geckodriver_64bit_path)   
            driver.maximize_window()            
            driver.implicitly_wait(const.timeout)                         
        logger = WebdriverBase.instance.get_logger(name)          

    def __getattr__(self, attr):
        return getattr(self.instance, attr)

    def get_driver(self):
        return driver   
    
 