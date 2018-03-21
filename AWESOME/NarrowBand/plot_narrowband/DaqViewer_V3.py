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
                             QAction,QToolBar, QFileDialog, QMessageBox,
                            QGroupBox, QDialog, QVBoxLayout, QDateEdit, QLabel,
                            QLineEdit, QTextEdit, QGridLayout, QComboBox, QCheckBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QLocale, QDate, QDateTime

from LoadData import DataLoaded_list, DataError_List
from PlotData import Plot_Data
from SitesInfo import Rx_ID, Tx_ID

class App(QDialog):
 
    def __init__(self):
        super().__init__()
        self.title = 'Data Viewer'
        self.left = 200
        self.top = 200
        self.width = 600
        self.height = 200
        self.initUI()
        self.update_PathFileNames()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('imgs/ISWI_Logo_sm.jpg'))
        
        # Tool bar
        self.tb=QToolBar(self)
        tuto=QAction(QIcon('imgs/open.png'), "&Tutorial (Ctrl+T)",
                self, shortcut="Ctrl+T", triggered=self.tutorial)
        self.tb.addAction(tuto)
        alert=QAction(QIcon('imgs/new.png'),"&About (Ctrl+A)",
                self, shortcut="Ctrl+A", triggered=self.about)
        self.tb.addAction(alert)
        #Horizontal layout
        
        self.createHorizontalLayout()
        self.createGroupGridBox()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.tb)
        windowLayout.addWidget(self.horizontalQWidget)
        windowLayout.addWidget(self.horizontalGroupBox)
        # Text :Show what is going on when clicking on button plot
        self.TextInfo= QTextEdit("Ready!", self)
        self.TextInfo.setReadOnly(True)
        windowLayout.addWidget(self.TextInfo)
        # Plot Button
        buttonPlot = QPushButton('Plot', self)
        buttonPlot.clicked.connect(self.on_plot)
        windowLayout.addWidget(buttonPlot)
        
        self.setLayout(windowLayout)
        
        self.show()
    

    def tutorial(self):
        QMessageBox.aboutQt(self)
    def about(self):
        QMessageBox.about(self, "DaqViewer",
                          '''
                          This is DaqViewer softaware for visualizing NarrowBand 
                          Data from AWESOME instrument.\n
                          Author: Ahmed Ammar \n
                          Date Created: Tue Mar 13 15:27:51 2018 \n
                          ''')
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
        
        DateEdit.dateChanged[QDate].connect(self.on_ShowDate)
        self.date= DateEdit.date()
        self.date= self.date.toPyDate()
        self.year, self.month, self.day = self.date.year, '{:02d}'.format(self.date.month), '{:02d}'.format(self.date.day)
        # Edit path to Narrowband Data
        label_PathNarrow = QLabel('Path to Narrowband Data', self)
        layout1.addWidget(label_PathNarrow)
        self.PathText= QLineEdit("C:/NarrowbandData/",self)
        self.PathText.textChanged[str].connect(self.update_PathFileNames)
        layout1.addWidget(self.PathText)
        # Select directory button
        BtnSelectDir = QPushButton('...', self)
        BtnSelectDir.clicked.connect(self.on_SelectDir)
        layout1.addWidget(BtnSelectDir)
        
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
            self.subplot1.toggled.connect(self.update_PathFileNames)
            self.layout2.addWidget(self.subplot1, 0,0)
            
            self.subplot2 = QCheckBox("Subplot N° 2", self)
            self.subplot2.setChecked(True)
            self.subplot2.toggled.connect(self.update_PathFileNames)
            self.layout2.addWidget(self.subplot2, 1,0)
            
            
            self.subplot3 = QCheckBox("Subplot N° 3", self)
            self.subplot3.toggled.connect(self.update_PathFileNames)
            self.layout2.addWidget(self.subplot3, 2,0)
            
            self.subplot4 = QCheckBox("Subplot N° 4", self)
            self.subplot4.toggled.connect(self.update_PathFileNames)
            self.layout2.addWidget(self.subplot4, 3,0)
            
            ## Recievers
            self.Rx1=  QComboBox(self)
            self.Rx1.addItems(Rx_ID.keys())
            self.layout2.addWidget(self.Rx1,0,1)
            self.Rx1.currentIndexChanged.connect(self.update_PathFileNames)
            
            self.Rx2=  QComboBox(self)
            self.Rx2.addItems(Rx_ID.keys())
            self.layout2.addWidget(self.Rx2,1,1)
            self.Rx2.currentIndexChanged.connect(self.update_PathFileNames)
            
            self.Rx3=  QComboBox(self)
            self.Rx3.addItems(Rx_ID.keys())
            self.layout2.addWidget(self.Rx3,2,1)
            self.Rx3.currentIndexChanged.connect(self.update_PathFileNames)
            
            self.Rx4=  QComboBox(self)
            self.Rx4.addItems(Rx_ID.keys())
            self.layout2.addWidget(self.Rx4,3,1)
            self.Rx4.currentIndexChanged.connect(self.update_PathFileNames)
            ## Transmitters
            self.Tx1=  QComboBox(self)
            self.Tx1.addItems(Tx_ID.keys())
            self.layout2.addWidget(self.Tx1,0,2)
            self.Tx1.currentIndexChanged.connect(self.update_PathFileNames)
            
            self.Tx2=  QComboBox(self)
            self.Tx2.addItems(Tx_ID.keys())
            self.layout2.addWidget(self.Tx2,1,2)
            self.Tx2.currentIndexChanged.connect(self.update_PathFileNames)
            
            self.Tx3=  QComboBox(self)
            self.Tx3.addItems(Tx_ID.keys())
            self.layout2.addWidget(self.Tx3,2,2)
            self.Tx3.currentIndexChanged.connect(self.update_PathFileNames)
            
            self.Tx4=  QComboBox(self)
            self.Tx4.addItems(Tx_ID.keys())
            self.layout2.addWidget(self.Tx4,3,2)
            self.Tx4.currentIndexChanged.connect(self.update_PathFileNames)
            
            ## High/Low res
            self.Low_High1 = QCheckBox("Low Res/(High Res)",self)
            self.layout2.addWidget(self.Low_High1,0,4)
            self.Low_High1.toggled.connect(self.update_PathFileNames)
            
            self.Low_High2 = QCheckBox("Low Res/(High Res)",self)
            self.layout2.addWidget(self.Low_High2,1,4)
            self.Low_High2.toggled.connect(self.update_PathFileNames)
            
            self.Low_High3 = QCheckBox("Low Res/(High Res)",self)
            self.layout2.addWidget(self.Low_High3,2,4)
            self.Low_High3.toggled.connect(self.update_PathFileNames)
            
            self.Low_High4 = QCheckBox("Low Res/(High Res)",self)
            self.layout2.addWidget(self.Low_High4,3,4)
            self.Low_High4.toggled.connect(self.update_PathFileNames)
            
            ## Amp/Phi
            self.Amplitude_Phase1 = QCheckBox("Amplitude/(Phase)",self)
            self.layout2.addWidget(self.Amplitude_Phase1,0,5)
            self.Amplitude_Phase1.toggled.connect(self.update_PathFileNames)
            
            self.Amplitude_Phase2 = QCheckBox("Amplitude/(Phase)",self)
            self.layout2.addWidget(self.Amplitude_Phase2,1,5)
            self.Amplitude_Phase2.toggled.connect(self.update_PathFileNames)
            
            self.Amplitude_Phase3 = QCheckBox("Amplitude/(Phase)",self)
            self.layout2.addWidget(self.Amplitude_Phase3,2,5)
            self.Amplitude_Phase3.toggled.connect(self.update_PathFileNames)
            
            self.Amplitude_Phase4 = QCheckBox("Amplitude/(Phase)",self)
            self.layout2.addWidget(self.Amplitude_Phase4,3,5)
            self.Amplitude_Phase4.toggled.connect(self.update_PathFileNames)
            
            
            self.setLayout(self.layout2)
            self.horizontalGroupBox.setLayout(self.layout2)
        
    def update_PathFileNames(self):
#        print(str(self.date.year))
        self.pathnames=[]
        self.filenames=[]
        self.TitlePlot=[]
        
        if self.subplot1.isChecked():
            self.Rx1.setEnabled(True); self.Tx1.setEnabled(True) 
            self.Low_High1.setEnabled(True); self.Amplitude_Phase1.setEnabled(True)
            self.path1= self.PathText.text() + \
            self.Rx1.currentText() + "/" + str(self.year) + \
            "/" + str(self.month) + "/" + str(self.day) + "/"
            if self.Amplitude_Phase1.isChecked() and self.Low_High1.isChecked():
                self.AmpPhi="D"
            elif self.Low_High1.isChecked():
                self.AmpPhi="C"
            elif self.Amplitude_Phase1.isChecked():
                self.AmpPhi="B"
            else:
                self.AmpPhi="A"
            
            self.file1=Rx_ID[self.Rx1.currentText()]+ str(self.year)[2:]+str(self.month)+str(self.day)+ \
            "*" + Tx_ID[self.Tx1.currentText()] + self.AmpPhi + ".mat"
            
            self.title1= self.Rx1.currentText() +", "+ str(self.year) + \
            "/" + str(self.month) + "/" + str(self.day)+ ", "+ self.Tx1.currentText()
           
            self.pathnames.append(self.path1)
            self.filenames.append(self.file1)
            self.TitlePlot.append(self.title1)
        else:
            self.Rx1.setEnabled(False); self.Tx1.setEnabled(False)
            self.Low_High1.setEnabled(False); self.Amplitude_Phase1.setEnabled(False)
        
        if self.subplot2.isChecked():
            self.Rx2.setEnabled(True); self.Tx2.setEnabled(True) 
            self.Low_High2.setEnabled(True); self.Amplitude_Phase2.setEnabled(True)
            self.path2= self.PathText.text()+ \
            self.Rx2.currentText() + "/" + str(self.year) + \
            "/" + str(self.month) + "/" + str(self.day) + "/"
            if self.Amplitude_Phase2.isChecked() and self.Low_High2.isChecked():
                self.AmpPhi="D"
            elif self.Low_High2.isChecked():
                self.AmpPhi="C"
            elif self.Amplitude_Phase2.isChecked():
                self.AmpPhi="B"
            else:
                self.AmpPhi="A"
            
            self.file2=Rx_ID[self.Rx2.currentText()]+ str(self.year)[2:]+str(self.month)+str(self.day)+ \
            "*" + Tx_ID[self.Tx2.currentText()] + self.AmpPhi + ".mat"
            
            self.title2= self.Rx2.currentText() +", "+ str(self.year) + \
            "/" + str(self.month) + "/" + str(self.day)+ ", "+ self.Tx2.currentText()
            
            self.pathnames.append(self.path2)
            self.filenames.append(self.file2)
            self.TitlePlot.append(self.title2)
        else:
            self.Rx2.setEnabled(False); self.Tx2.setEnabled(False)
            self.Low_High2.setEnabled(False); self.Amplitude_Phase2.setEnabled(False)
            
            
        if self.subplot3.isChecked():
            self.Rx3.setEnabled(True); self.Tx3.setEnabled(True) 
            self.Low_High3.setEnabled(True); self.Amplitude_Phase3.setEnabled(True)
            self.path3= self.PathText.text() + \
            self.Rx3.currentText() + "/" + str(self.year) + \
            "/" + str(self.month) + "/" + str(self.day) + "/"
            if self.Amplitude_Phase3.isChecked() and self.Low_High3.isChecked():
                self.AmpPhi="D"
            elif self.Low_High3.isChecked():
                self.AmpPhi="C"
            elif self.Amplitude_Phase3.isChecked():
                self.AmpPhi="B"
            else:
                self.AmpPhi="A"
            
            self.file3=Rx_ID[self.Rx3.currentText()]+ str(self.year)[2:]+str(self.month)+str(self.day)+ \
            "*" + Tx_ID[self.Tx3.currentText()] + self.AmpPhi + ".mat"
            
            self.title3= self.Rx3.currentText() +", "+ str(self.year) + \
            "/" + str(self.month) + "/" + str(self.day)+ ", "+ self.Tx3.currentText()
            
            self.pathnames.append(self.path3)
            self.filenames.append(self.file3)
            self.TitlePlot.append(self.title3)
        else:
            self.Rx3.setEnabled(False); self.Tx3.setEnabled(False)
            self.Low_High3.setEnabled(False); self.Amplitude_Phase3.setEnabled(False)
            
        if self.subplot4.isChecked():
            self.Rx4.setEnabled(True); self.Tx4.setEnabled(True) 
            self.Low_High4.setEnabled(True); self.Amplitude_Phase4.setEnabled(True)
            self.path4= self.PathText.text() + \
            self.Rx4.currentText() + "/" + str(self.year) + \
            "/" + str(self.month) + "/" + str(self.day) + "/"
            if self.Amplitude_Phase4.isChecked() and self.Low_High4.isChecked():
                self.AmpPhi="D"
            elif self.Low_High4.isChecked():
                self.AmpPhi="C"
            elif self.Amplitude_Phase4.isChecked():
                self.AmpPhi="B"
            else:
                self.AmpPhi="A"
            
            self.file4=Rx_ID[self.Rx4.currentText()]+ str(self.year)[2:]+str(self.month)+str(self.day)+ \
            "*" + Tx_ID[self.Tx4.currentText()] + self.AmpPhi + ".mat"
            
            self.title4= self.Rx4.currentText() +", "+ str(self.year) + \
            "/" + str(self.month) + "/" + str(self.day)+ ", "+ self.Tx4.currentText()
            
            self.pathnames.append(self.path4)
            self.filenames.append(self.file4)
            self.TitlePlot.append(self.title4)
        else:
            self.Rx4.setEnabled(False); self.Tx4.setEnabled(False)
            self.Low_High4.setEnabled(False); self.Amplitude_Phase4.setEnabled(False)
        
        print(self.pathnames)
        print(self.filenames)
        print(self.TitlePlot)

    def on_SelectDir(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Data's Directory (NarrowbandData)"))
        self.PathText.setText(file+"/")
    def on_plot(self):
        try:
            print(self.pathnames[0])
            Plot_Data(pathnames=self.pathnames, filenames=self.filenames, TitlePlot=self.TitlePlot)
            self.TextInfo.clear()
            self.TextInfo.textCursor().insertHtml("<p><h3><font color='blue'>Loaded Data: </font></p>")
            for data in DataLoaded_list: self.TextInfo.textCursor().insertHtml("<pre><h4><font color='green'>"+data + ", </font></pre>")
        except:
            self.TextInfo.clear()
            for data in DataError_List: self.TextInfo.textCursor().insertHtml("<pre><h4><font color='red'>Error!" + "\n" +  data + ", </font></pre>")
    
    def on_ShowDate(self, date):
        '''
        Select Year, Month and Day from calander
        '''
#        print(date.toPyDate())
        self.date= date.toPyDate()
        self.year, self.month, self.day = self.date.year, '{:02d}'.format(self.date.month), '{:02d}'.format(self.date.day)
        self.update_PathFileNames()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())