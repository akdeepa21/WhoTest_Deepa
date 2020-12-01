import unittest2
from HTMLTestRunner import HTMLTestRunner
from testclasses.uiAlignmentPageTest import UIAlignmentPageTest
from testclasses.addRemoveElementsPageTest import AddRemoveElementsPageTest
from testclasses.homePageTest import HomePageTest
import os
from utilityclasses.constants import Constants as const

class SuiteClass(unittest2.TestCase): 
    
    def suiteone(self):        
        test_suite = unittest2.TestSuite()
        test_suite.addTest(HomePageTest('test_home_page'))
        test_suite.addTest(AddRemoveElementsPageTest('test_add_elements'))
        test_suite.addTest(AddRemoveElementsPageTest('test_remove_elements'))
        test_suite.addTest(UIAlignmentPageTest('test_go_to_ui_alignement_page'))
        test_suite.addTest(UIAlignmentPageTest('test_go_to_ui_random_url_page'))
        test_suite.addTest(UIAlignmentPageTest('test_go_to_ui_shift_url_page'))
        test_suite.addTest(UIAlignmentPageTest('test_go_to_ui_random_shift_url_page'))
        return test_suite
        
    def setUpModule(self):
        print("Setup")
        HomePageTest.setUpModule()
        
    def tearDownModule(self):
        print("Teardown")
        HomePageTest.tearDownModule()
         
if __name__ == '__main__':
    path =os.getcwd()
    SuiteClass.setUpModule(object)
    test_suite = SuiteClass.suiteone(object)
    unittest2.TextTestRunner()
    runner =HTMLTestRunner(output=path + const.smoketest_reports, verbosity=2, descriptions=True, failfast=True, buffer=False, 
                        report_title= const.smoketest_reportstitle, template=None, resultclass=None)
    runner.run(test_suite)
    SuiteClass.tearDownModule(object)