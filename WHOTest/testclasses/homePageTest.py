'''
Created on Apr 17, 2019

@author: kdeepa
'''
from pageclasses.homePage import HomePage
from utilityclasses.readInputData import ReadData
from utilityclasses.screenshot import Screenshot
import unittest
from utilityclasses.constants import Constants as const

class HomePageTest(unittest.TestCase):
    '''
    classdocs
    '''
    def __init__(self, testName, **kwargs):
        super(HomePageTest, self).__init__(testName)
        self.testname = testName   
        pass
        
    @classmethod
    def setUpModule(self):        
        self.home_obj = HomePage("HomePageTest")
        self.logger = self.home_obj.logger
        self.home_obj.logger.info("=====================Started Automation in WHO Test=====================")            

    @classmethod
    def setUpClass(self):
        self.home_obj = HomePage("HomePageTest")
        self.data = ReadData.get_json_data(self)        
        pass
    
    def test_home_page(self):
        global tc_status
        try:
            self.home_obj.logger.info('Started test case execution in \'URL: {}\''.format(self.data['HomeURL']))
            expected = True
            test_type = 'positive'   
            self.home_obj.load_url(self.data['HomeURL'])     
            tc_status = self.home_obj.verify_home_page_status(test_type, const.home_page)
            if(tc_status != expected):
                self.home_obj.logger.debug('Failed to load \'URL: {}\''.format(self.data['HomeURL']))                                             
                self.fail(msg= 'Failed to load \'URL: {}\''.format(self.data['HomeURL']))
        except Exception as e:
            Screenshot.take_failure_sreenshot(self.home_obj)
            self.home_obj.logger.debug('Failed to load \'URL: {}\''.format(self.data['HomeURL']))
            raise
        
    @classmethod
    def tearDownClass(self):
        pass
    
    @classmethod
    def tearDownModule(self):          
        self.home_obj.driver.close()
        self.home_obj.driver.quit()
        self.logger.info("=====================Ended Automation in WHO Test=====================") 
        pass