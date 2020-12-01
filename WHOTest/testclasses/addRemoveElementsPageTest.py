'''
Created on Nov 27, 2020

@author: kdeepa
'''
from pageclasses.addRemoveElementsPage import AddRemoveElementsPage
from utilityclasses.readInputData import ReadData
from utilityclasses.screenshot import Screenshot
import unittest
from utilityclasses.constants import Constants as const

class AddRemoveElementsPageTest(unittest.TestCase):
    '''
    classdocs
    '''
    def __init__(self, testName):
        super(AddRemoveElementsPageTest, self).__init__(testName)
        self.testname = testName     
        pass

#     @classmethod
#     def setUpModule(self):        
#         self.addelems_obj = AddRemoveElementsPage("AddRemoveElementsPage")
#         self.logger = self.addelems_obj.logger
#         self.addelems_obj.logger.info("=====================Started Automation in WHO Test=====================")            
        
    @classmethod
    def setUpClass(self):
        self.addelems_obj = AddRemoveElementsPage("AddRemoveElementsPage")
        self.data = ReadData.get_json_data(self)
        self.logger = self.addelems_obj.logger

    def test_add_elements(self):
        global tc_status
        try:
            self.addelems_obj.logger.info('Started test case execution in AddRemoveElements Page')
            expected = True
            test_type = 'positive'
            self.addelems_obj.load_url(self.data['AddRemoveElementURL'])       
            self.addelems_obj.add_ElementsButtonClick()
            tc_status = self.addelems_obj.verify_added_elements(test_type, const.addedElements)
            if(tc_status != expected):            
                self.addelems_obj.logger.debug('Failed to validate Add/Remove Elements page.')
                self.fail(msg= 'Failed to validate Add/Remove Elements page.')
        except Exception as e:
            Screenshot.take_failure_sreenshot(self.addelems_obj)
            self.addelems_obj.logger.debug('Failed to validate Add/Remove Elements page.')
            raise
        
    def test_remove_elements(self):
        global tc_status
        try:
            self.addelems_obj.logger.info('Started test case execution in AddRemoveElements Page')
            expected = True
            test_type = 'positive'        
            self.addelems_obj.delete_ElementsButtonClick()
            tc_status = self.addelems_obj.verify_deleted_elements(test_type, const.addRemoveElements_page)
            if(tc_status != expected):            
                self.addelems_obj.logger.debug('Failed to validate Remove Elements page.')
                self.fail(msg= 'Failed to validate Remove Elements page.')
        except Exception as e:
            Screenshot.take_failure_sreenshot(self.addelems_obj)
            self.addelems_obj.logger.debug('Failed to validate Remove Elements page.')
            raise