# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 24/10/2013

@author: jdsantana
'''

from Common.Configuration import Configuration
from Common.Extractor import Extractor
from socket import socket, AF_INET, SOCK_STREAM
from DataBase.DB import DB

class LoadAccess:
    '''
    It allows load the data of access, before check if is posible get new data from the page,
    if is not posible load the data store in the database
    '''

    def __init__(self):
        '''
        Load the configuration
        '''
        self.__configuration = Configuration()

        self.__extractor = Extractor(self.__configuration.getAccounting())

    def getAccess(self, date_start=None, date_end=None, phone=None):
        db = DB()

        if(self.__checkNetwork()):
            db.insertAccess(self.__extractor.extract())

        return db.getAccess(date_start, date_end, phone)

    def __checkNetwork(self):
        '''
        It check if there are network
        '''
        s = socket(AF_INET, SOCK_STREAM)
        try:
            s.settimeout(5)
            s.connect((self.__configuration.getDomain(), 80))
            s.close()
            return True
        except Exception, ex:
            print ex
            return False
