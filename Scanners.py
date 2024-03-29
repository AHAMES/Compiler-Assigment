# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:41:25 2019

@author: Ahmed
"""
import re
from Tkinter import *
from MultiList import *
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
        return "Id"
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
                mlb.insert(END, (str(token[3]),str(token[1]), token[0], token[2]))
                number+=1
        line+=1
        
    return tokens

def main():
    global tokens
    code = codeText.get('1.0','end')
    mlb.delete(0,END)
    x=Tokenise(code)
    tokens=x
#for token in Tokens:
tokens=[]
root = Tk()
codeFrame= Frame(root)

resultsFrame=Frame(root)
title=Label(resultsFrame,text='Tokens')
title.configure(background='#4D4D4D',foreground='#FFFFFF')
tokensFrame1=Frame(resultsFrame)
#tokensList1=Listbox(tokensFrame1,height=27,width=51)
codeText = Text(codeFrame,width=100)
codeText.configure(insertbackground='#FFFFFF',background='#4D4D4D',foreground='#FFFFFF')

compileButton = Button(root,text='Compile Code',width=38,font=('Helvetica', '20'),command=main)
compileButton.configure(background='#4D4D4D',foreground='#FFFFFF')
mlb = MultiListbox(tokensFrame1, (('Line', 10,25),('Number', 10,25), ('Token', 15,25), ('Identification', 15,25)))
mlb.pack(fill='both', expand=1)
resultsFrame.pack(side=RIGHT)
title.pack(side=TOP,fill=X)
tokensFrame1.pack(side=RIGHT)       
codeFrame.pack(fill=BOTH)
codeText.pack(fill=BOTH)
compileButton.pack(fill=BOTH,side=BOTTOM)

root.mainloop()