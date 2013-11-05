# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 05/11/2013

@author: jdsantana
'''

from PyQt4 import QtGui
from Visual.About import Ui_MainWindow

class FrmAbout(QtGui.QMainWindow, Ui_MainWindow):
    '''
    It is the About UI implementation
    '''

    def __init__(self, parent):
        super(FrmAbout, self).__init__(parent)
        self.setupUi(self)
