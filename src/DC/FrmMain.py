# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 24/10/2013

@author: jdsantana
'''

from PyQt4 import QtGui, QtCore
from Visual.Main import Ui_MainWindow
from Common.Configuration import Configuration
from datetime import datetime

class FrmMain(QtGui.QMainWindow, Ui_MainWindow):
    '''
    It is the Main UI implementation
    '''

    def __init__(self, parent = None):
        super(FrmMain, self).__init__(parent)
        self.setupUi(self)

        self.__configuration = Configuration()

        '''
        Set configuration's options
        '''
        self.__setConfiguration()

        self.__setDateFiltrer()

        '''
        Signals
        '''
        #self.dateEdit_2.set

    def __setConfiguration(self):
        options = self.__configuration.getAppOptions()

        try:
            if(options['filtrer']['phone'] == 'True'):
                self.label_6.setEnabled(True)
                self.lineEdit.setEnabled(True)
            else:
                self.lineEdit.setText(options['filtrer']['number'])
        except Exception, ex:
            pass

    def __setDateFiltrer(self):
        today = datetime.today()

        self.dateEdit_2.setDate(QtCore.QDate(today.year, today.month, 1))
        self.dateEdit.setDate(QtCore.QDate(today.year, today.month, today.day))