"""

In The Name of GOD

Created on Fri Jul 31 15:51:01 2026

@author: Ali Pilehvar Meibody





Human (Ensan) <-----Interface (zabane barname) ---> Machine (Binary)



# qutation --> ignore 

Python  3 ghesmat

1- Python built in functions -------

Narenji mishodan, mishankht , () parantez dasht , vorodi k midi
khoroji mide 

function --> functional --> amalkardi , karbordi

print() ,len() , input() , type() , 
int() , float() , compelx, bool() , str() , ......


https://docs.python.org/3/library/functions.html



2- Keywords ----> logic manteghe barnamaro avaz koni

for , if , else ,.........

banafsh


3- -->  Variable dar nzar migire

variable (moteghayer) --> zarf k dar an chizi zakhir emikoni mriizi



zarf (variable)

esme --> [meghdar]

a=10

esme zarf a , dakhelesh 10 e 

esme zarf --> ghavanin --> _ , ba adad shoro , case snetive.....





dakhele zarf chia mitonim 
- Number  --> (int, float , complex)
- Bool --> (True , False)
- Str --> String (reshte)











"""


print('salam' , 40 , 'ali' , True)


#https://docs.python.org/3/library/functions.html

#abs --> absolute --> motlagh
abs(10) #Out[5]: 10

abs(-10) #Out[6]: 10
 

#Out[6]: ----> out ghermez --> khoroji 

#tabe ei --> khoroji daran --> berizi dar tabe

#age narizi --> be soorate Out inja neshon mide



a= -10
b = abs(a)



'''

a= -10
b = abs(a)


yek zarf besaz bename a --> -10 ro beriz  dakhelesh

az tabe ye absolute estefase kon (-10) --> +10 --> b

dastor dadi felano felanja beriz

namayesh bede


'''




abs(-10) #hjoloye jkhoroji zarf nazari --> Print out



a=0
b=1



c = bool(0) #False
d = bool(1) #True


#type

#int , float, complex, bool, str --> tabe dakhelie python --> casting 


a = 40

type(a) #Out[10]: int

#40.09

b=float(a) #casting

print(b) #40.0

type(b) #Out[13]: float




a=37.3

#float

b=int(a)

print(b) #37


#int() float() complex() bool() str()
#casting estefade mishe --> 5 ta tabe dakheli ayd grfti
#list() tuple() set() dict()


a=37.9
b=int(a)
print(b)

#37 -->asharo pak mikone


#math 

#len()


len('salam') #Out[17]: 5



#nesbat b naizwton bahsah raftar konid
print(len('salam')) #5

len_name = len('ali')


type('ali') #str



print('salam esmet chie:')

'''
In [22] :print('salam esmet chie:')
salam esmet chie:

In[23]:

'''
#harchi benevisi baraye karbar print mishe va montazer mimone chizi benevise taraf


input('salam esmet chie :')

'''
In [24] input('salam esmet chie :')
salam esmet chie :


yani montazerete javab benvisi va enter bezani

#Out[24]: 'ali'
'''






name = input('salam esmet chie :')


#miad aval print mikone salam esmet chie , montazer mishe karbar az 
#console benvise, harchi benevise , khoorjhi mide
#mirize tooye name



print(name) #ali



#2 nokteye kh mohem

#1---> input , khoroji midahad, khorojisho beriz tooye yek zarf

#2---> hamishe khoorji ro besoorate STR (string) midahad


sen = input('senet cheghadre?')



print(sen) #40

print(type(sen)) #<class 'str'>

# '40'    na 40

#khasiate tabeye input ine --> k miad khorojisho hamvare str mide




sen/4
'''
TypeError: unsupported operand type(s) for /: 'str' and 'int'

'''



sen = input('senet cheghadre?')

new_sen = float(sen)

#har amale riazi ee k daram rooye new_sen anajm midam




#3 --> vasete haro hazf kon



sen = float(input('senet cheghadre?'))


#az dakheli tarin bekhan 

#aval senet cheghadre?? --> taraf javab mide 
#mire dakhele float --> float mishe --> mide b zarfe akahr --> sen


print(sen) #40.0

print(type(sen)) #<class 'float'>

b= sen/4
print(b) #10



#hargone casting --> int() float() complex() bool() str() ......

#yechizi mizari toosh, int ro khorojhimdie 



sen = int(input('senet cheghadre?'))

print(type(sen)) #<class 'int'>



sen = int(float(input('senet cheghadre?')))


#37.5 FLOAT --> 3 7 . 5
#float -> int




'''

age inpiut ro khasti jolosho begiri

ya control C ya  dokme moraba ghermez




'''



#-----2- kjeywords--------------
#----------------for------

print('salam')


#agar bekham 50 bar benvisam salam

#yek khat benvisamo 50 bar tekrar beshe?

#logice manteghe barnamaro avaz koni


for i in range(0,50):
    print('salam')




#-------3---Variables------------
'''
dakhele zarf chia mitonim 
- Number  --> (int, float , complex)
- Bool --> (True , False)
- Str --> String (reshte)


'''



# Numbers

a=10 #int
b = 10.5 #float
c = 7j




a=10


a=50


a=80




#operation 

#a + b = c , aval zarf ro msiazi

#c = a + b

#()
c = a** b 
c = a*b 
c= a/b
c= a+b
c= a-b


c = (a**b) + 5
c = a**(b+5)


#dastor -> ejra kon, majbore k ejra kone


#human ----> python --> machine ()


#comparisonal(moghayese ei)
#soal miporsi
#== !=  > >= < <=

#montazer, soal porsidm --> True false

a=10
b=20

print(a==b) #False

print(a!=b) #true

print(a<b) #true
print(a<=b) #True

print(a>b) #False
print(a>=b) #False



#-----STr --> string ha

#harchizi da rkeyboarde shoam hast benvisidhg string 

#reshte reshte ee az character ha 


'''
C , C++

Character --> 


character, ---> reshte

harf, kalame, jomle --> str

berizesh dar yek zarf

va qutation bzn k man bfhmam in esme zarf nist



'''

name = 'ali'

sentence = ' be name khoda jalaseye dovom ro shoro mikonim '

#str




a=2
b='2'

#1- Python built in function
#2- Keywords
#3-Varibales
#3.1Numbers (int,float,complex)
#3.2. Bool 
#3.3.Str
#-------3.3.STR ha bokonim-----------


#3.3.1. Assignment --> str besazi

#esme zarf = qutation tosh mohtava

name = 'ali'

#esmo avaz
#Class
#class_
#class2

Class = 'computer'

company = 'fanavari co'

name = str('ali')



#3.3.2. Indexing

company = 'fanavari'


#computer --> index bandi mikonan

'''

-----------
RAm            |
               |
company size   |
type    value  |
-------------

value --> index gzoari mikone btone sdastresi 



fanavari

f  --> 0 
a ---> 1
n --> 2
a -->3
v -->4
a -->5
r --->6
i ---> 7 


1-->tamame value haye sequence --> indexing shodand dar Ram
2---> index ha az 0 shoro mishavad

'''




company = 'fanavari'

#az zarfe company ,indexe 0 ro bia behem bde
company[0] #Out[58]: 'f'

company[2] #--->n  a-->dovomin harfe ama dovomin index chon azz 0 shorop mishe

#3.3.3. slicing

#company[shoro:entha]

#exclude --> 

company[0:4] #'fana'

#f a n a v a r i
#0 1 2 3 4 5 6 7


company[5:7] #ar
company[5:8] #ari

company[8] #IndexError: string index out of range



#by default mifahme manzore az 0 ta 
company[:6] #Out[63]: 'fanava'
company[3:] #avari'



#company[shoro:entha:ghadam(step)]


#company[shoro:enteha:1]

#f a n a v a r i
#0 1 2 3 4 5 6 7

company[0:6] # 'fanava'

company[0:6:1] #'fanava'
#0 ta 6 ro yedone yedone bede

company[0:6:2] #'fnv'


new_name = company[1] + company[4] + company[5]
#######new_name = 'a' +'v' + 'a' = 'ava'

print(new_name) #ava





#-------
#1-Python buil in function
#2-kEYWORDS
#3-variabels (numbers, bool, str)
 
#asssignment --> megdhar
#indexing --> zarf[]   0 ,....
#slicing --> zaf[ebteda:enteha] enteha exclude 
#zarf[:enteha]  -->0
#zarf[ebteda:] --> mabzoet ta teshe
#zarf[ebteda:enteha:1] #step--> 1  , 2 , 3




#ama man ba str ham koli kar mikham anjam bdam


#str --> zamaniik shoma information darid






#--<> index , slice ,mikham taghurati ro roosh bdm





#Function haee k baraye STR (string )
#str.functions () -->


#https://www.w3schools.com/python/python_ref_string.asp


name='ali'

name.capitalize()

name.center()


txt = "banana"

x = txt.center(20)

print(x)
print(len(x)) #20



'''
Method	Description
capitalize()	+          Converts the first character to upper case
casefold()		           Converts string into lower case
center()	           	Returns a centered string
count()+		           Returns the number of times a specified value occurs in a string
encode()		           Returns an encoded version of the string
endswith()	           	Returns true if the string ends with the specified value
expandtabs()	           	Sets the tab size of the string
find()+	           	Searches the string for a specified value and returns the position of where it was found
format()		           Formats specified values in a string
format_map()		           Formats specified values from a dictionary in a string
index()		           Searches the string for a specified value and returns the position of where it was found
isalnum()		           Returns True if all characters in the string are alphanumeric
isalpha()	           	Returns True if all characters in the string are in the alphabet
isascii()	           	Returns True if all characters in the string are ascii characters
isdecimal()	           	Returns True if all characters in the string are decimals
isdigit()		           Returns True if all characters in the string are digits
isidentifier()	           	Returns True if the string is an identifier
islower()		           Returns True if all characters in the string are lower case
isnumeric()		           Returns True if all characters in the string are numeric
isprintable()		           Returns True if all characters in the string are printable
isspace()		           Returns True if all characters in the string are whitespaces
istitle()		           Returns True if the string follows the rules of a title
isupper()		           Returns True if all characters in the string are upper case
join()		           Converts the elements of an iterable into a string
ljust()		           Returns a left justified version of the string
lower()	+	           Converts a string into lower case
lstrip()	 +          	Returns a left trim version of the string
maketrans()		           Returns a translation table to be used in translations
partition()		           Returns a tuple where the string is parted into three parts
replace()+		           Returns a string where a specified value is replaced with a specified value
rfind()		           Searches the string for a specified value and returns the last position of where it was found
rindex()		           Searches the string for a specified value and returns the last position of where it was found
rjust()		           Returns a right justified version of the string
rpartition()		           Returns a tuple where the string is parted into three parts
rsplit()		           Splits the string at the specified separator, and returns a list
rstrip()+		           Returns a right trim version of the string
split()		           Splits the string at the specified separator, and returns a list
splitlines()		           Splits the string at line breaks and returns a list
startswith()		           Returns true if the string starts with the specified value
strip()	+	           Returns a trimmed version of the string
swapcase()		           Swaps cases, lower case becomes upper case and vice versa
title()	+	           Converts the first character of each word to upper case
translate()	           	Returns a translated string
upper()+		           Converts a string into upper case
zfill()		           Fills the string with a specified number of 0 values at the beginning


'''

#upper()

type('salam')



upper('salam') #NameError: name 'upper' is not defined

#tavabe ee hastan k fght baraye str bekar mire

name ='ali'

name.upper() #paantez

#Out[72]: 'ALI'

#taghir ijad nemikone, khoroji mide


print(name) #ali


new_name = name.upper()

print(name)#ali
print(new_name) #ALI

new_name2 = new_name.lower()

print(new_name2) #ali


brand = 'Kiko'



print(brand == 'kiko')

print('Kiko' =='kiko') #False

brand1='Kiko'
brand2='kiko'

print(brand1==brand2) #False

brand1[1]==brand2[1] #True
brand1[2]==brand2[2] #True
brand1[3]==brand2[3] #True
brand1[0]==brand2[0] #False



a=2
b='2'

#type


#case

name = 'ali'

print('Moshtarie gerami' , name)

#Moshtarie gerami ali

new_name = name.capitalize()
print('Moshtarie gerami' , new_name)

#Moshtarie gerami Ali

print('moshtarie gerami ', name.capitalize())





sentence='in the name of god'

sentence.capitalize()

#Out[90]: 'In the name of god'


sentence.title()
#Out[91]: 'In The Name Of God'


a=50

print(type(a)) #<class 'int'>

a.lower()
'''
AttributeError: 'int' object has no attribute 'lower'

'''




#zarf.function() 

#zarf taghir nmikonad, balke khorjii

#new_zarf = zarf.function()


#upper()
#lower()
#tilte()
#capitilize()

#---Str function 
'''
1-taghiri ijad mikonad ,

zarf.upper() , zarf.lower() ,zarf.title() zarf.capitalize() ,strip()
zarf.replace(old,new)



2-khrooji behet adad mdie

count()



3- Is 
yechizo checkmikonam behet true va false midan


'''

name = 'fanavari'


new_name = name.replace( 'f' ,'s' )
print(new_name) #sanavari



#strip() space ro hazf mikone

brand1='kiko'
brand2='kiko '

print(brand1==brand2) #False

print(len(brand1)) #4 -> k i k o
print(len(brand2)) #5 --> k i k o space

brand2[4] #' '
brand1[4] #IndexError: string index out of range


#kheyli jaha , user type  

brand2_normalzied= brand2.strip()



print(brand2_normalzied==brand1) #True

#space rast va chap ro hazf mikone


name = ' ali pilehvar '

name.strip() #Out[102]: 'ali pilehvar'

name.lstrip() #fght az chap --> left strip
name.rstrip() #righ --> az rast

#name.replace('a','b') harja a mdiid b 

name.replace(' ','') #'alipilehvar'


name.count('a') # 2

#yeja zakhire, print

name.find('a')  # 1 #find --> avalino k peyda mikoen behet pas mide na hamaro

'a' in name  # True


#tamrin --> tavabe ee k az str funciton tadris nashode ro ba yek mesal hal mikonid 


name='ali'
name.isalnum() #True

name='ali 4334'
name.isalnum() #False

name='32242334'
name.isalnum() #True



name='salam'
name.isdigit() #False

name='32873276'
name.isdigit() #true



name='32873276 '
name.isdigit() #false




name='23327h323dsdssdswd'
name.isdigit() #false



'''



1-Python built in functions
print() input() len()

2- Keywords 


3-Variables 

zarf --> value (meghdar)

3.1.Numbers [int,float,complex]  ** * / + - , == != > >= < <=
3.2. Bool [True , False]
3.3. String --> reshte 
[index] [start:end] zarf.str_function()

str function --> fght baraye str ha hastan , 
zarf.function()

emal nemishe, khorojhi mide

zarf_jadid = zarf.function()


3.3.1. Str function taghirati lower() upper() strip() replace()
3.3.2. .find('a')  .count('a')
3.3.3. True false --> isdigit() --> True , False




'''


name = 'ali'

name[0]='b'

'''
TypeError: 'str' object does not support item assignment
'''


new_name=name.replace('a','b')

#name -->ali
#new_name --> bli




#------------------------

#Chanta Value dashtim chetor?

#number, bool ,str --> tak value boodan

#agarma chandin megdhar ro bekhaymd ar yek zarf zakhire konim

#10 , 20 , 30

#Iterables---> dakheelsh iteration bezanin  [for ,....]

#list
#tuple
#set
#dictionary

#--------------------------
'''       List          '''
#--------------------------
#ordered (index) , changable, allow duplicated

a=10
b=20

#c=10,20,30,40


c = list([10,20,30,40]) #herfei nist

#beraket []
c = [10,20,30,40]



#harchizi ro mitoni bezari

c=[10,10.233223 , 1j , True , 'Ali']

c = [10,10,10,10,10,10,10,10]

#dastresi --> str 


#str --> yek listi az character ha hast

#name = 'ali' --> a l i 0 1 2

c=[10 , 10.233223 , 1j , True , 'Ali']
#  0      1        2      3       4


#zarf[index]
c[0]  #Out[3]: 10

c[1] #Out[4]: 10.233223

c[2]  #Out[5]: 1j



#change-------------
c[2]=10000

print(c)
#[10, 10.233223, 10000, True, 'Ali']




#slicing

c=[10 , 10.233223 , 1j , True , 'Ali']


c[1:4] #  1 2 3  #Out[8]: [10.233223, 1j, True]

d = c[1:4] 

print(d) #[10.233223, 1j, True]

name = c[4] # 'Ali'

character = name[1]

print(character) #l

#hamishe vasete ha ro hazf kon

c[4][1]

character = c[4][1]

print(character) #l


#dakhele yek list , list bezari

d= [10 , 20 , [10,20,30]]


d[2] # [10, 20, 30]

d[2][0] # 10


d[0][2] 
'''
TypeError: 'int' object is not subscriptable
'''




# Str functions -> emal nemishavad, balke khoroji mide (zarf)

# List functions --> emal mishavad , khoroji nemidahad


#jofteshon tavabe ei hastan k yeki baraye str ha bekar mire, 
#barsye list ha bekar miravad


name = 'ali'
print(type(name)) #<class 'str'>


#upper(name) -->python built in fucntions

#name.upper()

new_name = name.upper()

print(name) #ali
print(new_name) #ALI

#str functions emal nemsihavad, balke khoroji midahad


#List fucntion

#list.function() --> 

#emal mishavad ,khoroji nemidahad

'''
list functions


https://www.w3schools.com/python/python_ref_list.asp


Method  Description
append(+)       Adds an element at the end of the list
clear(+)         Removes all the elements from the list
copy()      Returns a copy of the list
count(+)          Returns the number of elements with the specified value
extend(+)       Add the elements of a list (or any iterable), to the end of the current list
index(+)        Returns the index of the first element with the specified value
insert(+)       Adds an element at the specified position
pop(+)     Removes the element at the specified position
remove(+)       Removes the first item with the specified value
reverse(+)    Reverses the order of the list
sort(+)      Sorts the list

'''



products =['Kiko','nike','adiddas','AP']

#yek adad vared konm
#chang 
#products[0]='sheglam'

#change --> b tabe niaz nadashti

#vared konam , jash konam --> insert konam

#insert

products.insert(1,'swatch')

#1 --> injori az tabve estefade msihe .insert(index,value)

#2--> niazi b zarf ndri


print(products)

#['Kiko', 'swatch', 'nike', 'adiddas', 'AP']








#-------
#b tahe list chizi ezafe konam --> kheyli vaghta 

products =['Kiko','nike','adiddas','AP']

len(products) #4 --> 0 1 2 3 

products.insert(3,'swatch')

print(products)

#['Kiko', 'nike', 'adiddas', 'swatch', 'AP']


products =['Kiko','nike','adiddas','AP']
products.insert(4,'swatch')
print(products)
#['Kiko', 'nike', 'adiddas', 'AP', 'swatch']


#len , bedonam yedone balatar az akahrin index, insert()

#tabe ei nist k man kh sade esm(value) -->b tahe 


products =['Kiko','nike','adiddas','AP']

products.append('swatch')


print(products)

#['Kiko', 'nike', 'adiddas', 'AP', 'swatch']




#shoma ag yek list ro bekhay b tahe in ezafe koni chtor?

products =['Kiko','nike','adiddas','AP']
new_products=['rolex' , 'D&G','zara']


products.append(new_products)


print(products)

#['Kiko', 'nike', 'adiddas', 'AP', ['rolex', 'D&G', 'zara']]
products[4] # ['rolex', 'D&G', 'zara']

#done done element ro b on tah ezafe konm 

#-> extend


products =['Kiko','nike','adiddas','AP']
new_products=['rolex' , 'D&G','zara']

products.extend(new_products)

print(products)

#['Kiko', 'nike', 'adiddas', 'AP', 'rolex', 'D&G', 'zara']


products[4] # 'rolex'
products[5] #'D&G'



#-----remove --> remove()

products =['Kiko','nike','adiddas','AP']

products.remove('nike')


print(products) #['Kiko', 'adiddas', 'AP']

products.remove('asdjhaduhsaasdj')
#ValueError: list.remove(x): x not in list



#element bdm bgm hazf kon, gahi mikham index bedam bgm hazf kon


#pop()
products =['Kiko','nike','adiddas','AP']

#hem emal mishe ham kjhoroji

products.pop(1) #Out[41]: 'nike'

print(products) #['Kiko', 'adiddas', 'AP']


#bana bar niazam agar niaz dahstamesh tooye yek zarf brizam


#clear and delete difference

a = [10,20,30,40]

a.clear()

print(a) #[]

#a= []



#az yek keyword estefade

#keyword --> banafsh -->

#baraye hazfe har zarfi --> az keyword del estefade

#del miad khdoe zarfo ba jash hazf mikone


del a
print(a) #NameError: name 'a' is not defined


del name
del new_name




names = ['ali','vahid','hamid','reza','ali']


names.count('ali') #Out[50]: 2


names.index('vahid') # 1
names.index('sdakjdns')
#ValueError: 'sdakjdns' is not in list


#names.index('vahid',2,5)
#ValueError: 'vahid' is not in list



#.index() --->  error mide ag nabashe


#.find() --> str

name='ali'

name.find('b') #Out[55]: -1
#-1 --> kh jaha b manie vojod nadashtan hast






a_list = ['ali','vahid','hamid','reza','ali']

a_list.sort()

print(a_list)

'''
['ali', 'ali', 'hamid', 'reza', 'vahid']


'''


a_list = ['ali','Amir','behta','Baran','zara']


a_list.sort()


print(a_list)


#['Amir', 'Baran', 'ali', 'behta', 'zara']

a_list.reverse()

print(a_list)

#['zara', 'behta', 'ali', 'Baran', 'Amir']


#-------------

a = [10,20,30,40]

b = a 
#yek zarf bename b beszz , a ro beriz tosh 

print(a) #[10, 20, 30, 40]
print(b) #[10, 20, 30, 40]



a.append(50)

print(a) #[10, 20, 30, 40, 50]
print(b) #[10, 20, 30, 40, 50]


#deep copy --> yani vaghty minevsiui b = a
#yani ta tahesh b = a , yani zarfe a ba b barabare
#pas hartaghiri rooye a bash e, rooye b ham etefagh mioofte

#backuop 

a = [10,20,30,40]
b = a.copy()  #snapshot migire

print(a) #[10, 20, 30, 40]
print(b) #[10, 20, 30, 40]


a.append(50)

print(a)  #[10, 20, 30, 40, 50]
print(b) #[10, 20, 30, 40]




# tavabe eei k khorji midan
#.count() .index() --> adad emal nmitonan
#.copy() -> khoroji mide
#.pop() --> ham emal mikone hajm khoroji

#ina emali hastan
#.insert() .append() .extend() .sort() .reverse() .remove() .clear()


#list haro yad grftim , [] , [index] ,[start:end] ,.list_functions()



#--------------------------------
#--------------------------------
'''          ITERABLES      '''
#--------------------------------
#--------------------------------

#list --> ordered (index), changable , allow duplicated
#tuple --> ordered (index) , unchangable , allow duplicated
#set --> unordered (no index) , unchangable , No duplicated
#dictionary --> index --> Keys



#------LIST------------
a1 = [10,20,30,40]
a1 = list([10,20,30,40])
a1[0] #Out[75]: 10  index dare (ordered)

a1[0]=400 #changable
print(a1) #[400, 20, 30, 40]

a1 = [10,10,10,20,30] #allow duplicated
print(a1) #[10, 10, 10, 20, 30]

#hameja list estefade msihe, 90% e jaha az list estefade mikonid




#-----TUPLE --------------
#index(ordered) , unchangable , allow duplicated
#Listi hast k change nadare ---> Database (paygahe dade) -->
# dataha k miano miran mire too hezaran function --> kole zarfo unchanagble esh mikonim

a2 = (10,20,30,40)
a2 = tuple((10,20,30))

print(a2) #(10, 20, 30, 40)

print(type(a2)) #<class 'tuple'>

a2[0] #Out[80]: 10
#ordered (index)

a2[0]=400
#TypeError: 'tuple' object does not support item assignment
#unchanagbkle

a2=(10,10,10,20)
print(a2) #(10, 10, 10, 20)


#pas agar man bekham yek tupel taghir bedam chtor??

a2 = (10,20,30,40)

a2[0]=100  #TypeError: 'tuple' object does not support item assignment

b = list(a2)

print(type(b)) #<class 'list'>

print(b) #[10, 20, 30, 40]

b[0]=100
print(b) #[100, 20, 30, 40]

a2= tuple(b)

print(type(a2)) #<class 'tuple'>

print(a2) #(100, 20, 30, 40)

a2=(10)
print(type(a2)) #<class 'int'>

#tuple tak elementi
a2 = (10,)
print(type(a2)) #<class 'tuple'>




#----SET----------
#unordered (no index) , unchangable , no duplicated

a3 = {10,20,30,40}
a3=set({10,20,30,40})

print(a3) #{40, 10, 20, 30}

a3[0] #TypeError: 'set' object is not subscriptable

#ordered nistan -> indedx nadaram

#a3[0]=400


a3 ={10,10,10,20,30}

print(a3) #{10, 20, 30}

#majmoe haye riazi 
#ya zamani k bekahhi -->tekrari haro hazf

#list ---> set --> list

a=[10,10,20,30,40]
#kara roo list kardi

b = set(a)

a = list(b)

print(a) #[40, 10, 20, 30]

'''
Method  Shortcut    Description
add()       Adds an element to the set
clear()     Removes all the elements from the set
copy()      Returns a copy of the set
difference()    -   Returns a set containing the difference between two or more sets
difference_update() -=  Removes the items in this set that are also included in another, specified set
discard()       Remove the specified item
intersection()  &   Returns a set, that is the intersection of two other sets
intersection_update()   &=  Removes the items in this set that are not present in other, specified set(s)
isdisjoint()        Returns whether two sets have a intersection or not
issubset()  <=  Returns True if all items of this set is present in another set
    <   Returns True if all items of this set is present in another, larger set
issuperset()    >=  Returns True if all items of another set is present in this set
    >   Returns True if all items of another, smaller set is present in this set
pop()       Removes an element from the set
remove()        Removes the specified element
symmetric_difference()  ^   Returns a set with the symmetric differences of two sets
symmetric_difference_update()   ^=  Inserts the symmetric differences from this set and another
union() |   Return a set containing the union of sets
update()    |=  Update the set with the union of this set and others

'''


#---------Dictionary-----------

'''
list ,  tuple

index    value
0       elm0
1       elm1
2       elm2
3       elm3
4       elm4
5       elm5




dict (dictionary)
key      value
key1      value1
key2     value2
key3     value3
key4    value4





set 
valu 
elm0
elm1
elm2
elm3
elm4





infromation (etelaat) hast
'''


a=['ali',49, '04402332231332', '09120000000' ,190 ,'tehran' ]


#b phone
#phoen trf idnexe 3 vome

a[3] # '09120000000'

a[4] #190


#a['ghad']
#a['phone']

#list?
print(type(a)) #<class 'list'>


#a_dict = { key1 : value1   , key2 : value2 , key3 : value3  }


a=['ali',49, '04402332231332', '09120000000' ,190 ,'tehran' ]
print(type(a)) #<class 'list'>
'''

index    value
0        ali
1        49
2
3
4
4



'''

a[0] #'ali'
a[5] #'tehran'


a[1]=50

print(a)
'''
['ali', 50, '04402332231332', '09120000000', 190, 'tehran']

'''





b= {'name' : 'ali'  , 'sen' : 49 ,
    'meli' :'04402332231332',
    'phone': '09120000000',
    'ghad':180 ,
    'city':'tehran'}

print(type(b)) #<class 'dict'>



'''

key   value
name   ali
sen    49
meli   ...
ghad   ..
phoen ....

'''
b['name'] # 'ali'

b['city'] #'tehran'



b['sen']=50
print(b)

'''
{'name': 'ali', 'sen': 50, 'meli': '04402332231332', 'phone': '09120000000', 'ghad': 180, 'city': 'tehran'}

'''


#kilidvazhe ye jadid ezafre koni

b['team'] = 'esteghlal'


print(b)

'''
{'name': 'ali', 'sen': 50,
 'meli': '04402332231332',
 'phone': '09120000000',
 'ghad': 180, 'city': 'tehran', 
 'team': 'esteghlal'}


'''


b.keys()

'''
Out[120]: dict_keys(['name', 'sen', 'meli', 'phone', 'ghad', 'city', 'team'])

'''

c = b.keys()
print(c)

print(type(c)) #<class 'dict_keys'>


d = list(c)
print(d)
#['name', 'sen', 'meli', 'phone', 'ghad', 'city', 'team']





b.values()

'''
dict_values(['ali', 50, '04402332231332', '09120000000', 180, 'tehran', 'esteghlal'])

'''

#dictioanry


d = list(b.values())
print(d)
#['ali', 50, '04402332231332', '09120000000', 180, 'tehran', 'esteghlal']


'''
Method  Description
clear() Removes all the elements from the dictionary
copy()  Returns a copy of the dictionary
fromkeys()  Returns a dictionary with the specified keys and value
get()   Returns the value of the specified key
items() Returns a list containing a tuple for each key value pair
keys()  Returns a list containing the dictionary's keys
pop()   Removes the element with the specified key
popitem()   Removes the last inserted key-value pair
setdefault()    Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()    Updates the dictionary with the specified key-value pairs
values()    Returns a list of all the values in the dictionary


'''



'''
Python


Human ( en) <-----Interface ----> Machine (bianry 0,1)


Python --> vocab, grammar


1- Python built in functions --> tavabe hastand baraye hame , yek amalkardi
narenji

print() , inpiut() , len() , type() ,....



2- Keywords -> logic manteghe barname ro avaz koni --> banafash

del , if , else , elif , for , while , def , and , or ,...



3- Variables --> sefid --> esme zarf

3.1. Numbers (int, float, complex) --> ** * / + - , == != > >= < <=
3.2. Bool (True,False)
3.3. Str --> '' , [index] [start:end:step] str.fucntions() --> emal nemishdo, khoroji midad
        zarf_jadid = zarf.str_fucntion()
        3.3.1. Taghirat --> .upper() .lower() .title() .replace() .strip() 
        3.3.2. Adad --> .count('a') .find('a')
        3.3.3. True false --> is --> .isdigit()
        
        
3.4. Iterables --> chanta Value ra dakhele yek zarf berizim

3.4.1. List (ordered(index),chanagble,allow duplicated)
        a=[10,20,30,10.3434, 1j , True , 'ali']
        a[index] , a[2:5]
        change --> a[index]=new_value
        list functions --> emal mishodan , khoroji nmikhas
        zarf.insert(4,new_value)
        zarf.append(value) ,zarf.extend(list)
        zarf.clear()   zarf.remove()
        zarf.pop() , .count() .index()
        
        aksare jaha shoma az list ha estefade mikonid
        
3.4.2. Tuple (ordered (index), unchanagbel , allow duplciated)
        yek listi hast k unchanagbel (DB)
        a= (10,20,30,40,50,60)
        a[index]
        a[index] =2323 --> error -> unchanagbel  b = list(a)  taghir a=tuple(b)
        tavabeye khodesho dahst
     
3.4.3. Set (unordered (no index) , unchanagble , no duplicated)
        majmoe riazi, gheyre terari
        a= {10,20,30,40}
        a[index ] NO --> indexi nadarad, chon index nadarad, taghiri nmitonad konad
        
        
        
3.4.4. Dictionary --> bejaye index value , key value
        a=['ali',40 , 180 ,...]
        a[0]
        
        
        a={'name':'ali' , 'sen' :40 ,....}
        
        a['name']
    
        a.keys()
        a.values()
        
        zamani k shoam information (etelaat darid)
        
        


'''




'''
Tamrin1 ------ jalase ghabl

ta panjshanbe ersal konand mamnoon




Tamrin 2 ------>


1--> Str functions ha list


str_functions.py --> done done random

name='esem khdoeton'

tabe haor tak tak emal konid va print()

#fingilish benveisid in tabe che karde



2---> List functions --> baaye functin haye list anjam dahid

list_functions.py



3,4(optional) tuple,set


5-->dictionary --> dict.py 

dictionary az information khodet mizare


'reshte_tahsili'


az tavabe dict functions azash estefade bokoni


'''







