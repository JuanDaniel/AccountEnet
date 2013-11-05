# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 05/11/2013

@author: jdsantana
'''
from DC.FrmAbout import FrmAbout

class ImpAbout():
    '''
    It class show data about this program
    '''

    def __init__(self, parent):
        self.__frm = FrmAbout(parent)

    def execute(self):
        self.__frm.show()
