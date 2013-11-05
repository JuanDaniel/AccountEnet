# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 30/10/2013

@author: jdsantana
'''

from DC.FrmCalculateTime import FrmCalculateTime
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QMessageBox

class ImpCalculateTime():
    '''
    It class allow cacule the dialy consume
    '''

    def __init__(self, parent):
        self.__frm = FrmCalculateTime(parent)

        '''
        Signals
        '''
        self.__frm.connect(self.__frm.pushButton, SIGNAL("clicked()"), self.__calculate)
        self.__frm.connect(self.__frm.lineEdit, SIGNAL("returnPressed()"), self.__calculate)
        self.__frm.connect(self.__frm.lineEdit_2, SIGNAL("returnPressed()"), self.__calculate)

    def __calculate(self):
        try:
            hours = int(self.__frm.lineEdit.text())
            days = int(self.__frm.lineEdit_2.text())

            if(days < 1 or days > 31):
                raise Exception('La cantidad de días debe de ser un valor válido')

            consume = float(hours) / float(days) * 60
            consume = '%s:%s:00' %(self.__convertToTime(consume))

            self.__frm.label_5.setText(u'Consumo por día %s' %consume)
        except ValueError, ex:
            QMessageBox.warning(self.__frm, 'Alerta', u'Para calcular el consumo diario,\n debe proporcionar valores válidos', QMessageBox.Ok)
        except Exception, ex:
            QMessageBox.warning(self.__frm, 'Alerta', u''+str(ex), QMessageBox.Ok)

    def __convertToTime(self, consume):
        '''
        Convert the posible consume to date format 00:00
        '''
        hour = int(consume / 60)
        min = int(consume % 60)

        if(hour < 10):
            hour = '0%s'%(hour)
        if(min < 10):
            min = '0%s'%(min)

        return hour, min

    def execute(self):
        self.__frm.show()
