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
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout,
                            QGroupBox, QDialog, QVBoxLayout, QDateEdit, QLabel,
                            QSpinBox, QGridLayout, QComboBox, QCheckBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QLocale, QDate, QDateTime
 
from PlotData import Plot_Data
from SitesInfo import Rx_ID, Tx_ID

class App(QDialog):
 
    def __init__(self):
        super().__init__()
        self.title = 'Data Viewer'
        self.left = 200
        self.top = 200
        self.width = 500
        self.height = 100
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('imgs/ISWI_Logo_sm.jpg'))
        # Plot Button
        buttonPlot = QPushButton('Plot', self)
        buttonPlot.clicked.connect(self.on_plot)
        
        self.createHorizontalLayout()
        self.createGroupGridBox()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalQWidget)
        windowLayout.addWidget(self.horizontalGroupBox)
        windowLayout.addWidget(buttonPlot)
        
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
        
        self.horizontalQWidget.setLayout(layout1)
    def createGroupGridBox(self):
            # Group Box 
            self.horizontalGroupBox = QGroupBox(" Subplots")
            self.layout2 = QGridLayout()
            self.layout2.setColumnStretch(1, 4)
            self.layout2.setColumnStretch(2, 4)           
            ## Groupbox elements
            ### Subplots
            self.subplot1 = QCheckBox("Subplot N° 1", self)
            self.subplot1.setChecked(True)
            self.subplot1.toggled.connect(self.checkbox_toggled)
            self.layout2.addWidget(self.subplot1, 0,0)
            
            self.subplot2 = QCheckBox("Subplot N° 2", self)
            self.subplot2.setChecked(True)
            self.subplot2.toggled.connect(self.checkbox_toggled)
            self.layout2.addWidget(self.subplot2, 1,0)
            
            
            self.subplot3 = QCheckBox("Subplot N° 3", self)
            self.layout2.addWidget(self.subplot3, 2,0)
            
            self.subplot4 = QCheckBox("Subplot N° 4", self)
            self.layout2.addWidget(self.subplot4, 3,0)
            
            ## Recievers
            self.Rx1=  QComboBox(self)
            self.Rx1.addItems(Rx_ID.keys())
            self.layout2.addWidget(self.Rx1,0,1)
            self.Rx1.currentIndexChanged.connect(self.Rx1_selection)
            
            self.Rx2=  QComboBox(self)
            self.Rx2.addItems(Rx_ID.keys())
            self.layout2.addWidget(self.Rx2,1,1)
            self.Rx2.currentIndexChanged.connect(self.Rx2_selection)
            
            self.Rx3=  QComboBox(self)
            self.Rx3.addItems(Rx_ID.keys())
            self.layout2.addWidget(self.Rx3,2,1)
            self.Rx3.currentIndexChanged.connect(self.Rx3_selection)
            
            self.Rx4=  QComboBox(self)
            self.Rx4.addItems(Rx_ID.keys())
            self.layout2.addWidget(self.Rx4,3,1)
            self.Rx4.currentIndexChanged.connect(self.Rx4_selection)
            ## Transmitters
            self.Tx1=  QComboBox(self)
            self.Tx1.addItems(Tx_ID.keys())
            self.layout2.addWidget(self.Tx1,0,2)
            self.Tx1.currentIndexChanged.connect(self.Tx1_selection)
            
            self.Tx2=  QComboBox(self)
            self.Tx2.addItems(Tx_ID.keys())
            self.layout2.addWidget(self.Tx2,1,2)
            self.Tx2.currentIndexChanged.connect(self.Tx2_selection)
            
            self.Tx3=  QComboBox(self)
            self.Tx3.addItems(Tx_ID.keys())
            self.layout2.addWidget(self.Tx3,2,2)
            self.Tx3.currentIndexChanged.connect(self.Tx3_selection)
            
            self.Tx4=  QComboBox(self)
            self.Tx4.addItems(Tx_ID.keys())
            self.layout2.addWidget(self.Tx4,3,2)
            self.Tx4.currentIndexChanged.connect(self.Tx4_selection)
            
            ## High/Low res
            self.Low_High1 = QCheckBox("Low Res/(High Res)",self)
            self.layout2.addWidget(self.Low_High1,0,4)
            
            self.Low_High2 = QCheckBox("Low Res/(High Res)",self)
            self.layout2.addWidget(self.Low_High2,1,4)
            
            self.Low_High3 = QCheckBox("Low Res/(High Res)",self)
            self.layout2.addWidget(self.Low_High3,2,4)
            
            self.Low_High4 = QCheckBox("Low Res/(High Res)",self)
            self.layout2.addWidget(self.Low_High4,3,4)
            
            ## Amp/Phi
            self.Amplitude_Phase1 = QCheckBox("Amplitude/(Phase)",self)
            self.layout2.addWidget(self.Amplitude_Phase1,0,5)
            
            self.Amplitude_Phase2 = QCheckBox("Amplitude/(Phase)",self)
            self.layout2.addWidget(self.Amplitude_Phase2,1,5)
            
            self.Amplitude_Phase3 = QCheckBox("Amplitude/(Phase)",self)
            self.layout2.addWidget(self.Amplitude_Phase3,2,5)
            
            self.Amplitude_Phase4 = QCheckBox("Amplitude/(Phase)",self)
            self.layout2.addWidget(self.Amplitude_Phase4,3,5)
            
            
            self.setLayout(self.layout2)
            self.horizontalGroupBox.setLayout(self.layout2)
         
    def checkbox_toggled(self):
        if self.subplot1.isChecked():
            self.Rx1.setEnabled(True)
        else:
            self.Rx1.setEnabled(False)
            
        if self.subplot2.isChecked():
            self.Rx2.setEnabled(True)
        else:
            self.Rx2.setEnabled(False)
            
    def Rx1_selection(self, text):
        pass
    def Rx2_selection(self, text):
        pass
    def Rx3_selection(self, text):
        pass
    def Rx4_selection(self, text):
        pass
    def Tx1_selection(self, text):
        pass
    def Tx2_selection(self, text):
        pass
    def Tx3_selection(self, text):
        pass
    def Tx4_selection(self, text):
        pass
    def on_plot(self):
        print('PyQt5 button click')
        Plot_Data(pathname="H:\\NarrowbandData\\Algeria\\2015\\03\\20\\", filename="*150320*NRK_000A.mat")
        
        
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