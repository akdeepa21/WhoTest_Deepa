'''
Created on Nov 27, 2020

@author: kdeepa
'''
from utilityclasses.constants import Constants as const
from core.webdriverBase import WebdriverBase
from core.pageBase import PageBase
from selenium.webdriver.common.by import By
import sys
from selenium.webdriver.common.action_chains import ActionChains

class AddRemoveElementsPage(object):
    '''
    classdocs
    '''


    def __init__(self, *args):
        '''
        Constructor
        '''
        selenium = WebdriverBase('AddRemoveElementsPage')
        self.driver = selenium.get_driver()
        self.logger = selenium.get_logger('AddRemoveElementsPage')
        
        '''Locators - AddRemoveElementsPage'''
        self.addElements = (By.XPATH, "//button[contains(text(), 'Add Element')]")
        self.deleteElements = (By.XPATH, "//button[@class='added-manually' and contains(text(), 'Delete')]")
        self.addedElements = (By.XPATH, "//div[@id='elements']//button[contains(text(), 'Delete')]")
        self.pageHeading = (By.XPATH, "//div[@id='content']//h3")
        
   
        
    @classmethod   
    def setUpClass(self, base_url):
        pass
    
    def load_url(self, base_url):
        self.logger.info("Trying to load URL \'{}\'".format(base_url))
        self.driver.get(base_url)
        self.driver.set_page_load_timeout(const.timeout)        
        self.elementPagefield = PageBase.findElement(self, self.addElements)
        if(self.elementPagefield !=None):
            self.logger.info('Loaded \'URL: {}\' successfully'.format(base_url)) 
            
    def add_ElementsButtonClick(self):
        addElementButton = PageBase.findElement(self,self.addElements)
        PageBase.clickElement(self, addElementButton)
        PageBase.waitForElementToBeDisplayed(self, self.addedElements)
        self.addedElementsView = PageBase.findElement(self, self.addedElements)
        if(self.addedElementsView !=None):
            self.logger.info('Added elements successfully')
        pass
        
    def delete_ElementsButtonClick(self):
        self.deleteElementsView = PageBase.findElement(self, self.deleteElements)
        PageBase.clickElement(self, self.deleteElementsView)
        PageBase.setPageLoadTimeout(self)
        status =PageBase.waitForElementNotToBeDisplayed(self, self.deleteElementsView)
        if(status == True):
            self.logger.info('Deleted elements successfully')
        pass

        
    def verify_added_elements(self, test_type, name):
        global error_msg
        try:
            self.logger.info('Verifying the Added Elements status..')
            if test_type == 'positive':                
                added_elements_view = PageBase.findElement(self, self.addedElements)
                verifyText = PageBase.getText(self, added_elements_view)
                if(name in verifyText and PageBase.elementIsDispalyed(self, added_elements_view)):
                    return (True)
            else:                           
                return (False)   
        except Exception as e:
            e= sys.exc_info()                          
            return (e[1]) 
        
    def verify_deleted_elements(self, test_type, name=None):
        global error_msg
        try:
            self.logger.info('Verifying the Deleted Elements status..')
            if test_type == 'positive':                
                if(PageBase.waitForElementNotToBeDisplayed(self, self.deleteElements)):
                    return (True)
            else:                           
                return (False)   
        except Exception as e:
            e= sys.exc_info()                          
            return (e[1]) 