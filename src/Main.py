# -*- coding: utf-8 -*-
#!/usr/bin/python
'''
Created on 23/10/2013

@author: jdsantana
'''

from PyQt4.QtGui import QApplication
from Enviroment.ImpMain import ImpMain

if __name__ == '__main__':
    app = QApplication([])
    frm = ImpMain(None)
    frm.execute()
    app.exec_()

    #extractor = Extractor(configuration.getAccounting())
    #extractor.extract()
