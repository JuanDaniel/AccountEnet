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
from PyQt4.QtCore import SIGNAL, QUrl
from Enviroment.ImpCalculateTime import ImpCalculateTime
from Common.Graphic import Graphic
from Enviroment.ImpAbout import ImpAbout
import os

class ImpMain():
    '''
    It is the implementation for FrmMain class
    '''

    def __init__(self, parent):
        self.__consume = '0:0:0'

        self.__frm = FrmMain(parent)
        self.__load = LoadAccess()
        self.__configuration = Configuration()

        '''
        Signals
        '''
        self.__frm.connect(self.__frm.actionConsumo_diario, SIGNAL("activated()"), self.__calculateDialyConsume)
        self.__frm.connect(self.__frm.actionAcerca_de, SIGNAL("activated()"), self.__about)
        self.__frm.connect(self.__frm.pushButton, SIGNAL("clicked()"), self.__filtrerAccess)

    def execute(self):
        self.__loadAccess()
        self.__frm.show()

    def __loadAccess(self):
        options = self.__configuration.getAppOptions()

        date_start = self.__frm.dateEdit_2.date().toString('yyyy-MM-dd')
        date_end = self.__frm.dateEdit.date().toString('yyyy-MM-dd')

        if(options['filtrer']['phone'] == 'False'):
            try:
                access = self.__load.getAccess(date_start, date_end, options['filtrer']['number'])
            except Exception, ex:
                QMessageBox.critical(self.__frm, 'Error', u'Se ha detectado que su configuración está corrupta', QMessageBox.Ok)
        else:
            access = self.__load.getAccess(date_start, date_end)

        self.__generateGraphic(access)
        self.__setAccess(access)

    def __generateGraphic(self, access):
        graphic = Graphic(access)

        graphic.generatePie()
        graphic.generatePolygon()

        self.__reloadGraphic()

    def __calculateDialyConsume(self):
        self.__instance = ImpCalculateTime(self.__frm)
        self.__instance.execute()

    def __filtrerAccess(self):
        date_start = self.__frm.dateEdit_2.date().toString('yyyy-MM-dd')
        date_end = self.__frm.dateEdit.date().toString('yyyy-MM-dd')
        phone = self.__frm.lineEdit.text()

        access = self.__load.getAccess(date_start, date_end, phone)

        self.__generateGraphic(access)
        self.__setAccess(access)

    def __setAccess(self, access):
        self.__consume = '0:0:0'
        self.__frm.tableWidget.setRowCount(0)

        i = 0
        for row in access:
            self.__frm.tableWidget.setRowCount(i+1)

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

        self.__consume = '%s:%s:%s' %(self.__convertTime(self.__consume))
        self.__frm.label_3.setText('Consumo %s' %self.__consume)

    def __convertTime(self, time):
        '''
        Created by ybarrio
        '''
        hour, min, seg = time.split(":")

        rest, seg = divmod(int(seg), 60)

        min = int(min) + rest
        rest, min = divmod(min, 60)

        hour = int(hour) + rest

        '''
        Convert the values to format 00:00:00
        '''
        if(hour < 10):
            hour = '0%s'%(hour)
        if(min < 10):
            min = '0%s'%(min)
        if(seg < 10):
            seg = '0%s'%(seg)

        return hour, min, seg

    def __changeConsume(self, duration):
        new_hour, new_min, new_seg = duration.split(':')
        old_hour, old_min, old_seg = self.__consume.split(':')

        hour = int(new_hour) + int(old_hour)
        min = int(new_min) + int(old_min)
        seg = int(new_seg) + int(old_seg)

        consume = "%s:%s:%s" % (hour, min, seg)
        self.__consume = consume

    def __reloadGraphic(self):
        self.__frm.webView.setUrl(QUrl(os.path.join('Extras', 'highcharts', 'pie-basic', 'index.html')))
        self.__frm.webView_2.setUrl(QUrl(os.path.join('Extras', 'highcharts', 'line-basic', 'index.html')))

    def __about(self):
        self.__instance = ImpAbout(self.__frm)
        self.__instance.execute()