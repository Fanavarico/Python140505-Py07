"""
In The name of GOD


Created on Fri Oct  2 15:25:59 2026

@author: Ali Pilehvar Meibody

L9




python built in functions, keywords (if,else, for , while,...) ,variables (int,float,iterables)
---> Functions




ma se no code nevisi darim 


1- Monolothic --> script --> .py minevisid --> run mikonid

2- Function -based --> modular --> yani koli folder , va dar har folder
file haye .py --> dar har .py --> koli fucntion darim
yek file main.py darim ke hamaro import mikonim va use mikonim


3- Object oriented programming (OOP) --> class and objects


fike haye moteade misazid ---> Package misazid



"""

#---------------------Function ha begim----------

def name(variabl1,variabl2):
    #logic
    output = variabl1 + variabl2
    return output


#ma mitavanim kole yek logic ro tabdil konim be yek capsul
#yek capsul (box) ke vorodi migire va khorojhi midadah




#---> Error --> shoma bayad dar file i ke tavabe mizarid
#user.py --> 10 ta function mizarid -> tamame tavabe bayad
#errror dasht ebashand



def bardasht(mojoodi,meghdar):
    
    mojoodi_jadid = mojoodi - meghdar
    
    return mojoodi_jadid






def bardasht(mojoodi,meghdar):
    
    if mojoodi ==0:
        raise ValueError('mojodi 0 hast')
        
    elif mojoodi < meghdar :
        raise ValueError('Mojoodi kafi nemibashad')
    
    elif meghdar <0 :
        raise ValueError('Meghdar nemitavand manfi bashad')
    
    mojoodi_jadid = mojoodi - meghdar
    
    return mojoodi_jadid


#jalase gozahste darmorede RAISE 
#va error type ha sohbat shod


#In jalasse noktash --> har tabe ke misazid
#bayad khatahaye pishbini shode ro raise bedid dakheelsh
#vaziefeye yek capsol , yek tbae haqts k raise ham dashte bashe



#estefade ??

#ino aya user mostaghim estefade mikone??

bardasht(100,)





#main.py 

#file --> karesh ychize dgas

#ma tavbeye khodmeono 

#folder --> modiriate_hesab/
#dakhelesh --> bardasht.py 

#tavabe ye mortabet be bardasht injas 


#gaurdrails (safe) , indirect (direct nist)

 
#hadafe aslie raise --> joloye kar kardan tabe ro begirid


'''
main.py

dokmeye 20000 --> main_bardasht(200000)

dokmeye 40000 --> main_bardasht(400000)


.....



@get(/bardasht)
def main_bardasht(amount):
    
    #ghesmate amniati
    check_ip()
    if check_ip == iran =
        yekari mikone
        
        
    #ghesmate sabte etelaat --> logging
    if shobe==
        sabte_moshakahsat(saat, shobe, fard,...)
        
    .........
    
    
    #amniati --> chandin laye amniati hast
    if validate_amount(amount)
    
    
    
    #etelaaate moshtari ro bedast miare
    #(7 sal pish) --> shomare kart
    
    
    #yekseri tavabe darim shomare_kart --> BOX --> etelaat
    
    zarf = return_name_by_card_number('6104.....')
    
    mojodi = return_mojoodi('6104.....')
    
    mojodi = return_mojodi(shomare_kart)
    
    
    mojoodi = bardasht(mojodi , amount)
    
    #sabt kone tarkaonesh ,,....
    
    return {'success':True, 'message':'برداشت با موفقیت انجام شد'}
    
    
    




'''




#main.py nistya --> tamame tavabeye package --> raise bezarim --> ok




#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------
#bardasht.py
def bardasht(mojoodi,meghdar):
    
    
    
    if mojoodi ==0:
        raise ValueError('mojodi 0 hast')
        
    elif mojoodi < meghdar :
        raise ValueError('Mojoodi kafi nemibashad')
    
    elif meghdar <0 :
        raise ValueError('Meghdar nemitavand manfi bashad')
    
    mojoodi_jadid = mojoodi - meghdar
    
    return mojoodi_jadid



#main.py

#from account_management.bardasht import bardasht


meghdar = float(input('meghdare bardasht ro hesab konid:'))

mojodi = 100000

new_mojodi = bardasht(mojodi,meghdar)


print('ba moafaghiat anajm shod')
print('mojodie alan : ',new_mojodi)





'''
meghdare bardasht ro hesab konid:20000
ba moafaghiat anajm shod
mojodie alan :  80000.0

'''





try:
    meghdar = float(input('meghdare bardasht ro hesab konid:'))
    
    
    mojodi = 100000
    
    new_mojodi = bardasht(mojodi,meghdar)


    print('ba moafaghiat anajm shod')
    print('mojodie alan : ',new_mojodi)

except ValueError:
    #bejaye inke error pas bdi va main.py az run biofte
    print('Amaliat moafagh amiz nabood')
    #return {success:False, 'message':'amaliat moagah amzi nabood'}
    
'''
meghdare bardasht ro hesab konid:20000
ba moafaghiat anajm shod
mojodie alan :  80000.0


fargh:

meghdare bardasht ro hesab konid:2383272837237268327328732772
Amaliat moafagh amiz nabood
'''



try:
    meghdar = float(input('meghdare bardasht ro hesab konid:'))

    mojodi = 100000

    new_mojodi = bardasht(mojodi,meghdar)


    print('ba moafaghiat anajm shod')
    print('mojodie alan : ',new_mojodi)

except ValueError:
    #bejaye inke error pas bdi va main.py az run biofte
    print('Amaliat moafagh amiz nabood')
    #return {success:False, 'message':'amaliat moagah amzi nabood'}

except TypeError:
    print('meghdare motabar vared nashode ')
    
except Exception as e:
    print("khataye gheyre ghabele pishbini etefagh oftad")
    print('amaliat moafagh nabood')
    
    #e --> zakhire db , send to telegram b admin
    
    
    
    
    




try:
    meghdar = float(input('meghdare bardasht ro hesab konid:'))

    mojodi = 100000

    new_mojodi = bardasht(mojodi,meghdar)


    print('ba moafaghiat anajm shod')
    print('mojodie alan : ',new_mojodi)
except Exception as e:
    print('amaliat moafagh nabood')





#try except --> shoma aksaran dar file main.py --> 
#vghty file e hast k bayad roo run abshe  nabayad intrupt bshe (motevaghef beshe)

#Kolesho --> try va except --> error handling mikonid

def name(var1,var2):
    try:
        c = var1 + var2
        return c
    
    except Exception as e:
        print(e)
        return 0
    
    
    
#name() --> yek amaliatio ejra mikone agh ok bod eturn mide age naabod --> error handl emikoni chi return



names=['ali','vahid','hamid']

#names -> database --> 100000000


count=0
for name in names:
    character = name[1]
    if character=='a':
        count= count + 1
    
 
print(count) #2



names=['ali','vahid','hamid','b','reza']

#names -> database --> 100000000


count=0
for name in names:
    try:
        character = name[1]
        if character=='a':
            count= count + 1
    except Exception as e:
        print(e)
        continue
    
    
    
    
    
#-------
try:
    meghdar = float(input('meghdare bardasht ro hesab konid:'))

    mojodi = 100000

    new_mojodi = bardasht(mojodi,meghdar)


   
except Exception as e:
    print('amaliat moafagh nabood')
else:
    print('ba moafaghiat anajm shod')
    print('mojodie alan : ',new_mojodi)
    



#10000 ---> ba moafaghiat anjam shod --> dakhele try
#100000000, error --> dakhgele except ejra mishe  


#---------------------------
#ch foros ch ghalat 

try:
    meghdar = float(input('meghdare bardasht ro hesab konid:'))

    mojodi = 100000

    new_mojodi = bardasht(mojodi,meghdar)


   
except Exception as e:
    print('amaliat moafagh nabood')
else:
    print('ba moafaghiat anajm shod')
    print('mojodie alan : ',new_mojodi)
    
finally:
    print('sepas gozaram')


'''

Try --> mizarid , except ham ejrbarie

try-except

else , finally --> optional
else bzar
finally bezar
nazar
joftresho bzar


else --> age doros ejra shod inam ejra kon
finally -_> ch doros ch ghalat --> in ro ejra kon




'''



try:
    meghdar = float(input('meghdare bardasht ro hesab konid:'))

    mojodi = 100000

    new_mojodi = bardasht(mojodi,meghdar)

#specific (moshakhas) ro avaz moshakahs mikoni
except ValueError:
    print('meghdar sahih nemibashad')
except TypeError:
    print('meghdar motabar nemibashad')
#gheyre ghabele entezar --> unexpected --> geenral -->error
except Exception as e:
    print('amaliat moafagh nabood') #geenral bede

#else o finally --> optionally (logice barnamt)
else:
    print('ba moafaghiat anajm shod')
    print('mojodie alan : ',new_mojodi)
    
finally:
    print('sepas gozaram')






#========================================================
#========================================================
#========================================================
#========================================================
#========================================================

#fundementale python --> 90% tadris shode
#10% --> OOP

#chizae tadris mishe --> faratar az fundementale --> pythone karbordi


'''

Python modules and packages


shoma vaghty chanta file darid , ahr file havie tavabe hast

baraye import



tarighe haye mokhtalefe imporet bood

from file import function
from file import function1,function2,...
import file.function
from file import *

from file import function as f



#-------ghanon gzoashtid

too file i k shoma run mikonid --> l1.py ,.. main.py 
bayad ba esm import konid


main.py
config.py


az config chizi biari to main
from config import function



main.py
/folder1
    config.py
    
from folder1.config import function



from folder1.folder_dKheli.........config import function



#------- baraye function haye doro baresh chijoir import konan az ham??

aaz yek file e hamonja import koni

main.py --> in run mishe (ghavaninehso bala goftm)
config.py
test.py

tooye config az test.py chizi vrdari
from .test import function


main.py --> in run mishe (ghavaninehso bala goftm)
config.py
accounts/
    test.py

from accounts.test import function

#inja --> main.py ham hast --:> folderam mishanse



#. kheyli estefade bsihar

main.py --> in run mishe (ghavaninehso bala goftm)
accounts/
    test.py
    config.py
    

from .test import felano





main.py --> in run mishe (ghavaninehso bala goftm)
birooni.py
accounts/
    test.py
    config.py

dakheel config az bironi yechi vrdaram

from ..birooni import function

#ghanone mohem dare --> agar .. zadi bargashti b pakcage asli (madar) 
#az hamonja address bde

from birooni import function




3 no chizi import mikonim dar python

1---> funciton haro az koja -> az file haye khodemon 
2--> python standard libraries --> ketabkhone haye standarde python
3---> external libraries 



python -> tose e dadan -> omadan -> ye package sakhtan --> toosh koli file gozashtan
va in tavabe --> kheyli mofidan (too fielde khases)

python yeseri haro . anaconda ya ba harchi python nasb mikoni --> ina ham rosh nasb mishe


folder apm/anaconda/libs/python_packages/math/

from apm.anaconda.libs.python_packages.math import function


#python --> shenasagari dare-->ketabkhone haro jashono mishnase

import math

#abzar nsi -> foldere 



import ketabkhone

ketabkhone.function1()

ketabkhone.function2()




from ketABKHONE import function1,function2
function1()
function2()



from ketabkhone import function1 as f1
f1()




'''


#===========================================================================
#===========================================================================
#===========================================================================
#===========================================================================
#===========================================================================
#===========================================================================
#===========================================================================
#===========================================================================
#===========================================================================
#===========================================================================
#===========================================================================


'''

3 ravesh code zani anjam mishe

1- monolothic -> script -> .py mizani va run mishe
python file.py --> run shod --> az bala b paein 100 khat 
function ,. functimn dakhele fodler .. --> yek file az bala ta pein euykbar run mishe



2- Function -based -->  project darid

main.py
/folder
/folder
/folder 

import bayad konid hame 0->main.py
import ha , try except ---> 





3 - Object oriented programming (OOP)

function -0-> mahdodiat daran

class --> object 
class ---> yek chizi hast ke shamele tavabe va moteghayer ha mishe

class 
    |
    function
    function2
    function3
    variabl1
    variable2
    
object



class, function --> mitone import beshe

A--> ma khodemon tabe neveshitm ,c lass nvshtim --> import --> packags and modules

B --> standard python libraries --> ketabkhone vojod dare , python hamzaman k isntall install
ketabkjone.function()    ketabkhone.class() estefade konim


C --> External libraries -> ketabkhone hastan , sherkate python
sherkat ha , danehsgah ha , developer --> tose e dadan
aval download badesh nasbeshon konimbadesh estefade konim




Chantasho yad midm


'''

#-------------------------------------------
#-------------------------------------------
#-------------------------------------------
#-------------------------------------------

'''
Ketabkhone ha --> class yad mide
---> internet --> reference --> documentation

--> donyaye emrozi --> hata ba gpt ham mishe yad grft

---> gpt berid jolo --> math --> 100000 tabe dare 

100 tabeye marofesho bhton yad bde --> 50 tasham bdonid kefayat mikone
hefz konim? --> na , fght motvajash shod, tarigheye esteafde

azin 50 tya , 5 tash estefade 


mohemtarin tavabe --> az bas estefade konid -_> by default yad migirid

'''



#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------

#bejaye inke khodeton beenvisid --> ina amadan uyani estefade

import math

#variable hastan 

math.pi #Out[15]: 3.141592653589793
math.e #Out[16]: 2.718281828459045

#tavabe ye mohemesh mishim

zarf = math.sqrt(100)
print(zarf) #10.0




#--------
from math import sqrt 
zarf = sqrt(100)



zarf= math.pow(2,3)
print(zarf) #8.0


pow(2,3) #Out[20]: 8



#-----gerd kardan

a = 10.1  #nazdik b 10 
b= 10.5  #vasate 10
c = 10.9  #nazdik b 11

math.floor(a) #Out[21]: 10  
math.floor(b) #10
math.floor(c) #10


math.ceil(a) #11
math.ceil(b) #11
math.ceil(c) #11


round(a) #Out[27]: 10
round(b) #10
round(c) #11

math.trunc(a)  #hazf mikone --> flooor()
math.trunc(b)
math.trunc(c)



math.fabs(-10) #Out[34]: 10.0
abs(-10) #Out[35]: 10




math.factorial(5) #Out[36]: 120

#5 * 4 * 3 * 2 * 1 = 120



# B M M --> bozorgtarin maghsome moshatarak

math.gcd(10,40) #Out[37]: 10



#K M M --> kochiktrin moghasome msohatarak
math.lcm(10,40) #Out[39]: 40


#-----logarithmic


#10 * 2 = 100

#log100 bar paye 10 = 2

math.log(100,10) #Out[40]: 2.0

math.log(100,2) #Out[41]: 6.643856189774725

#yekseri ->  loge makhsos

#log bar paye 120 

math.log10(100) #2


math.log2(8) #Out[43]: 3.0
math.log(8,2) #3



math.log(100) #Out[44]: 4.605170185988092
math.log(100,math.e) #Out[45]: 4.605170185988092

#default -> e 

#math.log --> LN

#e** 

math.exp(10) #Out[46]: 22026.465794806718


#------------Tavabe mosalasati---------------
#30 , 40 --> darajat

zavie = math.radians(30)

print(zavie) #0.5235987755982988

#ke betonam az tavabeye mosalasati --> math


zavie = math.radians(90)

 
math.sin(zavie) #Out[51]: 1.0


zavie = math.radians(0)


math.sin(zavie) #Out[52]: 0.0

math.cos(zavie) #Out[53]: 1.0

math.tan(zavie)


math.sinh() #sinue hyperbolic
math.cosh()
math.tanh()



#----------------
#fasleye beyne do ta noghte
#oghlidosi dashtim


#a = (x1,y2)
#b = (x2,y2)

# radical( x1 -x2)**2  + (y2 - y1)**2


a = (10,20)
b = (30,15)

math.dist(a,b) #Out[54]: 20.615528128088304



my_list=[10,20,30,40,50,60]
 

sum(my_list) #Out[55]: 210



#product
math.prod(my_list) #Out[56]: 720000000


'''
hale masaleye mohasebey masahate dayere



'''




#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
'''              Random        '''

import random 


#ye adade randomi beyne 0 ta 1 --> float
random.random() #Out[57]: 0.6920511169526059

random.random()  #Out[58]: 0.962586230939572


#yek adade randome int beyne a va b 
random.randint(10,20) #Out[59]: 12

random.randint(10,20)



for i in range(0,5):
    tas = random.randint(1,6)
    print(tas)


'''
1
6
2
5
2
'''

for i in range(0,5):
    tas = random.randint(1,6)
    print(tas)
    if tas == 6:
        tas = random.randint(1,6)
        print(tas)
    
'''
5
1
2
5
2
'''


for i in range(0,5):
    tas = random.randint(1,6)
    print(tas)
    if tas == 6:
        tas = random.randint(1,6)
        print(tas)
    
'''
6
5
2
3
1
3
'''  
    
    
    


random.randrange(10,20,2) #10 yebar , 16 


#-------
#yek adade float beyne yek a ta b 
# b do soorat 

#uniform
#tamame adade floate beyne 10 ta 20 yek shans baraye bardashte shodan darand

random.uniform(10,20) #Out[94]: 18.48854196443792



#gaussian (normal)
#Mohandesi , ejtemaei ,...
#gaussian distribution, normal distribution 


random.gauss(50, 10)

'''
random.gauss(50, 10)
Out[95]: 38.56046253653365

random.gauss(50, 10)
Out[96]: 66.0020577791648

random.gauss(50, 10)
Out[97]: 40.177808722430775

random.gauss(50, 10)
Out[98]: 61.751615776003476

random.gauss(50, 10)
Out[99]: 49.101879836007285

random.gauss(50, 10)
Out[100]: 39.69731621201995

random.gauss(50, 10)
Out[101]: 43.085278479959406

random.gauss(50, 10)
Out[102]: 45.48078300581259

'''


random.uniform(10,70)
'''
random.uniform(10,70)
Out[106]: 15.420068985875702

random.uniform(10,70)
Out[107]: 13.712820569865634

random.uniform(10,70)
Out[108]: 16.521339639306845

random.uniform(10,70)
Out[109]: 23.654139692342646

random.uniform(10,70)
Out[110]: 44.551981843837055

random.uniform(10,70)
Out[111]: 41.58842063799334

random.uniform(10,70)
Out[112]: 68.42500438926481

random.uniform(10,70)
Out[113]: 53.04502361768357

'''


#-------------------
my_list=[10,20,30,40]
my_list=['ali','vahid','hamid','reza']


random.choice(my_list) #Out[114]: 'vahid'



random.choices(my_list,k=2) #Out[116]: ['hamid', 'ali']

random.choices(my_list,k=2) #Out[117]: ['ali', 'reza']




#sang kaghza gheychi 


user_option = int(input('sang (1) ya kaghaz (2) ya gheychi (3) : '))

options = ['sang','kaghaz','gheychi']
computer_option = random.choice(options)


#----bord
#usere man : sang   , computer :  gheychi
#usere man : ghecyhi   , computer : kaghaz
#usere man : kaghaz   , computer : sang

#mosavi---------
#sang , sang
#kaghaz kaghaz
#gheychi gheychi

#1-->sang
#2-->kaghaz
#3--> gheychi

if user_option==1  and computer_option=='gheychi':
    winner = True
elif user_option ==3 and computer_option=='kaghaz':
    winner = True
elif user_option ==2 and computer_option=='sang':
    winner = True
elif user_option==1 and computer_option=='sang':
    winner = None
elif user_option==2 and computer_option=='kaghaz':
    winner = None
elif user_option==3 and computer_option=='gheychi':
    winner = None
else:
    winner = False
    
    
#if winner==True:
#    print('barande shodi')
   
if winner:
    print('barane shodi')
elif winner==None:
    print('mosavi')
else:
    print('bakhti')



# barande 3 bar bebare



#weight
prizes=['a','b','c']

random.choices(prizes,weight=[10,70,20],k=1)



#_-------shuffle ---->

import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist) #['banana', 'cherry', 'apple']


#taske badi 





random.uniform(10,20) #Out[124]: 13.691781444178304


random.uniform(10,20) #Out[125]: 16.24430096458077





random.seed(42)
random.uniform(10,20) #Out[126]: 16.39426798457884



random.seed(42)
random.uniform(10,20) #Out[127]: 16.39426798457884



random.uniform(10,20) #Out[128]: 10.25010755222667



#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------

#datetime

import datetime


zarf = datetime.datetime.now()

print(zarf) #2026-10-02 17:33:31.162810

zarf.year #Out[131]: 2026
zarf.month  #10
zarf.day #Out[133]: 2


zarf.hour #Out[134]: 17
zarf.minute #Out[135]: 33
zarf.second #Out[136]: 31


#custom besaziu

birthday = '1999/10/15'
print(type(birthday)) #<class 'str'>


birthday = datetime.date(1999,10,15)
print(type(birthday)) #<class 'datetime.date'>

birthday.year #Out[141]: 1999
 


#emrooz --> zamano dar bairim
today = datetime.date.today()


zarf = today - birthday
print(zarf) #9849 days, 0:00:00



#-----------
today = datetime.date.today()
#expiration subscribe --L> 30 ro 

expiration_date = today + datetime.timedelta(days=31)

print(expiration_date) #2026-11-02


expiration_date.strftime('%Y-%m-%d') #Out[150]: '2026-11-02'


expiration_date.strftime('%Y/%m/%d') #Out[151]: '2026/11/02'


#Y --> year
#m --> month
#d--> day
#H --> hours
#M --> minute
#S --> second

#% adaeesho inja bzar

expiration_date.strftime('%Y|||%m|||%d')  #Out[152]: '2026|||11|||02'



#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------

import time


#sleep


print('salam')

print('khodafez')

'''
salam
khodafez

'''


import time


print('salam')

time.sleep(5)

print('khodafez')




for i in range(0,100):
    #request
    time.sleep(2)
    




import random 

for i in range(0,100):
    #request
    my_random = random.gauss(2,0.5)  #1.1 , 1.5 , 2 , 2,6
    time.sleep( my_random)
    






#dovom -->
#shoam mikhahid yek fasele zmanai ro besanjid

import time

zarf = time.perf_counter()

print(zarf) #175777.537054166

print('salam')

a= 10

b= 30

c = a + b

print(c)

zarf2 = time.perf_counter()


print('time e barnamt')
print(zarf2 - zarf) #0.0004349169903434813




#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#------------------------------------------------------------------
#OS hast --> kar ba file ha


#pwd --> bema migoft kojaeim
#ls -> list midad
#cd -> harkeat mikrd
#mkdir --> msiakht
#touch -->file misakht
#rm --> file
#rm -rf -> folder


#koja mziadid --> shell 

#mostaghim dargahi bod harchimziadid --> compute ejra mishod


#inja  pwd /new
#mkdir new2

#dastoorateton (spyder,IDE,editor) --> Ipython --> machine


#CLI ------------------------------------------
import os 

os.getcwd() #Out[158]: '/Users/apm'



os.chdir('/Users/apm/desktop') #cd 

os.getcwd() #Out[161]: '/Users/apm/Desktop'

os.chdir('/Users/apm/desktop/test')

os.getcwd() #Out[163]: '/Users/apm/Desktop/test'

zarf = os.listdir()
print(zarf) #['.DS_Store', 'folder2', 'folder3', 'folder1']


os.mkdir('Data')

zarf = os.listdir()
print(zarf)
#['.DS_Store', 'folder2', 'folder3', 'folder1', 'Data']



os.path.exists('Data') #Out[168]: True



if os.path.exists('Data2'):
    #yekar kone
    os.chdir('Data2')
else:
    os.mkdir('Data2')




#yekchizi bebini fiel ya directory
os.path.isfile('main.py') #true --> file , false --> folder
os.path.isdir('Data2')



Base_path = '/Users/apm/'
desktop_path = 'desktop/'
test_path = 'test/' 

#/Users/apm/desktop/test/
main_path = os.path.join(Base_path,desktop_path,test_path) #Out[170]: '/Users/apm/desktop/test/'
 
if os.path.exists(main_path):  
    os.chdir(main_path)
else:
    os.mkdir(main_path)
    os.chdir(main_path)







Base_path = '/Users/'
name=input("name folderetono bedid") 
name_path =name +'/'
desktop_path = 'desktop/'
test_path = 'test/' 

#/Users/apm/desktop/test/
main_path = os.path.join(Base_path,name_path,desktop_path,test_path) #Out[170]: '/Users/apm/desktop/test/'
 
if os.path.exists(main_path):  
    os.chdir(main_path)
else:
    os.mkdir(main_path)
    os.chdir(main_path)





#-------------

os.rename('old.txt','new.txt')

os.remove('Data')


#ramz haei ro darid toye .py nemizarid
#admin_passsword
#API_KEY = 'weuhdsaghudksah8732shua327629718ysh'

#Telergam_api_key = 'bxjdshgkudaghsidsuye8hdasjye'


#(base) apm@APMs-MacBook-Pro test % touch .env

#dakheleshe vim konin va benveisi

'''
(base) apm@APMs-MacBook-Pro test % touch .env
(base) apm@APMs-MacBook-Pro test % vim .env 
(base) apm@APMs-MacBook-Pro test % cat .env
Telegram_token = 'sdjhgsdjhgdshsdjhbjashds'
open_ai_token = 'shjsbksbhjxbsxaz'
admin_pass = 'jcsbjksdsksd'

'''

os.getcwd() #Out[173]: '/Users/apm/Desktop/test'


open_ai_token = os.getenv('open_ai_token')

print(open_ai_token) #None

#main.py --> ejra ro 


open_ai_token = os.getenv('open_ai_token',False)


#.gitignore 

#.env





#--------------Advanced --------------------
#subprocesss
#sys
#argparse





#--------------------------------------------
'''
Default -> yekseri kararo baramon anjam midan ama

ketabkhone haei hastan k kheyli kheyli karbordi hastand

external library --> python ya laptabet hsoam by default ndrateshon

download, install krd


terminal
pip --version

(base) apm@APMs-MacBook-Pro test % pip --version
pip 24.2 from /Users/apm/anaconda3/lib/python3.12/site-packages/pip (python 3.12)



age nadad
Microsoft--> 
Macos/linux --> 



pip --> abzare --> komak mikone shoma ketabkhone haye ezxternal ro download konid


numpy --> baraye mohasebat 

list=[10,20,30,40]  #pythonic neveshte shode 
array --> in yek objected c++ , ma mitoni pythonic behesh dastresi 
60 x bishtre baraye har mohasebe

ketabkhoen -->numpy --> array()

list() 

numpy.array()



numpy --> mohasebat , array (list)
scipy , sympy --> mohasebate riazi --> differential , integral , numerical modeling hale adadi
pandas --> pak sazi dade ha cleaning 
matplotlib , seaborn --> rasm , visualization

sklearn (scikit-learn) --> Machine learning


Pytorch , Tensorflow (keras) --> deep learning
 Meta        Google


Django --> backend , website --> easy , kond tare
fastapi --> backend, website --> sakht tar --> sari 



search pip esmesh --> Pypi --> copy

terminal --> pip install esme -->download install


import--> mokhafaf


import numpy as np
import pandas as pd




#import sklearn
from sklear.neural_network import MLPRegressor



'''
import numpy


zarf = numpy.array([10,20,30,40])





import numpy as np
import matplotlib.pyplot as plt 
x=np.array([1,2,3,4,5])
y=np.array([2,4,6,8,10])

plt.plot(x,y)
plt.show()



plt.scatter(x,y)
plt.show()




#=================================================
#=================================================
#File and extensions ----------------------------

'''
(base) apm@APMs-MacBook-Pro test % pwd
/Users/apm/desktop/test
(base) apm@APMs-MacBook-Pro test % ls
users.txt
'''

#tabeye dakheli --> open()

#open(path)  masire oon file hast

#/users/apm/desktop
#C://apm/desktop/...



#/Users/apm/Desktop/test  masire folder
#oon file ham dar nazar


#/Users/apm/Desktop/test/users.txt --> addrese file e man

file = open('/Users/apm/Desktop/test/users.txt')

print(file) #<_io.TextIOWrapper name='/Users/apm/Desktop/test/users.txt' mode='r' encoding='UTF-8'>

#file ro dar yek zarf zakhire krdm


#open(path,operation)

'''
r --> read
w --> write
a --> append
b --> vinary
+ --> read and write


'''
#-----read----------
file = open('/Users/apm/Desktop/test/users.txt','r')

#mode --> halate khondan baz mikone

#kolesho
zarf = file.read()
#hamaro pas midad besorate str

zarf = file.read(3) #character ro bekhone


print(zarf)
'''
In the name of god
Hello everyone
goodbye
'''

file.close()





file = open('/Users/apm/Desktop/test/users.txt','r')

file.readline() #Out[193]: 'In the name of god\n'
#yk khat ro besorate str pas mide 


file.readline() #Out[194]: 'Hello everyone\n'

file.readline() #Out[195]: 'goodbye'

file.readline() #Out[196]: ''


#-------
file = open('/Users/apm/Desktop/test/users.txt','r')

#kole khat haro bsorate yek listi az kaht ha mide
file.readlines()

#Out[198]: ['In the name of god\n', 'Hello everyone\n', 'goodbye']


file.close()


#---az in raveshe file=open  . file.close() --> rahat tare va professional


with open('/Users/apm/Desktop/test/users.txt','r') as file:
    
    text = file.read()
    print(text)
    
    
'''
In the name of god
Hello everyone
goodbye
'''



with open('/Users/apm/Desktop/test/users.txt','r') as file:
    
    text_list = file.readlines()
    count = 0 
    for line in text_list:
        if 'a' in line:
            count = count + 1 
            
    print(count)
            





#----------------- Write ------
#overwrite
with open('/Users/apm/Desktop/test/users.txt','w') as file:
    file.write('salam')
    
    
    
    
with open('/Users/apm/Desktop/test/users.txt','w') as file:
    file.write('salam')
    file.write('khoobi')
    
#salamkhoobi
     
    
    
with open('/Users/apm/Desktop/test/users.txt','w') as file:
    file.write('salam\n')
    file.write('khoobi')  
    
    
    
    

    
with open('/Users/apm/Desktop/test/users.txt','w') as file:
    names=['ali\n','vahid\n','reza']
    file.write('salam\n')
    file.writelines(names)  
     

#-----:> farsi

with open('/Users/apm/Desktop/test/users.txt','w',encoding='utf-8') as file:
    file.write('سلام')
    
with open('/Users/apm/Desktop/test/users.txt','r',encoding='utf-8') as file:
    file.read()
     
    
    
    
    
    
#ezafe ->append
with open('/Users/apm/Desktop/test/users.txt','a') as file:
    file.write('salam')
    
     
#append --> ezafe kon


#hamchin fili vojod nadare
with open('/Users/apm/Desktop/test/users2.txt','w') as file:
    file.write('salam')
    
    
#w --> age file nabashe ham --> misaze minevise
#     age bashe -> pakesh mikone --> rosh minevisde
with open('/Users/apm/Desktop/test/users3.txt','x') as file:
    file.write('salam')
    
    
    




  
import os

if os.path.exists('/Users/apm/Desktop/test/users5.txt'):
    with open('/Users/apm/Desktop/test/users5.txt','a') as file:
        file.write('salam')




import os


try:
    if os.path.exists('/Users/apm/Desktop/test/users5.txt'):
        with open('/Users/apm/Desktop/test/users5.txt','a') as file:
            file.write('salam')
except Exception as e:
    print('error khord')
    
    
    
try:
    if os.path.exists('/Users/apm/Desktop/test/users5.txt'):
        with open('/Users/apm/Desktop/test/users5.txt','a') as file:
            file.write('salam')
except FileExistsError:
    print('')
except FileNotFoundError:
    print('')
except PermissionError:
    print('')
except Exception as e:
    print('error khord')
    


#write read append


'''
error handling (Try except)

Python packages 

standard libraries

File management --> .txt



Binary
CSV
Json





'''
    


    


