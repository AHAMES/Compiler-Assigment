# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:41:25 2019

@author: Ahmed
"""
from PySide2.QtWidgets import QApplication, QLabel
 
app = QApplication([])
label = QLabel("Hello Qt for Python!")
label.show()
app.exec_()