# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:41:25 2019

@author: Ahmed
"""

code = open("Code.txt", "r")
import re

def identifiers(inputString):
    newToken=""
    splitPoint=0
    if str(inputString[0][0]).isalpha() and (inputString[1]=='' or inputString[1]=='Identifier'):
        for i in range(0,len(inputString[0])):
            if str(inputString[0][i]).isalpha() or str(inputString[0][i]).isdigit() or inputString[0][i]=='_':
                newToken+=inputString[0][i]
            else:
                splitPoint=i
                return [True,newToken,splitPoint]
        return [True,newToken,splitPoint]
    elif str(inputString[0][0]).isdigit() and str(inputString[1])!='integer':
        for i in range(0,len(inputString[0])):
            if str(inputString[0][i]).isdigit():
                newToken+=inputString[0][i]
            else:
                splitPoint=i
                return[False,newToken,splitPoint]
    else:
        return [False,"",0]       

def integerLiteral(inputString):
    if inputString.isdigit():
        return True
    return False 
def binaryOperation(inputString):
    if inputString=='=':
        return True
    if inputString=='*':
        return True
    if inputString=='-':
        return True
    if inputString=='+':
        return True
    if inputString=='<':
        return True
    if inputString=='>':
        return True
    if inputString=='&&':
        return True
    return False

def symbols(inputString):
    if inputString==';':
        return True
    if inputString=='.':
        return True
    if inputString=='[':
        return True
    if inputString==']':
        return True
    if inputString=='(':
        return True
    if inputString==')':
        return True
    if inputString=='{':
        return True
    if inputString=='}':
        return True
    return False    

def reservedWord(inputString):
    clas='class'
    iff='if'
    lse='else'
    pub='public'
    pri='private'
    prot='protected'
    ret='return'
    vod='void'
    stat='static'
    man='main'
    nw='new'
    j=0
    m=True
    if(len(inputString)==len(clas)):
        for i in inputString:
            if clas[j]!=i:
                m=False
                break
            j+=1
        if m==True:
            return m
    if(len(inputString)==len(iff)):
        j=0
        m=True
        for i in inputString:
            if iff[j]!=i:
                m=False
                break
            j+=1
        if m==True:
            return m
    if(len(inputString)==len(lse)):
        j=0
        m=True
        for i in inputString:
            if lse[j]!=i:
                m=False
                break
            j+=1
        if m==True:
            return m 
    if(len(inputString)==len(pub)):
        j=0
        m=True
        for i in inputString:
            if pub[j]!=i:
                m=False
                break
            j+=1
        if m==True:
            return m
    if(len(inputString)==len(pri)):
        j=0
        m=True
        for i in inputString:
            if pri[j]!=i:
                m=False
                break
            j+=1
        if m==True:
            return m
    if(len(inputString)==len(prot)):
        j=0
        m=True
        for i in inputString:
            if prot[j]!=i:
                m=False
                break
            j+=1
        if m==True:
            return m
    if(len(inputString)==len(ret)):
        j=0
        m=True
        for i in inputString:
            if ret[j]!=i:
                m=False
                break
            j+=1
        if m==True:
            return m
    if(len(inputString)==len(vod)):
        j=0
        m=True
        for i in inputString:
            if vod[j]!=i:
                m=False
                break
            j+=1
        if m==True:
            return m  
    if(len(inputString)==len(vod)):
        j=0
        m=True
        for i in inputString:
            if vod[j]!=i:
                m=False
                break
            j+=1
        if m==True:
            return m
    if(len(inputString)==len(stat)):
        j=0
        m=True
        for i in inputString:
            if stat[j]!=i:
                m=False
                break
            j+=1
        if m==True:
            return m
    if(len(inputString)==len(man)):
        j=0
        m=True
        for i in inputString:
            if man[j]!=i:
                m=False
                break
            j+=1
        if m==True:
            return m
    if(len(inputString)==len(nw)):
        j=0
        m=True
        for i in inputString:
            if nw[j]!=i:
                m=False
                break
            j+=1
        if m==True:
            return m
    return False

def dataType(inputString):
    integ='int'
    strin='String'
    boole='boolean'
    j=0
    m=True
    if(len(inputString)==len(integ)):
        for i in inputString:
            if integ[j]!=i:
                m=False
                break
            j+=1
        if m==True:
            return m
    if(len(inputString)==len(strin)):
        j=0
        for i in inputString:
            if strin[j]!=i:
                m=False
                break
            j+=1
        if m==True:
            return m
    if(len(inputString)==len(boole)):
        j=0
        for i in inputString:
            if boole[j]!=i:
                m=False
                break
            j+=1
        if m==True:
            return m
    return False   
    
def IndentifyTokens(inputString):
    if symbols(inputString)==True:
        return "symbol"
    elif dataType(inputString)==True:
        return "Type"
    elif reservedWord(inputString)==True:
        return "reserved_word"
    elif binaryOperation(inputString)==True:
        return "OP"
    elif integerLiteral(inputString)==True:
        return "integer"
    else:
        return ""
    
def Tokenization(code):
    codeLines=code.read().splitlines()
    filteredTokens=[]
    comment=False
    line=1
    for i in codeLines:
        line_tokens = re.split(' |\t',i)
        for j in range(0,len(line_tokens)):
            if ('//' in line_tokens[j]) :
                if(line_tokens[j][0]!='/'):
                    
                    x=line_tokens[j].split('//',1)
                    filteredTokens.append(['//'+x[1],"Comment",line])
                else:
                    filteredTokens.append([line_tokens[j],"Comment",line])
                comment=True
            elif (len(line_tokens)==1 and line_tokens[j]==''):    
                break
            elif(comment==True):
                filteredTokens.append([line_tokens[j],"Comment",line])
            elif line_tokens[j]!='':
                filteredTokens.append([line_tokens[j],IndentifyTokens(line_tokens[j]),line])
                
                    
        comment=False
        line+=1
    comment=False
    Tokens=[]
    for i in range(0,len(filteredTokens)):
        if '/*' in filteredTokens[i][0]:
            if(filteredTokens[i][0]!='/'):
                x=filteredTokens[i][0].split('/*')
                Tokens.append(['/*'+x[1],"Comment",filteredTokens[i][2]])
            comment=True
        elif comment==True:
            Tokens.append([filteredTokens[i][0],"Comment",filteredTokens[i][2]])
        if comment==False:
            if(filteredTokens[i][1]!='Comment'):
                Tokens.append([filteredTokens[i][0],filteredTokens[i][1],filteredTokens[i][2]])
            else:
                Tokens.append([filteredTokens[i][0],"Comment",filteredTokens[i][2]])
        if '*/' in filteredTokens[i][0]:
            comment=False
    return Tokens

    


Tokens=Tokenization(code)
size=len(Tokens)

while(True):
    for i in range(0,len(Tokens)):
        x=identifiers([Tokens[i][0],Tokens[i][1]]) 
        if x[0]==False and (Tokens[i][1]==""):
            Tokens[i][1]='Invalid'
            m=Tokens[i][0].split(Tokens[i][0][x[2]],1)
            if(len(m[1])>0 and (str(x[1]).isdigit())==False):
                symbol=Tokens[i][0][x[2]]
                line=Tokens[i][2]
                del Tokens[i] #delete the old token
                Tokens.insert(i,[symbol,IndentifyTokens(symbol),line]) #add the splitting symbol
                if(m[1]!=''):
                    Tokens.insert(i+1,[m[1],"Identifier",line]) #add new token to the mix
            elif(len(m[1])>0 and (str(x[1]).isdigit())==True):
                if(len(m[1])>0 and (str(Tokens[i][0][x[2]]).isdigit())==False):
                    symbol=Tokens[i][0][x[2]]
                    line=Tokens[i][2]
                    del Tokens[i] #delete the old token
                    Tokens.insert(i,[x[1],"integer",line]) #add new token to the mix
                    Tokens.insert(i+1,[symbol,'symbol',line]) #add the splitting symbol
                    if(m[1]!=''):
                        Tokens.insert(i+2,[m[1],IndentifyTokens(m[1]),line])
                    
        elif x[0]==False and (Tokens[i][1]=="Identifier"):
            if IndentifyTokens(Tokens[i][0][0])=="symbol":
                m=Tokens[i][0].split(Tokens[i][0][x[2]],1)
                if(len(m[1])>0 and ~(str(Tokens[i][0][x[2]]).isdigit())):
                    symbol=Tokens[i][0][x[2]]
                    line=Tokens[i][2]
                    del Tokens[i] #delete the old token
                    Tokens.insert(i,[symbol,'symbol',line]) #add the splitting symbol
                    Tokens.insert(i+1,[m[1],"Identifier",line]) #add new token to the mix
        elif x[0]==False and str(x[1]).isdigit():
            m=Tokens[i][0].split(Tokens[i][0][x[2]],1)
            if(len(m[1])>0 and (str(Tokens[i][0][x[2]]).isdigit())==False):
                    symbol=Tokens[i][0][x[2]]
                    line=Tokens[i][2]
                    del Tokens[i] #delete the old token
                    Tokens.insert(i,[x[1],"integer",line]) #add new token to the mix
                    Tokens.insert(i+1,[symbol,'symbol',line]) #add the splitting symbol
                    if(m[1]!=''):
                        Tokens.insert(i+2,[m[1],IndentifyTokens(m[1]),line])
        else:
            if x[2]==0 and Tokens[i][1]=="":
                Tokens[i][1]='Identifier'
            elif x[2]!=0 and (Tokens[i][1]=="" or Tokens[i][1]=="Identifier") :
                m=Tokens[i][0].split(Tokens[i][0][x[2]],1) #take the splited part
                symbol=Tokens[i][0][x[2]]
                line=Tokens[i][2]
                del Tokens[i] #delete the old token
                Tokens.insert(i,[x[1],"Identifier",line]) #add new token to the mix
                Tokens.insert(i+1,[symbol,IndentifyTokens(symbol),line]) #add the splitting symbol
                if(m[1]!=''):
                    Tokens.insert(i+2,[m[1],IndentifyTokens(m[1]),line])
            else:
                continue
    if(size!=len(Tokens)):
        size=len(Tokens)
    else:
        break
#for token in Tokens:
    
