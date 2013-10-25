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

    def getAccess(self, date_start=None, date_end=None, phone=None):
        self.__connect()

        sql = 'SELECT date_start, date_end,  phone, duration FROM access'

        if(date_start):
            sql = sql + ' WHERE date_start >= %s' %date_start
        if(date_end):
            sql = sql + ' AND date_end <= %s' %date_end
        if(phone):
            sql = sql + ' AND phone = %s' %phone

        access = []
        for a in self.__cursor.execute(sql):
            access.append({'date_start':a[0], 'date_end':a[1], 'phone':a[2], 'duration':a[3]})

        self.__close()

        return access

    def insertAccess(self, access):
        self.__connect()

        for a in access:
            if(not self.__exist(a)):
                sql = "INSERT INTO access(date_start, date_end, phone, duration) VALUES('%s', '%s', '%s', '%s')" %(a['date_start'], a['date_end'], a['phone'], a['duration'])

                self.__cursor.execute(sql)
        self.__connection.commit()

        self.__close()

    def __exist(self, access):
        sql = "SELECT * FROM access WHERE date_start = '%s'" %(access['date_start'])

        if(len(self.__cursor.execute(sql).fetchall())):
            return True

        return False

    def __connect(self):
        self.__connection = sqlite3.connect(os.path.join('Extras', 'access.db'))
        self.__cursor = self.__connection.cursor()

    def __close(self):
        self.__connection.close()


