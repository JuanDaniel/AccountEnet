# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 24/10/2013

@author: jdsantana
'''

from DC.FrmMain import FrmMain
from Common.LoadAccess import LoadAccess

class ImpMain():
    '''
    It is the implementation if FrmMain class
    '''

    def __init__(self, parent):
        self.__frm = FrmMain(parent)
        self.__load = LoadAccess()

    def execute(self):
        self.__load.getAccess()

        self.__frm.show()
