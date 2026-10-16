"""
Created on Fri Oct 16 14:56:51 2026

@author: Ali Pilehvar Meibody

L11




"""

#=====================================
#=====================================
#=====================================



'''
Human <----python----> Machine

Python --> yek zabane barnam enevsii

1- Python kernel   2-IDE/EDITOR

anaconda --> mohit haye mojaza misakht , too har mohit
ma yek python yek ide dashtim

4 ta spyder daahte bashi



python yek zaban e



1- Python built in functions 
print() len() type() input()
open() .......



2-keywords 
    2.1. Sharti --> if , if else, if elif (multiple sleetion)
                and,or, any , all , break , continue , pass
            
    2.2. Halghe ha --> for , while
                    print, count, append 
                    
                
                    
3- Variables
    3.1.Numbers (int,float,complex) --> operation (** * , ==)
    3.2. Bool (True,False)
    3.3. STR (string) --> khodesho, accesss [] ,slicde, str functions (.lower() .upper(),..)
    
    3.4. Iterablees --> multiple valeus inside one variable
        3.4.1. List --> ordered(index) , changable, allow duplicated
                    .append() .insert() .remove() ,..
        3.4.2. Tuple --> ordered(indewx) , unchnagbale, allow duplciated
                () --> db database
                
        3.4.3. Set --> no order, unchnagbale , no duplicated {} --> set haye riazio
        
        3.4.4. Dictionary --> {key:val ,key:valuy}
        
        
        
        


fundemental Python hastan --> yek code bezani 



Function --> def function() , default ,,......
Class --> class includes attriubutes , methods 







3 no code nevisi darim

1- Monolothic --> az bal ab paein minevisi
2- Function based --> tabe mineviosi
3- CLASS (Object oriented prograaming (OOP))



------->Python
   |
   |
   |---->  website (backend) --> django / fastapi 
   |----> data --> data analysis, data science
   ------> AI --> machine learning , deep learning, agents
   |----> security , automation ,......
   
   
   
website --> rooye run dari --> hamishe roo run bashe roo serveer


main.py -->baghie chizaro (function,class) --> file haye dige mizarishon

data analysis, data science , ML training --> yek .py runeshon mikoni 






Import haro ovordim jolo--->
            main.py -->hamaro ba esme khdoeshon (absolute)
            too file haye dige --> age onja . 
            age birone (va package madar nist) ..
            
            package besazid
            
       
3 no package
1-package khodeton
2- standard library --> ketabkhone ha hastan 
    math , random, time, datetime  , os , pathlib ,  csv , json , collections , argparse
hamrahe poython hastand


3- external libraries -->yani yek organization onaro sakhte 

 --> ketabkhone darim

esbat b applicationi k darim kar mikonim

website --> django / fastpi  
data analysis --> numpy (mohasebat) , scipy , sympy (mohsabeta moadelat)
            pandas --> data cleaning , kar ba data
            matplotlib ,seaborn --> rasme data 
            
            scikit-learn (sklearn) ---> model haye Machine learning 
            
            Tensorflow /keras (googl) | pytorch (Meta) --> Deep learning
            

_ . _ . _ 


mohem tarine 
dovomie --> feature ha -> vizhegi

3.1 

3.4 --> vzihegi haye bsihtri dare


3.4.0 --> in yani fresh
buga dar maid ye hafgte

3.4.1

3.4.3 


3.5.

4.

yek project bezani --> dataei az bimarestane nikan gharb , maghzo asab --> data --> excel

mikhay porozhato shoro koni


anaconda --> create nevironemnt --> python , spyder 
varedesh mishi , hal amikhay package numpy , pandas ,




PIP  --> abzar 

besoorate cl (command line) dakhele command line interface (CLI)
mac/linux --> terminal
windows --> cmd , powershell , git bsh 


powershell



hamontor k laptabeton yedone spyder nadare, 3,4 ta 
root , env1 ,env2

powershell baraye harkodom shoma yedone darid



env --> nikan_proj 


----------------RAVESHE 1----------------

miri anaconda navigatro --> slect mikoni mohiteto  --> 
powershell ---> install (yekbar)

hardafe search bzni powersheel 

powershell (env1) 





----------------RAVESHE 2----------------
powershelle root ro baz kon


(base) apm@APMs-MacBook-Pro ~ % conda activate DL
(DL) apm@APMs-MacBook-Pro ~ % conda deactivate
(base) apm@APMs-MacBook-Pro ~ % 




yeki az mohemtarin chziash 0--> joda az cd , pwd, .....

installe package

yek abzari darim bename pip 

pip install ......

pip --> pypi.org --> package (gitlab, github)




yek package mikham downloa dkonm 


miri too google --> pypi package



maslaan pypi numpy --> avalin safe miri dakhel

https://pypi.org/project/numpy/#description

yek ghesmat copy kon
pip install numpy


--> powershell , motmaenam ke kojam? tooye mohitamam



install koni pip --> homebrew mac, widget --> widnows --> gpt pip ndrm instal 


pip install numpy


---> versione
 pip install numpy==1.4.6 


spydereto baz mikoni ?? --> spydere MEM (hamomn env)

'''

import numpy #import numpy


import numpy as np


a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a)
'''
[[1 2 3]
 [4 5 6]]

'''

a.shape #Out[5]: (2, 3)


#a = [1,2,3,4]
a = np.array([1,2,3,4])
print(a) #[1 2 3 4]
print(type(a)) #<class 'numpy.ndarray'>

a.shape #Out[9]: (4,)



a[0] #Out[10]: np.int64(1)




'''
class -> Product , Service

advanced topice dclasss


users.txt --> datahamon zkahiran ->taghir bdim ,a dd user, deleted user 
function anjam bdim


mahdodiat 
class anjam bedim 


.txt --> database ? --> dtaabase ro shoro konim 
database o flask ro be enteha

'''

#class Product besazam


#class --> method , attributes 

#chiz besazi --> objct besazi 

#clss bsazid --> object dar biarid

class Atom:
    def __init__(self,element,x,y):
        pass
    
    
    
    
class Product:
    '''
    
    
    '''


    def __init__(self,code,name,price,stock):
        self.code = code
        self.name = name 
        self.price = price
        self.stock = stock 
        self.sell_count = 0
        
    def show(self):
        print('-'*30)
        
        print(f'Product Name : {self.name}')
        print(f'Product code : {self.code}')
    
        print(f'    PRICE     : {self.price}')
        
        if self.stock>0:
            print('Mojood ast')
        else:
            print('Mojoodi nadarad')
        
        
        
        
        print('-'*30)
        
        
    def apply_discount(self,percentage):
        
        if percentage >100:
            raise ValueError('No more than 100')
        elif percentage >1 : #1 - 100
        
            self.price = self.price - percentage/100 * self.price
            print('az price kam shod')
            
        else: 
            raise ValueError('no less than 1')
            
            
    def sell(self,quantity):
        if self.stock < quantity:
            raise ValueError('Mojodi kafi nist')
        
        if quantity<0:
            raise ValueError('no negative quantity')
            
            
        self.stock = self.stock - quantity 
        
        self.sell_count = self.sell_count + quantity 
        
        
    def restock(self,quantity):
        if quantity<0:
            raise ValueError('no negative quantity')
            
        self.stock = self.stock + quantity 
        
        
        
    def is_available(self):
        if self.stock>0:
            return True 
        else:
            return False
        
        
    def __str__(self):
        return f'{self.code}:{self.name}'
        
        
        
    
        
        
    
    
    
    
    
#p1 = Product()
#p1.code 


pr1 = Product(code='n1',name='zara ',price=13 , stock = 4)

print(pr1) #<__main__.Product object at 0x122a7a2f0>

#n1:zara 


pr1.is_available() #Out[22]: True


pr1.apply_discount(10)

pr1.show()

'''
------------------------------
Product Name : zara 
Product code : n1
    PRICE     : 11.7
Mojood ast
------------------------------

'''


pr1.sell(1000) #ValueError: Mojodi kafi nist

pr1.sell(2)



'''

digital product --> name , code , price , stock , link_download 

physical prodiuct --> name, codde,  price, stock , vazn, hazine_ersal 

'''


class DigitalProduct:
    def __init__(self,name,code,price,stock,download_link):
        self.name = name
        self.code = code 
        self.price = price
        self.stock = stock 
        self.download_link = download_link 
        
        
        
    def show(self):
        pass
        
        
        
    def sell(self): 
        pass 




#class haei besazi --> class madar 

#chera tavabe o dobar ebenvisam --> nemitonm ers bebaram azash
#inheritance 




class DigitalProduct(Product):
    def __init__(self,code,name,price,stock,download_link):
        super().__init__(code,name,price,stock)
        self.download_link = download_link
        self.download_records = 0
        
    def return_download_link(self):
        return self.download_link 
    
    def submit_download(self,amount):
        self.download_record = self.download_record + amount 
        
    def show(self):
        print('-'*30)
        
        print(f'Product Name : {self.name}')
        print(f'Product code : {self.code}')
    
        print(f'    PRICE     : {self.price}')
        
        if self.stock>0:
            print('Mojood ast')
        else:
            print('Mojoodi nadarad')
        
        
        print(f'download links : {self.download_link}')
        
        
        print('-'*30)







import math 

class Location:
    def __init__(self,address , x_cordinate, y_cordinate):
        self.address = address
        self.x_cordinate = x_cordinate
        self.y_cordinate = y_cordinate
        
        
    
    def calculate_distance(self,location):
        
        if not isinstance(location,Location):
            raise NotImplemented
            
        
        x_distance = self.x_cordinate - location.x_cordinate 
        
        y_distance = self.y_cordinate - location.y_cordinate
        
        distance = math.sqrt(x_distance **2  + y_distance **2 )
        return distance
        
        #radical [ x2-x2)**2   (y2-y2)**2   ]
        
        
        
    
    
location1 = Location('jahanshahr,...',400,-200)


print(type(location1)) #<class '__main__.Location'>

location1.address


location1.calculate_distance('salam')



location2 = Location('sadat abad,....',460,-400)



location1.calculate_distance(location2) #Out[39]: 208.806130178211





class PhysicalProduct(Product):
    def __init__(self,code,name,price,stock,mass,address,x,y):
        super().__init__(code,name,price,stock)
        self.mass = mass 
        
        self.base_location = Location(address=address,x_cordinate=x,y_cordinate=y)
        self.price_per_mass_meter = 1000
        
    def send(self,destination_location):
        
        distance = self.base_location.calculate_distance(destination_location)
        
        return distance * self.mass * self.price_per_mass_meter
        
        
    


dpr1= DigitalProduct('e10','anti0gravity',5 , 100 , 'https://amazon.com/dkdjshhdsgxcgzh')


dpr1.show()

'''
------------------------------
Product Name : anti0gravity
Product code : e10
    PRICE     : 5
Mojood ast
------------------------------
'''




class PhysicalProduct(Product):
    def __init__(self,code,name,price,stock,mass,address,x,y):
        super().__init__(code,name,price,stock)
        self.mass = mass 
        
        self.base_location = Location(address=address,x_cordinate=x,y_cordinate=y)
        self.price_per_mass_meter = 1000
        
    def send(self,destination_location):
        
        distance = self.base_location.calculate_distance(destination_location)
        
        return distance * self.mass * self.price_per_mass_meter
        
        
        
    
        
#==========================================
#==========================================
#==========================================
#==========================================
#==========================================
#==========================================
#==========================================

'''
text management 

.txt  --> yek file e k tohsh text vojod dre

users.txt

ali|12345|ali@gmail.com|active
sara|abc123|sara@gmail.com|active
reza|hello789|reza@gmail.com|blocked



'''


#-----def ---------

#addrese daghigeh filame
file_name = '/Users/apm/Desktop/users.txt'




with open(file_name,'r') as file:
    for line in file:
        line = line.strip()
        print(line)
        

'''
ali|12345|ali@gmail.com|active
sara|abc123|sara@gmail.com|active
reza|hello789|reza@gmail.com|blocked
'''

with open(file_name,'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split('|')
        print(parts)

'''
['ali', '12345', 'ali@gmail.com', 'active']
['sara', 'abc123', 'sara@gmail.com', 'active']
['reza', 'hello789', 'reza@gmail.com', 'blocked']
'''


users =[]
with open(file_name,'r') as file:
    for line in file:
        line = line.strip()
        parts = line.split('|')
        username = parts[0]
        password = parts[1]
        email = parts[2]
        status = parts[3]
        
        user = {'username':username, 'password':password,
                'email':email, 'status':status}
        
        users.append(user)
        
        

print(users)



def read_users():
    users =[]
    try:
        with open(file_name,'r') as file:
            for line in file:
                line = line.strip()
                parts = line.split('|')
                username = parts[0]
                password = parts[1]
                email = parts[2]
                status = parts[3]
                
                user = {'username':username, 'password':password,
                        'email':email, 'status':status}
                
                users.append(user)
        
        return users
    
    except Exception as e:
        return None
            
            
            
users = read_users()
        
print(users)
'''
[{'username': 'ali', 'password': '12345', 'email': 'ali@gmail.com', 'status': 'active'}, {'username': 'sara', 'password': 'abc123', 'email': 'sara@gmail.com', 'status': 'active'}, {'username': 'reza', 'password': 'hello789', 'email': 'reza@gmail.com', 'status': 'blocked'}]
'''


def find_user(username):
    
    users = read_users()
    
    for user in users:
        if user['username']==username:
            return user
    
    
    
find_user('ali')

'''
{'username': 'ali',
 'password': '12345',
 'email': 'ali@gmail.com',
 'status': 'active'}
'''


def valdiate_password(password):
    
    #if  lenb()
    #isdigit
    
    return True


    #return False


def add_user(username,password, email,status):
    
    result = find_user(username)
    
    if result :
        print('Duplicated username')
        return False
    
    
    #if pass
       
   #if not valdiate_password()L
   #   retur false
   
   #if not validate_emali():
       
       
    if status not in ['active','blocked']:
        print('nemishe fgth active o blocked')
        return False
    
    #if result is not None :
      # raise
    
    line = f'{username}|{password}|{email}|{status}'
    
    try:
        with open(file_name , 'a') as file :
            file.write(line)
            
            print('sucessfull')
            return True
            
    except Exception as e:
        return None
    
    
        
    
add_user('ali','32232','dssdds','active')
'''
Duplicated username
Out[55]: False
'''

add_user('vahid','123456','vahid@gmail.com','active') #Out[56]: True


read_users()
'''
[{'username': 'ali',
  'password': '12345',
  'email': 'ali@gmail.com',
  'status': 'active'},
 {'username': 'sara',
  'password': 'abc123',
  'email': 'sara@gmail.com',
  'status': 'active'},
 {'username': 'reza',
  'password': 'hello789',
  'email': 'reza@gmail.com',
  'status': 'blocked'},
 {'username': 'vahid',
  'password': '123456',
  'email': 'vahid@gmail.com',
  'status': 'active'}]

'''


find_user('vahid')
'''
{'username': 'vahid',
 'password': '123456',
 'email': 'vahid@gmail.com',
 'status': 'active'}
'''


def nime_delete_user(username):
    
        
    users = read_users()
        
    my_user = find_user(username)
    
    if my_user in users:
        
        users.remove(my_user)
        
    else:
        return False
        
        
        
def delete_user(username):
    
    users=read_users()
    clean_users=[]
    
    found= False
    
    for user in users:
        if user['username']==username:
            found = True
            
        else:
            clean_users.append(user)
            
    if found:
        
        with open(file_name,'w') as file:
            for user in clean_users:
                file.write(f"{user['username']}|{user['password']}|{user['email']}|{user['status']}\n")
            
            return True
        
    else:
        print('not found')
        return False
        
    

        
delete_user('sara')        
            
            
read_users()
'''
[{'username': 'ali',
  'password': '12345',
  'email': 'ali@gmail.com',
  'status': 'active'},
 {'username': 'reza',
  'password': 'hello789',
  'email': 'reza@gmail.com',
  'status': 'blocked'}]
'''


find_user('sara') #find_user('sara')

#def login o...


class User:
    def __init__(self,username,passwrod,email,status):
        self.username = username 
        self.password = password 
        self.email = email 
        self.status = status
        
        
    def to_format(self):
        formatted_name = f'{self.username}|{self.password}|{self.email}|{self.status}\n'
        return   formatted_name 
    
    
    def __str__(self):
        return f'User:{self.username}'


#user1 = User('ali',1234,ali@gamil,active)
#user1.to_format()      
        
        

class FileManager:
    def __init__(self,file_name):
        self.file_name = file_name
        self.users =[]
        
        
    
    def read_users(self):
        with open(file_name,'r') as file:
            for line in file:
                line = line.strip()
                parts = line.split('|')
                username = parts[0]
                password = parts[1]
                email = parts[2]
                status = parts[3]
                
               # user = {'username':username, 'password':password,
                #        'email':email, 'status':status}
                
                user = User(username,password,email,status)
                
                self.users.append(user)
        



    def is_user_found(self,username):
        self.read_users()
            
        for user in self.users:
            if user.username==username:
                return True 
            
        return False
    
    
    
    def find_user(self,username):
        if self.is_user_found(username):
            for user in self.users :
                if user.username == username:
                    return user 
    


    def add_user(self,username,password,email,status):
   
        if not self.is_user_found(username):
            
            #username|password|email|status
            my_user = User(username,password,email,status)
            formatted_text = my_user.to_format()
            
            with open(self.file_name ,'a') as file :
                file.write(formatted_text)
                return True
            
        return False
            
        
    def delete_user(self,username):
        '''
        
        delete is not worked yet --> fix next sesson
        '''
        
        if self.is_user_found(username):
            my_user = self.find_user(username)
            
           # print('my_users',my_user)
            
           # print('len userd before remove',len(self.users))
            
            #self.users.remove(my_user)
            
           # print('len userd',len(self.users))
            clean_users=[]
           
            for user in self.users:
                if user.username!=username:
                    clean_users.append(user)
                   

            with open(self.file_name, 'w') as file:
                
                print('ejra')
            
                for user in clean_users:
                    print('ejra write')
                
                    file.write(user.to_format())
            
                return True

        else:
            return False
        
        
    def login(self,username,passwrod):

        if self.is_user_found(username):
            user = self.find_user(username)
            if user.passwrod == passwrod:
                return True
            else:
                return False
            
        else:
            return False
        
        

        
        
        
users_file_manager = FileManager(file_name='/Users/apm/Desktop/users.txt')
     

users_file_manager.read_users()


users_file_manager.is_user_found('ali') #Out[72]: True

users_file_manager.is_user_found('hamid') #Out[73]: False



my_users = users_file_manager.users
my_users[0].username #Out[87]: 'ali'
my_users[1].username #Out[88]: 'sara'
my_users[2].username #Out[89]: 'reza'

users_file_manager.is_user_found('vahid') #Out[107]: False



users_file_manager.add_user('vahid','1234565657','vahid@gmail.com','active')

#Out[108]: True



users_file_manager.is_user_found('vahid') #Out[109]: True



users_file_manager.delete_user('ali')


#  FileManager(file_name='/Users/apm/Desktop/customers.txt')




            