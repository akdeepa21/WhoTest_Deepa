'''
Created on Nov 27, 2020

@author: kdeepa
'''
from utilityclasses.constants import Constants as const
import json
import os
import sys

class ReadData(object):
    '''
    classdocs
    '''

    def get_json_data(self):        
        path = os.getcwd() + const.test_data_file_name  
        with open(path) as json_file:
            json_data = json.load(json_file)
            return (json_data)

    def __init__(self, params):
        '''
        Constructor
        '''
        