'''
In The Name of GOD


Ali Pilehvar Meibody

16 Mordad 1405 - Fanavari Co

JALASE 3  Python 07 




'''



'''

Human (En) <-----Interface ---> Machine (bianry ,0,1)

Interface --> Python --> mokhafaf karde 0,1 --> python 


1-Python kernel 2- IDE/Editor (toosh code benvisam) -->ipython kernel --> machine -->ejra

man dastoor dadam computer --> programming


Python yek zaban --> vocabs , grammar 


# qutation --> coomment (description)


1- Python built in functions (tavabe dakheli python)
narenji (spyder)  ()  kari amalkardi

print() input() len() type() ,.....



2- Keywords --> logice barnamaro bwekhahid avaz koni --> banafsh
if else elif , for , while , def ,. and , or ,....


3- Variable Name 

zarf esm [value (meghdar)]


3.1. Numbers (int, float, complex)
   3.1.1. Mathematical operation --> () ** * / + - =
   3.1.2. Comparisonal operation --> == != > >= < < =
   
3.2. Bool (True , False)

3.3. Str (string) rehste e az character hae k shoam to keyboardet dari
     esm_zarf = 'sdjhjhgds'
     dastresi --> index --> 0 
     zarf[0]  
     zarf[1]
     zarf[start:end]  
     zarf[2:5]  2,3,4
     str functions --> emal nemishdoan, khoroji midadan
     
     new_zarf = zarf.lower()
     
     1--> lower() upper() title() strip() replace(old,new)
     2---> count('a')  .find('a')
     3--> isdigit() isalnum()
     
    
    
3.4. Iterables (chizhaee k ma bekhahim multiple value ra dakhele yek zar fbrizim
        
    3.4.1. List --> ordered (index), changable , allow duplicated 
        
        a = [10,20,30.43432,True,'dsa']
        
        a[index]
        a[0]
        
        a[0,3] 0 1 2
        
        a[0]=1000 change
        
        list functions --> emal mishan , khoroji nemidan
        
        a.insert(1,'dssd')
        a.append('')
        a.clear()
        a.remove()
        
    3.4.2. Tuple --> database 
        ordered (index) , unchangabel , allow duplicated
        listi hast k change nmishe
        
        a=(10,20,30,40)
        
        a[0]
        
        a[0]=1000 XXXXXXXX
        
        
        b = list(a)
        taghireto bedi
        
        a=tuple(b)
        
    3.4.3 Set --> majmoei haye riazi
    unordered (index nadaran) ,unchangable, No duplciated
    
        a={10,20,30,40,50}
        
        a[0] XXX --> index 
        
        
    3.4.4. Dict --> infromation (etelaat)
        a=['ali',30 , '0919111111','Tehran']
        
        a[1] -->sen
        
        a['sen']
        
        
        index value
        0
        1
        2
        
        
        key     value
        key1     value1
        
        
        a={'key1':value1 , 'key2'Lvalue2}
        a=['ali',30 , '0919111111','Tehran']
        
        
        b = {'name':'ali' , 'sen' :30 , 
             'phone' :'0919,,,,,,'}
        
        
        b['name'] --> ali
        
        b['name'] = 'vahid'
        
        
        b['code_meli'] ='0440......'
        
        

'''









a=20

print('salam')


#gahi shoma mikhahid yek khat az code, ya yek ghesmat az codeton
#ro bebandid b yek sharti (shart)

#yani man migam nemikham hamishe
#print salam ejra bshe


#python az bala b paein , chap b rast mese ye ensan mikhone codeto run mikone

#logico bekham avaz konm az keyword

#--> if else elif 








#a=10
#a=100
a='ali'

print('salam')




#agar a 10 bood : print('salam')

# 4 ta space ya yek tab (balaye caps lock) 



a=5

if a==10:
    print('salam')


#agar in shart True shod ejra kon, ag nashod ejra nakon





a=5

#print(a==10) --> False


if a==10:
    print('salam')







a=10

#print(a==10) -->  True


if a==10:
    print('salam')






'''

ye khat code daram --> in hamishe ejra mishe

print('salam') -->hamishe



bekhah shartish koni
yek khat gahbelsh --> if bezari

oon dastoro 4 ta space, 1 tab jolo 


if shart:
    print('salam')


shart---> True , False

== != > > < <=

isdigit() --> True false


'''






#Taklif --> agar sen balaye 18 bod benevise ghanoni 


sen = 10



print('ghanoooni')


#agar sen =10 --> ejra nashe
#agar sen =15 ejra nashe

#age sen = 19 --> ejra bshe --> ghanooni



sen = 10


if sen>18:
    print('ghanoooni')


'''

tarigheye nevehstam 


shekondam --> b sharti 

goftm ch dastorie 

bad 4 ta space

'''


'''

darkesh motefavete

'''


sen = 20


if sen>18:
    print('ghanoooni')

'''
sakhatre if




if shart:
    dastooor
    
    
dastoore man vabaste mishe b True bodane shart



'''


#az karbar tedade mahsoolatesho begire
#agar balaye 20 ta mahsole bege mobarake



'''
Farsi --> barname benevsi


Developer  farsi(en) --> Python


Computer Python --> Binary(0,1)




namayesh dahad, neshan dahad , show kone --> print()
begire , az karbar begirad, vared konad, --> input()
agar ama shart -_> if else ,....


'''

#az karbar tedade mahsoolatesho begire
#agar balaye 20 ta mahsole bege mobarake



print('------- Fanavari Shop ---------')
print('===============================')
print('salam arz shod')
tedad = int(input('Tedade mahsoolateton cheghadre ? :'))
#int , float


print('mobarake')


#hamishe ejra mikone mobarake





#--------------------

print('------- Fanavari Shop ---------')
print('===============================')
print('salam arz shod')
tedad = int(input('Tedade mahsoolateton cheghadre ? :'))
#int , float


if tedad>20:
    print('mobarake')



'''
------- Fanavari Shop ---------
===============================
salam arz shod
Tedade mahsoolateton cheghadre ? :10

vaghty man 10 zadam ,shart k tedad>20 --> fasle msihe

pas in zabone baz nmishe pas hichi ejra nmsihe



-->
------- Fanavari Shop ---------
===============================
salam arz shod
Tedade mahsoolateton cheghadre ? :30
mobarake

'''



print('------- Fanavari Shop ---------')
print('===============================')
print('salam arz shod')
tedad = int(input('Tedade mahsoolateton cheghadre ? :'))
#int , float


if tedad>20:
    print('mobarake')



'''
------- Fanavari Shop ---------
===============================
salam arz shod
Tedade mahsoolateton cheghadre ? :dah
Traceback (most recent call last):

  Cell In[35], line 4
    tedad = int(input('Tedade mahsoolateton cheghadre ? :'))

ValueError: invalid literal for int() with base 10: 'dah'

'''



print('------- Fanavari Shop ---------')
print('===============================')
print('salam arz shod')
tedad = int(input('Tedade mahsoolateton cheghadre ? :'))
#int , float


if tedad>20:
    print('mobarake')


#az karbar tedae mahsol begire
#agar adad dad --> zgar tedade >20 -->mobarake




print('------- Fanavari Shop ---------')
print('===============================')
print('salam arz shod')
tedad = int(input('Tedade mahsoolateton cheghadre ? :'))
#int , float


if tedad>20:
    print('mobarake')



#pas moshkel in bod k agar user bejaye adad, biad
#horof bezane --> nmitone tabeye int() onro b adad tabdil kone
#ali --:> ??   hamid , vahid -->

#error !!
#eerrorr --> app az kar miofte



'''

az user tedade mahsol ro begire (input)

--> int() ghablesh agar adad bod tabdilesh kon b int


'''

print('------- Fanavari Shop ---------')
print('===============================')
print('salam arz shod')
raw_number = input('Tedade mahsooleton cheghadre?:')
#raw --> kham 

print(type(raw_number)) #<class 'str'>
#<class 'str'>

#'10'

#type(raw_number)==int

a=10 #karaye riazi , int() ,...
b='10' #In nemitone


#------------
#------------
#------------


print('------- Fanavari Shop ---------')
print('===============================')
print('salam arz shod')
raw_number = input('Tedade mahsooleton cheghadre?:')
#raw --> kham

#raw number ? --> str 
#az ai beporsi --> aghaye ai --> chijori yek variable str ro befahmam hamash az number hast 

#print(raw_number.isdigit()) #True

#False
#False

#True --> zmani fght adad bashe

#raw_number.isdigit() --> shart 


if raw_number.isdigit(): 
    number = int(raw_number)
    
    if number >20:
        print('mobarake')
        

    
#-------------
print('------- Fanavari Shop ---------')
print('===============================')
print('salam arz shod')
raw_number = input('Tedade mahsooleton cheghadre?:')
if raw_number.isdigit(): 
    number = int(raw_number)
    if number >20:
        print('mobarake')
        
    

'''
Python az bala b paein az chap b rats mikhone ejra mikone
aval 3 ta printo mikone, bad dakhele input ro print mikone
montazer mishe user chizi vared kone

chzii k vared kard ro besorate str (string) mirize tooey raw_numebr 



raw_number.isdigit() ---> 
Agar True shod zabonash baz mishe

ag nashod --> hichi nmishe


ag true bashe --> zabone baz mishe





------- Fanavari Shop ---------
===============================
salam arz shod
Tedade mahsooleton cheghadre?:30
mobarake
'''





#Just IF --> faghat if 

'''
Shorooot 3 no hastan

vaghty code mnizni shoma , dar hame soorat codet ejra mishe
print()

a=10
c= a+b

har khat codet ejra mishe


bekhay shartish koni (agar o ama )



keywords --> if



1- Just If

fght if ---> rahzan mibinam

tamame code ha k az bala miano man mese karavan mibinam k daran rad mishan


if --> yek rahzane  jolouye hamaro migire

onae k sharteshon True bashe majboreshon mikone k ejra konan codo






2- If else



3- Elif 


'''

#shartish konm
#baraye

#shart -> chizi hast k javabesh True False

#1--> == != > >= <= <
#2--> str function is 
#3---> function() --> True false


if a>10:
    print('salam')
    
    
    
    
    

    
#aya fgrht yek khat ro mitonim shartish koniM.

#na ye section

#ta madami k ma yek tab(4 space) jolo hastim
#behesh migan badaneye shart --> if body



a=10
b=20
c=a+b
print("salam")
print(c)



if sen>18:
    a=10
    b=20
    c=a+b
    print("salam")
    print(c)
    
print('khobi')


#1--> joz ye khat , mitoni na tanha baraye yek khayt
#balke baraye chan khat shoma hsartish koni






sen = 10

if sen>18:
    print('salam')
    
print('khodafez')



#sen = 20 -->
'''
salam
khodafez
'''

#khodafez


#1--ta madami k dastorat y tab fasele dare b oon if motealegh hast

#2--> bad az if --> baraye hame yejoore


'''
      |
      |
     \/
     If(shart)
     |
  --------
 |True    | False
 |        |
dastor1   |
|         |
-----------
     |
     |
     |
  edameye code



'''



#paye ye pythone entezaei 

number = input('productet ro begoo:')

number = 30


l1=[10,20,30,40]

#l1=open(;;file)

l1[0]=100



'''
sakhtare just if



if shart:
    dastoor1
    dastoor2 (optional)
    ...
    
    ....
    
    
jozvi az body nist (false , tye)

dastoor canta

shart --> True False

'''

#sen <15 , ghad > 190  ---> estedade basketball


#and or
#and --> va --> joftesh --> bayad  
#or --> ya --> yekodom --> hadegahal


#dota shart darim --> age bgim joftesh Bayad True shavad --> ham sharte 1 va sharte 2 --> and

#dota shart darim -> hadegahal yeki , --> ya sharte 1 true she ya sharte 2 true she --> or


#And --> dar soratie k joftesh true bashe true mide

print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) #False



print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False


'''

if shart:
    dastoor
    
    
    
if shart1 and/or shart2:
    dastorr
    
    
joftesh hatman true she
vaghty bekahhim jfot sharta true bashe


if shart1 and shart2:
    dastopoor



agf begi hadegahal yekish

if shart1 or shart2:
    dastoor

'''


#dostan --> sen<15 , ghad > 150 bashe --> basketabll potential

#bayadie --> yeki karfrarma, pezehsk 


sen = input('senet cheghadre? :')
ghad = input('ghadet chegahdre?:')


print('potential basketball dari')

#in dar hame sorat ejra mishe haa sne , gahd



#-------

sen = int(input('senet cheghadre? :'))
ghad = float(input('ghadet chegahdre?:'))
#sen<15    ghad>150

#and or 
if sen<15 and ghad>150:
    print('potential basketball dari')

'''
senet cheghadre? :20
ghadet chegahdre?:120



senet cheghadre? :14 
ghadet chegahdre?:120


senet cheghadre? :18
ghadet chegahdre?:180


senet cheghadre? :12
ghadet chegahdre?:180
potential basketball dari
'''


#academy 

#ghadesh bishtar az 150 ya senesh zire 18 bod biad


sen = int(input('senet cheghadre? :'))
ghad = float(input('ghadet chegahdre?:'))
#sen<15    ghad>150

#and or 
if sen<15 or ghad>150:
    print('potential basketball dari')

#hame halati ghaboli

#joz inke baham batel she

#ham sene>15 , ham ghadesh <150 




'''

if shart:
    dastoor1
    dastoor(optional)
    ....
    
inja jozve if nist



if shart1 and/or shart2:
    dastoor1
    dastoor2(optional)





'''


print('------- Fanavari Shop ---------')
print('===============================')
print('salam arz shod')
raw_number = input('Tedade mahsooleton cheghadre?:')
if raw_number.isdigit(): 
    number = int(raw_number)
    if number >20:
        print('mobarake')
       



       
#if raw_number.isdigit() and number>20:
     
#yek shart poiushniaze sharte diagr hast --> if haye too dar too mizanim
'''
error
name = input("esmet chie")
if name='ali':
    print('salam')

'''


'''
sharti vghty khastim bokonim --> sharti ha
conditional statement ()

1- just if  --> rahzan 

      |
      |
     \/
     If(shart)
     |
  --------
 |True    | False
 |        |
dastor1   |
|         |
-----------
     |
     |
     |
  edameye code

      
veleshon kon 





2- if else

dorahi mikhahi  (gate)



rahe 1 --> dastoor 1 

      |
      |
     \/
     If(shart)
     |
  --------
 |True    | False
 |        |
dastor1   dastooor2
|         |
-----------
     |
     |
     |
  edameye code

chizi bename velesh kon nadarim

sen>18 -_> yechizi 
<18 --> hichi NAA --> yechizi 



3- elif



'''



sen = input('senet cheghadre:')

if sen>18:
    print('ghanoni')
    


#40 --> ghanoni
#25 --L ghanonio
#15 --> hichi (velesh kon) rahzan

#masael -_> tasmim begirim az kodom if mikhahi m 

#agar --> if ha gharar hast esrteafde konim az kodom?




#senet chegahdr --> >18 -_> ghanoni ei
#ag nabood hichi nagam 

'''

>18 (true) yekaro kon, ag nabod hichi rahzan




just if , if else, elif 

'''

sen = input('senet?:')

if sen>18:
    print('gjhanoni')
    
    


#agar sen>18 --> ghanoni , age nabod --> ghanoni nisti

#just if , if else, elif


if sen>18:
    print('ghanoni hasti')
else:
    print('ghanoni nisti')



#---example

sen=16

if sen>18:
    print('ghanoni hasti')
else:
    print('ghanoni nisti')

#20 -->ghanoni hasti


#16 --> ghanoni nisti




#agar add vared nakard -> hichi --> motasefane ehstebah vared krdi

print('------- Fanavari Shop ---------')
print('===============================')
print('salam arz shod')
raw_number = input('Tedade mahsooleton cheghadre?:')
if raw_number.isdigit(): 
    number = int(raw_number)
    if number >20:
        print('mobarake')
else:
    print('shoma number vared nakardid')
    
    
    
    
#-------------------------
'''
yek app i darim ke b shoma producti mikhahid 
bekharid 

mige produyct code 91 Zara khedmate shoma . 
code takhfif : 
    
    Z15 --> bege code takhfif emal shod
    
    eshtebah gof --> code takhfif eshtebah hast
    
'''


print('') #jalase 1 ro mojadad hamzaman bebinid va code bezanidesh


#code ro begire , check kone ag z15 bod emal shod ag nabod emal nashod



print('shoma mahole code 91 Zara  ro kharidari kardid')

code = input('code takhfif ra vared namaeed:')

#code takhfif 
#code_takhfif
#2code
#print


#sharte shoma bayd chzioi bashe k True false

#== != > >= < <=

#.isdigit() .


#code barabar bashe ba Z15 

#code='sajhasdg'
#print(code=='Z15')


#code='Z15'
#print(code=='Z15')

#


print('shoma mahole code 91 Zara  ro kharidari kardid')
code = input('code takhfif ra vared namaeed:')
 

if code == 'Z15':
    print('emal shod')
else:
    print('EMAL NASHOD')


'''
shoma mahole code 91 Zara  ro kharidari kardid
code takhfif ra vared namaeed:Z15
emal shod


shoma mahole code 91 Zara  ro kharidari kardid
code takhfif ra vared namaeed:shagsgddsg
EMAL NASHOD
'''


print('shoma mahole code 91 Zara  ro kharidari kardid')
code = input('code takhfif ra vared namaeed:')
 

if code == 'Z15':
    print('emal shod')
else:
    print('EMAL NASHOD')


a='z15'
b='Z15'
print(a==b) #False
#pyuthon case sensetive



print('shoma mahole code 91 Zara  ro kharidari kardid')
code = input('code takhfif ra vared namaeed:')
 

if code == 'Z15' or code=='z15':
    print('emal shod')
else:
    print('EMAL NASHOD')


#-----


print('shoma mahole code 91 Zara  ro kharidari kardid')
code = input('code takhfif ra vared namaeed:')

#code --> lower() -- > faslee heyae chapo rasto hgazf --> z15

code2 = code.lower() #Z15 ->z15 , z15-->z15 , sdjshdahsdg --> sdjshdahsdg , ALI -->ali

code3 = code2.strip() # z15 z15 

if code3=='z15':
    print('emal shod')
else:
    print('EMAL NASHOD')


#ino biaem --> herfei tar bokonim --> vasete hareo hazf kon


print('shoma mahole code 91 Zara  ro kharidari kardid')
code = input('code takhfif ra vared namaeed:')

if  code.lower().strip()  =='z15':
    print('emal shod')
else:
    print('EMAL NASHOD')
        
     
'''

1500 euro --> backend (python (django))

500-600 euro --> frontend (html,..)


2100 euro bedi ->b do nafar 


full-stack -->  1900 karo mibandam




'''




'''
shart ha estefade konim



se ta shart darim


1- just if --> rahzan , fght kasani k sharteshon True bashe

      |
      |
     \/
     If(shart)
     |
  --------
 |True    | False
 |        |
dastor1   |
|         |
-----------
     |
     |
     |
  edameye code






2- Dorahi hast --> if else --> if True --> yek akr , false --> yk kare dg 


if shart:
    dastor1
    dastor2
    ........
else:
    dastoor3
    dastoor4
    ....
    



      |
      |
     \/
     If(shart)
     |
  --------
 |True    | False
 |        |
dastor1   dastooor2
|         |
-----------
     |
     |
     |
  edameye code




3- dorahi bashim k dorahi haee to dar too bashan
elif 


agar sene fard bala 18 bashe benevis ghanoni , ag nabod hichi nanevi s--> 

age sene fard bala 18 bashe beenevis ghanoni ag nabashwe benevis ghanoni nisti --> do rahi

age sene fard bala 18 bashe benevis ghanoni , ag nabood ( ag >14 nime ghanoni , zire 14 motalaghan gheyre ghanoni)



      |
      |
     \/
     If(shart1)
     |
  --------
 |True    | False
 |        |
dastor1   shart2
|         |
|       -------------
|       |true       |false
|       dastoor2   dastooor3
-----------
     |
     |
     |
  edameye code




'''



if sen>18:
    print('ghanoni')
    a=10
    b=20
    d=a+b
    print(d)
    
else:
    print('gheyre ghanoni')
    a=100
    b=200
    c=a+b
    print(c)
    
    
    
    
#---------
sen = int(input('senet chegahdre?:'))

if sen>18:
    print('ghanoni')
elif sen>14:
    print('semi ghanonie')
else:
    print('motalghan gheyre ghanoni')
    
    
'''

      |
      |
     \/
     sen>18
     |
  --------
 |True    | False
 |        |
ghanoni   sen>14
|         |
|       ----------------------
|       |true(18>x>14)      |false (>14)
|       semi gahanoni       motalaghan
-----------
     |
     |
     |
  edameye code




'''
    
     
    
'''

ghad >180 --> basketball 

ag beyne 180 - 160 --> valyball

zire 160 --> football





farsi --> python 



yek appi mikham k az karbar ghadesho begire va bbini age ......


agar 180 b bala bood --> basketbal
ag 180>x>160 --> vollyball
ag 160>< ---> football

rahzan, dorahi, dorahi haye to dar too

elif
'''



ghad = int(input('ghadet cheghadre?'))


if ghad>180:
    print('boro basketball')
elif ghad>160 : #ey kasani k kochiktar aaz 180 hastid , 
    print('boro vollyball')
else: #>180 --> >160 --> <160
    print('boro football')
    
    



'''
L1 ro bekhoonid

L2 ro bekhoonid

code bznid --> 


L3 --->

Quiz3 ---

q3.1. Yek adad begire az karbar , bebine positive, negative, zero


q3.2.yek adad begire bebine farde ya zoje


q3.3. yek machine hesab besazid , 
yek adade (number1) yek adade number2
yechizi begire operation (jam , tafrigh,taghsim,zarb)
anjam bede print kone


q3.4. nomreye daneshjo ro begri eye adadi beyne 0 ta 20

ag 18 - 20 --> A
16 0 18 --> B

14-16 --C
10-14 --> d

<10 --> f (faill)


q3.5. az karbar esme product ro begire berize to zarf

gheymatesho begire berize too zarf

code takhfif begire

age code takhfif barabar bood ba z14

20% az gheymat kam kone nmaayesh bede
bege gheymate nahaei ine 


q3.5.2. --> ag code takhfif eshtebah zad --> bege 
ghalat zadid

q3.5.3 --> ag ghalat zad, bege yekbar dg mitoni emtehan kone
ag doros zad anjam bde (takhfif) ag na --> bege block shodid

'''



















'''


