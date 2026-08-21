"""
IN The Name of GOD


Created on Fri Aug 21 15:22:33 2026

@author: Ali Pilehvar Meibody


l4 -------

"""


'''

Overview--------------

Human (en) <----Interface ---> Machine(binary 0,1)


Interface --> python --> yekseri az dastoorate binary ro --> python trasnlate mokhafaf



yek zaban -->


Computer 1-Ipython kernel 2-IDE/Editor (code bezani)



IDE/Editor (spyder, vs code) code python --> ipython --> MAACHIN Dastoor ejra barmigrde



Pythpn zaban 

.py zakhire mishe --> ro bayad befrestid b machine kernel ipython


IDE (spyder) .py besazid va bakhshsiho run bznid

zire barname , oon ghesmati k shoma slect --> movaghat tabdil .py 
va ersal



.py k havie python code bashe ro --> keenele python

# '' "" mitonid comment benevsid, ignore (sarfe nazar)

az bala b paein, ac chap b rast b khoondane codeton ejra krdnesh 


az bala b paein

1-Python built in funciton (tavabeye dakheli python)

print() input() len() type() ......

source jalasate gzoashte


tabe hast --> yek kari anjam narneji

2- Keywords --> banafsh --> logice barnamro taghirbde
if else elif and or 

For , while ro ham yad bgirim 


3- Variables (moteghayer) --> esme zarf

zarf [mohatvaee] --> esmesh ro mizarim

3.1. Numbers (int, float, complex)
    ** * + - / =
    == != > >= < <= --> Booolean
    
3.2 Boolean --> True , False

3.3. String --> '' keyboardeto -> string
            name = 'ali'
            name[1]  index --. index az 0 shoro mishod
            name[-1] --> az akharin
            
            -1 -> not found -> -1 
            -1 --> akahri
            
            name[start:end] end --> exclude
            
            
            str fucntions -> zarf.fucntion()
            
            str.lower() .upper() .....
            str.count('a') --> 0 
            str.find('a') --> 
            
            
            str.islower() --> trUE FALSE
            
            str fucntions emal nemishavad, khoroji mide
            
            new_name = name.fucntion()
            
3.4. iterables --> chanta value ra mikhahid dakhele yek zarf 


    3.4.1 List --> orddered (index) , chanagble, allow duplicated
    
        a[index]
        a[start:end]
        
        a[index]=322
        
        list fucntion --> list.fucntion()
        
        .append() .extend()
        
        emal mishodan , khoroji nmidadan
        
        my_list.append('new element')
        

    3.4.2. tUPLE --> ordered (index) , unchangable , allow duplicated 
            --> database . casting --> -->lisyt change --> tuple
    
    3.4.3. Set --> unordered (index), unchanagble, duplciated
            --> set haye riazi , amaliate majmoei , hazfe tekrari
    
    3.4.4. Dictionary --> index --> key
    
    key value --> information (etelaat ro zakhire konim)
    
    


'''


name = 'ali'

#0 1 2

name[2] #Out[1]: 'i'

name[-1] #Out[3]: 'i'

name[-2] #Out[4]: 'l'




name='mohsen'

name.count('a') #Out[4]: 0

name.find('m') #0

name.find('a') #Out[7]: -1


#----------------------------
#----------------------------
#----------------------------



a = 'dsjsdhsdds72332'

a.isalnum() #Out[8]: True

a = '32233232'

a.isalnum()

#a.isdigit()

a='33223'

a.isdigit()




#======================================
#======================================
#======================================

'''
Linux, mac --> terminal 

man inja --> terminal ejra mishe


windows --> CMD, Powershel, git bsh

cmd -->jaygozin, powershell jaygozin
git bsh --> hamonie man inja daram miznm



'''



A=20

print('salam') #salam

#A=10 --> SALAM

#a=20 --> salam

#astori man dashtam k b a hich rabti ndsht sharti nabod


#man gahi agarbekhaham 

#yek khat ya chandin khat ro shgartish konam
#Yani hamishe run nshe --> is --> conditional statement 

#(shart)

#if else elif


'''

1- Just If

ke shoam mesle yek rahzan , fght kasani k sharteshon tRUE mishe mikhahid
baraye onha dastori ejra shavad

   |
   shart(True false)
   |
----------------
|True     |false
kar        |
|          |
------------
      |
      |
      



2 - If else

do rahi doros konid, agar true bod felan kar , ag nabod velesh nakon


ya kare1 kare 2 


   |
   shart(True false)
   |
----------------
|True     |false
kar1        kar2
|          |
------------
      |
      |
      
      
      
3- if elif else

do rahi hay etoo dar too bezanam

   |
   shart(True false)
   |
----------------
|True     |false
kar1        
|          |
          shart2 
           |
        ---------
        True      false
        kare2      kare3
------------
      |
      |
      



'''


sen = int(input('senet cheghdre?'))


if sen>10:
    print('salam')
    
    
#az tamame kasani k seneshono vared mikonan

#fght kasani k in shrt true mishe

#sen>10  --> 

#if shart -->shart -> yekchzii bashe k y atru ebede ya false bede

#True --> in dastor ejra mishe
#fALSE --> EJRA NMISHE

sen = int(input('senet cheghdre?'))


if sen>10:
    #True 
    print('salam')
else:
    #fasle
    print('khodafez')
    
    




    
    
    












if sen>20:
    print('salam bish az 20')
elif sen>10 :
    print('salam 10- 20')
else:
    print('kochiktar az 20 ')
    
    
'''
 |
 
 
'''


#----Machine hesab 

num1 = int(input('number 1 ro bede:'))
num2 = int(input('number 2 ro bede:'))
operation = input('amaliateto begoo (jam,tafrigh,zarb,taghsim):')


'''
agar nevesht jam --> num1 + num2 --> 
tafrigh --> num1 - num2

taghsim --> num1 / num2

zarb -> num1 * num2


print()



negah b on taklifam







zzabane farsi --> Number 1 , Number 2 , Operation


useri darm --> 3 ta chizi begiram 


adade 1 --> --> zakhire
adade 2 --> zakhire
amaliat --> amaliat zakhire

bar ase in -->mohasebe mikham anajm 


agar nevehst jam --> number1 + number
agar nevsh tafrigh --> number1 - number
agar nevsh zarb --> number1 * number
agar nevsh taghsim --> number1 / number



agar --> if elif else

1-just idf 2- if else 3-elif




'''

number1 = int(input('shomareye 1 o bede:'))

number2 = int(input('shoamreye 2 ro bde:'))

amaliat = input('amaliat ro begi (jam, tafrigh, zarb,taghsim):')

#amaliat = tafrigh

if amaliat =='jam':
    result = number1 + number2
    
    print(result)
    
    #print(number1 + number2)
    #number1 + number2
    

if amaliat =='tafrigh':
    result = number1 - number2
    
    print(result)
    
    
if amaliat =='taghsim':
    result = number1 / number2
    
    print(result)
    

if amaliat =='zarb':
    result = number1 * number2
    
    print(result)
    


'''
jam --> 1 + 2 --> result

3 ta operationh ezafe anajm dad
3 bar moajdad check


4 ta if estefade krdim
'''




'''
Errro ma darim

syntax error --> invalid syntax --> '' : if = ye charatcer

logical error --> eshtebah manteghi krdi 
, implementbesazi ro nasakhti


doroste dostan (erroor nist) --> optimize nist (behine nist)
behine bokoni (optimizesh koni)




'''



number1 = int(input('shomareye 1 o bede:'))

number2 = int(input('shoamreye 2 ro bde:'))

amaliat = input('amaliat ro begi (jam, tafrigh, zarb,taghsim):')



if amaliat=='jam':
    result= number1 + number2
    print(result)

elif amaliat=='tafrigh':
    result = number1 - number2
    print(result)
    
elif amaliat=='zarb':
    result= number1 * number2
    print(result)

elif amaliat=='taghsim':
    result= number1/number2
    print(result)

else:
    print('shoma chizi vared kardid k motabar nist invalid value')
    #assert ZeroDivisionError('shoma chizi vared kardid k motabar nist invalid value')
    
    






#--------------------
'''
karbord
1---> erroro begirid

agar jaei erro rbod --> shart bezarid
True --> erroro begir

2--> drahi baz koni



3---> 4,5 entkehab drid (jam, zarb, taghsim ,...)
entekhab haye goonagono gosaste . range ,....





4---> entekhab hae k range dare

Moadele

az danesh amooz nomre ash ro begirid
agar 15-20 --> begdid shoma A hastid
agar 10-15 --> begidshoma B hastid
agar zire 10 --> shoma F hastid.

'''

score = float(input('denshjoye gerami nomre at:').strip())

#  40
#40


'''

beyne 20 - 15  --> A (shamele 15)
beyne 10 - 15 -->  B
beyne 0 -10 --> F


if elif elif


soal bepors az khodet


'''
score = float(input('denshjoye gerami nomre at:').strip())

if score>=15:
    #.....
    print('shoma A hastid')

elif score>=10:
    print('shoma B hastid')
    
else:
    print('shoma F hastid')


'''


    |
   aya bisha z 15 hast?

True           False

A               aya bish az 10 hast
           True                  False
             B                     F




'''



score = float(input('denshjoye gerami nomre at:').strip())

if score>=15:
    #.....
    print('shoma A hastid')

elif score>=10:
    print('shoma B hastid')
    
else:
    print('shoma F hastid')


'''


+binahyat    --------   15 -------- 10 --------- - binahayatr
              A               B           F
              
              
              
EXTERNAL LIMIT --> mahdodiate bironi

socre man nemitone bish az 20 yta kamtar az 0




gate --> rahzan bezari 


'''



score = float(input('denshjoye gerami nomre at:').strip())


if score<=20 and score >=0:

    if score>=15:
        #.....
        print('shoma A hastid')
    
    elif score>=10:
        print('shoma B hastid')
        
    else:
        print('shoma F hastid')

else:
    print('Shoma bayad rangeton 0 ta 20')
    







score = float(input('denshjoye gerami nomre at:').strip())


if score>20:
    print('Maximume nomre bayad 20 bashad')
elif score>=15:
    print('shoma A hastid')
    
elif score>=10:
    #beyne 10 vfa 15p
    print('shoma B hastid')
    
elif score>=0: 
    print('shoma F hastid')
    
else:
    print('nomreye manfi man nemigiram')
    
    
#-------------------------



'''
Python

1- Python built in function


2- Keywords
if elif else

3- Variables 

'''



'''
Naghshe rah



Zaban farsi --> Plan PRD , --> implement

az user begire --> input()
namayesh bede be user --> print()
zakhire koni  movaghat --> variables 
zakhire koni daem -> Database (DB)

agar o ama --> conditional statement 

if khali ---> fght yek sharto barresi konid va fght  kasani k Trye mishan oo ejr akone
if else --> do rahi mikhahid
if elif elif else --> chand rahi 
---> (chanta entekhabe gosaste (jam , tafrigh)) if operation=='jam'
--> chanta netkehabe baze ei range --> if a>20 elif a>15 ,......


dore koni L3 , L4


1---> email kamel .py --> harchizi bezanid 
niaz b tozih text , teelrgam voic


2---> goroh rafe eshkal , telegram 





'''



#==========================================
'''      Loop     '''
#==========================================
#loop --> halghe 



print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')
print('salam')

'''
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam

'''



#man fght yekbar benevism print('salam') va dah bar ejra she
#logico beham mizanm --> dast too logic 

#az kodom 3 shakaheye keywords 


repeat(10):
print('salam') #SyntaxError: invalid syntax




print('khodafez')


repeat(10):
    print('salam')
    
    #maami k inja hastim
    #kole inja ro 10 bar repeat kon
    
    
#mane ali --> reepat()

#oon afradi k python ro sakhtan --> 


#for -->

#for 
    


'''
for baraye repeat aslan nayamade ast



for shomarande in baze :
    dastoooor
    
    
    
baze--> [1,2,3,4,5,6,7,8,9,10] , [ali,vajid,reza, hamid]
be ezaye shomarande --> i , k , l , esm , number , 

i --> done done chizae k into hast bezar va dastoor ro ejra kon





'''
#repeat(5)

for i in [1,2,3,4,5]:
    print('salam')
    
'''

i --> 1 ---> dastoor ro ejra mikone -> print(salam) --> salam
i --> 2 --> dastoor ro ejra 0->print(salam) --> salam
i ---> 3 ---> dasto ejra --> pritn(slaam) 0->salam
i-->4 -->dastoor ejra --> salam
i-->5 --> dastooor ejra --> salam 


az in halghe (loop) miad bironn

adie



salam
salam
salam
salam
salam


'''


for j in [1,2,3,4,5]:
    print('salam')
    
'''
fght shoamrande esmesh avaz shode

j=1 -> dastoro ejare --> print salam
j=2
j=3
j=4
j=5

'''


for numb in [1,2,3,4,5]:
    print('salam')

'''
salam
salam
salam
salam
salam
'''


#for numb in [1,2,3]

#agar mikhaham az 1 ta 100 nenvisam sakhtame

#yek tabeye dakheli --> range(start,end,step)


for i in range(0,100,1):
    print('salam')
   


print('khodafez')

    


'''
be ezaye shomarandamon (i) k dar in range-->[0,1,2,3,4.....,99] 100 ta raghame

i=0 --> dastor ro ejra mikone --> print('salam') --> salam
.....

i=99 --> dastoor ejra mikone --> print('salam') --> salam

100 ta salam -> 0 ta 9

i=100 --> miad biron azz halghe



salam
....1000
.....


'''


for i in range(0,100,1):
    print('salam')
   

    print('khodafez')


'''
i=0 --> dastor ro ejra kon ->body --> print(salam) print(lkhodafez)  salam khodafez
i=1 -->   salam khodafez




salam
khodafez
salam
khodafez
salam
khodafez
salam
khodafez
salam
khodafez
salam
khodafez
salam
khodafez
salam
khodafez
salam
khodafez

'''


for i in range(0,100,1):
    print('salam')
    
for i in range(0,100,1):
    print('khodafez')

'''
i=0 --> salam , 
i=1 -->salam ...salam


i=0 --> khodefaze


salam
1000
...
salam

khodafez
100 
khodafez



'''

for i in range(0,100,1):
    print('salam')
    
for j in range(0,100,1):
    print('khodafez')





for j in range(10,50,1):
    print('salam')

'''
40 ta salam print kard

'''
for j in range(10,50,2):
    print('salam')

#j=10 ->print salam --> salam
#j=12 -->prin t dsalam

'''
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
salam
'''

for j in range(10,50,2):
    print('salam')
    

    
for i in range(50):
    print('salam')


#start:0 ,end-->begi ,  step : 1      
    


for i in range(10,50):
    print('salam')

#az 10 ta 50



for i in range(10,50,2):
    print('salam')





for j in range(10,50,1):
    print(j)
    
   
    

'''
j-->10 -->dastoro ro ejra mikone -->print(j)-->print(10)-->10
j-->11 --> dastoor ro ejra mikone --> print(j) --> print(11) -->11
....

j-->49 ---> dastoor ro ejra mikone --> print(j) -->print(49) --> 49


10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49

'''
    








count = 0

for j in range(10,50,1):
    print('salam')
    count = count + 1
    
    
'''
count = 0



j->10 --> salam , count = 0 + 1 = 1
j-->11 --> salam , count = 1 + 1 = 2





'''

print(count) #40

#10 -> 49

    



#dynamic repeat


    

#-----------------------------
for i in ['ali','vahid','reza']:
    print('salam')


'''
i=ali --> dastoor ejra mikone --> print(salam) -->salam
i=vahid -->salam
i=reza -->salam

b ezaye elemnt haye dkahele list



in yek vasile shode --> salam print



static loop -> loop static (sabet)

static repeat --> salam 
khodafesz


'''



#static loop --> print('salam') i , j , kl


#range(start,end,step)


#range(start=0 , end , step=1)
#range(100) ---> range(0,100,1)
#range(10,100) --> range(10,100,1)
#range(10,100,2)


for i in range(0,5):
    print('salam')



for i in range(0,5,1):
    print('salam')



#harkodom ro bznm
'''
i=0 --> print('salm') -->salam
i=1 --> print('salm') -->salam
i=2 --> print('salm') -->salam
i=3 --> print('salm') -->salam
i=4 --> print('salm') -->salam

5 ta salam


'''


for i in range(0,5,2):
    print('salam')
    
'''
i=0  --> print('salam') -->salam
i=2  -->print(salam)-->salam
i=4  -->print('salam') -->salam
i=6 -->


salam
salam
salam
'''

for i in range(0,6,2):
    print('salam')
    
'''
i=0 ---> print('salam') -->salam
i=2 --> print('salam') -->salam
i=4 -->print('salam') -->salam
i=6 --> X

'''
    
    
    
    


for i in ['ali','vahid','reza']:
    print('salam')
    
    
    
    
    
#----------------------------
#dynamic loops

#azon shomarand eham estefade konm

for i in range(0,10):
    print(i)
    
    
'''
i=0 --> print(i)-->print(0)--> 0
i=1 ---> print(i) -->print(1)-->1
i=2 
i=3
io.

i=9 --> print(i)--> print(9)-->9


0
1
2
3
4
5
6
7
8
9


'''

'''

for variable  in baze:
    dastoor1
    dastooor2



for i in [dssddsds]:
    sdsd
    

'''





#adade zoje beyne 0 ta 20 ro print kone


for i in range(0,20,2):
    print(i)

#range(0,20,2)-->[0,2,4,6,8,10,12,14,16,18,]
   

#i --> [0,2,4,6,8,10,12,14,16,18,]
#dastoro ejra mikone

'''
i=0  --> print(i) -->print(0)-->0
i=1 -->print(i)-->print(1)-->1
...
i=18 -->print(i)-->print(18)-->18


0
2
4
6
8
10
12
14
16
18

'''

    





#adade farde beyne 40 ta 60 ro print kone

#range(40,60,2) -> 40 , 42 , 44 , 46
#40 , 43 , 46

#40 , 41, 42 , 
#(41,60,2)--> 41,43, 45, .....59,


for i in range(41,60,2):
    print(i)

'''
41
43
45
47
49
51
53
55
57
59
'''



#yek listi az esm ha dashte bashid
#esm haro print kone

my_list = [ 'ali'  ,'vahid'  , 'reza'  ,'hamid' ]


#iteration konam 

#i --> tooye yek jae k iteration --> jashon i=ali , vajid ,

#listo --> iterable --> chizi k mishavad dakheelsh iteration kard

my_list = [ 'ali'  ,'vahid'  , 'reza'  ,'hamid' ]


for i in my_list:
    print(i)
    
    
'''
i=ali --> print(i) -->print(ali) -->ali
i=vahid
i=reza
i=hamid




ali
vahid
reza
hamid


'''




#yek listi az esm ha dashte bashjid, 
#andaze har esm ro print kone

my_list = [ 'ali'  ,'vahid'  , 'reza'  ,'hamid' ]

for i in my_list:
    
    #i -->khode esmo
    #len(i) --> andazasho
    print(len(i))
  
'''
3
5
4
5
'''


#static repeat


for i in [1,2,3,4,5]:
    print('salam')



for i in range(0,100):
    print('salam')
#range --> listaro misaze, i mire toosh



for i in ['ali','vahid','reza']:
    print('salam')



#vaghhyy miran toye lsit, range -->salam ,
#static repeat

#shoamrande dynamic bashe estefade nmikone



#dynamic repeat
    
for i in [1,2,3,4,5]:
    print(i)

#i=1 print(salam) salam

#i=1 print(i) -->print(1)-->1
#i=2 print(i) -->print(2)-->2

#dastoor mortabet bashe b shomaande

for i in range(0,100):
    print(i)
#range --> listaro misaze, i mire toosh

for i in ['ali','vahid','reza']:
    print(i)




#-----Iterations-------

my_users = ['ali','vahid','reza']
for i in my_users:
    print('salam')
    
'''
static repeat

salam
salam
salam



'''
   

my_users = ['ali','vahid','reza']
for i in my_users:
    print(i)
    
    
'''
dynamic repeat

ali
vahid
reza



'''


#--->iteration
my_users = ['ali','vahid','reza']
for i in my_users:
    print(len(i))
    
'''
3
5
4
'''
    

my_users = ['ali','vahid','reza']
for esm in my_users:
    print(len(esm))
    
    
    
#fght esm haei k ba a shoro mishavad ro print kon

my_users = ['ali','vahid','reza']

for esm in my_users:
    esm[0]
    

#dastam reside behesh


'''
esm=ali ---> dastooor
esm = vahid
esm = reza


'''

#1-->printesh kon

my_users = ['ali','vahid','reza']

for esm in my_users:
    print(esm[0])
    
    
'''
a
v
r


'''

#esmhae ro darin list print kon k horofe avaleshon a bashe




my_users = ['ali','vahid','reza']
for esm in my_users:
    if esm[0]=='a':
        print(esm)

#ali

'''
esm --> 'ali' --->dastooro ejra mikone
if esm[0]=='a':
    print(esm)
    
    
if a==a->true -> print(esm) -->esm --> ali


esm --> vahid
if esm[0]=='a':
    print(esm)
    
if v==a --> False

esm --> reza
if r==a --> false 


'''


my_users = ['ali','vahid','reza']
for esm in my_users:
    #if esm[0]=='a':
    #    print(esm)  
    if esm.startswith('a'):
        print(esm)
        
#ali


my_users = ['ali','vahid','reza']
for i in my_users:
    print(i)


#gtp ,......

my_users = ['ali','vahid','reza']
for i in range(len(my_users)):
    print(i)
    
    

'''
len(my_users)--->3


my_users = ['ali','vahid','reza']
for i in range(3):
    print(i)
    
    
i=0  print(0) -->0
i=1  print(1)--->1
i=2  print(2)-->2
    

'''
    


#i khode lement beshe
my_users = ['ali','vahid','reza']
for i in my_users:
    print(i)

'''
ali
vahid
reza

'''


my_users = ['ali','vahid','reza']
for i in range(len(my_users)):
    #print(i)--->index
    print(my_users[i])
    
    
'''
for i in range(len(3)) 

i=0 --->print(my_users[i]) --> print(my_users[0])-->print(ali ) -->ali
i=1-->
i=2 


na tanha b khdoe elemnt hay elist niaz dari

balkje b tartibo indexesh ham niaz dari

'''
    
    
    
    
    
#i-->tooye on list, indexe oon liste
    
    
    
    
    
    
'''

static repeat --->

dynamic repeat --->


iteration --->
Karbordi tarin







'''
#---> 

my_users = ['ali','vahid','reza']
for esm in my_users:
    #if esm[0]=='a':
    #    print(esm)  
    if esm.startswith('a'):
        print(esm)
        


my_users = ['ali','vahid','reza']
for esm in my_users:
    if esm[0]=='a':
        print(esm)
        
        

#baoon ravesh (advanced)
my_users = ['ali','vahid','reza']
for i in range(len(my_users)):
    if my_users[i][0] =='a':
        print(my_users[i])
    
    
    
#-----------
 
#iteration   
my_users = ['ali','vahid','reza']

for i in my_users:
    print(i)



#-----
'''
Iteration anajm dahid


mirid dajhele yek list --> for mizanid

dakhelesh --> if mizanid 

dakhele yek list , yek sharti ro berid va check konid



too liste moshtaria (user)ha kasanii k horofe avale esmeshon a

product hae k horofe avalesh z

product haei k zara hastan ,

listi dari az user, product ,......

miri toosh mikhay done done daresh biari (iteration)


yek chizi check



dakhele for --> 

agar yek chzio mikhay if
agar dorahi --> if else
agar chanrahi if elif else




inja --:> access kardi , action

to dstresi peyda krdi b on esm haek a daran

1--> printeshojn kon



'''




my_users = ['ali','vahid','reza','amir','hamid']

for esm in my_users:
    if esm[0]=='a': #access
        print(esm) #action
    
'''

ali
amir


2-->beriz dar yek liste dg

'''

my_users = ['ali','vahid','reza','amir','hamid']

a_list=[]

for esm in my_users:
    if esm[0]=='a': #access
        #print(esm) #action
        #bejaye porint krdn briz too yek liste jodagane
        a_list.append(esm)
        
        
'''
esm -> ali --> 
if esm[0]=='a': #access
    #print(esm) #action
    #bejaye porint krdn briz too yek liste jodagane
    a_list.append(esm)
    
[].append(ali) --->< 

a_list = [ali]



esm --> vahid
if esm[0]=='a': #access
    #print(esm) #action
    #bejaye porint krdn briz too yek liste jodagane
    a_list.append(esm)
    
v==a false 

a_list = [ali]



esm -->amir
if esm[0]=='a': #access
    #print(esm) #action
    #bejaye porint krdn briz too yek liste jodagane
    a_list.append(esm)


a=a -->true  
    
a_list.append(esm)
a_list.append(amir)

a_list = [ali]

a_list.append(amir) --> [ali,amir]




'''
    





#-------------------
'''
12 ta taklif 




'''

my_users = ['ali','vahid','reza','amir','hamid']

a_list=[]

for esm in my_users:
    if esm[0]=='a': #access
        #print(esm) #action
        #bejaye porint krdn briz too yek liste jodagane
        a_list.append(esm)
        
    
        
    
    
    
    
    
    
        
print(a_list) #['ali', 'amir']




#acction--.> 1 namayesh --> print
#2- beriz to yek list --> .append()
#3---> count --> 
#na mikham namayeh bdi na mikham joda 

#yek list , az beyneshon kasani k horofe aaleshon a hast ro beshmor
#shomaresh kon

my_users = ['ali','vahid','reza','amir','hamid']

count = 0

for esm in my_users: #Iteration
    if esm[0]=='a': #access
        #print(esm)
        #a_list.append(esm)
        count = count+ 1
        

'''
esm = ali --> ejra
if esm[0]=='a': #access
    count = count+ 1

a==a -->true --> count = 0 + 1 = 1


esm = vahid
if esm[0]=='a':   v ==a -->false -->count ejra nmishe



#har zamani
esm = amir
if esm[0]==a         a==a -->true
count = count + 1 = 1 + 1 =2


'''

print(count) #2




'''
dar in jalase L4


looop haro khondim --> for loop


for shomarande in baze:
    dastoor
    dastoorat
    
    
static loop
for i in range(0,100):
    print('salam')
    
    
dynamic loop
for i in range(0,100):
    print(i)
    
    
iteration
my_list=[....,...,..]

new_list=[] # for action2

count = 0  #for action3


for esm in my_list:
    if esm[0]=='a': #access
        #actiopn1 --> print
        print(esm)
        
        #action2 -->berize too ye list
        new_list.append(esm)
        
        #action3 --> beshmore
        count = count + 1 



az takalifi 12 gane hast

4 ta --> if eliof else


8 tash --> for



jalaseye yaande --> L5 --> while --> yekseri mabahes


l1,l2,lk3 hatman tamash konid (3 jalase) jalase ye 5 --->
 


tamrin haram -->github , git vasl bshid -->onja bzrid --> email konid

agar natomestn , bahone pazirtofte bashad --> baray ebande khdo efile ro ersal


charshangwe --> git cli --> bishtr git 



'''


