# -*- coding: utf-8 -*-
'''
Author: Ahmed Ammar, ahmed.ammar@fst.utm.tn
Purpose: - - - 
Inputs: - - -
Outputs:  - - -
Date Created: Tue Mar 27 11:48:12 2018
Date Modified: M D, Y
Date Released: M D, Y
Versions:
    V0.01: ---
    
'''
import glob
import shutil
for ii in range(1,31):
    dd= str('{:02d}'.format(ii))
    
    FileList=glob.glob("H:/NarrowbandData/Tunisia/2017/09/"+ dd+ "/*DHO*A.mat")
    dest_dir="H:/NarrowbandData/Tunisia/2017/09/DHO"
    for filename in FileList:
        print(filename)
        shutil.copy(filename, dest_dir)