# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CheckData.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QInputDialog, 
                            QLineEdit, QFileDialog, QMainWindow)
import pandas as pd
import os
from clsTableModel import PandasModel

class Files:
    # Class Variable
    num_of_files = 0
    
    def __init__ (self):
        #Instance Variable
        self.FileDir = './'
        self.r1 = 0
        self.c1 = 0
        self.df = pd.DataFrame()
        Files.num_of_files += 1
    
    def getFileDir(self,widget):
        fdir, _ = QFileDialog.getOpenFileName(widget,
                                          "Choose File 1", 
                                          "",
                                          "All Files (*);;CSV Files (*.csv)")
        self.FileDir = fdir
        return fdir

    def readfile (self):
        self.df = pd.read_csv(self.FileDir, 
                              sep = ',', 
                              skiprows = self.r1)

class Ui_MainWindow(QMainWindow):
    
    File1 = Files()
    File2 = Files()
    
    def setupUi(self, MainWindow):

        #Interface--------------------------------------------------------------
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        self.btn_File1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_File1.setObjectName("btn_File1")
        self.gridLayout.addWidget(self.btn_File1, 0, 0, 1, 1)
        self.txtbox_File1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtbox_File1.setEnabled(True)
        self.txtbox_File1.setObjectName("txtbox_File1")
        self.gridLayout.addWidget(self.txtbox_File1, 0, 1, 1, 1)
        self.btn_File2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_File2.setObjectName("btn_File2")
        self.gridLayout.addWidget(self.btn_File2, 1, 0, 1, 1)
        self.txtbox_File2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txtbox_File2.setObjectName("txtbox_File2")
        self.gridLayout.addWidget(self.txtbox_File2, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tbl_preview = QtWidgets.QTableView(self.centralwidget)
        self.tbl_preview.setObjectName("tbl_preview")
        self.verticalLayout.addWidget(self.tbl_preview)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, 
                                           QtWidgets.QSizePolicy.Expanding, 
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.rdbtn_File1 = QtWidgets.QRadioButton(self.centralwidget)
        self.rdbtn_File1.setChecked(True)
        self.rdbtn_File1.setObjectName("rdbtn_File1")
        self.horizontalLayout.addWidget(self.rdbtn_File1)
        self.rdbtn_File2 = QtWidgets.QRadioButton(self.centralwidget)
        self.rdbtn_File2.setObjectName("rdbtn_File2")
        self.horizontalLayout.addWidget(self.rdbtn_File2)
        self.btn_preview = QtWidgets.QPushButton(self.centralwidget)
        self.btn_preview.setObjectName("btn_preview")
        self.horizontalLayout.addWidget(self.btn_preview)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        
        self.File1.FileDir = os.path.dirname(os.path.realpath(__file__))
        self.File2.FileDir = os.path.dirname(os.path.realpath(__file__))
        self.btn_File1.clicked.connect(lambda:self.txtbox_File1.setText(str(self.File1.getFileDir(self.centralwidget))))
        self.btn_File2.clicked.connect(lambda:self.txtbox_File2.setText(str(self.File2.getFileDir(self.centralwidget))))
        self.btn_preview.clicked.connect(self.PrintDir)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_File1.setText(_translate("MainWindow", "File 1"))
        self.btn_File2.setText(_translate("MainWindow", "File 2"))
        self.rdbtn_File1.setText(_translate("MainWindow", "File 1"))
        self.rdbtn_File2.setText(_translate("MainWindow", "File 2"))
        self.btn_preview.setText(_translate("MainWindow", "Preview"))
      
#Behavior Function-------------------------------------------------------------     
    def PrintDir(self):
        if self.rdbtn_File1.isChecked() == True:
            self.File1.readfile()
            model = PandasModel(self.File1.df)

        else:
            self.File2.r1 = 4
            self.File2.readfile()
            model = PandasModel(self.File2.df)
        
        self.tbl_preview.setModel(model)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

