# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 23/10/2013

@author: jdsantana
'''

from _pyio import __metaclass__
from Common.Singleton import Singleton
import sqlite3
import os

class DB:
    __metaclass__ = Singleton
    '''
    Make the access to sqlite data base
    '''

    def __init__(self):
        self.__connection = sqlite3.connect(os.path.join('Extras', 'access.db'))
        self.__cursor = self.__connection.cursor()

    def getAccess(self, date_start=None, date_end=None, phone=None):
        sql = 'SELECT * FROM access'

        if(date_start):
            sql = sql + ' WHERE date_start >= %s' %date_start
        if(date_end):
            sql = sql + ' AND date_end <= %s' %date_end
        if(phone):
            sql = sql + ' AND phone = %s' %phone

        return self.__cursor.execute(sql)

    def insertAccess(self, access):
        for a in access:
            sql = "INSERT INTO access(date_start, date_end, phone, duration) VALUES('%s', '%s', '%s', '%s')" %(a['date_start'], a['date_end'], a['phone'], a['duration'])

            self.__cursor.execute(sql)
        self.__connection.commit()

    def close(self):
        self.__connection.close()


