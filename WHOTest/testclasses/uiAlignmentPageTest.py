'''
Created on Nov 27, 2020

@author: kdeepa
'''
from pageclasses.uiAlignmentPage import uiAlignmentPage
from utilityclasses.readInputData import ReadData
from utilityclasses.screenshot import Screenshot
import unittest
from utilityclasses.constants import Constants as const

class UIAlignmentPageTest(unittest.TestCase):
    '''
    classdocs
    '''
    def __init__(self, testName):
        super(UIAlignmentPageTest, self).__init__(testName)
        self.testname = testName      
        pass

    @classmethod
    def setUpClass(self):
        self.uipage_obj = uiAlignmentPage()
        self.data = ReadData.get_json_data(self)
        self.logger = self.uipage_obj.logger

    def test_go_to_ui_alignement_page(self):
        global tc_status, originalElemDict
        try:
            self.uipage_obj.logger.info('Started test case execution in UI Alignment Page Test')
            expected = True
            test_type = 'positive'        
            self.uipage_obj.load_url(self.data['ShiftingElementsURL'])
            originalElemDict = self.uipage_obj.check_ui_element_location()
            tc_status = self.uipage_obj.verify_ui_page(test_type, const.shifting_page)
            if(tc_status != expected):            
                self.uipage_obj.logger.debug('Failed to validate UI Alignment page.')
                self.fail(msg= 'Failed to validate UI Alignment page.')
        except Exception as e:
            Screenshot.take_failure_sreenshot(self.uipage_obj)
            self.uipage_obj.logger.debug('Failed to validate UI Alignment page.')
            raise
    
    def test_go_to_ui_random_url_page(self):
        global tc_status, originalElemDict
        try:
            self.uipage_obj.logger.info('Started test case execution in UI Alignment Page Test')
            expected = True
            test_type = 'positive'        
            self.uipage_obj.load_url(self.data['ShiftingElementsURL'] + const.linkRandomClick)
            status = self.uipage_obj.check_ui_shifting_location(originalElemDict)
            tc_status = self.uipage_obj.verify_shifting_ui_page(test_type, status)
            if(tc_status != expected):            
                self.uipage_obj.logger.debug('Failed to validate UI Alignment page.')
                self.fail(msg= 'Failed to validate UI Alignment page.')
        except Exception as e:
            Screenshot.take_failure_sreenshot(self.uipage_obj)
            self.uipage_obj.logger.debug('Failed to validate UI Alignment page.')
            raise
        
    def test_go_to_ui_shift_url_page(self):
        global tc_status, originalElemDict
        try:
            self.uipage_obj.logger.info('Started test case execution in UI Alignment Page Test')
            expected = True
            test_type = 'positive'        
            self.uipage_obj.load_url(self.data['ShiftingElementsURL'] + const.linkShiftClick)
            status = self.uipage_obj.check_ui_shifting_location(originalElemDict)
            tc_status = self.uipage_obj.verify_shifting_ui_page(test_type, status)
            if(tc_status != expected):            
                self.uipage_obj.logger.debug('Failed to validate UI Alignment page.')
                self.fail(msg= 'Failed to validate UI Alignment page.')
        except Exception as e:
            Screenshot.take_failure_sreenshot(self.uipage_obj)
            self.uipage_obj.logger.debug('Failed to validate UI Alignment page.')
            raise
    
    def test_go_to_ui_random_shift_url_page(self):
        global tc_status, originalElemDict
        try:
            self.uipage_obj.logger.info('Started test case execution in UI Alignment Page Test')
            expected = True
            test_type = 'positive'        
            self.uipage_obj.load_url(self.data['ShiftingElementsURL'] + const.linkRandomShiftClick)
            status = self.uipage_obj.check_ui_shifting_location(originalElemDict)
            tc_status = self.uipage_obj.verify_shifting_ui_page(test_type, status)
            if(tc_status != expected):            
                self.uipage_obj.logger.debug('Failed to validate UI Alignment page.')
                self.fail(msg= 'Failed to validate UI Alignment page.')
        except Exception as e:
            Screenshot.take_failure_sreenshot(self.uipage_obj)
            self.uipage_obj.logger.debug('Failed to validate UI Alignment page.')
            raise