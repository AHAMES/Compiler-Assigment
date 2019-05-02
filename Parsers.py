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
parseMap={"class":{"P":["Classdec","Mc"],
                   'Classdec':["ClassdecD","Classdef"],
                   'ClassdecD':["ClassdecD","Classdef"],
                   'Classdef':["}",'Methoddec','VardecM',"{",'Extending','Id','class'],
                   'Mc':['}','}','Stat','{',')','Id',']','[','String','(','main','void','static','public','{','Id','class'],
                   'VardecM': [''],
                  },
          
         'Id':{'VardecM':['Vardec'],
               'Vardec':['Vardec','Vardef'],
               'Vardef':['Id','Type'],
               'Type':['Id'],
               'TypeA':[''],
               'Stats':['StatsD', 'Stat'],
               'StatsD': [ 'StatsD','Stat'],
               'Stat':['B','Id'],
               'Exp':['A','Id'],
               'C':['A',')','(','Id'],
               'D':['A',')','Paramst','(','Id'],
               'E':['Paramsd','Id'],
               'F':['G','Id'],
               'H':['I','Id'],
               'Paramst':['Paramstd','A','Id'],
               'J':['Paramstd','A',')','(','Id']},
          
          "{":{
               'Stats':["StatsD","Stat"],
               'StatsD':['StatsD','Stat'],
               'Stat':['}','Stats','{'],
               'Extending':[""]},     
          
          "}":{
           'VardecM':[''],
           'Methoddec':[''],
           'MethoddecD':[''],
           'Stats':[''],
           'StatsD':['']},     
          
          "(":{'Exp':['A',')','Exp','('],
           'Paramst':['Paramstd','A',')','Exp','(']},
          
          "[":{'TypeA':[']','['],
               'B':[';','Exp','=',']','Exp','['],
               'A':['A',']','Exp','['],
               'E':['F',']','[']},    
          
          "]":{'A':['']},
           
          ")":{"A":[''],
               'Params':[''],
               "G":["Paramsd"],
               "I":['Paramsd'],
               'Paramsd':[''],
               'Paramst':[""],
               "Paramstd":['']},
         
        ';':{'A':[''],},
        
        'public':{'VardecM': [''],
                  'Methoddec':['MethoddecD','Methoddef'],
                  'MethoddecD':['MethoddecD','Methoddef'],
                  'Methoddef':['}',';','Exp','return','Stats','Vardec','{',')','Params','(','Id','Type','public']},
                  
        'return':{
                  'Stats':[''],
                  'StatsD':['']},
                  
        'int':{
               'VardecM' :['Vardec'],
               'Vardec' :['VardecD','Vardef'],
               'Vardef':[';','Id','Type'],
               'Type':['TypeA','int'],
               'C':['A',']','Exp','[','int'],
               'Params':['E','int'],
               'J':['Paramstd','A',']','Exp' ,'[','int']},
               
        'boolean':{
               'VardecM' :['Vardec'],
               'Vardec' :['VardecD','Vardef'],
               'Vardef':[';','Id','Type'],
               'Type':['boolean'],
               'Params':['H','boolean']},
                
        'if':{
            'Stats':["StatsD","Stat"],
            'StatsD':['StatsD','Stat'],
            'Stat':['Stat','else','Stat',')','Exp','(','if'],
            },
                
        'while':{
                'Stats':["StatsD","Stat"],
                'StatsD':['StatsD','Stat'],
                'Stat':['Stat',')','Exp','(','while']
            },
        
        'System':{
                'Stats':["StatsD","Stat"],
                'StatsD':['StatsD','Stat'],
                'Stat':[';',')','Exp','(','println','.','out','.','System'],  
            },
                
        '.':{'A':['.','D']},
               
        '=':{'B':[';','Exp','=']},  
        
        'extends':{'Extending':['Id','extends']},
        
        '+':{
            'OP':['+'],
            'A':['A','Exp','OP']
            },
         
        '&&':{
            'OP':['&&'],
            'A':['A','Exp','OP']
            },
        
        '<':{
            'OP':['<'],
            'A':['A','Exp','OP']
            },
        
        '-':{
            'OP':['-'],
            'A':['A','Exp','OP']
            },
        
        '*':{
            'OP':['*'],
            'A':['A','Exp','OP']
            },
        
        'Integer':{
            'Exp':['A','Integer'],
            'Paramst':['Paramstd','A','Integer']
            },
        
        'true':{
            'Exp':['A','true'],
            'Paramst':['Paramstd','A','true']
            },   
        
        'false':{
            'Exp':['A','false'],
            'Paramst':['Paramstd','A','false']
            },   
        
        'this':{
            'Exp':['A','this'],
            'Paramst':['Paramstd','A','this']
            },
        
        'new':{
            'Exp':['C','new'],
            'Paramst':['J','new']
            },
        
        '!':{
            'Exp':['A','Exp','!'],
            'Paramst':['Paramstd','A','Exp','!']
            },
        
        'length':{
            'D':['A','length']
            },
        ',':{
            'A':[''],
            'G':['Paramsd'],
            'I':['Paramsd'],
            'Paramsd':['Paramsd','Id','Type',','],
            'Paramstd':{'Exp',','},
            },
}
terminal=['class','{','}','public','static','void','main','(','String','[',']',')',';','public','return','int','boolean','id','if','else','while','System','.','out'
          ,'println','=','Extends','+','&&','<','-','*','Number','True','False','This','new','!','length','identifier',',']
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