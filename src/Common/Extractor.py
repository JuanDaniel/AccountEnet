# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 23/10/2013

@author: jdsantana
'''

from urllib import urlopen
from lxml.html import fromstring
from datetime import datetime

class Extractor:
    '''
    The main objetive is extract all data connections for a account of ENET
    '''

    def __init__(self, url):
        self.__url = url

    def __load(self):
        file = urlopen(self.__url)
        self.__page = file.read()
        file.close()

    def extract(self):
        self.__load()

        doc = fromstring(self.__page)
        table = doc.cssselect('table')[4]
        trs = table.cssselect('tr')

        '''
        Remove the two firts rows
        '''
        del trs[0]
        del trs[0]

        '''
        Remove the last row
        '''
        del trs[len(trs) - 1]

        access = []
        for tr in trs:
            row = tr.cssselect('td div')

            '''
            Date Start
            '''
            date = row[0].text_content().split('-')
            time = row[1].text_content().split(':')
            date_start = datetime(int(date[2]), int(date[1]), int(date[0]), int(time[0]), int(time[1]), int(time[2]))

            '''
            Date End
            '''
            date = row[2].text_content().split('-')
            time = row[3].text_content().split(':')
            date_end = datetime(int(date[2]), int(date[1]), int(date[0]), int(time[0]), int(time[1]), int(time[2]))

            phone = row[4].text_content()
            duration = row[5].text_content()

            access.append({'date_start':date_start, 'date_end':date_end, 'phone':phone, 'duration':duration })

        return access