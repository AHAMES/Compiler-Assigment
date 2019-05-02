# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:45:43 2019

@author: Ahmed
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:41:25 2019

@author: Ahmed
"""
import re
from PyQt5.QtWidgets import QApplication, QLabel, QTableWidget,QPushButton,QHBoxLayout,QVBoxLayout,QWidget,QTextEdit,QTableWidgetItem


reservedTokens={
        ';':'symbol',',':'symbol','.':'symbol','[':'symbol',']':'symbol','(':'symbol',')':'symbol','{':'symbol',
        '}':'symbol','"':'symbol',"'":'symbol','=':'OP','*':'OP','-':'OP','+':'OP','<':'OP','>':'OP',
        '&&':'OP', '!':'OP','int':'Type','String':'Type','boolean':'Type','class':'reserved_word',
        'if':'reserved_word','else':'reserved_word','public':'reserved_word',
        'return':'reserved_word','void':'reserved_word','main':'reserved_word',
        'static':'reserved_word', 'new':'reserved_word','System':'reserved_word','while':'reserved_word',
        'extends':'reserved_word','this':'reserved_word', 'false':'reserved_word','true':'reserved_word',
        '/*':'Comment','//':'Comment','*/':'Comment'
}
        
def identifiers(inputString):
    if len(inputString)==0:
        return ""
    elif str(inputString[0]).isalpha()==False and str(inputString[0]).isdigit()==False or inputString[0]=='_':
        return "Invalid"
    elif (str(inputString[0]).isalpha()):
        for i in range(0,len(inputString)):
            if str(inputString[i]).isalpha() or str(inputString[i]).isdigit() or inputString[i]=='_':
                continue
            else:
                return "Invalid"    
        return "Identifier"
    elif str(inputString[0]).isdigit():
        for i in range(0,len(inputString)):
            if str(inputString[i]).isdigit():
                continue
            elif str(inputString[i]).isalpha() or inputString[i]=='_':
                return "Invalid"
              
        return "Integer"
            
def IndentifyTokens(inputString):
    
    for i in reservedTokens:
        if(len(inputString)==len(i) and i in inputString):
            return reservedTokens[i]   
    ID=identifiers(inputString)
    if ID!="":
       return ID
    return ""        
def addSpaces(codeLines):
    newLines=[]
    
    comment=False
    for i in codeLines:
        newString=''
        j=0
        while (j!=len(i)):
            ID=IndentifyTokens(i[j])
            if len(i)>1 and j<=(len(i)-2) and (i[j]=='*' and i[j+1]== '/'):
                newString+=(" "+i[j]+i[j+1]+" ")
                comment=False
                j+=1
            elif  comment==True:
                j+=1
                continue
            elif ID=='symbol':
                newString+=(" "+i[j]+" ")
            elif len(i)>1 and (ID=='OP' or i[j]=='&'):
                if (j+1)==len(i):
                    newString+=(" "+i[j]+" ")
                elif (i[j] == i[j+1]):
                    j+=1
                    newString+=(" "+i[j]+i[j]+" ")
                else:
                    newString+=(" "+i[j]+" ")
            elif (len(i)>1 and j<=(len(i)-2) and (i[j+1]=='*' and i[j]== '/')):
                    newString+=(" "+i[j]+i[j+1]+" ")
                    comment=True
                    j+=1
            elif (len(i)>1 and j<=(len(i)-2) and (i[j+1]=='/' and i[j]== '/')):
                newString+=(" "+i[j]+i[j+1]+" ")
                break
            else:
                newString+=i[j]
            j+=1
        newLines.append(newString)  
    return newLines
def Tokenise(code):
    
    codeLines=code.splitlines()
    codeLines=addSpaces(codeLines)
    line=1
    number=0
    token=[]
    tokens=[]
    for i in codeLines:
        if i=='':
            line+=1
            continue
        line_tokens = re.split(' |\t',i)
        for j in line_tokens:
            if j=='':
                continue
            else:
                tokenID=IndentifyTokens(j)
                token=[j,number,tokenID,line]
            if (len(token[0])!=0):
                tokens.append(token)
                tokenTable.insertRow(number)
                tokenTable.setItem(number , 0, QTableWidgetItem(str(token[3])))
                tokenTable.setItem(number , 1, QTableWidgetItem(str(token[1])))
                tokenTable.setItem(number , 2, QTableWidgetItem(token[0]))
                tokenTable.setItem(number , 3, QTableWidgetItem(token[2]))
                number+=1
        line+=1
        
    return tokens

def main():
    global tokens
    tokenTable.clearContents()
    count=tokenTable.rowCount()+1
    for i in range(0,count):
        tokenTable.removeRow(i)
    code=text.toPlainText()
    x=Tokenise(code)
    tokens=x
#for token in Tokens:
tokens=[]

app = QApplication([])
Appwindow = QWidget()
Appwindow.resize(1200,500)
Compiler=QHBoxLayout()

TextEditor=QVBoxLayout()
text=QTextEdit()
compilerBTN=QPushButton("Compile Code")
compilerBTN.clicked.connect(main)
TextEditor.addWidget(text)
TextEditor.addWidget(compilerBTN)

Result=QVBoxLayout()
label=QLabel("Tokens")
tokenTable=QTableWidget()
tokenTable.setColumnCount(4)
tokenTable.setHorizontalHeaderLabels(['Line','Number',"Token","ID"])
Result.addWidget(label)
Result.addWidget(tokenTable)

Compiler.addLayout(TextEditor,2)
Compiler.addLayout(Result,1)
Appwindow.setLayout(Compiler)
Appwindow.show()
app.exec_()