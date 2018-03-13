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
        
        # Nember of subplots
        ## Label N Subplots
        label_nSubplots= QLabel('Number of Subplots', self)
        layout1.addWidget(label_nSubplots)
         ## SpinBox N Subplots
        self.nSubplots= QSpinBox(self)
        self.nSubplots.setMinimum(0)
        self.nSubplots.setMaximum(10)
        self.nSubplots.setValue(0)
        self.nSubplots.setSingleStep(1)
        self.nSubplots.valueChanged.connect(self.on_nSubplots)
        layout1.addWidget(self.nSubplots)
        
        self.horizontalQWidget.setLayout(layout1)
    def createGroupGridBox(self):
            # Group Box 
            self.horizontalGroupBox = QGroupBox(" Subplots")
            #TODO: Grid layout to be incrimented for N subplots
            self.layout2 = QGridLayout()
            self.layout2.setColumnStretch(1, 4)
            self.layout2.setColumnStretch(2, 4)
            self.NemberOfSubplots=self.nSubplots.value()           
            ## See Function (signal)
            
            self.horizontalGroupBox.setLayout(self.layout2)
            
 
    @pyqtSlot()
    def on_plot(self):
        print('PyQt5 button click')
        Plot_Data(pathname="H:\\NarrowbandData\\Algeria\\2015\\03\\20\\", filename="*150320*NRK_000A.mat")
    
    @pyqtSlot(int)
    def on_nSubplots(self, value):
    ## Clear widgets from layout: PALEN & Blaa_Thor 
    ##(https://stackoverflow.com/questions/4528347/clear-all-widgets-in-a-layout-in-pyqt)
        for i in reversed(range(self.layout2.count())): 
            widgetToRemove = self.layout2.itemAt( i ).widget()
            # remove it from the layout list
            self.layout2.removeWidget( widgetToRemove )
            # remove it from the gui
            widgetToRemove.setParent( None )
        self.setLayout(self.layout2)
        
        for i in range(1,value+1):
            c1 = QLabel("Subplot N %i" % i)
            self.layout2.addWidget(c1, i,0)
            ## Recievers
            Rx=  QComboBox(self)
            Rx.addItems(Rx_ID.keys())
            self.layout2.addWidget(Rx,i,1)
            ## Transmitters
            Tx=  QComboBox(self)
            Tx.addItems(Tx_ID.keys())
            c2 = QLabel("Transmitter")
            self.layout2.addWidget(c2, i,2)
            self.layout2.addWidget(Tx,i,3)
            ## High/Low res
            Low_High = QCheckBox("Low/High res",self)
            self.layout2.addWidget(Low_High,i,4)
            ## Amp/Phi
            Amplitude_Phase = QCheckBox("Amplitude/Phase",self)
            self.layout2.addWidget(Amplitude_Phase,i,5)
                
        self.setLayout(self.layout2)
    
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