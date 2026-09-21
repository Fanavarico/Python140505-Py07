"""

In The Name of GOD
Created on Mon Sep 21 20:12:09 2026


@author: Ali Pilehvar Meibody

"""


'''
-------

Human (eng) <--------interface(python) -----> Machine (0,1 binary)



python -- zaban --> vocab , grammar


1 - Python built in function s--> tavabe ye dakheli python
spyder --> narenji
karbord daran, amalkard daran
print() , input() , len() , type() ,.....


2- Keywords --> logico taghir bedin

IDE/Editor , code python , run mizanid --> ipython --> trasnlate (execute) --> binary
ipython az bala b paeen, az chap be ratst mesle yek ensan mikhonatresh
agar hsoma bekhahid jaei mantegh ro avaz konid -->keywords

dakheel spyder --> banafsh


    2.1. Conditional statement (dastoorate shart)
    ama agar marid, dasdte bandi, range
        2.1.1. Just if -> rahzan --> catch konid
        if shart:
            dastooor
            
        2.1.2. If else --> do rahi besai
        if shart:
            dastor1
        else:
            dastoor2
            
        2.1.3. If elif else ->do rahi haye to dar too
        if shart1:
            datsoor1
        elif shart2:
            dastoor2
        else:
            dastoor3
            
            2.1.3.1. Multiple selection --> jam , tafrigh ,...
            2.1.3.2. Range --> 20 - 15 --> A , 15- 10 -->
            
            
        and -> dota shart hatman bayad baham true shan
        or --> hadegaghal yek shart
            
    2.2. Loops --> halghe ha
    
    2.2.1. For loop --> baze darim
        for shomarande in baze:
            dastoori 
        
        2.2.1.1.static repeat --> tekrare sabet
        for i in [1,2,3,4,5]:
            print('salam')
            
        for i in ['ali','vahid','hamid']:
            print('salam')
            
        for j in [1,2,3,4,5]:
            print('salam')

        for i in range(0,100,1):
            print('salam')
            
        
        2.2.1.2.dynamic repeat --> khode shomarande dakhele 
        khode dastoor bashe --> shomarand etaghir mikone
        dastooram taghir mikone --> dynamic repeat
        
        2.2.1.3. Iteration --> varede yek list beshid if o else o..
        
        for i in my_list: #iteration
            if i>500: #access
                #action
                print(i)
                count = count + 1
                new_list.append(i)
                
        pass --> boro jolo --> yek tabe, for , pass 
        continiue --> oon shoamrande ro mipare mire badi
        break--> mishkoni
        
        
    2.1.2. While
    
        while shart:
            anjam bede
            
        aval shoroe shart --> yek chizi bashe ke varedesh bshi
        i>10 -- > i =5 
        
        
        ekhtetam dashte basge (endless loop) i=i+1
        
        
        while True:
            hamishe vard mishe
            if shart:
                Break beshkon --> az halghe betone biad bron
        
    2.3. Functions --> box darim vorodiu migire va khoroji dare
    
    vorodi --> Box --> khoroji
    
    def name(v1,v2,...):
        logic
        return o1,o2,....
    
    zarf = name(10,20) -->
    
    L6 , L7 --> in details sohbat krdim
                
1(pythn buil in) narenji
keywords --> banafsh
harchi dg --> sefid --> esme yek zarf dar nazar migire


3-variables
    3.1. numbers 
        3.1.1. Int --> 10,20,30
        3.1.2. Float --> ashar 10.333
        3.1.3. complex -> 1j --> riaziate mokhtalet estefade mishe
        
        c = a + b
        ** , * , / , + , -
        
        comparison -> moghayese
        == != > >= < <= --> true false moghayese , dakhele yek if , while
        
    3.2. Boolean --> True , False
    
    3.3. Strng --> Str
    
        name='ali'
        qutation estefade mikordi
        
        access --> name[index] --> name[0] 
        
        index az 0 shoro mishe
        
        name[0:5]  0 1 2 3 4 
        
        str functions --> tavabe e bodan k emal nmishodna khorji midn (zarf)
        
        new_name = name.upper()
        new_name = name.strip()
        
        
    3.4. Iterables --> chandin meghdar ra varede yek zarf konim 
    multiple values inside one variabel
    
        3.4.1. List --> order (index) , changable, allow duplicated
        
            a=[10,20,30,40]
            a=['alio',20,20.443 , True]
            
            a[index]
            a[2:4]  elemente 2 , 3 bede
            
            a[3]='vahid'
            
            list functions --> khoroji nemidan, emal mishe
            
            a.append(10)
            
            #10 o b a ezafe mikone
            
            insert() append() clear() remove() pop()
            
        3.4.2. Tuple --> listi hast ke change nmishe (DBha eestefade msihe)
            order(index) , unchangabale, allow duplciated
            
            a= (10,20,30,40)
            a=(10,)
            
            a[2]  #datsresi
            
            a[2]=100 ### shdoani nist
            
            b = list(a)
            b[2]=100
            a  = tuple(b)
            
            casting
            
            tupel fucntions dari
            
            
        3.4.3. Set --> no order ( no index) , unchanagbale, No duplicated
        
            a={10,20,3,40}
            majmoeye riaziat
            
            set fucntion --> .interation() -->eshterak, ejtema ,..do majmoe sete riazi
            
            vaghty tekrari haro bkhahi haxf koni
            
            a=[10,20,30,40,10]
            
            b=set(a) #-->{10,20,30,40}
            a=list(b) #-->[10,20,30,40]
            
            
        
        3.4.4. Dictionary --> infrtomation [ensan, product,...]
        
        
        a=['ali',40,'0919...']
        
        a[2]
        
        
        index value
        0
        1 
        2
        
        key valye
        
        a={'esm':'ali'   , 'sen':40 , 'phone':'0919..'}
        
        a['phone']
        
        
        dictionary fucntiuons 
        
        .keys() -->kilkdvazeh haro
        .values() --> val haro
        .items() -->joftesho mide --> for
        
'''





#=============================================
#=============================================
#=============================================
#=============================================
#=============================================
# L6 - 20 tasks


'''
1_calculate_age.py

Dar in file shoam bayad yek tabe (function) benevisid ke yek vorodi begire (sale tavalod) va sen ro hesb kone va sen ro khoroji bede .

a ) hamin soal hast ke vorodi fght sale tavalod hast

b ) yek tabe digar besazid do vorodi begire, sale tavalod va tarikh . tarikh agar miladi bod besorate miladi hesab kone agar shamsi bood shamsi hesab kone. yani be tabe masalan bedim (1377,'shamsi') ya inke bedim (1999,'miladi')

c) hamoon tabeye (b) ro benevisid , agar tabe fght yek vorodi gereft , be sorate pish farz miladi dar nazar begire

d) tabe ro begone ei benevisid ke fght yek vorodi begire yani fght tarikh , ama khodesh betone tashkhis bede k miladi user dade ya shamsi (hint : range ro check koni )
'''


#BOX mikham 

# sal ----> Box --> sen
#vorodi : sal ---> BOX --> khoroji : sen

#ensan chikar mikone?

#vorodi : sal ---> ENSAN --> khoroji : sen

#mesal (mesal hamishe bzn) chantra
#ke tabe ei ke minevisi fght yek dota case ro ok nkone, geenralize (general)

#1370 --> chijori hesabmikonM?
#sali ke toosham -> 1405 - 1370 --> 35 sal



def calculate_age(birthday_year:int)->int:
    '''
    This function is used to get birthday year and return back the calculated age
    
    Input
    ------------
    birthday_year : int 
        this is the year that you born
        
    output
    -------------
    age : int
        this is calculated age on Shamsi calender
        
    **note : this function used 1405 as reference
    
    '''
    age = 1405 - birthday_year
    #print
    return age
    

help(calculate_age)
'''
Help on function calculate_age in module __main__:

calculate_age(birthday_year: int) -> int
    This function is used to get birthday year and return back the calculated age
    
    Input
    ------------
    birthday_year : int 
        this is the year that you born
    
    output
    -------------
    age : int
        this is calculated age on Shamsi calender
    
    **note : this function used 1405 as reference
    
'''

    
    
    
zarf = calculate_age(1375)
print(zarf) #30

calculate_age(1990) #Out[4]: -585



def calculate_age(birthday_year):
    age = 2026 - birthday_year
    #print
    return age

calculate_age(1990) #Out[5]: 36




#--------------
#input?? ---> front (html ,...) rsal mishe ba backedn
#codeton migire

#framework -> django, fastapi

'''
@post('/age')
def calculate_age(birthday_year):
    age = 2026 - birthday_year
    #print
    return age

'''

#sal = int(input('saleto bego'))
#calculate_age(sal)




#sal, tarikh ---> BOX ---> sen

def calculate_age(sal,tarikh):
    
    if tarikh=='shamsi':
        age = 1405 - sal
        return age
    elif tarikh=='miladi':
        age = 2026 - sal
        return age
    else:
        raise ValueError('Shoma mitavanid fght miladi ya shamsi bedid')
        #print(....)
        #return 
        #return None
        #hichi
        
        
ValueError()
SyntaxError()
#search error list
#gpt 10 taye mohemo bego
ZeroDivisionError()


calculate_age(1990,'miladi')

#use kon
calculate_age(1990,'ghamari')


#----------------------
#----------------------
#----------------------
#c
calculate_age(1990) #TypeError: calculate_age() missing 1 required positional argument: 'tarikh'



def calculate_age(sal,tarikh='miladi'):
    
    if tarikh=='shamsi':
        age = 1405 - sal
        return age
    elif tarikh=='miladi':
        age = 2026 - sal
        return age
    else:
        raise ValueError('Shoma mitavanid fght miladi ya shamsi bedid')
        #print(....)
        #return 
        #return None
        #hichi
        
        
        
calculate_age(1405,'shamsi')
calculate_age(1990,'miladi')
calculate_age(2000) #Out[16]: 26


calculate_age(1405,'miladi') #Out[17]: 621

#khodet befahmi, tabe nemifhme vase hmaina zt vorodimigire


#----d---- khodet befahm

#sal --> box --> sen


def calculate_age(sal):
    if sal>1500:
        age = 2026 - sal
    else:
        age = 1405 - sal
    
    return age
        
        

    
def calculate_age(sal):
    if sal>1500:
        age = 2026 - sal
        return age
    else:
        age = 1405 - sal
        return age

        


def calculate_age(sal):
    if sal>1405:
        age = 2026 - sal
        return age
    else:
        age = 1405 - sal
        return age

      


def calculate_age(sal):
    if sal>2026:
        raise ValueError('nemishe')
    elif sal>1405:
        age = 2026 - sal
        return age
    else:
        age = 1405 - sal
        return age


#----------------------------------------
#----------------------------------------
#----------------------------------------
#----------------------------------------
#2- calculate_number

def calculate_number(number):
    if number%2==0:
        return 'Even'
    else:
        return 'Odd'

zarf = calculate_number(10) #Out[18]: 'Even'



#b------

def isEven(number):
    if number%2==0:
        return True
    else:
        return False


#sen = int(input('seneto begoo:'))
#if isEven(sen):
    
isEven(10) #Out[20]: True

#---c---
def calculate_number(number):
    if number==0:
        return 'Zero'
    elif number>0:
        return 'positive'
    else: #number<0
        return 'negative'
    
    
#----------------------------------------
#----------------------------------------
#----------------------------------------
#----------------------------------------

def check_age(age):
    if age>18:
        return 'Welcome' #print XXXXX ->ZARF=check_age()
    
    else:
        return 'Access denied'


   
    
def check_age(age):
    if age>18:
        return 'Welcome' #print XXXXX ->ZARF=check_age()
    
    else:
        raise ValueError('Access denied') #return
        


    
#----------------------------------------
#----------------------------------------
#----------------------------------------
#----------------------------------------

#4_calculate_grade.py



#number --> Number --> str (a,b,c,)

def calculate_grade(grade):
    if grade>100:
        raise ValueError('nemishavad balaye 100 bshad')
    elif grade>=90: #[90 - 100]
        return 'A'
    elif grade>=80: #[80-90
        return 'B'
    elif grade>=70: #[70-80
        return 'C'
    elif grade>=60:
        return 'D'
    else: #<60
        return 'F'
    
zarf = calculate_grade(79)
print(zarf) #c


#----------------------------------------
#----------------------------------------
#----------------------------------------
#----------------------------------------
#5_name_cleaner.py

#string --> fucnton --> string pas mide


name = "   aLi   pILeHvAr     "

name.strip() #Out[22]: 'aLi   pILeHvAr'


name.replace(' ','') #Out[23]: 'aLipILeHvAr'


def name_cleaner(name):
    name2 = name.strip()
    clean_name = name2.title()
    return clean_name
    
    
def name_cleaner(name):
    clean_name = name.strip().title()
    return clean_name

    
  
def name_cleaner(name):
    return name.strip().title()


name = "   aLi   pILeHvAr     "
name_cleaner(name) #Out[27]: 'Ali   Pilehvar'
    



#---------------------
sentence='ali,payam,mohsen'

sentence.split()#Out[28]: ['ali,payam,mohsen']

sentence.split(' ')

sentence.split(',') #Out[30]: ['ali', 'payam', 'mohsen']





def name_cleaner(name):
    #name.split(' ')
    new_name = name.split() 
    clean_name =new_name[0].title() + ' ' + new_name[1].title()
    return clean_name
    


name_cleaner("   aLi   pILeHvAr     ") #Out[34]: 'Ali Pilehvar'


name_cleaner("   aLi   pILeHvAr  Meibody   ")  #Out[35]: 'Ali Pilehvar'
#rare case --> nader begard

def name_cleaner(name):
    #name.split(' ')
    splitted_name = name.split()
    
    joined_name=' '.join(splitted_name)
    clean_name = joined_name.title()
    return clean_name
    


name_cleaner("   aLi   pILeHvAr     ") #Out[34]: 'Ali Pilehvar'

name_cleaner("   aLi   pILeHvAr  Meibody   ")  # 'Ali Pilehvar Meibody'


#----------------------------------------
#----------------------------------------
#----------------------------------------
#----------------------------------------
#str --> function --> boolean
#checkinge too dar too

def check_email(email):
    
    if '@' in email:
        if '.com' in email:
            if ' ' not in email:
                return True
                
            else:
                return False
        else:
            return False
        
    else:
        return False
    
    
#----------
def check_email(email):
    
    #dorahi haye to dar too 
    #na if haye to dar to
    if '@' not in email:
        return False
    elif '.com' not in email:
        return False
    elif ' ' in email:
        return False
    else:
        return True


#-------- if haye jodagane + counting

def check_email(email):
    error_count=0
    

    if '@' not in email:
        error_count = error_count + 1
    
    if '.com' not in email:
        error_count = error_count + 1
        
    if ' ' in email:
        error_count = error_count + 1

    if error_count==0:
        return True
    else:
        return False
        


def check_email(email):
    pass_count=0
    
    if '@'  in email:
        pass_count = pass_count + 1
    
    if '.com'  in email:
        pass_count = pass_count + 1
        
    if ' ' not in email:
        pass_count = pass_count + 1

    if pass_count==3:
        return True
    else:
        return False



#-------
all()
any()


a=[True,True,False,True]

all(a) #Out[41]: False

#tabeye all yechizie -->ya true mide ya false
#age hame azaye list True bashan --> true


a=[True,True,False,True]
b= [True,True,True,True]
c = [True,False,False,False]
d = [False, False, False, False]

all(a) #fALSE --> hame true nisan
all(b) #True ->ham true
all(c) #fasle
all(d) #false


#any --> agr hadeghal yekishon True bashe
any(a) #true
any(b) #true
any(c) #true
any(d) #False


def check_email(email):
    shart1 = '@' in email
    shart2 = '.com' in email
    shart3 = ' ' not in email
    
    #har se ta shart bayad true bashe
    all_shart = [shart1,shart2,shart3]
    
    if all(all_shart):
        return True
    else:
        return False
        
    

def check_email(email):
    shart1 = '@' not in email
    shart2 = '.com' not in email
    shart3 = ' ' in email
    
    #har se ta shart bayad true bashe
    all_shart = [shart1,shart2,shart3]
    
    if any(all_shart):
        return False
    else:
        return True
    
#Moghayese --> computation (mohasebat)
#gpt --> begid kodom behine tarhast

#logical --> dorost bashe
#clean -> tamiz
#optimize ---> calculation (mohasebta) --> mohasbeat kmtr
#zamane kamtaer --> barghe kamtar


#----------------------------------------
#----------------------------------------
#----------------------------------------
#7_check_password.py
#password(str) -->box ---> str()

#tamrin --> rahe balaor inja 
def check_password(password):
    
    if len(password)<8:
        print('password kochiktar az 8 ragham hast')
        #raise ValueError('password kochiktar az 8 ragham hast'')
    elif password.isdigit():
        print('password bayad horof dahste bashe')
    elif password.isalpha():
        print('password bayad adad ham tosh bashe')
    #islower()
    else:
        print('password ba moafaghiat sabt shod')


#password(str) --> box --> True,False
def check_password(password):
    
    if len(password)<8:
        return False
    elif password.isdigit():
        return False
    elif password.isalpha():
        return False
    #islower()
    else:
        return True
    
    

print('------Login form---------')
username = input('user name:')
password = input('password:')

if check_password(password):
    #databse --> zahire mikoni ,... 
    
    print('ba moafghiat anjam shode')
else:
    print('error : sabt nashod')


#------------
def check_password_strength(password):
    #strength 
    #shart -> True doros bode
    shart1 = len(password)>=8
    shart2 = not password.isdigit()
    shart3 = not password.isalpha()
    shart4 = not password.islower()
    shart5 = not password.isupper()
    
    if all([shart1,shart2,shart3,shart4,shart5]):
        strengt=4
        
    elif all([shart1,shart2,shart3]):
        strength = 3 
    elif shart1:
        strength =2 
    else:
        strength=1
        
    return strength
        
#----------------------------------------
#----------------------------------------
#----------------------------------------
def count_letter(word,chararacter):
    count =0
    for char in word:
        if char == chararacter:
            count = count + 1 
            
    return count 


count_letter('alipilehvar','a') #Out[52]: 2
        
def count_letter(word,chararacter):
    count = word.count(chararacter)
    return count   

    
#jomle , kalame
sentence='i love python and i love deep learning'
#(sentence,love)

sentence.count('love') #Out[53]: 2


def count_word(sentence,word):
    count = sentence.count(word)
    return count 

#ba for

def count_word(sentence,myword):
    count = 0 
    senetnce_list = sentence.split()
    for word in senetnce_list:
        if word == myword:
            count = count + 1  
    return count 

    
    
#---------------
#find_max.py


def find_max(mylist):
    
    maximum = mylist[0]
    
    for number in mylist:
        if number >= maximum:
            maximum = number
    return maximum


def find_min(mylist):
    
    minimum = mylist[0]
    
    for number in mylist:
        if number <= minimum:
            minimum = number
    return minimum



#----average -->


#---sum----
def my_sum(mylist):
    total=0
    for number in mylist:
        total = total + number
        
    return total

#sum()



def my_len(mylist):
    count=0
    for number in mylist:
        count = count + 1
    return count


def average(mylist):
    avg = my_sum(mylist) / my_len(mylist)
    return avg

def average(mylist):
    avg= sum(mylist) / len(mylist)
    return avg


def average(mylist):
    count=0
    total=0
    for number in mylist:
        total = total + number
        count = count + 1
        
    avg = total / count
    return avg


#--11_failed_score.py---



#a---


def failed_score(scores):
    pass_list=[]
    for score in scores:
        if score>=10:
            pass_list.append(score)
    return pass_list

    
failed_score([10,12,20,5,6,7,18]) #Out[58]: [10, 12, 20, 18]


        
#--b----
def failed_score(scores):
    failed_list=[]
    for score in scores:
        if score<10:
            failed_list.append(score)
    return failed_list

failed_score([10,12,20,5,6,7,18]) #Out[59]: [5, 6, 7]




#---c


def pass_counter(scores):
    count = 0 
    for score in scores:
        if score>=10:
            #pass_list.append(score)
            count = count + 1
    return count

        
    
pass_counter([10,12,20,5,6,7,18]) #Out[60]: 4


#onaei ke fail shdoan ro beshmore
    
def failed_counter(scores):
    count = 0 
    for score in scores:
        if score<10:
            count = count + 1
    return count

        
#---12_calculator.py-------

def calculator(numb1,numb2,operation):
    if operation=='jam':
        result = numb1 + numb2 
        return result
    elif operation=='tafrigh':
        result = numb1 - numb2 
        return result
    elif operation=='zarb':
        result = numb1 * numb2 
        return result
    elif operation=='taghsim':
        result = numb1 / numb2 
        return result
    else:
        raise ValueError('shoma mitonid fght (jam,tafrigh,zarb,taghsim) estefade konid')



#estefade az tab eine

zarf = calculator(numb1=10,numb2=20,operation='jam')
    

#---------
numb1 = float(input('number 1eton ro bedid:'))
numb2 = float(input('number 2eton ro bedid:'))

operation = input('operationeton ro bedid')
    
    
calculator(numb1,numb2,operation)


#***** --> tabe barash mohem nist ke vorodi hash
#khodet neevshti, az input miad , ya az frontend miad ya ahrchi
#vorodi daryaft mikone ejra mikoen khoroji mide




def countdown(number):
    for i in range(0,number):
        print(10-i)


countdown(10)
'''
10
9
8
7
6
5
4
3
2
1
'''

def countdown(number):
    for i in range(0,number+1):
        print(10-i)



countdown(10)
'''
10
9
8
7
6
5
4
3
2
1
0

'''

#nokte-->tabe hatman --> khoroji ndre -> sedah bzni

def multiplication_table(number):
    for i in range(1,11):
        print(number,'*',i,'=',number*i)
        
multiplication_table(5)

'''
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50

'''



'''

voroditoon --> formi chizi darid dictionary 

name: ali  , lastname : pilehvar
phone : 0919.....
sen : 

{name:'ali' , }


listi az mahsolat darid --> [dict1,dict2,dict]
[tupletuple,tuple]

listi az listi

iterables az iterables ha dari


'''
#agar mojod bashe --> True , false

'''
products = {
    "iphone": 5,
    "macbook": 2,
    "airpods": 0
}
'''


def check_stock(products,product):
    if products[product]==0:
        return False
    else:
        return True
    
    

    
products = {
    "iphone": 5,
    "macbook": 2,
    "airpods": 0
}  
    
    
check_stock(products,'iphone')    #Out[68]: True
check_stock(products,'airpods') #Out[69]: False
check_stock(products,'glass') #KeyError: 'glass'

#production
products = {
    "iphone": 5,
    "macbook": 2,
    "airpods": 0
}  

products['iphone']

#motmaen nistik oon key vojod dre

products.get('iphone') #Out[71]: 5

zarf = products.get('glass')
print(zarf) #None

#error nmide


zarf = products.get('glass',0)
print(zarf)




#professional
def check_stock(products,product):
    availability = products.get(product,0)
    if availability==0:
        return False
    else:
        return True
    
    
    
#----------------------
def check_stock(products,product):
    for product_name, stock in products.items():
        if product_name==product:
            if stock==0:
                return False
            else:
                return True
        
  
    
#=================================================

products=[ {'code':'z1' , 'name' :'zara cloth 121' ,'price':30},
          {'code':'z2' , 'name' :'zara shooes 100' ,'price':45},
          {'code':'z3' , 'name' :'zara cloth 451' ,'price':35},
          {'code':'z4' , 'name' :'zara shooes 300' ,'price':55},
          {'code':'z5' , 'name' :'zara shooes 231' ,'price':60},
          {'code':'z6' , 'name' :'zara bag 400' ,'price':110},
          {'code':'z7' , 'name' :'zara bag 500' ,'price':95}]


def find_price_by_code(products,code):
    for product in products:
        if product['code']==code:
            return product['price']
            
find_price_by_code(products,'z3')    #Out[78]: 35


 
        
    
    
    
def find_name_by_code(products,code):
    for product in products:
        if product['code']==code:
            return product['name']
            
find_name_by_code(products,'z3') #Out[79]: 'zara cloth 451'

def find_tuple_by_code(products,code):
    for product in products:
        if product['code']==code:
            product_tuple = (product['code'],product['name'],product['price'])
            return product_tuple


find_tuple_by_code(products,'z3') #Out[81]: ('z3', 'zara cloth 451', 35)




#inout dakhele yek tabe estefade



def food_oder():
    print('Salam menuye ghaza : gheyme,ghorme sabzi,kabab,..')
    food_list=[]
    
    
    while True:
        ghaza  = input('ghazaro entekhab kon:')
        
        if ghaza=='order':
            break
        
        food_list.append(ghaza)
        
    return food_list   


food_lists=food_oder()
print(food_lists)
#['gheyme', 'ghorme', 'kabab', 'jooje', 'pitza']



#soale 18 , 19 , 20 --> dostanik naneveshtan benevisan (optional)
#ejbarish --> L8 --> pythonpackages o .. balad bashid
#dar file haye joda




#flder L6







