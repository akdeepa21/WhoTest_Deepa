'''
Created on Nov 27, 2020

@author: kdeepa
'''
from core.webdriverBase import WebdriverBase
from utilityclasses.constants import Constants as const
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PageBase(WebdriverBase):
    '''
    classdocs
    '''

    def __init__(self, name):
        '''
        Constructor
        '''
        selenium = WebdriverBase('PageBase')
        self.driver = selenium.get_driver()
        self.logger = selenium.get_logger()
        
    def closeBrowser(self):
        try:
            self.driver.close()
            self.logger.info("Browser closed successfully")
        except Exception as e:
            self.logger.error("Unable to close the browser")  
        
    def findElement(self, locator):
        self.logger.info("Going to find the " + str(locator))
        tries = 0
        element = None
        while tries < const.attempts and element is None:
            try:            
                element = WebDriverWait(self.driver, const.timeout).until(EC.presence_of_element_located(locator))                
            except Exception as e:
                self.logger.warning("Element not found "+str(locator))
                tries += 1
                if tries == const.attempts:
                    raise
        return element
    
    def findAllElements(self, locator):
        elements = ""
        self.logger.info("Going to find the element " + str(locator))  
        try: 
            elements = WebDriverWait(self.driver, const.timeout).until(EC.visibility_of_any_elements_located(locator))            
#             time.sleep(const.sleep)                
            elements = self.driver.find_elements(locator)                      
        except Exception as e:
            self.logger.warning("Unable to find the element " + str(locator))  
        return elements
                   
    def setPageLoadTimeout(self):
        self.logger.info("Going to wait for page load ")  
        try:                             
            self.driver.set_page_load_timeout(const.timeout)
        except Exception as e:
            self.logger.warning("Unable to wait for page load ")  
     
    def sendKeys(self, element, value):
        self.logger.info("Going to type " + '"'+str(value)+'"' + " on field "+str(element))
        try:
            element.clear()
            element.send_keys(value)
        except Exception as e:
            self.logger.warning("Unable to type on " + str(element))
    
    def getURL(self):
        self.logger.info("Going to get current URL")
        try:
            return self.driver.current_url  
        except Exception as e:
            self.logger.warning("Unable to get current URL")           
    
    def getText(self, element):
        self.logger.info("Going to get text of element "+str(element))
        try:
            mytext = element.text
            return mytext
        except Exception as e:
            self.logger.warning("Unable to get text of element " + str(element))
    
    def getAttribute(self, element, attribute): 
        self.logger.info("Going to get " + ' "'+str(attribute)+'" ' + "attribute of element "+str(element))
        try:        
            return element.get_attribute(attribute)  
        except Exception as e:
            self.logger.warning("Unable to get " + ' "'+str(attribute)+'" ' + "attribute of element "+str(element))           
 
    def elementIsDispalyed(self, element):
        self.logger.info("Going to find display status of element "+str(element))   
        try:
            stat = element.is_enabled()   
            return element.is_displayed()
        except Exception as e:
            self.logger.warning("Unable to find display of element "+str(element))
            
    def waitForElementToBeClickable(self, locator):
        self.logger.info("Going to find clickable status of element "+str(locator))  
        try:
            self.element = WebDriverWait(self.driver, const.timeout).until(EC.element_to_be_clickable(locator))
            return True
        except Exception as e:
            self.logger.warning("Element not found "+str(locator)) 
            return False
        
    def waitForElementToBeDisplayed(self, locator):
        self.logger.info("Going to find display status of element "+str(locator))  
        try:
            self.element = WebDriverWait(self.driver, const.timeout).until(EC.visibility_of_element_located(locator))
            return True
        except Exception as e:
            self.logger.warning("Element not found "+str(locator)) 
            return False
        
    def waitForElementNotToBeDisplayed(self, locator):
        self.logger.info("Going to find display status of element "+str(locator))  
        try:
            self.element = WebDriverWait(self.driver, const.timeout).until(EC.invisibility_of_element_located(locator))
            return True
        except Exception as e:
            self.logger.warning("Element is found "+str(locator)) 
            return False
        
    def clickElement(self, element):
        self.logger.info("Going to click on field "+str(element))
        try:                              
            element.click()         
        except Exception as e:
            self.logger.warning("Unable to click on field " + str(element))
            
    def switchToAlert(self):
        self.logger.info("Going to find the alert ")
        try:
            alert = self.driver.switch_to_alert()
            return alert
        except Exception as e:
            self.logger.warning("Unable to find the alert ")
            
    def acceptAlert(self, element):
        self.logger.info("Going to accept the alert ")
        try:
            element.accept()
        except Exception as e:
            self.logger.warning("Unable to accept the alert ")
            
    def select_from_drop_down_by_text(self, element, text):
        option = Select(PageBase.findElement(self, element))
        option.select_by_visible_text(text)
        
    def get_location(self, element): 
        self.logger.info("Going to get location of the element ")
        try:
            locDict=element.location
            return locDict
        except Exception as e:
            self.logger.warning("Unable to get location of the element ")
            return False
            
    def get_size(self, element): 
        self.logger.info("Going to get size of the element ")
        try:
            sizeDict=element.size
            return sizeDict
        except Exception as e:
            self.logger.warning("Unable to get size of the element ")
            return False   
        
    def traverse_elements(self, elemList):
        self.logger.info("Going to traverse through the element list ")
        elemlocationDict={}
        myDict ={}
        try:
            lenlist = len(elemList)
            for i in range(lenlist):
                locDict = elemList[i].location                
                elemText = elemList[i].text
                self.logger.info('Found \'Element: {}\' Location with \'Co-ordinates:{}\''.format(elemText, locDict))
                elemlocationDict[elemText]=locDict
                myDict.update(elemlocationDict)             
            return myDict
        except Exception as e:
            self.logger.warning("Unable to traverse through the element list ")
            return False 
        