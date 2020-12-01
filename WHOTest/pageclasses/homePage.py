'''
Created on Apr 17, 2019

@author: kdeepa
'''
from utilityclasses.constants import Constants as const
from core.webdriverBase import WebdriverBase
from core.pageBase import PageBase
from selenium.webdriver.common.by import By
import sys

class HomePage(object):
    '''
    classdocs
    '''

    def __init__(self, *args):
        '''
        Constructor
        '''
        
        selenium = WebdriverBase('HomePage')
        self.driver = selenium.get_driver()
        self.logger = selenium.get_logger('HomePage')
        
        '''HomePage - Locators'''
        self.homepageheading = (By.XPATH, "//h1[@class='heading' and contains(text(),'Welcome to the-internet')]")
     
    @classmethod   
    def setUpClass(self, base_url):
        pass
    
    def load_url(self, base_url):
        self.logger.info("Trying to load URL \'{}\'".format(base_url))
        self.driver.get(base_url)
        self.driver.set_page_load_timeout(const.timeout)        
        headingfield = PageBase.findElement(self, self.homepageheading)
        if(headingfield !=None):
            self.logger.info('Logged into \'URL: {}\' successfully'.format(base_url))   
            
    def set_email(self, email):
        self.logger.info('Trying to login into using \'Email: {}\''.format(email))
        emailfield = PageBase.findElement(self, self.email)
        PageBase.sendKeys(self, emailfield, email)   
        
    def click_launchdemo(self):
        launchdemofield = PageBase.findElement(self, self.launchdemobtn)
        PageBase.clickElement(self, launchdemofield)
        self.driver.set_page_load_timeout(const.timeout)
        user_profile = PageBase.findElement(self, self.userprofile)
        if(self.driver.title == const.home_page and user_profile !=None):
            self.logger.info('Logged into using UserMail successfully')
        
    def verify_home_page_status(self, test_type, value):
        global error_msg        
        try:          
            self.logger.info('verifying the login status...')        
            if test_type == 'positive':          
                verifyheadingfield = PageBase.findElement(self, self.homepageheading)                
                home_status = PageBase.getText(self, verifyheadingfield)
                if(home_status == value):           
                    return (True)       
            else:                                    
                return (False)  
        except Exception as e:
            e= sys.exc_info()                                       
            return (False, e[1])             
    