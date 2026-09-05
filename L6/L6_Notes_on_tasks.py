#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 17:47:52 2026

@author: apm




----Review on Functions------


funcction --> Box


vorodi ----> bOX ---> Khoroji 


chandin vorodi (hich) ---> BOX (Amaliat) ---> kHOROJI CHnadin ya hichi 



khoroji ba print motefavet hast




structure


def name(vorodi1,vorodi2,...):
    operation
    dastoorat ro mizari
    print(....)
    return vvariable



"""



def jam(a,b):
    c = a + b
    return c


zarf = jam(10,20)



'''

aval --> define beshe --> runesh koni --> ta beshname tabeye jam ro

dovom -> call --> use beshe estefade beshe


paramter --> a, b 
call --> argument (adad) ---> seda zad emishe ejra mishe


4 no tabe
1- na vorodi na khoroji
2- vorodi dare khoroji nadare
3- vorodi nadare khoorji dare
4- ham vorodi ham khoroji (in takmil tarine)



'''

def information(name,country):
    print('salam')
    print(name)
    print('az')
    print(country)
    
    
#call --> tedad argument --> ba paramtere tabe yeksan bashe

#2 ta vorodie, 2 ta bedi na kamtar na bsihtr

#information('ali','iran',30)   --> error
#information('ali') --> error
information('ali','iran')


#agar yek vorodi dadi , moshkel nakhore rrror nade
#bajye dovomin vborodi yek adadi pish farz vrdre

def information(name,country='iran'):
    print('salam')
    print(name)
    print('az')
    print(country)
    
    
    
#-----vorodi ha ----------
#harchizi bashe

#adad bashe

def jam(numb1,numb2):
    javab = numb1 + numb2
    return javab

zarf = jam(numb1=10 , numb2=20)
zarf = jam(10,20)
    
#dota vorodi dahstam--> dotasham adad bod (int,float,...)

#list o dictionaruy?


def information(users):
    count=0
    for user in users:
        if 'a' in user:
            count = count + 1
    
    return count
    


my_users=['ali','vahid','hamid','reza']

zarf = information(my_users)



#list migire --> adad pas mide

print(zarf) #4


zarf = information(['ali','vahid','hamid','reza'])




#----dictionaruy?

#fictionary- -->box --> string

def find_phone(user):
    phone = user['phone']
    return phone
    



dict1 = {'name':'ali','sen':30 , 'phone':'091200000'}

my_phone = find_phone(dict1)

print(my_phone)


#listi az dcitionary

my_users = [{'name':'ali','sen':30 , 'phone':'091200000'},
            {'name':'vahid','sen':40 , 'phone':'091300000'},
            {'name':'reza','sen':50 , 'phone':'091400000'}]


#bere listi az dictionary begrie --> jame senashono bede --> yek adad pas 

#list(dictioanry___. number)

def total_age_of_users(users):
    total = 0 
    for user in users:
        total = total + user['sen']
        
        
    return total


my_total = total_age_of_users(my_users)

print(my_total) #120




#local --<> dar tabe har zarfi ssakhte mishe --> movaghat hast va bironesh tarif shod nist
#global --> ooanei k brion az tabe hastan hame ja tarif shodan


#esm bebini tooye yek list hast ya nist

#yek tabe -< listi az asami vorodi1 , vorodi 2 esm

#tabe bayad khoroji --> Boolean (True , False)


def find_by_name(users,username):
    
    if username in users:
        return True
    else:
        return False
    
    
result = find_by_name(users=['ali','vahid','hamid'] ,username='ali' )

print(result) #True


result = find_by_name(users=['ali','vahid','hamid'] ,username='mohsen' )
print(result) #False

#2 vorodi (list, str) ---> Booleaan


#------chandin khoroji dahst ebashid

def operation(a,b):
    
    c = a + b
    
    d = a - b
    
    return c

zarf = operation(40,20)
    
print(zarf) #60

#2 vorodi ---> 1 khorji


# 2 vorodi --> 2 khjorji


def operation(a,b):
    
    c = a + b
    
    d = a - b
    
    return c , d

#@ 2 vorodi , 2 khoroji

#operation(a=20 , b = 20)

zarf = operation(20 , 20)
#yedone

print(type(zarf)) #<class 'tuple'>
print(zarf) #(40, 0)


#unpackingh


kh1 , kh2 = operation(20 , 20)

print(kh1) #40
print(kh2) #0


t , k = operation(20,20)


result , yekchize_digar = operation(40,50)

print(result) #90

print(yekchize_digar) #-10




#----------Nokteye payani-------
#tamame tavabe ro ziba benevsiid


#name e function --> bayad yekchizi bashe ke ba esmesh malom bashse che mikonad

#def jam_va_tafrigh

#vrariable , moteghayer ha --> a, b 

def jam_va_taghsim(numb1,numb2):
    
    javabe_jam = numb1 + numb2
    
    javabe_tafrigh = numb1  - numb2
    
    return javabe_jam , javabe_tafrigh



#mitoni type hint dashte bashi
#begi k har vorodie tabe behtre az chi bashe3
#in error nmide --> balke komak mikoen onkasi ketabe ro mikhone sue kon

int
float
complex
list
set
tuple
dict




def jam_va_taghsim(numb1: float ,numb2 : float) -> float:
    javabe_jam = numb1 + numb2
    
    javabe_tafrigh = numb1  - numb2
    
    return javabe_jam 


#docstring benevisid

def jam_va_taghsim(numb1: float ,numb2 : float) -> float:
    '''
    in chie va chi nist
    
    Parameters
    ----------
    numb1 : float
        adade avalinadadi ke kmikahhid
    numb2 : float
        dovomin adadi k mikhahid.

    Returns
    -------
    float
        jame do adadi ke bvared kardid rsa midahad.

    '''
    javabe_jam = numb1 + numb2
    
    javabe_tafrigh = numb1  - numb2
    
    return javabe_jam 


#jam_va_tafrigh(numb1,numb2)

#===========================================
#===========================================
#===========================================
#===========================================
#===========================================
#===========================================
#===========================================


#numb1 , numb2 , operation vorodi -->tabe --> khoroji --> adad (result)

#az user begire
#numb1 = input('numb 1 ro bede:')
#numb1 = input('numb 1 ro bede:')



#kari ba user nadarim, makhsosa taska 20 ta attaks input 


#tabe besaz k in bashe vorodi hash

def calculator(numb1,numb2,operation):
    if operation=='jam':
        result = numb1 + numb2
        return result
    #elif
    else:
        return None




#donaye vaghei code mzini --> az tabe bejaye tekrar esteafde koni
#yejaei az codet, input ,...

zarf = calculator(10,20,'jam')



#user kari kone

#yejori az library --> migiri ---> zarf1,zarf2,zaerf3

#zarf = calculator(numb1=zarf1,numb2=zarf2,operation=zarf3)


zarf1 = float(input('numb1:'))
zarf2 = float(input('numb2:'))
operation = input('kodam operation:')


calculator(zarf1,zarf2, operation)


#khodet mziani -> developing (tose e dsadan)
#az user migiri (fast api / django)
#input migiri , cli ,....

#oon vorodisho migire

#def name(vorodi1,....)





def login():
    username = input('useername:')
    password = input('password:')
    
    while username!='admin' or password!='admin':
        print('ghalat mibashad')
        username = input('useername:')
        password = input('password:')
        
    print('Login successfully')
    
    
    
login()
        




