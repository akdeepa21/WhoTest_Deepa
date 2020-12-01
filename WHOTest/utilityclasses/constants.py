'''
Created on Nov 27, 2020

@author: kdeepa
'''

class Constants(object):
    '''
    This class contains constants used through out Automation
    '''
    
    '''General'''
    timeout = 30
    attempts = 4
    sleep = 6  
    browser_firefox = "firefox"
    test_data_file_name="\\testData\\test_data.json"
    screenshot_folder ='\\screenshots\\'
    log_file_path =""
    log_file_name="\\testlogs.log"
    win_geckodriver_64bit_path = "\\drivers\\geckodriver.exe"
    title = "WHO Test"
    home_page = "Welcome to the-internet"
    addRemoveElements_page = "Add/Remove Elements"
    shifting_page = "Shifting Content: Menu Element"
    addedElements ="Delete"
    linkRandomClick =  "?mode=random"
    linkShiftClick =  "?pixel_shift=100"
    linkRandomShiftClick =  "?mode=random&pixel_shift=100"

    
    '''Reports'''
    smoketest_reports = '\\TestReports-Smoke'
    smoketest_reportstitle = 'WHO Test -  Automation Smoke Test Report'