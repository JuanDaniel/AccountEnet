# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 23/10/2013

@author: jdsantana
'''

from _pyio import __metaclass__
from Common.Singleton import Singleton
from configobj import ConfigObj

class Configuration:
    __metaclass__ = Singleton
    '''
    Load the external configuration
    '''

    def __init__(self):
        config = ConfigObj('configuration.conf')

        '''
        Domain
        '''
        self.__domain = config['enet']['domain']

        '''
        Account accounting
        '''
        self.__accounting = config['enet']['accounting']

    def getDomain(self):
        return self.__domain

    def getAccounting(self):
        return self.__accounting
