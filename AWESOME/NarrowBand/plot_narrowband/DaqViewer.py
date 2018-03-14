# -*- coding: utf-8 -*-
'''
Author: Ahmed Ammar, ahmed.ammar@fst.utm.tn
Purpose: Load NarrowBand data
Inputs: - - -
Outputs:  - - -
Date Created: Sat Mar 10 19:10:30 2018
Date Modified: M D, Y
Date Released: M D, Y
Versions:
    V0.01: ---
'''

from PyQt5 import QtWidgets, QtCore, QtGui
from SitesInfo import Rx_ID
from PlotData import Plot_Data
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.initUI()
        
         ## Select date 
        date= self.dateEdit.date()
        self.dateEdit.dateChanged[QtCore.QDate].connect(self.showDate)
        #TODO:
        # Receivers Sites Names : Prepare for station selction!
        print(Rx_ID)
        k=[key for key in Rx_ID]
        print(k)
            
        for key in Rx_ID:
            print(Rx_ID[key])
        
        
        
    def initUI(self):
        """
        Widgets & proprieties 
        """
        # Window proprieties
        ## Size
        self.resize(500, 300)
        self.setMinimumSize(QtCore.QSize(500, 300))
        self.setMaximumSize(QtCore.QSize(500, 1000))
        self.setWindowIcon(QtGui.QIcon('imgs/ISWI_Logo_sm.jpg'))
        ## Title
        self.setWindowTitle('DaqViewer')
        
        # QDateEdit widget        
        ## Date Label
        self.label_date= QtWidgets.QLabel(self)
        self.label_date.move(20, 40)
        
        self.dateEdit = QtWidgets.QDateEdit(self)
      
        self.dateEdit.setGeometry(QtCore.QRect(50, 45, 110, 22))
        self.dateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dateEdit.setCalendarPopup(True)
        
        self.today= QtCore.QDateTime.currentDateTime().date()
        self.dateEdit.setDate(QtCore.QDate(self.today))
        
        # Plot button
        self.plot_btn=QtWidgets.QPushButton(self)
        self.plot_btn.setGeometry(QtCore.QRect(200, 200, 110, 22))
        self.plot_btn.clicked.connect(self.plot)
       
    
        self.retranslateUi()
            
    def retranslateUi(self):
         ## Format date
         _translate = QtCore.QCoreApplication.translate
         self.dateEdit.setDisplayFormat(_translate("MainWindow", "dd-MMMM-yyyy"))
         self.label_date.setText(_translate("MainWindow", "Date"))
         self.plot_btn.setText(_translate("MainWindow", "Plot"))
    def plot(self):
        print("hello!")
        Plot_Data(pathname="H:\\NarrowbandData\\Algeria\\2015\\03\\20\\", filename="*150320*NRK_000A.mat")
            
    def showDate(self, date):
#        self.lbl.setText(date.toString())
        print(date.toPyDate())
        
    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyApplication = MainWindow()
    MyApplication.show()
    sys.exit(app.exec_())