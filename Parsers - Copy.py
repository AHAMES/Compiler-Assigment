# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 11:52:16 2019

@author: Ahmed
"""

#Grammar
"""
P -> Mc Classdec
Classdec -> Classdef Classdec
Classdec -> Classdef
Classdec -> ''
Classdef -> Class Id Extending { Vardec Methoddec }
Mc -> Class Id { Public Static Void Main ( String [] Id ) { Stat } }
Vardec -> Vardef Vardec
Vardec -> Vardef
Vardec -> ''
Methoddec -> Methoddef Methoddec
Methoddec -> Methoddef
Methoddec -> ''
Vardef -> TypeId ;
Methoddef -> public Type Id ( Params ) { Vardec Stats return Exp ; }
Type -> int []
Type -> boolean
Type -> int
Stats -> Stat Stats
Stats -> Stat
Stats -> ''
Stat -> { Stats }
Stat -> if ( Exp ) Stat else Stat
Stat -> while ( Exp ) Stat
Stat -> System . out . Println ( Exp ) ;
Stat -> Id = Exp ;
Stat -> Id [ Exp ] = Exp ;
Extending -> Extends Id
Extending -> ''
Op -> +
Op -> &&
Op -> <
Op -> +
Op -> -
Op -> *
Exp -> Number A
Exp -> True A
Exp -> False A
Exp -> ID A
Exp -> This A
Exp -> new int [Exp] A
Exp -> new Id ( ) A
Exp -> ! Exp A
Exp -> ( Exp ) A
A -> Op Exp A
A -> [ Exp ] A
A -> . length A
A -> . Id ( Paramst ) A
A -> ''
Id -> String
Params -> int [ ] Id Paramsd
Params -> booleanIdParamsd
Params -> int Id Paramsd
Params -> int [ ] Id
Params -> boolean Id
Params -> int Id
Params -> ''
Paramsd -> , Type Id Paramsd
Paramsd -> ''
Paramst -> Number A Paramstd
Paramst -> True A Paramstd
Paramst -> False A Paramstd
Paramst -> Id A Paramstd
Paramst -> This A Paramstd
Paramst -> new int [ Exp ] A Paramstd
Paramst -> new Id ( ) A Paramstd
Paramst -> ! Exp A Paramstd
Paramst -> ( Exp ) A Paramstd
Paramst ->  ''
Paramstd -> , Exp
Paramstd -> ''
"""


tokens=['(',"4",")"]
parseMap={
        "(":{"Exp":["expD","Term"],"Term":["TermD","Factor"],"Factor":["Exp",'eps']},
        "Number":{"Exp":["expD","Term"],"Term":["TermD","Factor"],"Factor":["Number"]},
        ")":{"expD":["eps"],"TermD":["eps"]},
}
terminal=['(','Number',')','eps']
parseStack=["$","Exp"]
i=0
while(parseStack[-1]!="$") and i != len(tokens):
    currentType=""
    top=parseStack[-1]
    current=tokens[i]
    if(top=='eps'):
        parseStack.pop()
        continue
    if(current.isdigit()==True):
        currentType="Number"
    if (current in parseMap):
        parseStack.pop()
        for j in parseMap[current][top]:
            parseStack.append(j)
        print parseMap[current][top]
        
    if currentType=="Number":
        parseStack.pop()
        
        for j in parseMap[currentType][top]:
            parseStack.append(j)
        print parseMap[currentType][top]
    top=parseStack[-1]    
    if top in terminal:
        parseStack.pop()
        i+=1