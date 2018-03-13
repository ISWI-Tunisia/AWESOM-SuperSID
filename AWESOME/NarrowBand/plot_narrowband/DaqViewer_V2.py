# -*- coding: utf-8 -*-
'''
Author: Ahmed Ammar, ahmed.ammar@fst.utm.tn
Purpose: - - - 
Inputs: - - -
Outputs:  - - -
Date Created: Tue Mar 13 15:27:51 2018
Date Modified: M D, Y
Date Released: M D, Y
Versions:
    V0.01: ---
    
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout,\
                            QGroupBox, QDialog, QVBoxLayout, QDateEdit, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QLocale, QDate, QDateTime
 
from PlotData import Plot_Data

class App(QDialog):
 
    def __init__(self):
        super().__init__()
        self.title = 'Data Viewer'
        self.left = 200
        self.top = 200
        self.width = 320
        self.height = 100
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('imgs/ISWI_Logo_sm.jpg'))
 
        self.createHorizontalLayout()
 
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalQWidget)
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
 
        self.show()
 
    def createHorizontalLayout(self):
        self.horizontalQWidget = QWidget()
        layout1 = QHBoxLayout()
        
        # Label Date
        label_date= QLabel('Date', self)
        layout1.addWidget(label_date) 
        # QDateEdit: Edit Date
        DateEdit = QDateEdit(self)
        DateEdit.setDisplayFormat("dd-MMMM-yyyy")
        DateEdit.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        DateEdit.setCalendarPopup(True)
        layout1.addWidget(DateEdit)
        
        today= QDateTime.currentDateTime().date()
        DateEdit.setDate(QDate(today))
        date= DateEdit.date()
        DateEdit.dateChanged[QDate].connect(self.on_ShowDate)
        
#        buttonBlue = QPushButton('Done', self)
#        buttonBlue.clicked.connect(self.on_plot)
#        layout1.addWidget(buttonBlue) 
# 
        self.horizontalQWidget.setLayout(layout1)
        
        self.horizontalGroupBox = QGroupBox(" Subplots")
        layout2 = QHBoxLayout()
        
        buttonPlot = QPushButton('Plot', self)
        buttonPlot.clicked.connect(self.on_plot)
        layout2.addWidget(buttonPlot) 
 
        self.horizontalGroupBox.setLayout(layout2)
 
    @pyqtSlot()
    def on_plot(self):
        print('PyQt5 button click')
        Plot_Data(pathname="H:\\NarrowbandData\\Algeria\\2015\\03\\20\\", filename="*150320*NRK_000B.mat")
    
    def on_ShowDate(self, date):
        '''
        Select Year, Month and Day from calander
        '''
        print(date.toPyDate())
        self.date= date.toPyDate()
        self.year, self.month, self.day = self.date.year, '{:02d}'.format(self.date.month), '{:02d}'.format(self.date.day)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())