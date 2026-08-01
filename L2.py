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



name='ali'

name[0]='b'
'''

TypeError: 'str' object does not support item assignment

'''




#str --> listi az character ha hast
#list --> listi az element ha hast


#zarf[2]  --> 0 1 2chaeracter

#list --> list[2] -->2 vomin element 

#----------------------
#numbers, bool, str --> tak value boodan


#agar man chandin megdhar ra bekhaham dar yek zarf zkhire konm che???



#10 , 20 30 

#Iterables --> dakheelsh iteration --> 

#List
#tuple
#set
#dictionary


#-------LIST--------
#indexed , changable , allow duplicated


a=10

b=20

#c=10,20,40,50

#list

c = [10,20,30,40]

#c=list---> [eleme1,elem2,elem3,]
c  = list([10,20,30,40])



c = [10,20,30,40]


#harchizi k delet mikhad
#---assignment

#c=open('User/apm/desktop/moshtarian.csv')
#c[5]






c= [10 ,10.323232 , 1j , True , 'Ali']
#   0      1        2  

#dastresi-->elemnt dastresi pedya konM???

c[0] #Out[123]: 10

c[1] #Out[124]: 10.323232


c[2] = 1000

print(c)
'''
[10, 10.323232, 1000, True, 'Ali']
'''




#slicing

c= [10 ,10.323232 , 1j , True , 'Ali']

d = c[1:4] #[10.323232, 1j, True]

name=c[4]

name[1]

#-------
c[4][1] #Out[130]: 'l'
#az C k yej liste , ali ro bekesh biron
#[1] --> l



d = [10 ,20 , [10,20,30]]

d[2] #[10, 20, 30]

d[2][0] #10


d[0][2] #TypeError: 'int' object is not subscriptable



#str fucntions 

#List fucntions --> tavabe ei k baraye list jhastan

name.upper() #Out[137]: 'ALI'

zarf = name.upper()



'''
list functions


https://www.w3schools.com/python/python_ref_list.asp


Method	Description
append(+)	    Adds an element at the end of the list
clear(+)	     Removes all the elements from the list
copy()	    Returns a copy of the list
count(+)	      Returns the number of elements with the specified value
extend(+)    	Add the elements of a list (or any iterable), to the end of the current list
index(+)	    Returns the index of the first element with the specified value
insert(+)	    Adds an element at the specified position
pop(+)	   Removes the element at the specified position
remove(+)    	Removes the first item with the specified value
reverse(+)	  Reverses the order of the list
sort(+)	     Sorts the list

'''


#insert(index,value)-------


products =['Kiko','nike','adiddas','AP']

#insert()

products.insert(1,'swatch')


#NameError: name 'products' is not defined


#tavabaye str --> emal nmishod, khorojhi midad (zarf)
#tavabeye list --> emal mishe, khoroji nemide 


print(products)

'''
['Kiko', 'swatch', 'nike', 'adiddas', 'AP']

'''
products =['Kiko','nike','adiddas','AP']

len(products) #4

products.insert(3,'swatch')


print(products) #['Kiko', 'nike', 'adiddas', 'swatch', 'AP']




products =['Kiko','nike','adiddas','AP']

products.insert(4,'swatch')

print(products)

#['Kiko', 'nike', 'adiddas', 'AP', 'swatch']



#append(element)
products =['Kiko','nike','adiddas','AP']

products.append('swatch')
#yek elemento 


print(products)
#['Kiko', 'nike', 'adiddas', 'AP', 'swatch']


#yek liste dg ei ro b entehaye yek liste dg 
#append

#extend

products =['Kiko','nike','adiddas','AP']
new_products=['rolex' , 'D&G','zara']


#yedone elemnt product tahesh
#products.append(')

products.append(new_products)




products =['Kiko','nike','adiddas','AP']
new_products=['rolex' , 'D&G','zara']
products.extend(new_products)




products.remove('nike')

print(products) #['Kiko', 'adiddas', 'AP', 'swatch']

products.remove('nnnnnnnn') #ValueError: list.remove(x): x not in list


products =['Kiko','nike','adiddas','AP']

products.pop(1)

#na tanha hazf mikone, (emal)
#oon elemente hazf shode ham bsorate khoroji mide
#zarf briuzi


print(products) #['Kiko', 'adiddas', 'AP']


#delete , clear --> tamame python

#dlkdeet --> az paye o asas hazf koni

#clear --> dakhelesho remove koni

products.clear()


print(products) #[]
a=[]


#baraye tamame variable ha hast na fght list
del products

print(products) #NameError: name 'products' is not defined



products =['Kiko','nike','adiddas','AP']

products.sort()


print(products)
#['AP', 'Kiko', 'adiddas', 'nike']

#aval horofe bozorg ro omade a - z
#horofe kochik a - z

products =['Kiko','nike',10 , 100 , 200 , 'adiddas','AP']

products.sort() #TypeError: '<' not supported between instances of 'int' and 'str'

print(products)




products =['Kiko','nike','adiddas','AP']
products.count('Kiko') #Out[163]: 1 , 2, 3



#0---------
products =['Kiko','nike','adiddas','AP']
products.index('Kiko') # 0
products.index('AP') #Out[165]: 3




a=[10,20,30,40]

b = a
print(a) #[10, 20, 30, 40]
print(b) #[10, 20, 30, 40]






a.append(50)
print(a)  #[10, 20, 30, 40, 50]
print(b) #[10, 20, 30, 40, 50]

a=[10,20,30,40]

c =  a.copy()


a.append(50)

print(a) #[10, 20, 30, 40, 50]
print(c) #[10, 20, 30, 40]





a='ali'

b = a

a[0]='g' #TypeError: 'str' object does not support item assignment



#--------------
#str , list 

#Tuple , Set , dictionary
#list --> indexed , changable, allow duplicated
#tuple --> indexed , unchangable , allow duplicated
#set --> XX INdex , unchangable , No duplicated
#Dictionary --> index (dige ei)


#---------------

a = [10,10,10,10]

#------tuple -->
#[]

a= (10,20,30,40)

a=tuple((10,20,30,40))

print(type(a)) #<class 'tuple'>


a[0] #Out[181]: 10

a[0:3] #Out[182]: (10, 20, 30)

a[0]=100


'''
TypeError: 'tuple' object does not support item assignment

'''

#tuple --> list

#lisyt --> hamishe

#tuple --> database (paygahe dade)
a= (10,20,30,40)

print(type(a)) #<class 'tuple'>

b = list(a)

print(type(b)) #<class 'list'>

b[0]=1000
print(b) #[1000, 20, 30, 40]


a = tuple(b)

'''
https://www.w3schools.com/python/python_ref_tuple.asp


Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found


'''



a=(10)
print(type(a)) #<class 'int'>


a=(10,)
print(type(a)) #<class 'tuple'>





#------------
#list --> indexed, changable ,allow duplicated
#tuple -> indexed , unchangable(db) , allow duplicated
#set --> unindexed , unchnagbale , No duplicated


#{}

a={10,20,30,40}

print(a)
#{40, 10, 20, 30}

a[0] #TypeError: 'set' object is not subscriptable

#a[]


#kheyli jaha tooye majmoe ha


a=[10,20,20,30,40,50]

b = set(a)

print(b)
#{40, 10, 50, 20, 30}

'''
Method	Shortcut	Description
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns True if all items of this set is present in another set
 	<	Returns True if all items of this set is present in another, larger set
issuperset()	>=	Returns True if all items of another set is present in this set
 	>	Returns True if all items of another, smaller set is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others

'''



'''

iterable python --> Python neveshte 



ketabkhone --> numpy

numpy array <---> list
object --> C++
python --> Interface 


import numpy as np
a = np.array([10,20,30,40])
a[0] #Out[198]: 10



'''



#------------
#list --> sequence 
#tuple --> db
#set --> majmoe riaziat



a=['ali',49, '04402332231332', '09120000000' ,190 ,'tehran' ]



a[0] #Out[199]: 'ali'

a[1] #Out[199]: 'ali'


#bejaye index --> 

#a[3]

#a['phone']
#a['name']

#dictionary



'''
list , tuple (unchangable)

index   value
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
value
elm0
elm1
elm2






'''

#bazi az datah kilidvazhe eie , information (etelaat)

a=['ali',49, '04402332231332', '09120000000' ,190 ,'tehran' ]



#{}

'''
zarf = {  key1 : value1  , key2 :value2 , ....    }


'''

a_list=['ali',49, '04402332231332', '09120000000' ,190 ,'tehran' ]

a_tuple=('ali',49, '04402332231332', '09120000000' ,190 ,'tehran' )

a_set={'ali',49, '04402332231332', '09120000000' ,190 ,'tehran' }



#a_dict={'name' : 'ali' , 'sen':49 , 'meli':'04402332231332' }

a_dict={'name' : 'ali' ,
        'sen':49 ,
        'meli':'04402332231332',
        'phone':'09192111221',
        'city':'tehran'}


a_list[0] #Out[203]: 'ali'

a_dict['name'] #Out[204]: 'ali'

a_dict['sen'] #Out[205]: 49



a_dict['new_key']  = 'new_value'

a_dict['country'] = 'iran'


a_dict.keys()
'''
dict_keys(['name', 'sen', 'meli', 'phone', 'city', 'country'])

'''

a_dict.values()
'''
dict_values(['ali', 49, '04402332231332', '09192111221', 'tehran', 'iran'])

'''


'''
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary


'''

a_dict={'name' : 0 ,
        'sen':1 ,
        'meli':2,
        'phone':3,
        'city':4}


a_dict['name'] #0

a_list[a_dict['name']]


#internal indexing 

'''
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary

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


4-->dictionary --> dict.py 

dictionary az information khodet mizare


'reshte_tahsili'


az tavabe dict functions azash estefade bokoni





1- Python buklt in functions (mohem tarinash)
2- Keywords
3- Variables (int,float, complex, str, list,tuple,set ,dictionary)



jalaseye ayande -->morori roo hame mbahes 

Keywords (If, else ,elif)

inja bema ejaze mdiei avalipsudocode -->

shebhe code --> va ejaze mdie k ma avalin shebhe barname ro benvisam

bejaye yadgirie entezaei , amaliati yadesh begirim








'''











