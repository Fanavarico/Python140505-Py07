"""
In The name of GOD

Created on Fri Sep  4 15:27:01 2026


@author: Ali Pilehvar Meibody

L6




"""


'''

-------------------------------

Human (en) <------- inTERFACE -------> machine (0,1 binary)


interface --> python --->

1--> ipuython kernel --> dakhele laptabe

2--> ide/editor -> code --> ipython kernel --> trasnlate 0,1 -->ejra mishe

shoma javabo mibinid



Python --> language --> zabane --> grammar , vocab



#
qoutation --> comment, sohbat, tadris 



Known -->python mishnase

1- Python built in functions --> print() input() len() type()

2- Keywords --> logice --> ipython --> az bala b paein chap b rast --> ejra 
---> banfash --> if , else, elif , for , while , and , or ,.... def



unknown --> sefid --> esme yek zarf

zarf -> variable --> moteghayer --> value (meghdar)

shorot dare --> 4 shart --> adad , character _ , esme tabe ,.....

zarf = value



3- Variables
    3.1. Numbers (int, float, complex) -> ** * / + - --> c = a + b ||| == != > >= < <= --> True False
    3.2. Boolean --> Bool --> True , False  
    3.3. Str --> string --> har chizi keybaordet hatso benevisi --> qutation -->
    name='ali'
    
    name[index] --> 0 
    name[start:end] --> end exclude
    name[index] = XXXX --> Changable 
    
    str functions ---> function fght baraye str ha hast -->
    tavabeye str emal nemishan , khorojhi midan
    newzarf = zarf.function()
    zarf.function() ---> 1-convert --> .lower() .upper()
                         2-adad --> .count('a')  .find('a')
                         3-tru false -> .islower() .isupper()
                         
                         
    3.4. Iterabsl --> multiple value in one variable 
                    chand meghdar dakhele yek moteghayer (zarf)
                3.4.1. List --> ordered (index) , chanagable, allow duplicated
                        a= [10,20,True,'ali']
                        a[index]
                        a[start:end]
                        a[0] =100
                        
                        list fucntions --> fucntion hae hast ke baraye list hastan
                        
                        emal mishan , khoroji nemdiahand
                        
                        a=[]
                        a.append('ali')  #niazi nist zarfi jolosh bezare
                        
                        print(a)---> a=['ali']
                        
                3.4.2. Tuple --> ordered(index) , unchanagbale , allow duplicated
                    db estefade mishe
                    a  = (10,20,30)
                    a=(10,)
                    a=(10) --> number
                    
                    a[index]
                    
                    a[index]=new_value --> unchanagbale
                    
                    casting -->
                    b = list(a)
                    a[index]=new_value
                    b = tuple(a)
                    
                    
                3.4.3. Set --> unordered (no index) , unchanagbale , nO DUPLICATD
                
                    --> majnmoe haye riazi
                    
                    a = {10,20,30,40}
                    
                    
                    3.4.4. Dictionmary --> bahse information
                
                    a=['ali',40 , 4000000,'Iran']
                    
                    a[3]
                    
                    
                    b={'name':'ali' , 'sen':30 , 'keshvar':'iran'}
                    b=['keshvar'] --> iran
                    
                    
                    index value  --> list
                    
                    key value --> dictionary
                
                
                         



-------Keywords ------------


Bahse sharti bood --> agar ama ya harchizi shod --> if , ....


1- Just if --> rahzan --> catch koni , errorio begiri , donable

if shart:
    dastooor
    
    
    
shart --> True --> dastor ejra mishe
            --> false ->ejra nmsihe
            
            
            
            
2- If else --> do rahi

shart false shod -> nemigivel koni


if shart:
    dastor1
else:
    dastoor2
    
shart-->truie --> dastor1
shart-->false --> bikhial nmsihe --> dastore 2


3- elif --> do rahi haye too dar too

if shart:
    dasdtoor1
elif shart2:
    dastoor2
else:
    dastooor3




Multiple selction --> az user yechizi begir --> agar jam , tafrigh, zarb ,... selection --> dastoori ejra bshe
--> elif

if operation=='jam':
    c = a + b
elif operation =='tafrigh':
    
    
    
    
Range --> score 20 > 15 --> a  15 - 10 --> b 


if score>20:
    print('enmitone')
elif score>15:#---> beyne 15 ta 20
    print('a')
elif score>10: #beyne 10 ta 15
    print('b')
elif score>0: # beyne 0 ta 10
    print('f')
else: #zire 0 
    print('nomre negative(manfi) nadari'

          

          
-------Loops ------------



-------1- for Loops ------------

For --> zamani ke mikhahim be andazeye moshakahs yek kari ro anjam bedim
        zamahi ke mikhahim iteration anhjam dahim .
        
    
    
for i in [1,2,3,4,5]:
    print('salam')
    

be ezaye i hae k hinja hast --> i=1 , i=2 , i=3 , i=4 , i=5 dastore zir ro ejra kon


#range(start,end,step) --->listi --> start , start+step , ..... , end - 1


for i in range(0,100):
    print('salam')



static repeat

for i in range(0,100):
    print('salam')
    
dastoret tekrari bashe --> sabet tekrar



dynbamic repeat
#shomarande harchizi mitone bashe, i bashe j bashe, esm ,-->zarf

az shoamrande dar dastoor estefade koni --> dynamic repeat

i ro taghir midi , dastoro ejra kon, too dastor i ham hast , i ham taghir , har dafe dastoret

for i in range(0,100):
    print(i)
    
    

iteration

users=['ali','vahid','hamid','reza']

for user in users:
    print(user)
    
    
    
#if , 
 
#iuteration-->varede yek list beshi done done check (if)

count = 0
new_list=[]
for user in users:
    if user[0]=='a':#access
        #action
        print(user) 
        count = count + 1
        new_list.append(user)
        
        

        
3 ta keywords --> pass , continiue , break

for i in range(1,10):
    if i==3:
        break
    print(i)
    
    
i=1,2,3, ---> break --> az halghe kharej mishod

        
       
for i in range(1,10):
    if i==3:
        continiue
    print(i)
    
i=1,2, 4,5,6  

halgeh ro gaht nmikone, balke edame nemdi ehalghe ro baraye oon shoamande


for i in range(1,10):
    pass


error nakhori , 



-------2- for Loops ------------

dar for ha yek mahdode , yek baze bood k dakheelsh loop mziaid
begim --> ta zamani ke

while shart:
    dastoor
    
    
    
ta zamani k in shart==Trye bashe -->dastor ro ejra kon




aval --> bayad hsart=True beshe --> biad varede halghe beshe
varded ke beshe --> dastor ro ejra mikone

barmigrde-->sharto check mikone --> true --> dobare halghe , false -_> maid biron

ta abad anjam mide



yek-->sharti ro bezarid k baraye onaei k mikhahid gireshon bndazid , halghe --> True (shoroe halghe, start loop)

do --> dakhele dastor yek rahe farar ham bezarid --> break kone, i=i+1 shart-->false --> (endless loop ,sharte payan bezarid)



#hamishe true hast-->hamishe yek akri ro anaj mide -->

while True:
    kare...
    
    if :
        break
    

'''

b=[10]


a=(10)
print(type(a)) #<class 'int'>

a=(10,)
print(type(a)) #<class 'tuple'>



while True:
    password = input('password ro vared konid')

    if len(password) > 8:
        if not password.isdigit() and not password.isalpha():
            if not password.islower() and not password.isupper():
                break

            else:
                print('password nemitone faghat kochik bashe ya faghat bozorg bashe')

        else:
            print('passworde shoma ham bayad digit dahste bashe ham horof')

    else: 
        print('password zire 8 rgham nabashad')

    

print('passworde shoam moafaghiat sabt shod')




#raveshe rdigar



while True:
    password= input('passwordeto vared kon:')
    
    
    if len(password)<8:
        print('password nemitavand kochak tar az 8 bashad')
        
    elif password.isdigit():
        print('passworde shoam nemitavandad fght adad bashad')
    elif password.isalpha():
        print('passworde shoam nmitavansd hamash horof bashad')
    
    elif password.isupper():
        print('shoma bayad ham az horofe kochak ham az horofe bozorg estefade konid')
    elif password.islower():
        print('shoma bayad ham az horofe kochak ham az horofe bozorg estefade konid')
   
    else:
        print('ba moafaghiat passwordeton sabt shod')
        break
        
    
    
my_user=['ali','vahid','hamid','reza']


for user in my_user:
    print(user)
    
'''
ali
vahid
hamid
reza

'''




#for shoamrande in iterable

#iterable --> string,list, tuple , set , dictionary , 
    
#c/c++ --> string --> listi az character ha


#ali --> ['a','l','i']

name='ali'

#ali --> a     l      i
for character in name:
    print(character)
    
    
'''
a
l
i

'''

  #list --> shoamrande --> avalin element, dastor ejra , dovomin element dastor

#string --> shoamrsande -->avalin element --> avalin character  
    
        
        
my_user=['ali','vahid','hamid','alireza']


#har esmi k a toosh bashe --> oono beshmorid

count=0
for user in my_user:
    if 'a' in user:
        count = count + 1



print('Tedade uswer haei ke a darand :',count)

#Tedade uswer haei ke a darand : 4





my_user=['ali','vahid','hamid','alireza']


#har esmi k a toosh bashe --> oono beshmorid

count=0
for user in my_user:
    for character in user:
        if character =='a':
            count = count + 1
            


print('tedade kole a haei k dar tamame esm ha hast :',count)




#1-->mitavan dar string ha iteration anjam dad
#2--> nested loop --> daakhele yek loop, yek loiope diige bezanid



#tuple -->

a=(10,20,30,40)

for i in a:
    print(i)
    
'''
10
20
30
40

'''




mylist = [ ('ali',10) , ('vahid',20) , ('reza',30)]

#yek luste --> 3 ta element dare  -> har elemente --> tuple --> 2 ta element


for i in mylist:
    print(i)

'''
('ali', 10)
('vahid', 20)
('reza', 30)
'''



for i in mylist:
    print(i[0])

'''
ali
vahid
reza

'''




#unpacking


mylist = [ ('ali',10) , ('vahid',20) , ('reza',30)]

for i in mylist:
    print(i[0])
    
    
for name,number in mylist:  
    print(name)

'''
ali
vahid
reza

'''

for name,number in mylist:  
    print(number)

'''
10
20
30
'''


#set --->

c = {10,20,30,40,50}


for i in c:
    print(i)
    
    
 
'''
50
20
40
10
30
'''



#frontend <---> backend



#dictionary --->

#inaj mohem tarin ghazias --> website (frontend) --> 

products={'code':'z13' ,'brand':'zara' ,'price':10000 ,'user':'user10'}


products['brand']



for i in products:
    print(i)
    
    
'''
code
brand
price
user

'''


#3 ta tabeye dakheli darim


for i in products.keys():
    print(i)
    
'''
code
brand
price
user

'''

for i in products.values():
    print(i)
'''
z13
zara
10000
user10

'''




for i in products.items():
    print(i)

'''
('code', 'z13')
('brand', 'zara')
('price', 10000)
('user', 'user10')
'''

#unpacking


for key,value in products.items():
    print(key)
    print(value)
    print('-------')
    
    
 
    
 
#-------website--------

#ye listi --> az yek dictionary beheton barmigrde


kharid_ha = [ {'code':'z13' ,'brand':'zara' ,'price':1000 ,'quantity':2}  ,
             {'code':'b15' ,'brand':'breshka' ,'price':2000 ,'quantity':5},
             {'code':'k27' ,'brand':'kiko' ,'price':3000 ,'quantity':1}]




for kharid in kharid_ha:
    product_total =  kharid['price'] * kharid['quantity']
    print(product_total)
    
'''
2000 --> z13 
10000
3000
'''



kharid_ha = [ {'code':'z13' ,'brand':'zara' ,'price':1000 ,'quantity':2}  ,
             {'code':'b15' ,'brand':'breshka' ,'price':2000 ,'quantity':5},
             {'code':'k27' ,'brand':'kiko' ,'price':3000 ,'quantity':1}]


total=0

for kharid in kharid_ha:
    product_total =  kharid['price'] * kharid['quantity']
    
    total = total + product_total
    
    
'''
khjarid in [dict1,dict2,dict3]

kharid = dict1 =  {'code':'z13' ,'brand':'zara' ,'price':1000 ,'quantity':2}
dastooro ejra mikone --> 1000 * 2 = 2000 = product_total   --> total = 0 + 2000 --> 2000


kharid= dict2 ={'code':'b15' ,'brand':'breshka' ,'price':2000 ,'quantity':5}
dastooro ejra jon --> 2000 * 5 = 100000 ---> product_total --> total = 2000 + 10000 = 120000

kharid = dict3 = {'code':'k27' ,'brand':'kiko' ,'price':3000 ,'quantity':1}
dastoroo ejra kon --> 3000 * 1 = 3000 --> prodyct_total--> total = 120000  + 3000 =150000



'''




print(total) #15000


#---------------------

print('salam') #salam



#salam , adasd 

number= 43

#shomareye shoma hast : 43 

print('shomaraye shoma hast :' , number , 'mamnoon')



# f string 
print(f'shomareye shoma hast : number  mamnoon')
#shomareye shoma hast : number  mamnoon

#doree oon chzi ke manziresh harf nis, balke esme zarfe 
#va mikhahi man meghdaresho jay gozari konm {}
print(f'shomareye shoma hast : {number}  mamnoon')

#f string --> yani yek chizi in vasat bayad az biron biaratesh

#{} ono -> zarfesh migrde, valyue

#shomareye shoma hast : 43  mamnoon





#=============================================
#=============================================
#=============================================
#=============================================
#=============================================
#=============================================

'''
-------- Functions ------------



1- Monolotic code --> psudocode  --> script, automation
2-  def - based --> function based --> bar paye ye tavabe
3- Object oriented programming -> OOP--> class object

'''

#yek mesal bezanm --> az moshtari productesho migiri codesho 
#miri khode product ro peyda mikoni --> azash confoirmation 
#gheymato neshon midi 

#code takhfifm  migiri

#emal mikoni 

print('=========================')
print('Foroshgah Plutus')
print('=========================')


CODE_TAKHFIF = 'zaranew'

products=[ {'code':'z1' , 'name' :'zara cloth 121' ,'price':30},
          {'code':'z2' , 'name' :'zara shooes 100' ,'price':45},
          {'code':'z3' , 'name' :'zara cloth 451' ,'price':35},
          {'code':'z4' , 'name' :'zara shooes 300' ,'price':55},
          {'code':'z5' , 'name' :'zara shooes 231' ,'price':60},
          {'code':'z6' , 'name' :'zara bag 400' ,'price':110},
          {'code':'z7' , 'name' :'zara bag 500' ,'price':95}]

#hint : alan man productam kojas? --> akhele yek zarfi bename products --> RAM ejra msihe
#yani agar man spyder ro bbndm -> mahv mishe 

#donayye vaghei --> in data 0-> DB (database) --> HARD --> hichvaght hazf nmishe

#ba yek ketabkhane --> import mikonm 
#products


all_product_codes =[]
for product in products:
    all_product_codes.append(product['code'])




product_code = input('code mahsoleto befrest:')

    
while product_code.lower().strip() not in all_product_codes:
    print('code shoma vojod nadarad , code digari befrestid')
    product_code = input('code mahsoleto befrest:')
    
    

for product in products:
    if product_code == product['code']:
        print('-----mahsole shoma yaft shod-----')
        print('code mahsole shoma:',product['code'])
        #print(f"code mahsole shoma:  {product['code']} ")
        print('name mahsole shoma:',product['name'])
        print('gheymat mahsole shoma:',product['price'])
     
answer = input('code takhfif bede :')

for product in products:
    if product_code == product['code']:
        initial_price = product['price']
        
        if answer.lower().strip() == CODE_TAKHFIF:

        
            #final_price = initial_price  - 20/100 * initial_price
            #final_price = 80/100 * initial_price
            final_price = 0.8 * initial_price
            
        else:
            final_price = initial_price
        

print('------------------')
print('GHheymate nahaei : ',final_price)
        
        
        


#l6_example1.py



all_product_codes =[]
for product in products:
    all_product_codes.append(product['code'])



product_code = input('code mahsoleto befrest:')

    
while product_code.lower().strip() not in all_product_codes:
    print('code shoma vojod nadarad , code digari befrestid')
    product_code = input('code mahsoleto befrest:')
    
    

#product = find_product(product_code)
#print(product['name'])
#print(product['price'])



for product in products:
    if product_code == product['code']:
        print('-----mahsole shoma yaft shod-----')
        print('code mahsole shoma:',product['code'])
        #print(f"code mahsole shoma:  {product['code']} ")
        print('name mahsole shoma:',product['name'])
        print('gheymat mahsole shoma:',product['price'])
     
answer = input('code takhfif bede :')

for product in products:
    if product_code == product['code']:
        initial_price = product['price']
        
        if answer.lower().strip() == CODE_TAKHFIF:

        
            #final_price = initial_price  - 20/100 * initial_price
            #final_price = 80/100 * initial_price
            final_price = 0.8 * initial_price
            
        else:
            final_price = initial_price
        

print('------------------')
print('GHheymate nahaei : ',final_price)
        
        



#---------------------
'''
Tavabe baraye in omadan --> yek code tekrari ro 
ya yek kar --> function --> amalkardi ro --> shoma yek bar benvisi

yek esm bzari roosh, har dafe bejay eneevshtan chandin khat code --> sedash koni


--> didgahe avalie bashe

tabe ro moarefi mikonm, harf miznm -_>

'''


#---------------------
'''
1- define --> besazid

2--> call () --> sedda konid





sakhatar

shart dashtim abraye esm gozarie moteghayer <-->

tabe ha --> esm daran . 

    - ba adad shoro nashe
    - hich characteri joz _ nmishe
    - case sensetive 
    - esme tabe haye dakheli ya keyword haro nmitonid bzarid
    


Box --> uyek jabas 


input(vorodu) -------> [BOx] ----> Khoroji (output) begiuri


box ro misazimd. badesh feed mikonim input ro

definition of function | calling the function 




def name(vorodi1)



def name(vorodi1,vorodi2 ,vorodi3,vordoi4,....):
    harcheghadr inja code beazani moratbeet ba tabe
    
    #tabe ham miutone khrooji dste bashe ham nadashte bashe
    


'''

#calculate_discount()
#NameError: name 'calculate_discount' is not defined


#yek tabe besazam --> behesh numb1 , numb2 --> jam kone baram 

'''
             |--------|
numb1 -----> |   JAM  |
numb2 -----> |         |-----> jameshon ro 
             |--------|

'''
def jam(numb1 , numb2):
    javab = numb1 + numb2
    print(javab)
    
    
jam(numb1=10 , numb2=20) # --> not define --> aval fucntion ro bayad run bzni

jam(numb1=10 , numb2=20,num3=1000) #TypeError: jam() got an unexpected keyword argument 'num3'

jam(numb1=10 ) #TypeError: jam() missing 1 required positional argument: 'numb2'


jam(numb1=10 , numb2=20) #30


jam(numb1=40 , numb2=60) #100


jam(10,20)


'''

yek file .py sakhte

numb1=10
numb2=20
answer= numb1 + numb2
print(answer)



'''

'''
4 halat bashand



1-vorodi dashte bashe, khoroji nadashte bashe

2-vorodi dashte bashe, khoroji dashte bashe

3-voirodi nadashte bashe , khorojhi dashte bashe

4-navorodi , na khoorji 




'''



def jam(numb1 , numb2):
    javab = numb1 + numb2
    print(javab)
    
#30


d = jam(10,20)
    
    
print(d) #None


#Mohemtarin nokte --> print khoroji nist .

#print --> namayesh
#khoroji yani --> yehcizi pas bede man betonamberizam to zarf


    
    
def jam(numb1 , numb2):
    javab = numb1 + numb2
    #print(javab)
    return javab

jam(10,20)


'''
jam(   --> bezar begardam beyne tavabe am bebinam tabe e bename jam darma ya na
    
mibine hats --> chnta vorodi ? --> 2 ta mikahd --> check mikone

dari --> numb1 = 10   , numb2 = 20 

javab = nujmb1 + nujmb2 = 10 + 20 = 30 

return 

returb -0> bargardoon --> jaei k sedat zadan
ziresh yek zarf bzrm 


'''
    
#yek bar tarif krdio python fhmid xchizi bename **jam** vojod dare
 
def jam(numb1 , numb2):
    javab = numb1 + numb2
    #print(javab)
    return javab





zarf = jam(10,20)

    
print(zarf) #30






def jam(numb1 , numb2):
    javab = numb1 + numb2
    print(javab)
    return javab



zarf2 = jam(10,20)



#-------------------------------------------
'''
4 no tabe darim


inputs (optional) ----> BOX ---> output (optional)


'''



# 1- NA vorodi , na khoroji


def welcome():
    print('=================')
    print('=================')
    print('=================')
    print('=================')
    print('Khosh amadid hamegi')
    print('=================')
    print('=================')
    print('=================')
    print('=================')
    
    

welcome()
    
#khoroji yani betoni jolosh zarf bzre, ya tabe --> return



#------------------------------------
# 2-  vorodi dare ,  khoroji nadare

def jam(a,b):
    c = a + b
    print(c)
    
    
    
jam(30,40)

#print --> 30


zarf = jam(30,40)

#dobare ->30

#print(zarf)---> zarf ->None


def jam(a,b):
    c = a + b
    print(c)
    #return None



#------------------------------------
# 3(KAMEL TARN)-  vorodi dare ,  khoroji dare

def jam(a,b):
    c = a + b
    return c



zarf = jam(30,40)




def jam(a,b):
    c = a + b
    print(c)
    return c



zarf = jam(30,40)




#------------------------------------
# 4- vorodi nadare , khoroji dare


def pi():
    return 3.14

a = pi()




pi = 3.14
a = pi



print()




len('ddsdssds') #--> andazash


'''


str ---> box --> int andaze



'''


def mylen(word):
    count = 0 
    
    for character in word:
        count = count + 1 
        
    return count
     

    
zarf = len('ali') 
print(zarf) #3


zarf2 = mylen('ali')
print(zarf2) #3




#azinja bebad ham vorodi dare ham khoroji dare 

#vali --> tavabeye diageri ham darim  -> voorodi khoroji elzami nist 



def jam(numb1,numb2):
    javab = numb1 + numb2
    
    return javab



#numb1 , numb2 --> parametr
#10 , 20 --> argument


zarf = jam(10,20)


zarf = jam(numb1=10 , numb2=20)




#-----default------

def information(name,country):
    print('salam')
    print(name)
    print('az')
    print(country)
    
    

#tabe ordi dare, khoroji ndre yaniz arf nmitonm bzrm

information('ali','iran')

'''
salam
ali
az
iran

'''


information(name='ali' , country='iran')
'''
salam
ali
az
iran

'''


information('ali')
#TypeError: information() missing 1 required positional argument: 'country'

#1 vorodi bedi

#ya bsiha z 2 vordoii

#fght 2 vorodi migire



def iran_information(name):
    print('salam')
    print(name)
    print('az')
    print('iran')
    


#aksare user hat az iran hastand


iran_information('ali')




# do ta tabe

#python behet ejaze mdie , in dota ro too yek tabe benvisi



def information(name,country='iran'):
    print('salam')
    print(name)
    print('az')
    print(country)
    


information(name='ali')
    
#ag nadi --> khodesh default --> counntry = iran

'''
salam
ali
az
iran
'''

information(name='ali',country='france')
'''
salam
ali
az
france
'''


#F = M * a
#niroo = jerm * shetab



def force(m,a):
    f = m * a 
    
    return f
    
#force(m=10)
#agar taraf shetabv ro nadad-->shetabe zamin ro default


def force(m,a=9.8):
    f = m * a 
    
    return f
    

#force(m=10)


#mohemtarin notke--> parametr haye gheyre defaulkt bayad aval
#tarif shan badsh parametr haye default

#Ghalate
def force(a=9.8,m):
    f = m * a 
    
    return f
    


'''
def name(non-defaultparametrs ,....., default_paramets):
    
    
    
    
Yek tabe benevisid , numb1 , numb2 , operation --> vorodi

operation --> jam , tafrigh 

khoroji --> javab

print kone -> NA





'''
#----------------------------


#calculator

#calculator(numb1=10 , numb2=20 , operation='jam') --> 30
#calculator(numb1=10 , numb2=20 , operation='tafrigh') --> -10

def calculator(numb1,numb2,operation):
    if operation=='jam':
        javab = numb1 + numb2
        return javab
    elif operation=='tafrigh':
        javab = numb1 - numb2
        return javab
    else:
        print('fght ba tafrigh va jam javab dahid')
        return None


#numb1=input(')
#numn2=inpi
#operation

#calculator(...)


zarf = calculator(numb1=10,numb2=20,operation='jam')


print(zarf) #30





def calculator(numb1,numb2,operation):
    if operation=='jam':
        javab = numb1 + numb2
        return javab
    elif operation=='tafrigh':
        javab = numb1 - numb2
        return javab
    else:
        print('fght ba tafrigh va jam javab dahid')
        return None


zarf = calculator(10,20,'zarb')

#fght ba tafrigh va jam javab dahid
print(zarf) #None


def calculator(numb1,numb2,operation):
    if operation=='jam':
        javab = numb1 + numb2
        return javab
    elif operation=='tafrigh':
        javab = numb1 - numb2
        return javab
    else:
        raise ValueError('fght ba tafrigh jam javab dahid')


zarf = calculator(10,20,'zarb')






def calculator(numb1,numb2,operation):
    if operation=='jam':
        javab = numb1 + numb2
    elif operation=='tafrigh':
        javab = numb1 - numb2

    return javab



    

zarf = calculator(10,20,'jam')

print(javab) #NameError: name 'javab' is not defined
print(numb1)
print(numb2)
print(operation)




#-----------------


def jam(a,b):
    c = a + b 
    return c



d = jam(10,20)

print(a) #NameError: name 'a' is not defined

print(c)  #NameError: name 'c' is not defined


'''
a=10
b=20
c= 10 + 20 
return c 

d --> 30



'''



#local variables ---->


#python miad functione shoaro ejra kone
#zarf hae ke misaze ro -> movaghati misaze va palk mikone

def jam(a,b):
    c = a + b 
    return c



d = jam(10,20)




#agar zarf vojodnadashte bashe--> movaghati msiaze , return pak mikone zarfo

#zarf -> a=50


a=50
def jam(a,b):
    c = a + b 
    return c

d = jam(a=10,b=20)


print(a) #50

print(c) #NameError: name 'c' is not defined


#c o hamzaman k tabe run mishe , biron az tba eham beshanse adade movaghat nabashe
#local --> glocal 


def jam(a,b):
    global c #c ro movaghati nasaz
    c = a + b 
    return c



d = jam(a=10,b=20)


print(c) #30







#-----------
#vorodi mitone list ham bashe

def apply_discount_on_products(products,discount):
    price_list=[]
    for price in products:
        new_price = price - (discount/100) * price
        price_list.append(new_price)
        
    return price_list
        
        
        
    






#apply_discount_on_products([1000,200,300,400])



new_prices = apply_discount_on_products(products=[100,200,300,400] , discount = 20)


print(new_prices)


#3kafie besh liste gheymat bedam 100 , 200 , 300 ,400   , 20

#[80.0, 160.0, 240.0, 320.0]



new_prices = apply_discount_on_products(products=[100,200,300,400] , discount = 30)





#-----ziba nevisi--------------

#dostan vaghty tabe minevsiid , esme tabe, esme variable ha hamechi ro ziba benevsiid 
#mafhoom dashte bashe , esme tabe , esme zar hame ,kasi ke codeton ro mikhone motvaje beshe


#2 


def jam(a,b):
    c = a + b
    return c


#nam gozari
def jam(number1 , number2):
    result = number1 + number2
    return result

jam()


#hint

def jam(number1 : float , number2 : float):
    result = number1 + number2
    return result


def jam(number1 : float , number2 : float)-->float:
    result = number1 + number2
    return result



def apply_discount_on_products(products,discount):
    price_list=[]
    for price in products:
        new_price = price - (discount/100) * price
        price_list.append(new_price)
        
    return price_list
        


def apply_discount_on_products(products : list,discount : float):
    price_list=[]
    for price in products:
        new_price = price - (discount/100) * price
        price_list.append(new_price)
        
    return price_list
        



def apply_discount_on_products(products : list,discount : float):
    '''
    
    in tabe baraye discount hast 
    baraye inke yek listi az price ha begire yek discount ro ..
    
    ....
    ...
    
    
    
    
    '''
    price_list=[]
    for price in products:
        new_price = price - (discount/100) * price
        price_list.append(new_price)
        
    return price_list



apply_discount_on_products()




#--------
#niazi nisty

