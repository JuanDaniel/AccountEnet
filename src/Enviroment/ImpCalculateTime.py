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

    def __calculate(self):
        partialy = int(self.__frm.lineEdit.text())
        total = int(self.__frm.lineEdit_2.text())

        try:
            if(total < partialy):
                raise Exception('La disponibilidad de horas debe de ser menor que el total')

            consume = float(partialy) / float(total) * 60

            print consume

            self.__frm.label_5.setText(u'Consumo por día: %f' %consume)
        except ValueError, ex:
            QMessageBox.warning(self.__frm, 'Alerta', u'Para calcular el consumo diario,\n debe proporcionar valores válidos', QMessageBox.Ok)
        except Exception, ex:
            QMessageBox.warning(self.__frm, 'Alerta', str(ex), QMessageBox.Ok)

    def execute(self):
        self.__frm.show()
