# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 24/10/2013

@author: jdsantana
'''

from PyQt4 import QtGui
from Visual.CalculateTime import Ui_MainWindow

class FrmCalculateTime(QtGui.QMainWindow, Ui_MainWindow):
    '''
    It is the CalculaTime UI implementation
    '''

    def __init__(self, parent = None):
        super(FrmCalculateTime, self).__init__(parent)
        self.setupUi(self)