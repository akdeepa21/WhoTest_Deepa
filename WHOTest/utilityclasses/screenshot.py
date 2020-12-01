'''
Created on Nov 27, 2020

@author: kdeepa
'''
from utilityclasses.constants import Constants as const
from datetime import datetime
import os

class Screenshot(object):
    '''
    classdocs
    '''
    def take_failure_sreenshot(self):
        path = os.getcwd()     
        fail_url = self.driver.current_url
        self.logger.debug('Failure web page URL: ' + fail_url)
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')        
        self.driver.save_screenshot(path + const.screenshot_folder +'%s.png' % now)
        pass

    def __init__(self, params):
        '''
        Constructor
        '''
        