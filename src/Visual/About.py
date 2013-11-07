# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/About.ui'
#
# Created: Wed Nov  6 20:33:41 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(562, 356)
        MainWindow.setMinimumSize(QtCore.QSize(562, 356))
        MainWindow.setMaximumSize(QtCore.QSize(562, 356))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/applications-office_icon.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout_2.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "AccountEnet :: Acerca de", None))
        self.pushButton.setText(_translate("MainWindow", "Aceptar", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/icons/applications-office.svg\" style=\"float: left;\" /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:75px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">AccountEnet</span> es una aplicación creada con el fin de ayudarle a administrar su consumo de la cuota de internet.</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:75px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Con AccountEnet usted será capaz de poder generar reportes y gráficos estadísticos de los accesos aplicando filtros como rango de fecha, teléfono y más...</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:75px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:75px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Si hasta este momento a usted le es muy engorroso poder obtener estos datos, no lo piense más, ésta es su solución.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:75px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:75px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">AccountEnet ha llegado para quedarse con usted, es la aplicación que tanto ha soñado.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:75px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:75px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Si desea colaborar o reportar algún bug no dude en contactar al desarrollador.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:75px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:75px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">2013</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:75px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\">Juan Daniel Santana Rodés</p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:75px; margin-right:10px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline; color:#0000ff;\">juandanielsantana@gmail.com</span></p></body></html>", None))

import resources_rc
