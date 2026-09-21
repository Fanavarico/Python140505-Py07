"""
L7

Created on Fri Sep 18 15:23:16 2026

@author: Ali Pilehvar meibody


"""


#------Functions----------------
'''

Functions ---> 



voroodi ---> [BOX] ---> Khoroji

vorodi1,2,... ---> [BOX] --> kjhoroji1,2,.....


sakhtar (structure)


def esme_tabe(v1,v2,v3):
    logic ()mantegh
    return o1,o2




'''


#step1 --> defintion (sakhtan)


def jam(numb1,numb2):
    result = numb1 + numb2
    return result



#step2 --> call , seda zadan, estefade

#zarf = jam(10,20)
zarf = jam(numb1=10,numb2=20)

#hich frghi in dita nadaran baham 


#yejk zarfe movaghati msize bename numb1 =10 
#numb2 =20

#mire ejra mikone --> badane (boyd)  tabe





def jam(numb1,numb2):
    result = numb1 + numb2
    print(result)
    
    
    
jam(10,20)

#dige niaz b zarf nist

#numnb=10 , numb2=20

#20+10 -->30
#print(30) -->30

#chizi nemigam baresh gardoon

#niazi b zarf nis

#zarf -->

zarf = jam(10,20)

print(zarf) #None 


#tabe ha besorate by default (pish farz) , None mifrstand


#magar inke ma moshakhas konim khoroji ro


def jam(numb1,numb2):
    result = numb1 + numb2
    print(result)
    return result
    result2 = numb1 - numb2 
    return result2 


zarf = jam(10,20)
    
    
print(zarf) #30

#edameye code dige ejra nmsihe vaghty tabve be return mirese




def calculator(numb1,numb2,operator):
    if operator=='jam':
        result = numb1 + numb2
        return result
        A = 10 
        b= A+40
        
    elif operation =='tafrigh':
        result = numb1 - numb2
        return result
        
    
    





def jam(numb1,numb2):
    result = numb1 + numb2
    #print(result)
    return result


zarf = jam(10,20)



#-----nokteye --> 40 min gioftm
#chanta khoroji dashte

'''
numb1 -->        ---> tafrigh
numb2 ---> Box  ---> jam



'''

def jam_tafright(numb1,numb2):
    result_jam = numb1 + numb2
    result_tafrigh = numb1 - numb2

    return result_jam

zarf = jam_tafright(10,20) 
print(zarf) #30 --> result jam 


def jam_tafright(numb1,numb2):
    result_jam = numb1 + numb2
    result_tafrigh = numb1 - numb2

    return result_tafrigh

zarf = jam_tafright(10,20) 

print(zarf)  #-10 --> result ertafrigh



#dota khroji


#tavabe vaghty yedone khoroji mide -> zarfi ke mizarim joosh
#baste be oon khroji, int, float, complex, str, bool, list ,...




def jam_tafright(numb1,numb2):
    result_jam = numb1 + numb2
    result_tafrigh = numb1 - numb2

    return result_jam ,result_tafrigh


#zamani chandin khoroji (bish az 1 khoroji) outpu1 , outpu2 ,...
#hamro mziare tooye yek tuple va pas mide --> baz ye khoroji pas mide tabe
#ama khorje tuple -> toosh khoroji ha hastan




zarf = jam_tafright(10,20)

#in dot afrghi ndrn
zarf = jam_tafright(numb1=10,numb2=20)


#choon tabe , vaghty chandind khoroji dare
#khoroji haro dakhele yek TUPLE mirize va pas mide


print(type(zarf)) #<class 'tuple'>

print(zarf) #(30, -10)
#do ta khoroji

#b khoroji avali dastresi

zarf[0] #Out[11]: 30
zarf[1] #Out[12]: -10


#unpacking ---> anjam bedi


#agar bedonam dota zarf pas midde

#bjaye inke yek zarf bezarim va oon zarf beshe tupel --> [index] azash khroji begiri
#zarf = jam_tafright(numb1=10,numb2=20)

#chon tabe dota khoroji dare ma mitonim jolosh dota zarf bzrim

zarf1 , zarf2 = jam_tafright(numb1=10,numb2=20)

print(zarf1) #30
print(zarf2) #-10





#print(result_jam) #NameError: name 'result_jam' is not defined
#print(result_tafrigh) #NameError: name 'result_tafrigh' is not defined
#choon zarf ha (variable) haye dakhele tabe temporary (movaghat) hastan -> Local Global nistan



#----
#be in vorodi ha , esme bvariable ha migan parametre tabe

def jam_tafright(numb1,numb2):
    result_jam = numb1 + numb2
    result_tafrigh = numb1 - numb2

    return result_jam ,result_tafrigh


#vaghty mikhay tabe ro seda bezani , vorodi haeiu k toosh mziari -- > argument


#parametr --> esme varibale haee to jolo tabe mogheye define hast
#argument --> esme variable haee ke jolo tab emizari vaghty call mikonish


#argument ha --> do dast emitoni bedi --> keyword argumnet bedi ya positional


#keyword arguments
jam_tafright(numb1=10,numb2=20) #Out[17]: (30, -10)


#positional arguments
jam_tafright(10,20) #Out[18]: (30, -10)


#amalkardi ina yeksanan
#ama b in nahveye argument gozahstanet migan chi?


#avali migan--> keyword
#dovomi migan --> positional





jam_tafright(10,20,30) #TypeError: jam_tafright() takes 2 positional arguments but 3 were given
jam_tafright(10) #TypeError: jam_tafright() missing 1 required positional argument: 'numb2'

#age kamtar az required argument (argument hae k niaz dare) shoam adad bedi
#age bekhay errror nakhori

#age trf fght numb1 ro dad, numb2 ro default bezar 10
#age ham numb2 ro dad overwrite --> numb2


def jam_tafright(numb1,numb2=10):
    result_jam = numb1 + numb2
    result_tafrigh = numb1 - numb2

    return result_jam ,result_tafrigh



jam_tafright(numb1=10,numb2=20) #Out[21]: (30, -10)

#nokte --> age vorodi dovomo nadam -> error nmide
#chon neveshte shdoe , agar user nadad -> pish farxz numb2=10

jam_tafright(numb1=10) #Out[22]: (20, 0)






#vorodi(sal) --> box --> senamo
#shamsi
def calculate_age(sal):
    sen = 1405 - sal
    return sen


#miladi --> 
def calculate_age(sal):
    sen = 2026 - sal
    return sen





#--------
#sal , tarikh ---> []box  ---> sen



def calculate_age(sal,tarikh):
    
    if tarikh.strip().lower() == 'shamsi':
        sen = 1405 - sal
    elif tarikh.strip().lower() == 'miladi':
        sen = 2026 - sal
    else:
        #print('ya shamsi ya miladi')
        raise ValueError('Ya Shamsi ya miladi')
        #ZeroDivisionError()
        #ValueError()
        #FileExistsError()
        #FileNotFoundError()
    
    return sen

calculate_age(1370,'shamsi') #Out[24]: 35

calculate_age(1991,'miladi') #Out[26]: 35

calculate_age(1412,'ghamari')

calculate_age(1991)
#TypeError: calculate_age() missing 1 required positional argument: 'tarikh'







def calculate_age(sal,tarikh='miladi'):
    
    if tarikh.strip().lower() == 'shamsi':
        sen = 1405 - sal
    elif tarikh.strip().lower() == 'miladi':
        sen = 2026 - sal
    else:
        #print('ya shamsi ya miladi')
        raise ValueError('Ya Shamsi ya miladi')

    return sen


#behshe error nmide --> default miladi dar nazar migire
calculate_age(1991) #Out[29]: 35

#na error migire
#ham inke calculate_age(1991,tarikh='miladi')

calculate_age(1380,tarikh='shamsi')  #Out[30]: 25





'''

def range(end, start , step):
    


def range(end, start=0 , step=1):
    



'''
#positional argument
range(0,100,1)

#keyword argument
range(start=0,stop=100,step=1)

#avalinek ag yedon e vrodoi --> error nmidad
#khodesh mifhmid manzoret hast --> sgtat=0 , step=1
range(100)  #----> 0 ta 100 1 





#---------------------------------------------
#---------------------------------------------
#---------------------------------------------
#-----------Mohem tarin nokte-----------------
#---------------------------------------------
#---------------------------------------------
#----tamiz , clean code bezanid




#Vaghty tamzi bvenisid--> mabngesh rahat tare
#vaghty clean bashe code --> debuging, peyda kardane bug rahat tare
#khdoeton codetono bebinid --> behtar mifhmidesh
#vaghty yek fard (shekrat) , review kone, confirm kone , resume ro
#--> tamiz bashe --> ham mifhme chikar krdi ham olaviateshe -->codi minevsiid tamiz bashe 10 ta karmand befhaman

#dar asre agentice emrozi --> codeton tamiz bashe --> agent ha ham behtr mifhman




#-----
#esme tabe ya variable nmitone reserve shdoe bashe (narenji banafsh)


#def max(list)

#def max(list):
    
    
'''
def MAX(LIST):
    
    
def max2(list2):
    
    
    
def max_(list_):
    
    
def my_max(my_list)
'''

#esm haye variable , tabe --> mafhom dashte bashe --> yek fard codeton ro mibine


#ba negah be esme tabe --> kole karesh malom she
#ba negah b esme vorodi befshmim vorodi chi mikhad
#va tamame zarf haye dakhel




#type hint --> hata begim che typi ro ma expect (enteza) darim

#type hint --> eerror nmdie --> hint(komak)



def calculate_age(sal,tarikh='miladi'):
    

    if tarikh.strip().lower() == 'shamsi':
        sen = 1405 - sal
    elif tarikh.strip().lower() == 'miladi':
        sen = 2026 - sal
    else:
        #print('ya shamsi ya miladi')
        raise ValueError('Ya Shamsi ya miladi')
    
    return sen





def calculate_age(sal : int ,tarikh='miladi'):
    
    if tarikh.strip().lower() == 'shamsi':
        sen = 1405 - sal
    elif tarikh.strip().lower() == 'miladi':
        sen = 2026 - sal
    else:
        #print('ya shamsi ya miladi')
        raise ValueError('Ya Shamsi ya miladi')
    
    return sen

calculate_age(10.22332) #agr ashari gzoasht ham




def calculate_age(sal ,tarikh='miladi'):
    
    a = type(sal)
    print(a)
    
    if tarikh.strip().lower() == 'shamsi':
        sen = 1405 - sal
    elif tarikh.strip().lower() == 'miladi':
        sen = 2026 - sal
    else:
        #print('ya shamsi ya miladi')
        raise ValueError('Ya Shamsi ya miladi')
    
    return sen

calculate_age(sal=1380) #<class 'int'>



def calculate_age(sal ,tarikh='miladi'):
    
    if type(sal) == int:
        if tarikh.strip().lower() == 'shamsi':
            sen = 1405 - sal
        elif tarikh.strip().lower() == 'miladi':
            sen = 2026 - sal
        else:
            #print('ya shamsi ya miladi')
            raise ValueError('Ya Shamsi ya miladi')
        
        return sen
    else:
        raise ValueError('bayad sen ro int vared koni')


calculate_age(1380)

calculate_age(12.323) #ValueError: bayad sen ro int vared koni





def calculate_age(sal ,tarikh='miladi'):
    
    if isinstance(sal , int):
        if tarikh.strip().lower() == 'shamsi':
            sen = 1405 - sal
        elif tarikh.strip().lower() == 'miladi':
            sen = 2026 - sal
        else:
            #print('ya shamsi ya miladi')
            raise ValueError('Ya Shamsi ya miladi')
        
        return sen
    else:
        raise ValueError('bayad sen ro int vared koni')

#jolosho begiri



#type hint --> jolosho nmigire , flaot komak mikone cleaning






#docstring benevisid

def calculate_age(sal:int,tarikh='miladi'):
    '''
    This function is used for calculation of age by year
    
    
    
    Parameters
    ----------
    sal : int
        this is the heay you born.
    tarikh : int, optional
        this is calender type . by default is 'miladi'

    Raises
    ------
    ValueError
        when you insert something rather than Miladi and shamsi.

    Returns
    -------
    sen : int
        this is calculated age.

    '''
    
    if tarikh.strip().lower() == 'shamsi':
        sen = 1405 - sal
    elif tarikh.strip().lower() == 'miladi':
        sen = 2026 - sal
    else:
        #print('ya shamsi ya miladi')
        raise ValueError('Ya Shamsi ya miladi')
    
    return sen





def calculate_age(sal:int,tarikh='miladi'):
    '''
    

    Parameters
    ----------
    sal : int
        sale tarikhe tavalod.
    tarikh : str, optional
        noe tarikh ra beguid. The default is 'miladi'.

    Returns
    -------
    None.

    '''






def jam(numb1,numb2):
    result = numb1 + numb2
    return result


#positional --> 
jam(10,20) #Out[31]: 30

#keyword
jam(numb1=10,numb2=20)


#tooye joftesh behet javab mide


#sjhoma gahi mikhay fght positional argument begire

#ya fght keyword argument


#har parametri bad az * --> keyword arguments

def jam(*,numb1,numb2):
    result = numb1 + numb2
    return result

jam(10,20) #TypeError: jam() takes 0 positional arguments but 2 were given
jam(numb1=10,numb2=20) #Out[34]: 30




#-----
#harchi ghabl az / biad -> fght positional
def jam(numb1,numb2,/):
    result = numb1 + numb2
    return result


jam(10,20) #Out[35]: 30
jam(numb1=10,numb2=20) #TypeError: jam() got some positional-only arguments passed as keyword arguments: 'numb1, numb2'


#--------
def alaki(a,b,c,d):
    return True


alaki(10,20,30,40) #posigtional
alaki(a=10,b=20,c=30,d=40) #keywordi




def alaki(a,b,/,*,c,d):
    return True

#onaei ke poshte / hastand --> fght positional (adad)
#onaei ke bad az * hastand --> fght keyword (esm)

alaki(10,20,c=30,d=40)





alaki(10,20,d=40,c=30)


def alaki(a,b,c,/,*,d):
    return True


alaki(10,20,30,d=40)





#--------------------------------
#--------------------------------
#--------------------------------
#dota nokte yek tabe 
#adad nmigire, list begire

#man yek tabe mikahm k 5 ta adad begire --> behem bishtrinesho bde

def max_5(v1,v2,v3,v4,v5):
    my_list= [v1,v2,v3,v4,v5]
    my_max = max(my_list)
    return my_max

max_5(10,20,30,40,50) #Out[41]: 50





def max_(my_list):
    my_max= max(my_list)
    return my_max



my_list = [10,20,30,40,50]
max_(my_list)
    

max_([10,20,30,40,50])



#list, tuple, set , dictionary


#------chandind tabe ke dairmo 



#-------sum----------
#dakheli
sum([10,20,30,40,50]) #Out[43]: 150


#1 vorodi (liste) ---->BOX --> khoroji (1 adad)


#in tabe ro khodemon besazim


def my_sum(my_list):
    total=0
    for element in my_list:
        total = total + element
        #return total
    
    return total
        
        
my_sum([10,20,30,40,50]) #Out[45]: 150

sum([10,20,30,40,50]) #Out[48]: 150
    


#-----len------

def my_len(my_list):
    count = 0 
    for element in my_list:
        count = count + 1
    return count
        
        


my_len([10,20,30,40,50]) #Out[46]: 5
len([10,20,30,40,50]) #Out[47]: 5




#------- Azinja recode bayad beshe ta inja

#--------average
#list --> mianginesho hesab mikone
def average(my_list):
    miangin  = sum(my_list) / len(my_list)
    return miangin




def average(my_list):
    miangin  = my_sum(my_list) / my_len(my_list)
    return miangin


#2 ta tabe , toye yek tabam az on dota estefade krdm

average([10,20,30,40,50]) #Out[48]: 30.0



#niaz b tavabe ghabli

def average(my_list):
    count = 0 #--> len
    total = 0 #--> sum
    for element in my_list:
        count = count + 1 
        total = total + element
        
        
    miangin = total/count
    return miangin


        
    

#sum()/len()
    

my_list = [10,20,50,40,30] 

   
def my_max(my_list):
    maximum = my_list[0]
    
    for element in my_list :
        if element > maximum:
            maximum = element
    
    return maximum



my_max(my_list) #Out[49]: 50

max(my_list) #Out[50]: 50


    
    
    
def my_min(my_list):
    minimum = my_list[0]
    
    for element in my_list :
        if element < minimum:
            minimum = element
    
    return minimum
    

my_list = [10,20,50,40,1,4343343343,30] 

my_min(my_list) #Out[52]: 1
min(my_list) #Out[53]: 1




#list --> str ham haminkaro konima 

string = '32329329322123'
maximum = string[0]
for element in string:
    if element> maximum :
        maximum  = element
     
        
#-----------------------------------
#list darim --> [10,20,30,10,50,10,20,40,80]
#most frequent --> bishtarin tekrar ro dare 

#[10,20,30,10,50,10,20,40,80] ---> box -> 10

my_list = [10,20,30,10,50,10,20,40,80]

'''
{
 '10'  : 3
 
 '20' : 2
 
 30 : 1
 
 50  :1
 
 40  : 1
 
 80 : 1

 
 }




'''





my_list = [10,20,30,10,50,10,20,40,80]

my_dict = {}


for element in my_list:
    if element not in my_dict:
        my_dict[element] = 1
    else:
        my_dict[element] = my_dict[element] + 1
        
        
        

#_------

my_list = [10,20,30,10,50,10,20,40,80]

my_dict = {}


for element in my_list:
    if element in my_dict:
        my_dict[element] = my_dict[element] + 1
    else:
        my_dict[element] = 1
        

print(my_dict)
'''
{10: 3, 
 20: 2, 
 30: 1, 
 50: 1, 
 40: 1, 
 80: 1}

'''


for i in my_dict:
    print(i)
        
        
for i in my_dict.items():
    print(i)
'''
(10, 3)
(20, 2)
(30, 1)
(50, 1)
(40, 1)
(80, 1)
'''

for i,j in my_dict.items():
    print(i)
    print(j)

'''

10
3
20
2
30
1
50
1
40
1
80
1

'''


for key,value in my_dict.items():
    print(key)
    print(value)





'''
{10: 3, 
 20: 2, 
 30: 1, 
 50: 1, 
 40: 1, 
 80: 1}

'''

maximum_count = 0

for key,value in my_dict.items():
    if value>maximum_count:
        maximum_count = value
        maximum_element = key
        
        
        
print(maximum_count) #3
print(maximum_element) #10








def find_most_frequent(my_list):
    '''
    
    My_list : List   
    
    Output : element --> most freequent
    
    '''
    
    my_dict = {}
    for element in my_list:
        if element in my_dict:
            my_dict[element] = my_dict[element] + 1
        else:
            my_dict[element] = 1
            
    #yek --> my_dict --> {keys : number , values : ttedadesh}
    
    
    maximum_count = 0

    for key,value in my_dict.items():
        if value>maximum_count:
            maximum_count = value
            maximum_element = key
            
    return maximum_element
        
    

find_most_frequent([10,20,30,10,10,10,10,10,20])
#Out[64]: 10



        


#---------------------
sentence = 'I love python and i want to learn python every day and I am going to learn deep learning '

#peyda konam -> boishtarin kalame tekrar shode chie?

#def -->

#find_most_frequent_in_sentence( string)

#bishtarin kalameye tekrar shode ro peyda mikone bva pas mide

#find_most_frequent(list) --> most

#string bedam --> bishtrin word (strin)


#1-string -->  string




find_most_frequent(sentence) #Out[67]: ' '


sentence.split(' ')

'''
['I',
 'love',
 'python',
 'and',
 'i',
 'want',
 'to',
 'learn',
 'python',
 'every',
 'day',
 'and',
 'I',
 'am',
 'going',
 'to',
 'learn',
 'deep',
 'learning']

'''



def find_most_frequent_in_sentence(sentence):
    words_list = sentence.split(' ')
    
    most_frequent_elemnt = find_most_frequent(words_list)
    return most_frequent_elemnt
    

find_most_frequent_in_sentence(sentence) #Out[70]: 'I' #Out[72]: 'python'




#----------------------------------------------
#------- Python modules and Packages --------
#-----------------------------------------------


#ta inja ma code mizdim  --> alan man 950 khat code zdm dakhele .py 

#file .py darim --> kolan be .py file ha migam --> module

#vaghty varede yek company, startup , app mishim -->
#ma masalan 180 K lines 4 month 

#app --> 180 k khat code dare --> .py nevesht enashdoe

#too chandind .py neevshte mishe --> chandin madules

#package ---> chandin modules kenare ham



#yek file misazam bename calculator.py



'''
----Desktop
     |
     |---l7.py
     |---calculator.py

'''

JAM(10,20)
#NameError: name 'JAM' is not defined


#import kardan

#boro az file calculator.py import kon function JAM


#from calculator.py import JAM  

from calculator import JAM  

JAM(10,20) #Out[5]: 30


#az calculator import kon yek tabe e bename JAM
from calculator import JAM

JAM(10,20)



#import --> package
#**dakhele package
import calculator.JAM
calculator.JAM(10,20)




from calculator import JAM as j
#az file e calculator.py import kon JAM ro , mokhafafesh j

#JAM(10,20)
j(10,20)


#from sklearn.neural_network import MLPRegressor as ml


#chandin tabe ogvord?
#inaro beshnas mna dastresi be ina daram
from calculator import JAM , TAFRIGH


JAM(10,20) #Out[7]: 30

TAFRIGH(10,20) #Out[8]: -10

JAMM()


#-------
#SHODANI -->MISHE
#PROFESSIONAL
from calculator import *

#harchi ke hasto nist
JAM(10,20)

#1-->b ram feshar maire, 1000000 tabe bashe
#2--> onmoghe shoma ocde mizni JAMM -> erro


JAMMMMMMMMMM(10,20)


#---------------------
#---------------------
#---------------------

#--> berid be package --> my_package_l7 negah konid

#from users.signup import sign_up



'''
--my_packages
	| main.py
	| users\
	|----------information.py
	|----------signup.py
	|----------login.py
	| plans\
	|----------price.py
	|----------buy.py
	|----------credit.py
	| data\



vaghty tooye main.py

from users.information import har_function

from plans.buy import ...



#--------------


--my_packages
	| main.py
	| users\
	|----------information.py
	|----------signup.py
	|----------login.py
	| plans\
	|----------price.py
	|----------buy.py
	|----------credit.py
	| data\

buy.py yek fucntion az price.py
hgarjaei az folder plans bekhahi chizi vrdari

tooye buy mikhay  az yek function az price estefade

--->buy.py
from .price import .....

--->buy.py hastam
from ..users.information import login

'''


#l7-->desktop
#claculator -->desktop
#app -->desktop

from calculator import JAM


from calculator import a
print(a) #10


from calculator import USERS



from calculator import JAM 



'''

functions, class, variables 

dakhele yek .py (madules) --> directory (folder package)


va importeshon mikonim


har file .py --> __name__


khode file ro run mikone __name__ == 'main'

'''


from calculator import JAM


'''
har file e .py yekchzii dar delesh dare

bename __name___


agar yek file sakhtid ke khast 

ham variable,function , .. too delesh vbashe baraye import--> dakhele yek file .py 





'''



'''
chandin malsle 5,6 masale --> function ha


3 ta masale --> import ha hastand --> yad begirid


in hafte --> jalse baraye --> onine --> 20 task



---
l8 --> ayande --> standard python libraries , packages (pip) , read,write Input/output file (file management)
Try exception ro mikhonim

pish niazesh -->
1- Function
2- Import ha



'''




'''
Tamrin ----->


4 ta soal darim --> 3 ta soal mortabet be tavabe hast
1 soal mortabet be packages





1- yek dictionary aZ mahsoolat darim 

products = {
'laptab': 1200,
'phone': 800,
'tablet': 500,
'headphone': 150,
'mouse': 50
}


Chandin tabe benevisid ke in dictionary ro besoorate vorodi begire
va


- bishtarin gheymat ro pas bede
- esme mahsoli ke bishtarin gheymat ro dare pas bede
- hamin 2 taro baraye **kamtarin** ham anjam dahid
- jame kole mahsoolat ro pas bede
- miangine kole mahsolat ro pas bede



2- yek dictionary az mahsolato mojodi ro darid , in ro be soorate vorodi yek atbe migire
va do khoroji mide, do ta list mide ke yeki list esme mahsolati hast ke
mojodi darand , yeki list mahsolati ke mojodi nadaand

inventory = {
    "apple": 20,
    "banana": 5,
    "orange": 0,
    "milk": 12,
    "bread": 0
}



3- Yek tabe benvisid ke yek listi az karmandan ba etelaatesho migire


employees = {
    "E01": {
        "name": "Ali",
        "age": 28,
        "salary": 3000
    },

    "E02": {
        "name": "Sara",
        "age": 32,
        "salary": 4500
    },

    "E03": {
        "name": "Reza",
        "age": 25,
        "salary": 2800
    }
}


- balatarin hoghogh ro harki migire esmesho pas bedde
- kamtarin hogh ro harki migire esmesho pas bede
- yek listi az esme afradi k hoghoghe bish az 3000 migiran pas bede
- do vorodi begire tabe, yeki in dictionary (employees) yeki ye adad ke bedre liste esme afradi ke hoghoghe bishtar az oon adad ro migiran ro pas bede
- miangine kole hoghogh haro pas bede




3- yek tabe benevisid ke yek listi az tuple ha dare o ino be onvane vorodi migirie

sales = (
    ("Ali", "Laptop", 1200),
    ("Sara", "Phone", 800),
    ("Ali", "Phone", 800),
    ("Reza", "Laptop", 1200),
    ("Sara", "Laptop", 1200),
    ("Ali", "Mouse", 50)
)


- yek tabe benvisid  ke khoroji yek dictionary bede ke har fard yek key hast va jolosh jame kharidesho zade
- yek tabe benevisid ke khorojish yek dictionary bede ke key ha esme mahsolat bashe va jolosh tedde foroshe mahsolat
- yek tabe benevsiid ke khoroji ye adad bede ke majhmooe daramade foroshgah hast






--------------------------------
--------------------------------
--------------------------------
--------------------------------


4 - Yek folder besazid bename bank_package ke 

shoma bayad yek folder va dfile haei injori besazid:


bank_project/
│
└── bank/
    │
    ├── account.py
    ├── fees.py
    │
    └── app/
        ├── main.py
        └── calculator.py


shoma dakhele account.py yek tabe benevisid bename show_balance(balance) ke yek vorodi migire va khoroji 
*100 mikone o pas mide


dar calculator.py yek tabe benevisid bename deposit(balance,amount) ke biad balance ro be alaveye amoutn kone va pas bede


dar file fees.py yek tabe bename apply_fee(balance,fee) ke az balance fee ro kam kone va pas bede


dar tabeye main.py shoma bayad yek script benevsiid ke hamchin chizi

```python
balance = 1000

print(show_balance(balance))

balance = deposit(balance, 500)
print(show_balance(balance))

balance = apply_fee(balance, 50)
print(show_balance(balance))

```


kole taklife shoma do chiz hast , 1- inke tabe haro takmil konid
2- dar main.py import haro benevisid.






'''











