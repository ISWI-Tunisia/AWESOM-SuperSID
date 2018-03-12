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

from PyQt5 import QtWidgets, QtCore
from SitesInfo import Rx_sites
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.initUI()
        
        
        
    def initUI(self):
        """
        Widgets & proprieties 
        """
        # Window proprieties
        ## Size
        self.resize(500, 300)
        self.setMinimumSize(QtCore.QSize(500, 300))
        self.setMaximumSize(QtCore.QSize(500, 1000))
        ## Title
        self.setWindowTitle('DaqViewer')
        
        # QDateEdit widget
        self.dateEdit = QtWidgets.QDateEdit(self)
        self.dateEdit.move(20, 20)
        
        self.dateEdit.setGeometry(QtCore.QRect(20, 20, 110, 22))
        self.dateEdit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.dateEdit.setCalendarPopup(True)
        
        self.today= QtCore.QDateTime.currentDateTime().date()
        self.dateEdit.setDate(QtCore.QDate(self.today))
        ## Format date
        _translate = QtCore.QCoreApplication.translate
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "dd-MMMM-yyyy"))
        ## Select date 
        date= self.dateEdit.date()
        self.dateEdit.dateChanged[QtCore.QDate].connect(self.showDate)
        #TODO:
        # Receivers Sites Names : Prepare for station selction!
        print(Rx_sites)
        k=[key for key in Rx_sites]
        print(k)
            
        for key in Rx_sites:
            print(Rx_sites[key])
            
    def showDate(self, date):     
        
#        self.lbl.setText(date.toString())
        print(date.toPyDate())
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MyApplication = MainWindow()
    MyApplication.show()
    sys.exit(app.exec_())