# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 12:41:25 2019

@author: Ahmed
"""
import re

reservedTokens={
        ';':'symbol','.':'symbol','[':'symbol',']':'symbol','(':'symbol',')':'symbol',
        '{':'symbol','}':'symbol','=':'OP','*':'OP','-':'OP','+':'OP','<':'OP','>':'OP',
        '&&':'OP', '==':'OP','int':'Type','String':'Type','boolean':'Type','class':'reserved_word',
        'if':'reserved_word','else':'reserved_word','public':'reserved_word','private':'reserved_word',
        'protected':'reserved_word','return':'reserved_word','void':'reserved_word','main':'reserved_word',
        'static':'reserved_word', 'new':'reserved_word','System.out.println':'reserved_word',
        'while':'reserved_word','extends':'reserved_word','this':'reserved_word', 'false':'reserved_word',
        'true':'reserved_word'
}
def identifiers(inputString):
    newToken=""
    splitPoint=0
    if inputString[0][0]=='S' and inputString[1]!='reserved_word':
        for i in range(0,len(inputString[0])):
            if inputString[0][i]=='.' or str(inputString[0][i]).isalpha()==True:
                newToken+=inputString[0][i]
            else:
                splitPoint=i
                if newToken=='System.out.println':
                    return {'Type':"reserved_word_split",'newToken':newToken,'Split_Point':splitPoint}
    newToken=""
    splitPoint=0          
    if IndentifyTokens(str(inputString[0][0]))=='symbol' and len(inputString[0])>1:
        return {'Type':"_split",'newToken':newToken,'Split_Point':splitPoint}
    elif str(inputString[0][0]).isalpha() and (inputString[1]=='' or inputString[1]=='Identifier'):
        for i in range(0,len(inputString[0])):
            if str(inputString[0][i]).isalpha() or str(inputString[0][i]).isdigit() or inputString[0][i]=='_':
                newToken+=inputString[0][i]
            else:
                splitPoint=i
                return {'Type':"Identifier_split",'newToken':newToken,'Split_Point':splitPoint}
        return{'Type':"Identifier",'newToken':newToken,'Split_Point':0}
    elif str(inputString[0][0]).isdigit() and str(inputString[1])!='Integer':
        for i in range(0,len(inputString[0])):
            if str(inputString[0][i]).isdigit():
                newToken+=inputString[0][i]
            elif str(inputString[0][i]).isalpha():
                newToken="Invalid" 
            else:
                splitPoint=i
                return{'Type':"Integer_split",'newToken':newToken,'Split_Point':splitPoint}
        return{'Type':"Integer",'newToken':newToken,'Split_Point':0}
    else:
        return {'Type':inputString[1],'newToken':"",'Split_Point':0}       


def IndentifyTokens(inputString):
    
    for i in reservedTokens:
        m=False
        if(len(inputString)==len(i)):
            j=0
            m=True
            for c in inputString:
                if i[j]!=c:
                    m=False
                    break
                j+=1
        if m==True:
            return reservedTokens[i]
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

    

def main(File):
    code = open(File, "r")
    Tokens=Tokenization(code)
    size=len(Tokens)
    
    while(True):
        for i in range(0,len(Tokens)):
            identifierResult=identifiers([Tokens[i][0],Tokens[i][1]])
            if 'Invalid' in identifierResult['newToken']:
                Tokens[i][1]='Invalid'
            elif 'split' not in identifierResult['Type']:
                if IndentifyTokens(Tokens[i][0])!='':
                    Tokens[i][1]=IndentifyTokens(Tokens[i][0])
                else:
                    Tokens[i][1]=identifierResult['Type']
            else:
                line=Tokens[i][2]
                symbol=Tokens[i][0][identifierResult['Split_Point']]
                if len(Tokens[i][0])>1 and (symbol=='='):
                    if Tokens[i][0][identifierResult['Split_Point']+1]=='=':
                        symbol+='='
                if len(Tokens[i][0])>1 and(symbol=='&'):
                    if Tokens[i][0][identifierResult['Split_Point']+1]=='&':
                        symbol+='&'
                spliter=Tokens[i][0].split(symbol,1)
                del Tokens[i]
                if spliter[0]=='' and spliter[1]!='':
                    Tokens.insert(i,[symbol,'symbol',line])
                    Tokens.insert(i+1,[spliter[1],"",line])
                elif spliter[1]=='' and spliter[0]!='':
                    Tokens.insert(i,[spliter[0],identifierResult['Type'].replace("_split",""),line])
                    Tokens.insert(i+1,[symbol,'symbol',line])
                else:
                    Tokens.insert(i,[spliter[0],identifierResult['Type'].replace("_split",""),line])
                    Tokens.insert(i+1,[symbol,'symbol',line])
                    Tokens.insert(i+2,[spliter[1],"",line])
        if(size!=len(Tokens)):
            size=len(Tokens)
        else:
            break
    return Tokens
#for token in Tokens:
    
res=main('Code.txt')