# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtStdOut = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtStdOut.setGeometry(QtCore.QRect(10, 150, 621, 281))
        self.txtStdOut.setObjectName("txtStdOut")
        self.btnAnalyze = QtWidgets.QPushButton(self.centralwidget)
        self.btnAnalyze.setGeometry(QtCore.QRect(510, 110, 113, 32))
        self.btnAnalyze.setObjectName("btnAnalyze")
        self.cbLanguage = QtWidgets.QComboBox(self.centralwidget)
        self.cbLanguage.setGeometry(QtCore.QRect(80, 80, 81, 61))
        self.cbLanguage.setObjectName("cbLanguage")
        self.cbLanguage.addItem("")
        self.cbLanguage.addItem("")
        self.cbLanguage.addItem("")
        self.cbLanguage.addItem("")
        self.cbLanguage.addItem("")
        self.cbLanguage.addItem("")
        self.lblLanguage = QtWidgets.QLabel(self.centralwidget)
        self.lblLanguage.setGeometry(QtCore.QRect(10, 100, 81, 16))
        self.lblLanguage.setObjectName("lblLanguage")
        self.lblInputFile = QtWidgets.QLabel(self.centralwidget)
        self.lblInputFile.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.lblInputFile.setObjectName("lblInputFile")
        self.lblOutputFile = QtWidgets.QLabel(self.centralwidget)
        self.lblOutputFile.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.lblOutputFile.setObjectName("lblOutputFile")
        self.lneInputFile = QtWidgets.QLineEdit(self.centralwidget)
        self.lneInputFile.setGeometry(QtCore.QRect(90, 30, 381, 21))
        self.lneInputFile.setObjectName("lneInputFile")
        self.lneOutputFile = QtWidgets.QLineEdit(self.centralwidget)
        self.lneOutputFile.setGeometry(QtCore.QRect(90, 60, 381, 21))
        self.lneOutputFile.setObjectName("lneOutputFile")
        self.btnInputBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnInputBrowse.setGeometry(QtCore.QRect(480, 30, 113, 32))
        self.btnInputBrowse.setObjectName("btnInputBrowse")
        self.btnOutputBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnOutputBrowse.setGeometry(QtCore.QRect(480, 60, 113, 32))
        self.btnOutputBrowse.setObjectName("btnOutputBrowse")
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(280, 0, 91, 20))
        self.lblTitle.setObjectName("lblTitle")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menuCoh_MetrixML = QtWidgets.QMenu(self.menubar)
        self.menuCoh_MetrixML.setObjectName("menuCoh_MetrixML")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuCoh_MetrixML.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnAnalyze.setText(_translate("MainWindow", "Analyze"))
        self.cbLanguage.setItemText(0, _translate("MainWindow", "en"))
        self.cbLanguage.setItemText(1, _translate("MainWindow", "zh"))
        self.cbLanguage.setItemText(2, _translate("MainWindow", "de"))
        self.cbLanguage.setItemText(3, _translate("MainWindow", "es"))
        self.cbLanguage.setItemText(4, _translate("MainWindow", "fr"))
        self.cbLanguage.setItemText(5, _translate("MainWindow", "ar"))
        self.lblLanguage.setText(_translate("MainWindow", "Language:"))
        self.lblInputFile.setText(_translate("MainWindow", "Input File:"))
        self.lblOutputFile.setText(_translate("MainWindow", "Output File:"))
        self.btnInputBrowse.setText(_translate("MainWindow", "Browse"))
        self.btnOutputBrowse.setText(_translate("MainWindow", "Browse"))
        self.lblTitle.setText(_translate("MainWindow", "Coh-MetrixML"))
        self.menuCoh_MetrixML.setTitle(_translate("MainWindow", "Coh-MetrixML"))
