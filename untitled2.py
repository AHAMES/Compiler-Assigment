# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:22:57 2019

@author: Ahmed
"""

import pandas
x=pandas.read_excel("New Microsoft Excel Worksheet.xlsx")
parseMap={}
for i in x:
    if i=='Nonterminal':
        continue
    print ',\''+str(i)+'\''
    for j in x[i]:
        if not (pandas.isnull(j)):
            split=j.split('->')
            if (str(i) not in parseMap):
                
                parseMap[i]={}
                
            
            #parseMap[str(i)][str(split[0])]=str(split[1].split(' ')[-1:0])
        
        