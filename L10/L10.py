"""
Created on Fri Oct  9 15:05:02 2026

@author: apm




Ghabl az L9 --> Function haro yad gereftim


Vorodi --> function --> khoroji begirim 

default sazi, *args, **kwargs , Tamiz nevisi (docstring) esme variable ha esme tabe

tabe ha --> raise gharar bedim -> error management dakhele tabe bashe

estefade tabe ha kojan?


app minevism 
1--> main.py -_> import moikonim tavabe ro 


2--> ketabkhone ha, package ha --> yek foldere k koli file dakhelesh , har file function hast , import mikonim



Try except sohbat krdim 


Standard python library --> yekseri package hast ke hamrahe
python dakhele computere shoma hast mitonid mostaghim import konid
azash estefade konid


math , os , random , time, datetime --> L9.py

L9_Advances_Topics.py ---> mabahese koli



CLasss ha  , object
object oriented programming (OOP)
shey garaei


ahamiate --->
C++ , C

C --> class nadasht , object nadasht

C++ upgrade --> class ro cover kone , zaboen jadid , 
dastoatesho , optimize ,conceopt haei


def 

class 

"""


#chandin danesh amooooz 
#mikham man 10 ta danesh amozamo ba moshakahsateshon ro dashte basham



name_danesh_amoz1= 'ali'
sen_danesh_amoz1 = 18
nomre_danesh_amoz1 = 20



name_danesh_amoz2= 'vahid'
sen_danesh_amoz2 = 20
nomre_danesh_amoz2 = 18

#10 ta --> 30 khat 

#estefade konm

name_danesh_amoz10= 'reza'
sen_danesh_amoz10 = 40
nomre_danesh_amoz10 = 19



#3 ta moshakhasat , 10 ta moshakhasat 

#100 khat minevshtm baraye moarefie 10 nfr


#20 ta vizhegi --> 200 khat baaye 10 nfr


#1---> man yekseri afradi daram shabihe haman , name, sen , --> man mjborm koli zarf dashte basham


#rahe hal 

danesh_amoz1={'sen':30, 'name':'ali','score':20}



#2----> man yekseri tavabe daram k in tavabe ye man mikham beham dige vasl bashan va maghadir ro baraye har chiz negah dare


#--> show_balance() bardasht() variz()






#def show_balance():
  
    
def bardasht(balance,amount):
    balance = balance - amount 
    return balance

bardasht(100,5) #Out[105]: 95

#moshtari daram --> ali , vahid , hamid


ali_customer = {'name':'ali','sen':40 , 'balance':2000}
ali_customer['balance'] = bardasht(ali_customer['balance'],1000)

#gahan --> vahid , reza, hamid ,...ykseri vizhegi daran
#$------> maghadir daran (name,sen,ballance)
#------> kar ha roshon mishe najam -> (show_balance, bardasht,variz)


def variz(balance, amount):
    balance = balance + amount 
    return balance


ali_customer['balance'] = variz(ali_customer['balance'] , 10000)



#tedade ziadi az yek 'CHIZ' darid ke 
            #magahdire moshtarak
            #tavabe moshyatrak daran
            
            
            
#-->moshtarak -->moshtarie bank --> hamashon az yek no hastan --> az yek type
#--> az yek class hastand
#def custoer():
    
    
    
class Customer:
    
    def __init__(self,name,sen,balance):
        pass
    
    
#ali = Customer(name='ali',sen=20,balance=2000)
#vaghty mikhahi az class object besazid yekseri information midi 



user1 = Customer(name='ali', sen=30, balance=40000)


print(type(user1)) #<class '__main__.Customer'>


user1.name #AttributeError: 'Customer' object has no attribute 'name'





class Customer:
    
    def __init__(self,name,sen,balance):
        #too dele object .name 
        self.name = name 
        self.sen = sen
        self.balance = balance

#in classe
#az class ma objecyt misazim

obj1 = Customer(name='ali',sen=20,balance=20000000)

obj1.name #Out[113]: 'ali'
obj1.sen #Out[114]: 20



class Customer:
    
    def __init__(self,esm,sen,mojoodi):
        #tabeye __init__ moshakhas mikone
        #ke dar lahzeye skahte object chegone user bayad object besaze
        
        #too dele object .name 
        self.name = esm 
        self.age = sen
        self.balance = mojoodi
        
        
#object besaze

obj1 = Customer(esm='ali', sen=20, mojood=200000)

obj1.esm #TypeError: Customer.__init__() got an unexpected keyword argument 'mojood'

obj1.name  #Out[116]: 'ali'


obj1.sen 
obj1.age

    

#---------
obj1 ={'name':'ali','age':20,'balance':20000}
obj1 = dict({'name':'ali','age':20,'balance':20000})
obj1['name']
    
print(type(obj1)) #<class 'dict'>
    
    
    
obj1 = Customer(esm='ali',sen=20,mojoodi=20000)
obj1.name

    
obj1 = Customer('ali',20,20000)

#Positional, keywoirds
    
    
    
#classs --> yek chizi hast ke az roosh object misazid
#ke havie attributes va methode

#attributes --> self.sen self.name self.balance





class Customer:
    
    def __init__(self,esm,sen,mojoodi):
        #tabeye __init__ moshakhas mikone
        #ke dar lahzeye skahte object chegone user bayad object besaze
        
        #too dele object .name 
        self.name = esm 
        self.age = sen
        self.balance = mojoodi
        
    def welcome(self):
        print('salam customere aziz')
   
        
obj1 = Customer('ali',20,20000)

#chia hast??? 
obj1.name #Out[124]: 'ali'
obj1.asjhshdjgdsajhxz
#AttributeError: 'Customer' object has no attribute 'asjhshdjgdsajhxz'

obj1.age #20
obj1.balance #20000


#--Methods --> tavabeye dakhele on class
obj1.welcome()  #zarf nis (attribute) tabe hast (method)






obj2 = Customer('vahid',30,30000)
obj2.name 
obj2.balance 
obj2.age

obj2.welcome() #salam customere aziz




#---------------------------

class Customer:
    
    def __init__(self,esm,sen,mojoodi):
        #tabeye __init__ moshakhas mikone
        #ke dar lahzeye skahte object chegone user bayad object besaze
        
        #too dele object .name 
        self.name = esm 
        self.age = sen
        self.balance = mojoodi
        
    def welcome(self):
        print('salam customere aziz')
        print(self.name)

obj1 = Customer('ali',20,20000)

obj1.welcome()
'''
salam customere aziz
ali
'''


obj1.bardasht(4000)


obj2 = Customer('Vahid',40,20000)

obj2.welcome()

'''
salam customere aziz
Vahid
'''




#def welcome(name):
    
    
    

class Customer:
    
    def __init__(self,esm,sen,mojoodi):
        #tabeye __init__ moshakhas mikone
        #ke dar lahzeye skahte object chegone user bayad object besaze
        
        #too dele object .name 
        self.name = esm 
        self.age = sen
        self.balance = mojoodi
        
    def welcome(self):
        print('salam customere aziz')
        print(self.name)
        
        
    def bardasht(self,amount):
        
        self.balance = self.balance - amount 
        
        print('ba moafaghiat anjam shod')
   
    
obj1 = Customer('ali',20,20000)

#atrribute
obj1.name #ali
obj1.age #20
obj1.balance # 20000


#methods --> function
obj1.welcome()
'''
salam customere aziz
ali
'''


obj1.bardasht(1000)
#ba moafaghiat anjam shod


obj1.balance #Out[137]: 19000




class Customer:
    
    def __init__(self,esm,sen,mojoodi):
        #tabeye __init__ moshakhas mikone
        #ke dar lahzeye skahte object chegone user bayad object besaze
        
        #too dele object .name 
        self.name = esm 
        self.age = sen
        self.balance = mojoodi
        
    def welcome(self):
        print('salam customere aziz')
        print(self.name)
        
        
    def show_balance(self):
        print('mojodie shoma hast:', self.balance)
        
        
        
    def bardasht(self,amount):
        
        self.balance = self.balance - amount 
        
        print('ba moafaghiat anjam shod')
        print('mojodie alane shoma:',self.balance)
        
   
    def variz(self,amount):
        self.balance = self.balance + amount
       
        print('ba moafaghiat anjam shod')
        print('mojodie alane shoma:',self.balance)



   
obj1= Customer(esm='ali',sen=20,mojoodi=200)
  
#attributes hst
obj1.name #ali
obj1.age #20
obj1.balance #200




#methiods -->
obj1.welcome()
'''
salam customere aziz
ali

'''


obj1.show_balance()
#mojodie shoma hast: 200


obj1.bardasht(10)
'''
ba moafaghiat anjam shod
mojodie alane shoma: 190
'''

obj1.show_balance()
#mojodie shoma hast: 190


obj1.balance
#Out[147]: 190


obj1.variz(200)
'''
ba moafaghiat anjam shod
mojodie alane shoma: 390
'''

obj1.show_balance()
#mojodie shoma hast: 390






#welcome()



class Customer:
    
    def __init__(self,esm,sen,mojoodi):
        #tabeye __init__ moshakhas mikone
        #ke dar lahzeye skahte object chegone user bayad object besaze
        
        #too dele object .name 
        self.name = esm 
        self.age = sen
        self.balance = mojoodi
        
    def welcome(self):
        print('salam customere aziz')
        print(self.name)
        
        
    def show_balance(self):
        print('mojodie shoma hast:', self.balance)
        
        
    def return_balance(self):
        return self.balance
        
        
    def bardasht(self,amount):
        
        self.balance = self.balance - amount 
        
        print('ba moafaghiat anjam shod')
        print('mojodie alane shoma:',self.balance)
        
   
    def variz(self,amount):
        self.balance = self.balance + amount
       
        print('ba moafaghiat anjam shod')
        print('mojodie alane shoma:',self.balance)



obj1 = Customer('ali',20,2000)

obj1.name #Out[151]: 'ali'

#method ha 

#khoroji ndrn print
#dastoor
obj1.show_balance() #mojodie shoma hast: 2000

zarf = obj1.show_balance() #mojodie shoma hast: 2000
print(zarf) #None


zarf = obj1.return_balance()
print(zarf) #2000


#Khoroji drn









#-----function-----


#vorodi --> Box --> khroji miodad


#class --> mikhahid maange konid yekseri chizi k moshtarekan
#vzihegi moshtarek --> bank_customer , ,.....

#class :
    #def __init__():
        #attrebute
        #self. 
        #self.
    
    #def func1(self,):

        
'''
Function ---> vorodiu --> Box --> khoroji

Class --> object misazim obj1 = Class() obj2 = class() ..

    attributes --> obj1.att1  obj2.att1

    methods -->  obj1.method() 






'''

class Bank_Customer:
    
    #be in fek kon object misazi ch etelaati lazeme
    #baraye skahte object az class
    def __init__(self,first_name,last_name,code_meli , phone, address , initial_balance):
        
        #self.first_name = first_name
        #self.fullname = first_name + ' ' +  last_name
        self.fullname = f'{first_name} {last_name}'
        self.national_id = code_meli
        self.phone_number = phone
        self.address = address
        self.balance = initial_balance
        
        self.sum_daily_withdraw = 0
        
        self.information = {'full_name':f'{first_name} {last_name}' ,
                            'national_id':code_meli,
                            'phone':phone,
                            'address':address}
        
        
        
        self.minimum_balance = 50000
        self.karmozd = 0.01 #1/100
        self.maximum_deposit = 100000000
        self.currency = 'toman'
        self.show_balance_karmozd = 1000
        
        self.maximum_withdraw_at_once = 500000
        self.maximum_sum_withdraw = 10000000
        
        
    def welcome(self):
        '''
        

        Returns
        -------
        None.

        '''
        print(f'salam moshtarie aziz {self.fullname} be banke plutus khosh oomadid')
        
        
        
    def show_balance(self):
        if self.balance < self.show_balance_karmozd + self.minimum_balance:
            raise ValueError('Mojodie moshahedeye mojodi kafi nist')
            
            
        self.balance = self.balance - self.show_balance_karmozd
        
        print('balance shoma hast :' , self.balance)
        
    def bardasht(self,amount=0):
        
        if amount + self.karmozd * amount +self.minimum_balance > self.balance :
            raise ValueError('Mojodi kafi nemibashad')
        
        elif amount <0:
            raise ValueError('amount mitavanad fght mosbat bashad')
        
        elif amount > self.maximum_withdraw_at_once:
            raise ValueError('shoma ejaze ye bardahst bish az 50000 nadarid')
            
        elif self.sum_daily_withdraw + amount > self.maximum_sum_withdraw:
            raise ValueError('shoma be saghfe bardashte roozane rresidi')
            
            
        self.balance = self.balance - amount - self.karmozd * amount
        
        
        self.sum_daily_withdraw = self.sum_daily_withdraw  + amount +  self.karmozd * amount
        
        
        
        print('ba moafaghita anjam shod')
        print('mojodie shoma :',self.balance)
        
    
    def variz(self,amount=0):
        
        if amount <0:
            raise ValueError('amoutn nemitavand manfi bashad')
            
        elif amount > self.maximum_deposit:
            raise ValueError('shoma be saghfe variz khordid')
            
            
        self.balance = self.balance + amount 
        
                
        print('ba moafaghita anjam shod')
        print('mojodie shoma :',self.balance)
        
        






obj1 = Bank_Customer('ali', 'pilehvar meibody', '04400000000', '0919....', 'iran , ,', 100000)

obj1.first_name #AttributeError: 'Bank_Customer' object has no attribute 'first_name'

obj1.fullname #Out[167]: 'ali pilehvar meibody'
obj1.national_id #Out[168]: '04400000000'


obj1.balance #Out[169]: 100000

zarf = obj1.information

print(type(zarf)) #<class 'dict'>
print(zarf)
'''
{'full_name': 'ali pilehvar meibody', 'national_id': '04400000000', 'phone': '0919....', 'address': 'iran , ,'}

'''

#2 ta soal

#1-->vorodi chi bzaram? age hichi -> self 
#har vorodi --> self,
obj1.welcome()

#2-->khoroji dare?? 
#zard = obj1.welcome()

#return


#method-------
obj1.welcome()
#salam moshtarie aziz ali pilehvar meibody be banke plutus khosh oomadid




obj2 = Bank_Customer('vahid', 'rezaei', '04400000000', '0919....', 'iran , ,', 100000)

obj2.welcome()
#salam moshtarie aziz vahid rezaei be banke plutus khosh oomadid



#obj1.bardasht(1000)
#zarf = 





obj1.show_balance() #balance shoma hast : 100000

obj1.variz(200000000000000000000)

#ValueError: shoma be saghfe variz khordid

obj1.variz(20000)

'''
ba moafaghita anjam shod
mojodie shoma : 120000
'''


obj1.show_balance()
#balance shoma hast : 120000




#obj1.show_transactions()

'''

+2000
-5000
+10000


'''


#=========================
#=========================
#=========================
#=========================
#----adding transactions-----

class Bank_Customer:
    
    #be in fek kon object misazi ch etelaati lazeme
    #baraye skahte object az class
    def __init__(self,first_name,last_name,code_meli , phone, address , initial_balance):
        
        #self.first_name = first_name
        #self.fullname = first_name + ' ' +  last_name
        self.fullname = f'{first_name} {last_name}'
        self.national_id = code_meli
        self.phone_number = phone
        self.address = address
        self.balance = initial_balance
        
        self.sum_daily_withdraw = 0
        
        self.information = {'full_name':f'{first_name} {last_name}' ,
                            'national_id':code_meli,
                            'phone':phone,
                            'address':address}
        
        
        self.transactions = []
        
        
        self.minimum_balance = 50000
        self.karmozd = 0.01 #1/100
        self.maximum_deposit = 100000000
        self.currency = 'toman'
        self.show_balance_karmozd = 1000
        
        self.maximum_withdraw_at_once = 500000
        self.maximum_sum_withdraw = 10000000
        
        
    def welcome(self):
        '''
        

        Returns
        -------
        None.

        '''
        print(f'salam moshtarie aziz {self.fullname} be banke plutus khosh oomadid')
        
        
        
    def show_balance(self):
        if self.balance < self.show_balance_karmozd + self.minimum_balance:
            raise ValueError('Mojodie moshahedeye mojodi kafi nist')
            
            
        self.balance = self.balance - self.show_balance_karmozd
        
        print('balance shoma hast :' , self.balance)
        
    def bardasht(self,amount=0):
        
        if amount + self.karmozd * amount +self.minimum_balance > self.balance :
            raise ValueError('Mojodi kafi nemibashad')
        
        elif amount <0:
            raise ValueError('amount mitavanad fght mosbat bashad')
        
        elif amount > self.maximum_withdraw_at_once:
            raise ValueError('shoma ejaze ye bardahst bish az 50000 nadarid')
            
        elif self.sum_daily_withdraw + amount > self.maximum_sum_withdraw:
            raise ValueError('shoma be saghfe bardashte roozane rresidi')
            
            
        self.balance = self.balance - amount - self.karmozd * amount
        
        
        self.sum_daily_withdraw = self.sum_daily_withdraw  + amount +  self.karmozd * amount
        
        
        self.transactions.append(f'- {amount}')
        
        print('ba moafaghita anjam shod')
        print('mojodie shoma :',self.balance)
        
    
    def variz(self,amount=0):
        
        if amount <0:
            raise ValueError('amoutn nemitavand manfi bashad')
            
        elif amount > self.maximum_deposit:
            raise ValueError('shoma be saghfe variz khordid')
            
            
        self.balance = self.balance + amount 
        
        
        self.transactions.append(f'+ {amount}')
        
        print('ba moafaghita anjam shod')
        print('mojodie shoma :',self.balance)
        
    def show_transactions(self,count= 10 , mode='standard'):
        
        if len(self.transactions)<=count:
            #error -> 
            requested_transactions = self.transactions
        else:
            requested_transactions = self.transactions[len(self.transactions)-count : ]
            #requested_transactions = self.transactions[-1-count:-1]
            
        
        
        
        if mode=='professional':
            print("*******************************")
            print('--------- Plutus Transactions -----------')
            for transact in requested_transactions:
                
                if transact[0] == '-':
                    print(f'Bardasht {transact}')
                    
                    
                else:
                    print(f'Variz {transact}')
                    
            
            
            
        elif mode =='standard':
            
        
            print('=================================')
            print('--------- Plutus Transactions -----------')
            for transact in requested_transactions:
                print(transact) 
                print('-----')
                
            print('=================================')
        
        else :
            raise ValueError('mode mitone ya standard bashe ya professional')
                
        






obj1 = Bank_Customer('vahid', 'rezaei', '04400000000', '0919....', 'iran , ,', 100000)
      

obj1.bardasht(10000)
'''
ba moafaghita anjam shod
mojodie shoma : 89900.0

'''
obj1.variz(20000)

'''
ba moafaghita anjam shod
mojodie shoma : 109900.0
'''


obj1.variz(100000)
'''
ba moafaghita anjam shod
mojodie shoma : 209900.0
'''

obj1.bardasht(50000)
'''
ba moafaghita anjam shod
mojodie shoma : 159400.0
'''


obj1.show_balance()
#balance shoma hast : 158400.0


obj1.balance #Out[201]: 158400.0

#attribute --> obj=bank_customer() --> self.transaction = []

obj1.transactions

#Out[211]: ['- 10000', '+ 20000', '+ 100000', '- 50000']

#obj1.show_transactions()

obj1.show_transactions()

'''
=================================
--------- Plutus Transactions -----------
- 10000
-----
+ 20000
-----
+ 100000
-----
- 50000
-----
=================================

'''

obj1.show_transactions(mode='standard')
'''
=================================
--------- Plutus Transactions -----------
- 10000
-----
+ 20000
-----
+ 100000
-----
- 50000
-----
=================================
'''

obj1.show_transactions(mode='professional')
'''
*******************************
--------- Plutus Transactions -----------
Bardasht - 10000
Variz + 20000
Variz + 100000
Bardasht - 50000
'''


obj1.show_transactions(mode='academic')
#ValueError: mode mitone ya standard bashe ya professional




obj1.show_transactions(2)

'''
=================================
--------- Plutus Transactions -----------
- 10000
-----
+ 20000
-----
=================================

'''



#ketabkhone ha --> function import, class


#MLPRegressor --> multi layer perceptron regressor -->
#shabake asabie masnoei sade 

#Memari daram --> 



from sklearn.neural_network import MLPRegressor


'''
class MLPRegressor:
    def __init__(self,hidden_layer_sized, )
    
    
    
    
    def train(self,data)
    
    
    
    
    def predict(self,new_x):
        return predicted_y
'''

data = open('experimental.xlsx')


ANN = MLPRegressor(hidden_layer_sizes=(100,10))

ANN.train(data)


ANN.predict(data)





class Product:
    
    def __init__(self,code,name,brand , colour, category,price):
        self.code = code
        self.name = name
        self.brand = brand
        self.colour = colour 
        self.category = category 
        self.price = price 
        
        
    def apply_discount(self,discount):
        self.price = self.price  - discount/100* self.price 
        
        return self.price 
    
    
        
        
        
product1 = Product(code='N14',name='lipgloss',brand='kiko',colour='red',category='lipglosses',price=14)



product1.price #Out[223]: 14



print(type(product1)) #<class '__main__.Product'>


print(type('ali')) #<class 'str'>


zarf = 'ali'

zarf = str('ali')

'''

class str:
    def __init__(self,value):
        
        
        
        
    def lower(self):
        
        self.value???
        
        return kochikshodaro
        
    
    def find(self,character):
        
        for i in range(0,len(self.value)):
            if self.value[i] == character:
                return i
            
            
    def count(self,character):
        count=0
        for i in self.value:
            if i ==character:
                count = count + 1
            
        return count
        
    



class list:
    
    def __init__(values):
    
        self.values = values
        
        
        
    def append(self,element):
        
        self.values = [values , element]
        
        #return nemidadd







class tuple:
    
    def __init__(values):
    
        self.values = values
        
        
        
    def append(self,element):
        
        self.values = [values , element]
        
        #return nemidadd


    @property
    def values(self):
        raise Error





'''

print(zarf)


new_zarf = zarf.lower()



zarf.find('l') #Out[232]: 1

zarf.count('a') #Out[233]: 1
print()




a = [10,20,30,40]

a = list([10,20,30,40])


a.append(60)



#------------------------------------------------
#------------------------------------------------
#------------------------------------------------



class Product:
    
    def __init__(self,code,name,brand , colour, category,price):
        self.code = code
        self.name = name
        self.brand = brand
        self.colour = colour 
        self.category = category 
        self.price = price 
        
        
    def apply_discount(self,discount):
        self.price = self.price  - discount/100* self.price 
        
        return self.price 
    
    
    


product1 = Product(code='N14',name='lipgloss',brand='kiko',colour='red',category='lipglosses',price=14)


print(type(product1)) #<class '__main__.Product'>

print(product1)
#<__main__.Product object at 0x127ed0070>



#def -->dunder function --> double underscore functions


#1--->__init__ --> ()
#2--> __str__ 

class Product:
    
    def __init__(self,code,name,brand , colour, category,price):
        self.code = code
        self.name = name
        self.brand = brand
        self.colour = colour 
        self.category = category 
        self.price = price 
        
        
    def apply_discount(self,discount):
        self.price = self.price  - discount/100* self.price 
        
        return self.price 
    
    
    def __str__(self):
        sakhtam = f'{self.name}:{self.code}'
        return sakhtam
    
    
    def __repr__(self):
        sakhtam = f'{self.name}:{self.code}'
        return sakhtam
        
    
    
product1 = Product(code='N14',name='lipgloss',brand='kiko',colour='red',category='lipglosses',price=14)
 
print(product1) #lipgloss:N14



#product1.attribute

#product1.methods



#print(products1)


product1 = Product(code='N14',name='lipgloss R',brand='kiko',colour='red',category='lipglosses',price=14)
product2 = Product(code='N14',name='lipgloss B',brand='kiko',colour='purple',category='lipglosses',price=13)

print(product1 == product2) #False
#L10_Advanced_topics.py


class Product:
    
    def __init__(self,code,name,brand , colour, category,price,stock):
        self.code = code
        self.name = name
        self.brand = brand
        self.colour = colour 
        self.category = category 
        self.price = price 
        self.stock = stock
        
        
    def apply_discount(self,discount):
        self.price = self.price  - discount/100* self.price 
        
        return self.price 
    
    
    def __str__(self):
        sakhtam = f'{self.name}:{self.code}'
        return sakhtam
    
    
    def __repr__(self):
        sakhtam = f'{self.name}:{self.code}'
        return sakhtam
    
    
    def __eq__(self,other):
        
        return self.code == other.code
    
    
    def __len__(self):
        return self.stock
        
        
        
    
    
product1 = Product(code='N14',name='lipgloss R',brand='kiko',colour='red',category='lipglosses',price=14,stock=10)
product2 = Product(code='N14',name='lipgloss B',brand='kiko',colour='purple',category='lipglosses',price=13,stock=20)

print(product1 == product2) #True


product1.stock #Out[250]: 10

len(product1) #Out[251]: 10

len(product1)



#-------jalase ayande------------
#cls --> proeprty method, static method --> advanxced python 


'''
4 ta .py --> L9_L10/


Task1 --> jalase L9 --> kar ba try except  , file management

Task2 --> jalase L9 --> OS , math 


L10
Task 3 --> yek class az products 

Task 4 --> yek class az ... (jazab)




'''






