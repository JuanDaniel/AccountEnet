# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 24/10/2013

@author: jdsantana
'''

from DC.FrmMain import FrmMain
from Common.LoadAccess import LoadAccess
from PyQt4.QtGui import QTableWidgetItem

class ImpMain():
    '''
    It is the implementation for FrmMain class
    '''

    def __init__(self, parent):
        self.__consume = '0:0:0'

        self.__frm = FrmMain(parent)
        self.__load = LoadAccess()

    def execute(self):
        self.__loadAccess()
        self.__frm.show()

    def __loadAccess(self):
        access = self.__load.getAccess()

        count = self.__frm.tableWidget.rowCount()
        i = 0
        for row in access:
            count = count + 1
            self.__frm.tableWidget.setRowCount(count)

            '''
            Date Start
            '''
            date = row['date_start'].split()
            self.__frm.tableWidget.setItem(i, 0, QTableWidgetItem(date[0]))
            self.__frm.tableWidget.setItem(i, 1, QTableWidgetItem(date[1]))

            '''
            Date End
            '''
            date = row['date_end'].split()
            self.__frm.tableWidget.setItem(i, 2, QTableWidgetItem(date[0]))
            self.__frm.tableWidget.setItem(i, 3, QTableWidgetItem(date[1]))

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

