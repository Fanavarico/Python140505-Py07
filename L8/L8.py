"""
Created on Fri Sep 25 15:08:19 2026

3 Mehrmah 1405

@author: Ali Pilehvar Meibody


------- L8 ----------------

FUnciton
package , import
standard library python
External library


"""

#==================================================
'''

Functions ---> advanced topic

L6 , review on 20 task , L7 , Doshanbe


vorodi ---> BOX ---> khoroji

v1,2,... --> bOX --0> kh1,kh2,kh3

def name(v1,v2,...):
    logic
    return kh1,kh2


default sazi anajm bdi

jam(10,20) #positional argumen t
jam(numb1=10,numb2=20) #keyword arguments


tamame variable ha dakhele tab elocal hastand -->
nokate ziadi 

type hint, clean benevsiid 




vorodi -> int, float, list ,.....

L7 --> my_sum() my_len() my_max() my_min() find_freqeunt()




'''
def my_sum(mylist):
    total = 0 
    for number in mylist:
        total = total + number
        
    return total

# list --> BOX --> adad


mylist=[10,20,30,40,50]

my_sum(mylist) #Out[2]: 150


#1 parameter , 1 argument list bashe


#chandind parameter

#chandin adad bedi , hamaro jam kone baham
my_sum(10,20,30,40,50,60,70)

#def my_sum(num1,num2,num3,):
    
#man baayd taein konam
    

#harchegahdr k khastiii

#*arg
#staro --> vasl mikoni be numb

def my_sum(*numb):
    print(type(numb))
    print('---------')
    print(numb)  



my_sum(10,20,30)

'''
<class 'tuple'>
---------
(10, 20, 30)

'''


#pas man mitonam kari konam ke tabe am binahyat adad begiure
#positonal argument begire
#meghdar haro --> toye yek tuple mirize (zarf)
#mitonm azash estefade konm



def my_sum(*numbs):
    total = 0
    for numb in numbs:
        total = total + numb
        
    return total
        
#in tabe yek vorodi nemigire


#positional arguments
my_sum(10,20,30,40,50,60,70,80,90,100)

#Out[6]: 550




#-------

def information_processor(my_dict):
    new_age = my_dict['sen'] + 40
    return new_age


my_dict={'sen':30,'name':'ali'}

information_processor(my_dict) #Out[8]: 70

information_processor(sen=30,name='ali')

def information_processor(sen,name):
    new_age = my_dict['sen'] + 40
    return new_age

information_processor(sen=30,name='ali',phone='019')

#binahayat keyword begire tabam

    

#keywordi
#**kwarg

def information_processor(**my_dict):
    new_age = my_dict['sen'] + 40
    return new_age

    
information_processor(name='ali',sen=30,phone='0199',city='tehran',country='iran')

#binahayat keyword argument begire




#..
def information_processor(name,sen,**my_dict):
    new_age = my_dict['sen'] + 40
    return new_age





#------------------------------------------

'''
1- yek dictionary aZ mahsoolat darim 

products = {
'laptab': 1200,
'phone': 800,
'tablet': 500,
'headphone': 150,
'mouse': 50
}


- dictionary ---> BOX --> adad: bishtarin gheymat

'''
#def find_max_in_dict
products = {
'laptab': 1200,
'phone': 800,
'tablet': 500,
'headphone': 150,
'mouse': 50
}

for product in products:
    print(product)

'''
laptab
phone
tablet
headphone
mouse
'''
products = {
'laptab': 1200,
'phone': 800,
'tablet': 500,
'headphone': 150,
'mouse': 50
}

for product in products.keys():
    print(product)
'''
laptab
phone
tablet
headphone
mouse
'''

for product in products.values():
    print(product)

'''
1200
800
500
150
50
'''


#key , value

for product,price in products.items():
    print(product)
    print(price)
'''

laptab
1200
phone
800
tablet
500
headphone
150
mouse
50

'''


chiz = products.keys()
chiz[0] #TypeError: 'dict_keys' object is not subscriptable
print(chiz) #dict_keys(['laptab', 'phone', 'tablet', 'headphone', 'mouse'])

list(chiz) #Out[17]: ['laptab', 'phone', 'tablet', 'headphone', 'mouse']
list(chiz)[0] #Out[18]: 'laptab'
products[list(chiz)[0]] #Out[19]: 1200



products.values()

list(products.values()) #Out[20]: [1200, 800, 500, 150, 50]
list(products.values())[0] #Out[21]: 1200



def find_max_value_in_products(products):
    products_values = list(products.values()) # [1200, 800, 500, 150, 50]
    max_value = products_values[0]
    for value in products_values:
        if value>=max_value:
            max_value = value
            
    return max_value
            
         
            
def find_max_value_in_products(products):
    products_values = list(products.values()) # [1200, 800, 500, 150, 50]
    max_value = max(products_values)
    
    return max_value


find_max_value_in_products(products) #Out[23]: 1200


#adad


#esme mahsolo begiram
    
    
         
            
         
        
def find_max_product_in_products(products):
    products_values = list(products.values()) # [1200, 800, 500, 150, 50]
    max_value = products_values[0] #1200
    
    for product,price in products.items():
        if price >=max_value:

            max_value = price
            max_product =product 
            
    return max_product
   
find_max_product_in_products(products)   #Out[25]: 'laptab'


#do ta khoroji 
def find_max_product_in_products(products):
    products_values = list(products.values()) # [1200, 800, 500, 150, 50]
    max_value = products_values[0] #1200
    
    for product,price in products.items():
        if price >=max_value:

            max_value = price
            max_product =product 
            
    return max_value, max_product
   
find_max_product_in_products(products)   #Out[26]: (1200, 'laptab')

def find_max_product_in_products(products):
    products_values = list(products.values()) # [1200, 800, 500, 150, 50]
    max_value = products_values[0] #1200
    
    for product,price in products.items():
        if price >=max_value:

            max_value = price
            max_product =product 
            
    max_dict = {'price':max_value , 'name':max_product}
            
    return max_dict
   

find_max_product_in_products(products)
#Out[28]: {'price': 1200, 'name': 'laptab'}
    

def sum_in_products(products):
    products_values = list(products.values()) # [1200, 800, 500, 150, 50]
    total_product_values = sum(products_values)  
    return total_product_values
    

def sum_in_products(products):
    total = 0 
    for price in products.values():
        total  = total +price
    return total


#sum / len()


def len_in_products(products):
    count = 0 
    for price in products.values():
        count  = count +1
    return count

        
def average_in_product(products):
    
    total = sum_in_products(products)
    lenn = len_in_products(products)
    
    average = total / lenn
    return average





#--------------
#vorodi (dictionary) --:> BOX --> 2 khorji ,list1 ,list2

#list1 --> esme onaei hast k available
#list2 -->esme onaei hast k unavailabele


inventory = {
    "apple": 20,
    "banana": 5,
    "orange": 0,
    "milk": 12,
    "bread": 0
}


def availabilities_in_inventory(products):
    available_list=[]
    unavailable_list=[]
    
    for product,stock in products.items():
        if stock==0:
            unavailable_list.append(product)
            
        else:
            available_list.append(product)
    
    return available_list , unavailable_list
            
            
            
        
availabilities_in_inventory(inventory)


'''
Out[31]: (['apple', 'banana', 'milk'], ['orange', 'bread'])
'''
zarf = availabilities_in_inventory(inventory)

zarf[0] #Out[33]: ['apple' , 'banana', 'milk']
zarf[1] #Out[34]: ['orange', 'bread']

zarf1, zarf2 = availabilities_in_inventory(inventory)

print(zarf1) #['apple', 'banana', 'milk']
print(zarf2) #['orange', 'bread']





#---------------------------------------
#---------------------------------------
#---------------------------------------
# ADVANCED --> Niazi b  yadgiri nist 


a = [10,20,30,40]


print(a) #[10, 20, 30, 40]


#list,tuple,set,dictionary --> Iterable --> man ghabeliate iteration daronam daram 



#iter()

b = iter(a)

print(type(b)) #<class 'list_iterator'>

#ye chizi has k e iteration mikone
#roye ki ? rooye iterable (a)

print(b) #<list_iterator object at 0x1222cf0a0>


next(b) #Out[42]: 10

next(b)
next(b)


zarf = next(b)

print(zarf) #40

next(b) #StopIteration


#generator -->generationi dari --> azin ravesh estefade mikoni


#next()
#iter()



#------------

def my_something(my_list):
    for number in my_list:
        return number
    
    
my_something([10,20,30,40]) #Out[47]: 10



my_something([10,20,30,40])


#yek tabe dashte bvashid 
#yek kari --> iteration --> geenrator() besazid

#100000 adad darid
#harmogeh ke yek usere jadid registyer krd -> ye adad bgirid usere chndome






def my_something(my_list):
    for number in my_list:
        yield number
    
#return --> Yield

zarf = my_something([10,20,30,40])

print(zarf) #<generator object my_something at 0x12238d2a0>
print(type(zarf)) #<class 'generator'>

#agr variabliu bezarid joloye tabe ei k yield dare--> generator tahvil mihgirid


#bironesh next bznid

next(zarf) #Out[52]: 10 mitonm brizm yek zarfe dige

next(zarf) #Out[53]: 20

next(zarf) #Out[54]: 30


#geenration 1 mikllion adad, 1 miliard adad


def generators():
    my_list=[]
    for i in range(0,10000000000):
        my_list.append(i)
        
    return my_list



#in processs


#generator bashe -_> ahrdafe seda khir adad bede
#1 ,2 ,3 ,.. 1milliard 

#20 suer --> 1 milard adad tolid beshe

#return --> yiedl
#zarf = tabe
#dore tabe he next(zarf)
        
#--------------------
#shoma ba in mabahes ashan bashdi --> basic python --> tadris nakonan --> advanced python mishansan


#================================================
#================================================
#================================================
#================================================

def calculator(numb1,numb2,operation):
    if operation=='jam':
        result = numb1 + numb2
        return result
    elif operation=='tafrigh':
        result = numb1 - numb2
        return result
    elif operation =='zarb':
        result = numb1 * numb2
        return result
    elif operation =='taghsim':
        result = numb1 / numb2
        return result
    else:#operation = jam , tafrigh, zarb , taghsim
        print('in tabe fght jam , tafrigh, zarb , taghsim ')



zarf = calculator(10,20,'jam') #--> 30
zarf = calculator(10,20,'tafrigh') #-->  -10    

#print kone ???
zarf = calculator(10,2,'tavan')


#in tabe fght jam , tafrigh, zarb , taghsim 

print(zarf) #in tabe fght jam , tafrigh, zarb , taghsim 




def calculator(numb1,numb2,operation):
    if operation=='jam':
        result = numb1 + numb2
        return result
    elif operation=='tafrigh':
        result = numb1 - numb2
        return result
    elif operation =='zarb':
        result = numb1 * numb2
        return result
    elif operation =='taghsim':
        result = numb1 / numb2
        return result
    else:#operation = jam , tafrigh, zarb , taghsim
        #print('in tabe fght jam , tafrigh, zarb , taghsim ')
        raise 


'''
Syntax errror --> if a>10     : ro yadet mire , : , 

Logic error --> zamani k manteghi eshtebah --> hesabe bankie y frd hesba bshe --Z> manfi --> errror ? --> logical error


exceptions --> ina error behet mide python --> valueerror , ... listi azina hgast


https://docs.python.org/3/builtins/exceptions.html


ValueError

'''

float('salam')

#ValueError: could not convert string to float: 'salam'


10/0

#ZeroDivisionError: division by zero

#Typeerror

#filenoterror

#File notexist

#exception class hastand 







def calculator(numb1,numb2,operation):
    if operation=='jam':
        result = numb1 + numb2
        return result
    elif operation=='tafrigh':
        result = numb1 - numb2
        return result
    elif operation =='zarb':
        result = numb1 * numb2
        return result
    elif operation =='taghsim':
        result = numb1 / numb2
        return result
    else:#operation = jam , tafrigh, zarb , taghsim
        #print('in tabe fght jam , tafrigh, zarb , taghsim ')
        raise ValueError('in tabe fght jam , tafrigh, zarb , taghsim')




zarf = calculator(10,2,'tavan')

'''
zarf = calculator(10,2,'tavan')
Traceback (most recent call last):

  Cell In[61], line 1
    zarf = calculator(10,2,'tavan')

  Cell In[60], line 16 in calculator
    raise ValueError('in tabe fght jam , tafrigh, zarb , taghsim')

ValueError: in tabe fght jam , tafrigh, zarb , taghsim


'''





def withdraw(balance,amount):
    
    if balance<0:
        raise ValueError('Balance nemitavanad manfi')
    
    
    if amount<0:
        raise ValueError('Amountnemitavand')
        
    if balance < amount : 
        raise ValueError('mojodi hesab kafi nist')
    
    #databse, api ,......
    
    #100 khat complex
    
    
    #debugging
    #assert balance<0 , 'Balance is negative'
        
    
    balance = balance - amount
    
    return balance




#withdraw(200,10)

'''
if balance<0:
    raise ValueError('Balance nemitavanad manfi')


assert balance<0 , 'Balance is negative'

ddeveloper -->
'''


#------------------------------------
#------------------------------------
#------------------------------------

'''
L6---> tavabe ro yad grftim
L7 --> nokate mohmtri + Introduction on Packjage

L8 --> ta alan nokate advance ,.....

---> in jalase in part mikham didgahe karbrodi developeri , programmi , top level beheton bedam


vaghhty shoma code mzinid b 3 no code mizni 



1 - Monolothic structure --> yek code yekparche --> .py --> local (laptob) , server --> python file.py
1 bar ejra mishan -> az bala b paein mikjone, ejra mishe --> script 

---> shekrate yekseri data --> yek code bnvisid -> tamiz sazi kone
dar balash --> file migire ->kara anajm mishe --> khoroji save mikone
function,.... hamechi





2- Function based --> 

app shoma misazid, narm afzar, 

main.py --> file e appeton --> asli
folder darid , function haro to folder haye mojaza mizarid

main.py 


az bala ta pein chizi nminvisid to 100 file

100 file --> 99 file --> havie functione 
runable nist

zakhieye tabe ha hast onja

main.py --> az bala be paein azashon estefade miokonid

main.py --> tabe ei hast


#** ezafe kon tozihat ro ba login_processsor

main.py --> koli function hastan in fucntion ha vaslan b yek endpoint k vorodi azuseer az frontend miad

run koni javab bgiri

yek file python main.py --> hamihse rune roo serve




3- Object oriented programming (OOP)
function --> class object --> jalaseye badi 



Backend ba python

--> Django (ghadimi tare, kond tre, easy tar va rahat tare) --> function-based (class,....)
--> Fastapi --> jadid tare, ai comaptible, sakht tare --> class based berid jolo --> main.py (function)




'''


#----app khastyam besazam 

#main.py --> file k ghrare too server run bshe yani harchi bnvism inja use mishe

#yekseri fucntion --> tabe drm -> box drm 
#box -> hesabo kam mikone, hesabo ziad mikone, mojodi mibine

#account_management/ 
#accounts.py --> tabe haro mizram
#namayesh.py --> welcome() payan()



'''

my_package--
 |
 |--main.py
 |----folder1
         |---fil.py
         ----fil.py
  |----folder1
          |---fil.py
          ----fil.py



terminology --> be har file .py --> madule ماژول

folder ke shamele .py (madule ) --> package



Asliaro --> package
subpackaage , folder 






#---------------------------------------
import yek bar lazem e va baalye codet

baraye inke

folder ----desktop
             | main1.py
             | calculator.py
             
             
             
toye calculatro.py --> jam() , tafrigh() , zarb() , jam()

main1.py -->
from calculator import jam ,tafrigh, zarb 


(base) apm@APMs-MacBook-Pro desktop % pwd
/Users/apm/desktop

jaei ke file e hast

(base) apm@APMs-MacBook-Pro desktop % python main1.py

Ok





#0---------

-----My_projecty
    | main.py
    | accounts/
        |--------acc1.py ---> acc1_function()
        |--------acc2.py ---> acc2_function()
    
    
    | banks/
        |-----bank1.py  --->< bank1_function()
        |-----bank2.py ---> bank2_function()
        



main.py --> che fili __> file e aslime 

too server, local --> python main.py


dar fiule main.pyt baraye improt krdn 


 python main.py 
 
 python --> midone main.py --> kojas? --> my_project/




from accounts.acc1 import acc1_function 


python mirr file acc1.py ro yekabr run mikone 
error bashe?



agar man dar file acc2 bekham acc1 ro import konm?/




(base) apm@APMs-MacBook-Pro my_project % ls
accounts	banks		kenar.py	main.py




1---> dar main.py --> hamishe

age file kenari hast


from kenar import functions


age foldri hast ke file tooshe

from folder.file.file import function





ama file haye package ro


hatman mizani 
age hamonja bashe

from .file import function

ya age az folder haye kenari mikhay chiz vrdari
b sharti ke folderi k miay aghab main package nabashe
from ..file import function

agar foldere ghablet fodleri bashe k main_package
from folder.file import function



ghadim --> har folder ke msiakhti
bayad toosh yek file e misakhti bename
__init__.py





Python and Packages

16:10 






#--------------------------
#--------------------------
#--------------------------
#--------------------------



Python and packages --> devops , Package , Terminal


---my_package/
-----| main.py
-----| kenar.py
-----|----accounts/
------------|---acc1.py
-------------|---acc2.py
-------------|--subaccounts/
--------------------|subacc1.py
-----|----banks/
------------|---banks1.py
------------|---banks2.py




Ghanone vaal --> main.py --> harchi tooosh import mikoni
kenarie file ha hastan

from kenar import function
from utils import functions


age az folderi

from banks.banks1 import function
from accounts.acc1 import function




dakhele file haye dige -->

1---> age kenareshe  from .file import

dakhele acc1 mikhahi yek functin az acc2 

from .acc2 import function


2-->age bekhay biay foldere kenarit
dakhele acc1 , bank1

from ..banks.bank1 import function XXXX
---> negah mikoni .. brgashti b fodlere asli

from banks.bank1 import funciton 



dakhele subacc1.py
from ..acc1 import function

..acc1 --> miri toye foldere accounts (nemiri foldere madar)



Python --> 

python ....py 

too delesh do tachizi __Name___  , __package__

madare
python main.py ---> package -> misaze handle

main.py 



------case khasie ---------
---bank--
-------fees.py
-------appp---
-------------main.py
from ..fees import function

python main.py 


python -m bank.app.main




import ------------------




agar yek file dashte bashid
ke ham bekhahid azash import beshe
ham khodesh besorate jodagone run bshe


'''




#=========================
#=========================
#=========================
#=========================
#=========================


'''
folder ----> koli file o folder bezarim
too har file koli function bzarim 

k baghie bian azash estefade konan

#radicale (4)




1------python built in functions()
rahat dastresi
max() sum()

def max(list):
    maximum = list[0]
    for i in list:
        if i>maximum:
            maximum =i
    return maximum
        
'''
#niazi b import ndrn

max([10,20,30,40])

sum()

min()

#......


'''
2- python standard library

library --> ketabkhane 
ya yek foldere --> k koli package o , file , madule dakheleshe


ma hezran library mokjhtalef dar jahan darim

numpy --> baraye mohasebate pishraftas
pandas -> baraye data scientist --> clean 
matplotlib --> rasm , 

hooshe masnoei
sklearn --> scikit-learn --> organization 
koli 

sklearn.neural_network import MLPRegressor

MLPRegressor()

proghrammer --> yadgirie library ha


tensorflow 
....


rooye laptob?? 440 000 library
download konim --> aval 

bad mitonim azash estefade (import)


yekbar download ---> pip 


jalase ayande mofasal



pip install numpy


harjaeiii , har fili , har dolfi

external libraries --> organization, company
pip install --> use konid
'''

import numpy #import numpy




#------Standard libraries --> python dre to delesh
#niazi b nasb nist

#math

import math

#koli folder,file,function



math.sqrt(100) #ut[67]: 10.0


math.ceil(100.6) #Out[68]: 101
math.ceil(100.1) #Out[69]: 101


math.floor(100.4) #Out[70]: 100


'''
standard library --> pip install
hmain alan laptobeton dare


math --> amale riazi
random -->
json
csv


jalase ye karbordi --> in ketabkhone haro yad bgirdim
va asan atrigheye yadgirie ketabkhane haro dahste bashim




external --> numpy , pandas, sklearn



--> numpy ro tadris konm --> tarigheye yadgirie yek ketabkhone 



Hooshe masnoei --> algorithm(theory) , ketabkhone (numpy,pandas, scipy,sympy,tensorflow,statistics)




-------------
tamrin-------

3 ta package management baraton mizrm


3 ta soal optional , yield, .. ,list az tuple








-----------
L9

raise ---> Try exception
file management --> file ro open mikonim read, write

standard libraries --->
math , random, sys, .......



-------------
L10
object oriented programming --> class , object


FUNCTION --> CLASS ( function ha)






L11,L12,L13
numpy (library) --> 
database haro 
ketakhone pyqt , ---> GUI 
app basari yek chizi panel dashte bashe


moghadame ei bar django ham khedmateton begam




'''




'''
def sqrt(adad):
    radical
    return adad
'''




'''

------------- Takalif ------------------

baraye taklif haye jalase L8 , shoma bayad yek fodlere koli besazid bename L8_Tasks va dakhelesh task haye zir ro anjam dahid



1- Soale aval : dakhele L8_Tasks , yek project besazid bename project1 ke dota file bashe

project1/ 
├── main.py
└── calculator.py

dar file calculator.py , 4 tabe ye khali (mohem nist mitonid PASS bezarid toosh) dar calculator.py 
begzarid va dar file main.py har 4 taro import konid. va file main.py ro ejra konid agar error nagereftid 
yani masale hal shode



2- Soale dovom : shoma project 2 ro be in gone besazid, yani fodlere project2 va dakheelsh
main.py va user.py va hamchenin yek folder bename bank va ...


project2/
├── main.py
├── user.py
│
└── bank/
    ├── __init__.py
    ├── account.py
    ├── loan.py
    └── card.py



dar file haye zir in tavabe ye khali ro bezarid


in user.py :
def create_user():
    pass




in bank/account.py :
def create_account():
    pass

def close_account():
    pass



in bank/loan.py:
def request_loan():
    pass




in bank/card.py:
def create_card():
    pass



dar main.py bayad in mavared ro import konid
create_user
create_account
request_loan
create_card





3- soale sevom : yek folder besazid bename project3 ke file haye zir va do foldere accounts va payements dakhelesh bashe



project3/
├── main.py
├── config.py
│
├── accounts/
│   ├── __init__.py
│   ├── account.py
│   └── authentication.py
│
└── payments/
    ├── __init__.py
    ├── payment.py
    └── fee.py



tavabeye khalie zir ro tarif konid dar har kodam




in config.py:
def get_bank_name():
    pass


in accounts/account.py : 
def create_account():
    pass



in accounts/authentication.py:
def login():
    pass



in payments/fee.py:

def calculate_fee():
    pass



in payments/payment.py:
def make_payment():
    pass




khob shoma bayad dar file e main in tavabe ro import konid :
get_bank_name
create_account
login
make_payment
calculate_fee





hamchenin na tanha dar main , balke dar file haye diagr bayad yek digar ro import konid be in goone:

bayad dakhele config.py , tabeye login ro az authentication.py import konid.

bayad dakhele accounts/authentication.py , tabeye create_account ro az account.py import konid

dakhele payments/payment.py tabeye calculate_fee ro az file fee.py improt konid

hamchenin dakhele payments/payment.py bayad login ro az package accounts import konid







Soal haye Optional (ekhtiari) :

Optional 1 : Tabe ei besazid bename even_numbers ke vorodi yek adad bename n daryaft kone
va ba estefade iz dastoore yield , adade zoj ro az 2 ta n yeki yeki tolid kone

sepas yek geenrator besazido dakhele yek moteghayer gahrar dahid va ba next() 3 meghdare aval ro namayesh dahid




Optional 2 : tabe ei bename available_products benevisid ke dictionary mahsoolat ro daryaft konad , yani
vorodish yek dictioanry bashe mesle :

products = {
    "laptop": 3,
    "phone": 0,
    "tablet": 5,
    "mouse": 0,
    "keyboard": 2
}

va sepas , faghat name mahsolati ke mojodi anha bsih az sseft hast ro ba estefade az yield yeki yeki tolid konad (yani ye khoroji)

sepas yek geenrator besazido mahsolate mojod ro ba next() done done daryaft koni




optional3 : yek tabe be name create_profile benevisid ke do vorodie ejbari begire bename name,age 
alave bar in , betavanim har che tedade etelate ezafi ro ba estefade az **kwargs begire.

masalan : city, job, emnail , harchiii

khob tabe bayad inkaro kone :
- namo sen ro jnamayesh bede
- tamame etelaate ezafi ro namayesh dahad
- tedade etelaate ezafi ro chap kone
- agar city vojod dasht ,s hahro ro jodagone neshon bede
- agar email vojod nadasht ebenvise : email not provided
dar enteha ham tamame etelaate karbar ro dakhele yek dictionary jadid bezare o return kone



'''


#--------------------------
#------advanced python -m 





