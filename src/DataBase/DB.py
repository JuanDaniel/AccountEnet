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
    It class make the access to database and execute the queries
    '''

    def getAccess(self, date_start=None, date_end=None, phone=None):
        self.__connect()

        sql = "SELECT date_start, time_start, date_end, time_end, phone, duration FROM access"

        if(date_start):
            sql = sql + " WHERE date_start >= '%s'" %date_start
            if(date_end):
                sql = sql + " AND date_start <= '%s'" %date_end
            if(phone):
                sql = sql + " AND phone = '%s'" %phone

        elif(date_end):
            sql = sql + " WHERE date_start <= '%s'" %date_end
            if(phone):
                sql = sql + " AND phone = '%s'" %phone

        elif(phone):
            sql = sql + " WHERE phone = '%s'" %phone

        access = []
        for a in self.__cursor.execute(sql):
            access.append({'date_start':a[0], 'time_start':a[1], 'date_end':a[2], 'time_end':a[3], 'phone':a[4], 'duration':a[5]})

        self.__close()

        return access

    def insertAccess(self, access):
        self.__connect()

        for a in access:
            if(not self.__exist(a)):
                sql = "INSERT INTO access(date_start, time_start, date_end, time_end, phone, duration) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" %(a['date_start'], a['time_start'], a['date_end'], a['time_end'], a['phone'], a['duration'])

                self.__cursor.execute(sql)
        self.__connection.commit()

        self.__close()

    def __exist(self, access):
        sql = "SELECT * FROM access WHERE date_start = '%s' AND time_start = '%s'" %(access['date_start'], access['time_start'])

        if(len(self.__cursor.execute(sql).fetchall())):
            return True

        return False

    def __connect(self):
        self.__connection = sqlite3.connect(os.path.join('Extras', 'access.db'))
        self.__cursor = self.__connection.cursor()

    def __close(self):
        self.__connection.close()


