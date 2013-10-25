# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 24/10/2013

@author: jdsantana
'''

from PyQt4 import QtGui
from Visual.Main import Ui_MainWindow

class FrmMain(QtGui.QMainWindow, Ui_MainWindow):
    '''
    It is the Main UI implementation
    '''

    def __init__(self, parent = None):
        super(FrmMain, self).__init__(parent)
        self.setupUi(self)

        '''
        Date Start
        '''
        #self.dateEdit_2.set

        '''
        Date End
        '''
