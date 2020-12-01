'''
Created on Nov 27, 2020

@author: kdeepa
'''
from utilityclasses.constants import Constants as const
from core.webdriverBase import WebdriverBase
from core.pageBase import PageBase
from selenium.webdriver.common.by import By
import sys
from dictionaries import Dict

class uiAlignmentPage(object):
    '''
    classdocs
    '''
    def __init__(self, *args):
        '''
        Constructor
        '''
        selenium = WebdriverBase('uiAlignmentPage')
        self.driver = selenium.get_driver()
        self.logger = selenium.get_logger('uiAlignmentPage')
        
        
        '''Locators - uiAlignmentPage'''
        self.menuHome = (By.LINK_TEXT, "Home")   
        self.menuAbout =  (By.LINK_TEXT, "About")    
        self.menuContactUs =  (By.LINK_TEXT, "Contact Us")
        self.menuPortfolio =  (By.LINK_TEXT, "Portfolio")
        self.menuGallery =  (By.LINK_TEXT, "Gallery")
        self.shiftheading = (By.XPATH, "//div[@class='example']//h3[contains (text(), 'Shifting Content: Menu Element')]")
        
    @classmethod   
    def setUpClass(self, base_url):
        pass
    
    def load_url(self, base_url):
        self.logger.info("Trying to load URL \'{}\'".format(base_url))
        self.driver.get(base_url)
        self.driver.set_page_load_timeout(const.timeout)        
        self.elementPagefield = PageBase.findElement(self, self.shiftheading)
        if(self.elementPagefield !=None):
            self.logger.info('Loaded \'URL: {}\' successfully'.format(base_url)) 
            

    def check_ui_elements(self):
        global elemList
        self.homeElem = PageBase.findElement(self, self.menuHome)
        self.aboutElem = PageBase.findElement(self, self.menuAbout)
        self.contactElem = PageBase.findElement(self, self.menuContactUs)
        self.portfolioElem = PageBase.findElement(self, self.menuPortfolio)
        self.galleryElem = PageBase.findElement(self, self.menuGallery)
        elemList = [self.homeElem, self.aboutElem, self.contactElem, self.portfolioElem, self.galleryElem]
        return elemList 
    
    def check_ui_element_location(self):
        elemList = uiAlignmentPage.check_ui_elements(self)
        myElemDict = PageBase.traverse_elements(self, elemList)
        return myElemDict
 
            
    def check_ui_shifting_location(self, originalElemDict):    
        newElemDict = uiAlignmentPage.check_ui_element_location(self)
        is_equal = originalElemDict == newElemDict
        if(is_equal == True):
            self.logger.info('UI Elements are aligned properly')           
        return is_equal  
    
    def check_element_displayed(self):
        elemList = uiAlignmentPage.check_ui_elements(self)
        for elem in elemList(len(elemList)):
            status= PageBase.elementIsDispalyed(self, elem)
            if (status == True):
                self.logger.info('UI Elements are displayed properly') 
        
            
        
    def verify_shifting_ui_page(self, test_type, name=None):
        global error_msg
        try:
            self.logger.info('Verifying the ui shifting page status..')
            if test_type == 'positive':                
                if(name == True):
                    return (True)
            else:                           
                return (False)   
        except Exception as e:
            e= sys.exc_info()                          
            return (e[1]) 
        
    def verify_ui_page(self, test_type, name):
        global error_msg
        try:
            self.logger.info('Verifying the ui shifting page status..')
            if test_type == 'positive':                
                shift_page_view = PageBase.findElement(self, self.shiftheading)
                verifyText = PageBase.getText(self, shift_page_view)
                if(name == verifyText and PageBase.elementIsDispalyed(self, shift_page_view)):
                    return (True)
            else:                           
                return (False)   
        except Exception as e:
            e= sys.exc_info()                          
            return (e[1]) 