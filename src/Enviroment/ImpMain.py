# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 24/10/2013

@author: jdsantana
'''

from DC.FrmMain import FrmMain
from Common.LoadAccess import LoadAccess
from PyQt4.QtGui import QTableWidgetItem
from Common.Configuration import Configuration
from PyQt4.QtGui import QMessageBox

class ImpMain():
    '''
    It is the implementation for FrmMain class
    '''

    def __init__(self, parent):
        self.__consume = '0:0:0'

        self.__frm = FrmMain(parent)
        self.__load = LoadAccess()
        self.__configuration = Configuration()

    def execute(self):
        self.__loadAccess()
        self.__frm.show()

    def __loadAccess(self):
        options = self.__configuration.getAppOptions()

        if(options['filtrer']['phone'] == 'False'):
            try:
                access = self.__load.getAccess(None, None, options['filtrer']['number'])
            except Exception, ex:
                QMessageBox.critical(self.__frm, 'Error', u'Se ha detectado que su configuración está corrupta', QMessageBox.Ok)
        else:
            access = self.__load.getAccess()

        count = self.__frm.tableWidget.rowCount()
        i = 0
        for row in access:
            count = count + 1
            self.__frm.tableWidget.setRowCount(count)

            '''
            Date and Time Start
            '''
            self.__frm.tableWidget.setItem(i, 0, QTableWidgetItem(row['date_start']))
            self.__frm.tableWidget.setItem(i, 1, QTableWidgetItem(row['time_start']))

            '''
            Date and Time End
            '''
            self.__frm.tableWidget.setItem(i, 2, QTableWidgetItem(row['date_end']))
            self.__frm.tableWidget.setItem(i, 3, QTableWidgetItem(row['time_end']))

            '''
            Phone
            '''
            self.__frm.tableWidget.setItem(i, 4, QTableWidgetItem(row['phone']))

            '''
            Duration
            '''
            self.__frm.tableWidget.setItem(i, 5, QTableWidgetItem(row['duration']))

            self.__changeConsume(row['duration'])

            i = i + 1

        self.__consume = '%s:%s:%s' %(self.__convert_time(self.__consume))
        self.__frm.label_3.setText('Consumo %s' %self.__consume)

    def __convert_time(self, time):
        '''
        Created by ybarrio
        '''
        hour, min, seg = time.split(":")

        rest, seg = divmod(int(seg), 60)

        min = int(min) + rest
        rest, min = divmod(min, 60)

        hour = int(hour) + rest

        return hour, min, seg

    def __changeConsume(self, duration):
        new_hour, new_min, new_seg = duration.split(':')
        old_hour, old_min, old_seg = self.__consume.split(':')

        hour = int(new_hour) + int(old_hour)
        min = int(new_min) + int(old_min)
        seg = int(new_seg) + int(old_seg)

        consume = "%s:%s:%s" % (hour, min, seg)
        self.__consume = consume

