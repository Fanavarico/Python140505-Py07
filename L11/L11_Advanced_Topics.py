"""
Created on Fri Oct 16 14:56:51 2026

@author: Ali Pilehvar Meibody

L11 advances

Chanta ghesmat monde az class ha ke be onvane pishrafte shenakhte mishe

"""





#====================================
#====================================
'''        Class Attribute        '''    
#====================================
#====================================

'''
Ma ta alan migoftim class yechizi dare bename attributes va method

attributes yani moteghayer haei ke baraye oon object hast 


masalana


'''
class Product:

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.tax = 0.10


p1 = Product("Laptop", 1000, 5)
p2 = Product("Phone", 500, 10)

print(p1.tax)  # 0.1
print(p2.tax)  # 0.1

#object attributes yani pr1 va pr2 yechizi daran bename tax ke harkodom dare

#megdhare  tax baraye har mahsool besorate mojaza negahdari mikonim
#agar dar beyne hame mahsoolat moshtarak bashe ? mitonim behesh begim
#class attribute


#Class Attribute yani moteghayeri ke dar badane class tarif beshe na dakhele init ya method haye dg



class Product:

    tax = 0.10

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


p1 = Product("Laptop", 1000, 5)
p2 = Product("Phone", 500, 10)


#hala ma yek p1 , p2 darim , khodeshon attributes daran
#bename name,price,stock

#hamchnin yek attribute daran bename tax ke dar sat he class hast


#baraye dastresi behesh 2 rah hast

#aaz khode class 
print(Product.tax)  # 0.1

#az khode object ha
print(p1.tax)       # 0.1
print(p2.tax)       # 0.1



#Maziat chie? ine ke bekhay tax ro taghir bedi ba yek dastoor msihe, naizi nist
#baraye hame object ha taghir bedi


#ba yek dastoor
Product.tax = 0.20

#in taghir krd easy
print(p1.tax)  # 0.2
print(p2.tax)  # 0.2






#ama agar shoma in karo koni -->
p1.tax = 0.30

print(p1.tax)       # 0.3
print(p2.tax)       # 0.2
print(Product.tax)  # 0.2

#fght vase p1 avaz mishe chon instance attribtue hast na class attribute



#Koja kheyli estefade mishe ? --> baraye shomareshe object ha
class Product:

    total_products = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price

        Product.total_products += 1


p1 = Product("Laptop", 1000)
p2 = Product("Phone", 500)
p3 = Product("Monitor", 300)

print(Product.total_products) #3

#ba har bar sakhtanesh --> in shoamande tedadesh ziad mishe










#====================================
#====================================
'''  Encapsulation and property        '''    
#====================================
#====================================

#aya mishe attributes haye dakhele yek class ro az biron taghir dad ?

#bale


#masalan
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


p1 = Product("Laptop", 1000)



#gheymatesh ro bekhay bbini
p1.price  #1000

#mitoni be sadegi taghiresh bdi

p1.price = 2000

#hala ag bkhay bbini

print(p1.price)  #2000


#hala age beiaym benevsiim 

p1.price = -5000 

#aya mahsool ba gheymate manfi manteghi hast? kjheyr

#pas bayad betoonim ghavanine marboot b taghir egheymat ro control konim



# 3 gharardad namgzoari attributes darim

class Product:

    def __init__(self):
        self.price = 1000
        self._stock = 10
        self.__secret = "ABC"


#price ---> Public (dastresi mamooli)
#_stock --> Non_public (gharar dad baraye estefade dakheli)
#__secret --> name mangling -> taghire name dakheli baraye jologiri 


#Python mahdoodiate private nadare , vaghty shoma roye yek variable udnerline (_) 
#Mizarid yani agah in private e havaset bashe

#yadeton bashe ke az class , moshtari mostaghim estefade nemikone
#ya khodet estefade mikoni, ya yeki az ketabkhoonat 
#pas naizi nist jolosho sakht begiri , kafie ba yek _ neshon bedi
#agha in dakhelie 

#pas hamchin chizi besaz


class Product:

    def __init__(self, name, price):
        self.name = name
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, new_price):

        if new_price < 0:
            raise ValueError("Price cannot be negative")

        self._price = new_price


#inja dar asl harki product besaze bekhad bezanid .price 
#chizi nmaire, ama _price yani private dakhelie 

#pas na dast mizane na taghir mide (gharardade)

#bekhad prico bbine mizane .get_price()

#bekhad taghir bede mizane .set_price(new_price)
#va dakheel in tabe hala mitoni controllesh koni


p1 = Product("Laptop", 1000)

print(p1.get_price()) #bejaye p1.price

p1.set_price(1500)  #bejaye p1.pric = 1500

print(p1.get_price())



#In kar karbordie, ama python yek emkane behtari dare bename proeprty

#ba decoratore Properrty mitoni in kar ro jori koni ke
#shabihe yek attribute adi bashe




class Product:

    def __init__(self, name, price):
        self.name = name
        self._price = None
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):

        if new_price < 0:
            raise ValueError("Price cannot be negative")

        self._price = new_price




#yani price ro aval _ mizari khdoesham misazi

#ama dota tabe be esme hamoon variable mizsazi va 

#yek khali k harmoghe seda zad bargardoone , yedone ham setter 


p1 = Product("Laptop", 1000)

print(p1.price)   # 1000   #-->ino k mizni def price() seda mikhore

p1.price = 1500  #ino mziani tabe ye @price.setter seda mikhore

print(p1.price)   # 1500

p1.price = -100   # ValueError




#dar zaher darim ba yek attribute kar mikonim
#ama da rpposjht sahne dare ba methode getter va setter estefade mishe





#in property fsaghat baraye etebar sanji (validation) nist
#masalan fek kon damara mikhahim centigradd bezari va farenthait ham bashe

class Temperature:

    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32


t1 = Temperature(30)

print(t1.fahrenheit)  # 86.0



#tavajo kon .faenheit has na .farenheit()

#va to besadegi dige nemitoni tgahiresh bedi
t1.fahrenheit = 100  #AttributeError













#====================================
#====================================
'''  Other methods        '''    
#====================================
#====================================

'''
ta inja bishtare method ha ba self neevshte mishe 

aya bayad tamame method haye class self dashte bashe ?


na vagheiat .

ma dar python 3 no method darim 

1- instance method
2- class method
3- static method


'''



#------- 1 - instance methdo

#in haman methodi hast ke ghablan yad gerefte eim

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self, percentage):
        self.price -= self.price * percentage / 100


p1 = Product("Laptop", 1000)

p1.apply_discount(20)

print(p1.price)  # 800.0



#vaghty minevisim
p1.apply_discount(20)
#yani python p1 ro be onvane self dar ekhtiare method gharar mide




#-------- 2 - class method
#gahi mikhahim yek method bejaye objecte khas ba class kar konim
#miaym az @classmethod estefade mikonim

class Product:

    tax = 0.10

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def change_tax(cls, new_tax):
        cls.tax = new_tax


#yani bejaye self az cls estefade mikonim


Product.change_tax(0.20)

print(Product.tax)  # 0.2

#inja cls be hamoon class eshare mikone ke hamoon Product hast

#yeki az mohemtrin karbord ha --> sakhte object az dade haye mokhtalef


#masalan yek dade darim injori
data = {
    "name": "Laptop",
    "price": 1200
}


##mitonim benevisim

p1 = Product(data["name"], data["price"])


#ama raveshe behtar ine yek factory method dashet bashim
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            price=data["price"]
        )



#bejaye inke biaym 
#p1 = Product(data["name"], data["price"])



#mitonid ghable sakhte object, khode tabe ro seda bezani

data = {"name": "Laptop", "price": 1200}

p1 = Product.from_dict(data)

print(p1.name)
print(p1.price)



#kolan ziad mibinid tavabe ei mesle from_felan




#-------- 3 - static method

#gahi tavabe ei darim ke az nazare mozoei motealegh b clas hast
#ama be etelaate object niaz nadare (yani self nemikhad)
#be etelaate class ham niaz nadare (yani cls nemikhad)

#masalan motabar bodane code yek mahsool


class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def validate_code(code):
        return len(code) >= 4


#chon az self ya cls estefade nmikone
#mitoni vorodi self nazari va balasgh bezari staticmethod



#onmoghe bedone skahtane object ham mitoni azash estefade koni

print(Product.validate_code("A123"))  # True

print(Product.validate_code("A1"))    # False






#-----Yek mesale tarkibie vaghei ei

class Product:

    tax = 0.10
    total_products = 0

    def __init__(self, name, price):
        if not self.is_valid_price(price):
            raise ValueError("Invalid price")

        self.name = name
        self.price = price

        Product.total_products += 1

    # Instance Method
    def final_price(self):
        return self.price * (1 + self.tax)

    # Class Method
    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["price"])

    # Static Method
    @staticmethod
    def is_valid_price(price):
        return isinstance(price, (int, float)) and not isinstance(price, bool) and price >= 0


data = {"name": "Phone", "price": 500}

p1 = Product.from_dict(data)

print(p1.final_price())             # 550.0
print(Product.total_products)       # 1
print(Product.is_valid_price(-50))  # False










#=================================================
#=================================================
'''  Inheritance, Polymorphism , composition '''
#=================================================
#=================================================


# yad avari inheritance 
#goftim ke ma mahsole digital darim o phsyici

#har do no mahsol nam price ghabeliat forosh darand

#pas ma yek class misazim bename valed




class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(self.name, self.price)



#bad omadim too digitalProduct ono ers bordim



class DigitalProduct(Product):

    def __init__(self, name, price, download_link):
        super().__init__(name, price)
        self.download_link = download_link


class PhysicalProduct(Product):

    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight




#yani DigitalProduct yek no product hast
#phstyicalproduct yek no produyct hast





#Hamishe ingdhr sade yek class az yek classe dige ers nemibare

#chandin no ers bari darim




# 1-  Single inheritance --> ers barie sade

#hyek classe farzand az yek class valed ers bari mikone
class Animal:
    pass

class Dog(Animal):
    pass







# 2- Multilevel inehritance --> ers barie chand sat hi
class Mammal(Animal):
    pass

class Cat(Mammal):
    pass



#yani cat az mammal , mammal az animal.





# 3- Hierarchical Inheritance --> ers bari selsele maratebi

#in hamon chizi bod ke yad dadim , yani chand farzand az yek valed ers bebare


class Dog(Animal):
    pass


class cat(Animal):
    pass


#do farzande dog va cat az animal




# 4 - Multiple inheritance

#yani yek farzand az do class besorate hamzaman ers bebare
class Flyer:
    pass

class Swimmer:
    pass

class Duck(Flyer, Swimmer):
    pass



# 5 - hybrid inheritance --> ers bari tarkibi

#tarkibi az do ya chand sakhtare ghabli



'''

Nokteye mohem ine ke vaghty ma chandin class darim, in class ha mitonan baham rabete haye
motefavet dashte bashand


INHERITANCE (ERS BARI) yeki az in ravabet hast 


Ravabeti ke darim



pas inja darmorede rabeteye beyne class ha harf mizanim

'''


#A - INHERITANCE     (IS-A)

#yek class noe dige ei az classe dige hats

#masalan dog yek animal hast

class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog()
dog.eat()    # Inherited
dog.bark()   # Own method


#choon dog omade az animal ers borde

#key estefade mishe ? vaghty vaghean yek class yek noei az clase dige hast

#Mesle digitalproduct ke dar asl yek product hast




#B - ASSOCIATION (ERTEBAT)

#in yani do class ba ham ertebat daran ama maleke yek digar nistand


#masalan yek class darim Teacher va yek class darim student 
#dakhele teacher mitonim student haro ezafe konim b listesh

#In dota baham inehritance nistand ama baham ertebat daran


class Student:
    def __init__(self, name):
        self.name = name

class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

s1 = Student("Ali")
t1 = Teacher("Sara")

t1.add_student(s1)







# C - Aggregation (Tajmi)  (Weak HAS-A)

#in yani yek class majmoei az ashyaye digar ro dar ekhtiar darad, ama an ashya mitavanand mostaghel bashand

#maslaan yek teame football bazikon dare , vali bazikon bedone an team ham vojod dare




class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

p1 = Player("Ali")
p2 = Player("Reza")

team = Team("Barcelona")
team.add_player(p1)
team.add_player(p2)

#mohem ine ke p1 o p2 kharej az clas Team sakhte shodand .
#dar asl aggregation jozve association hesba mishe 




# D - Composition (Tarkib) (STRONG HAS-A)

#shabihe aggregeation hast vali malekiato vabastegi mafhoomi ajza be kol ghavi tare


#masalan yek sefareshe foroshgahi shamele item haye sefaresh ah hast
#in item ha dar modele ma motalegh be haman sefareshan va bedone sefaresh mani ei nemidan


class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        item = OrderItem(product, quantity)
        self.items.append(item)

order = Order()
order.add_item("Laptop", 2)
order.add_item("Mouse", 1)




#inja khode Order dar delesh miad class ro misaze
#farghesh ba ghabli ine ke 

#ghablie khode player vaghty object joda misazi khdoeshon ham karaye khodeshono daran
#amal misazi bad midi be tavabe


#ama dar inja, az biron nemisazi , balke yek tabe az classe Order khdoesh orderitem misaze



#che zamani estefade mishe? vaghty ajzaye dakhelie motlegh b sheye moshakahs hastand va 
#charkheye omreshan tahte modiriate an ast




# E - Dependency (Vabastegi) (USES-A)

#yani yek class baraye anjame kari az classe digari estegae mikone, bedone inke lozoman
#an ra be onvane yek vzihegi daemi dar nazar begie

#masalan yek gozaresh baraye chap shdoan az yek chapgar estefade mikone

class Printer:
    def print_text(self, text):
        print(text)

class Report:
    def generate(self, printer):
        printer.print_text("Sales Report")

printer = Printer()
report = Report()

report.generate(printer)



#yani class report baraye generate kardn niaz dare b printer




'''

*****

Aya hame in haro bayad hefz kard?

NA vagehan, shoma kafie bedonid ke

class ha mitonan mostaghel az ham bashand ya hamdigar ro ers bari konand

nesbat be niazemon miaym ravabete beyneshono anajm midim mesle
ers bari ya association ya .....


pas khondane in chzi ha fgth maro ashna tar mikone, gharar nist hefzeshon konim


'''















#--------------------------------------------
'''
Polymorphism   (chand rikhti)
'''
#--------------------------------------------

'''
dar barname nevisim, yek mafhoome mohem an ast ke
object haye mokhtalef mitavanand be yek darkhaste moshtarak , raftare motefaveti bedahand




yani fekr kon ma digitalprodyct darim va physical product

dar asl baraye digitalproduct gheymate delivery 0 hast ama delivery physical product be
jermesh rabt dare



pas miaym aval dakhgele classs Product ke madar hast in tabeye delivery_cost ro misazim ama
not implementesh mikonim k mostaghim nashe azash esteafde kard


ama in tabeye yeksan ro ham baaye digital misazim ham baraye physicalproduct va mitonan baham motefavet bashan


bebin daghighan yekchizi mesle overwrite hast . overwrite vaghtie ke
classe farzand yek tabe dare k esmsh ham esme tabeye valed (madar) hast ama
amalkard frgh mikone



inja class haye farzznd done donashon tabeye ham esm daran ama amalkardashon motefavete
kari ba madar nadarim 


balaei ro migan method ovrwrite,, be in migan polmorphism


'''




class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def delivery_cost(self):
        raise NotImplementedError(
            "Subclass must implement delivery_cost"
        )


class DigitalProduct(Product):

    def delivery_cost(self):
        return 0


class PhysicalProduct(Product):

    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight

    def delivery_cost(self):
        return self.weight * 5000




p1 = DigitalProduct("Python Course", 500)
p2 = PhysicalProduct("Laptop", 20000, 2)




#pas dar asl bebin methode do object yek nam dare

print(p1.delivery_cost())  # 0

print(p2.delivery_cost())  # 10000





#maziatesh chie? farz kon 100 mahsool darim

#bedone polymorphism ma bayad hey typesho check mikrdim


'''
if product_type == "digital":
    ...
elif product_type == "physical":
    ...
'''


#ama alan kheyli rahat
products = [
    DigitalProduct("Python Course", 500),
    PhysicalProduct("Laptop", 20000, 2),
    DigitalProduct("Ebook", 100),
    PhysicalProduct("Monitor", 5000, 5)
]

for product in products:
    print(
        product.name,
        product.delivery_cost()
    )



#yani hardafe prodiuct.delivery_cost() baraye ham product ha ejra mishe
#ba in tafavot ke age digital bashe tabeye khdoehs, phsycial bashe tabeye khodesh















#=================================================
#=================================================
'''  Built-in fucntions for class  '''
#=================================================
#=================================================


'''
az beyne tavabeye built in functisons, yekserish baraye kar ba class o obejct has


type()       tashkhise noe object
isinstance()    barresi inke object nemoneye yek clas hast ya na (true,false)
issubclass()   barresi rabete ers bari beyne class ha (true,fase)

getattr()     khandane attribute ba name matni
setattr()     sakht ya taghire attribute
hasattr()     barresi vojod attribute
delattr()     hazfe attribute

dir()       namayeshe name propertis va method haye ghabele dastresi
vars()     moshahede dictionary vizhegi haye object

super()    dastresi be piade sazi class badi dar tartibe ers bari


'''





#--------------------------------------------------
# A - typ, isinstance, issubclass


a = 10
b = "Ali"
c = [1, 2, 3]

print(type(a))   # <class 'int'>
print(type(b))   # <class 'str'>
print(type(c))   # <class 'list'>

#hala khodemon class misazim
class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price


p1 = Product("Laptop", 1000)

print(type(p1))
# <class '__main__.Product'>



#hata mitonim noesho hesab konim
print(type(p1) == Product)  # True





#taveye isinatne

#sakhtar -->isinstance(object, classinfo)

#in tabe barresi mikone objecte morede nazar aya az in class hast ya na
#Khoroji ro true false mide


a = 20

print(isinstance(a, int))    # True
print(isinstance(a, float))  # False
print(isinstance(a, str))    # False

#baraye barreis chan no hamzaman
value = 20.5

print(isinstance(value, (int, float)))
# True





#hamin kar ro mitonim dakhele class hamon estefade konim baraye etebarsanjie vorodi


class Product:

    def __init__(self, name, price):

        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number")

        if isinstance(price, bool):
            raise TypeError("Price cannot be boolean")

        if price < 0:
            raise ValueError("Price cannot be negative")

        self.name = name
        self.price = price


p1 = Product("Laptop", 1000)   # OK

p2 = Product("Phone", "500")   # TypeError

p3 = Product("Mouse", -100)    # ValueError






#hala fek kon ers bari karidm :
class Product:
    pass


class DigitalProduct(Product):
    pass


class PhysicalProduct(Product):
    pass


p1 = DigitalProduct()


print(type(p1) == Product)
# False

print(isinstance(p1, Product))
# True

print(isinstance(p1, DigitalProduct))
# True

print(isinstance(p1, PhysicalProduct))
# False


#age bebini p1 ham product hast ham digitla product
#chon chzii ke ers borde har joftesh hast





#tabeye issubclass mige ke rabete beynesho chie

#fek kon class A darim ba class B 

#ag class A az CLASS B ers bebare tabeye issubclass() true mide

print(issubclass(DigitalProduct, Product))
# True

print(issubclass(PhysicalProduct, Product))
# True

print(issubclass(Product, DigitalProduct))
# False



#hamchnin dar nazar begirid dar tarife issubclass har class, zir classe khdoesh ham hast
print(issubclass(DigitalProduct, Product))
# True

print(issubclass(PhysicalProduct, Product))
# True

print(issubclass(Product, DigitalProduct))
# False







#--------------------------------------------------
# B - ....atr()


#ta emroz baraye gereftane attribtue miomdim mizadim


p1.name
p1.price


#ama gahan ma esm haro nmidonim chie , pas behtre biaym azin esteafde konim

print(getattr(p1, "price"))  # 1000


#joftesh yekie ama maziatesh ine ke , age oon vizhegi vojod nadashte bashe
#bejaye error ma mitonim baiym yek chize pish frz bzarim , masalan
color = getattr(p1, "color", "Unknown")

print(color)  # Unknown


#sakhtar --> getattr(object, attribute_name, default)








#----setattr()

p1 = Product("Laptop", 1000, 10)

setattr(p1, "price", 1500)

print(p1.price)  # 1500



#in hamoon

p1.price = 1500
#hast



#sakhte attribute jadi
#ahata agar brand dakhele init nist ama mitonim besazim
setattr(p1, "brand", "Apple")

print(p1.brand)
# Apple





#----hasattr()

#gahi mikhaym fgt bdonim aya in object in attribtue ro dare ya na


print(hasattr(p1, "name"))   # True

print(hasattr(p1, "color"))  # False




#dakhele if estefade mishe

if hasattr(p1, "brand"):
    print(p1.brand)
else:
    print("Brand not available")




#yek emsale dige
class Product:

    def __init__(self, name):
        self.name = name


p1 = Product("Laptop")

if not hasattr(p1, "stock"):
    setattr(p1, "stock", 0)






#delattr()
#baraye hazfe attribtue

p1 = Product("Laptop", 1000, 10)

print(p1.stock)  # 10

delattr(p1, "stock")


#hala 
#print(hasattr(p1, "stock"))  # False






#------tamrine tarkibi-------
class User:

    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.status = "active"


user1 = User("ali", "ali@gmail.com")



print(getattr(user1, "username"))

setattr(user1, "status", "blocked")

print(hasattr(user1, "email"))

delattr(user1, "email")






#--dir() , vars()

#in do tabe baraye fahmidane sakhtare objecte ha karbod ziadi daran 

#farz konid yek object darim nemdionim ch attribtues ya methods ha dare 




class Product:

    tax = 0.10

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(self.name, self.price)


p1 = Product("Laptop", 1000)



print(dir(p1))

#khoroji ino mide
'''
['__class__', '__dict__', '__dir__', '__doc__',
 ..., 'name', 'price', 'show', 'tax']

'''








#hamchenin in tabe baraye object haei ke az ketabkhone haye dgar migriim besiar mofid ast


import math

print(dir(math))




#----vars()

#in tabe miad attributes haro mesle yek dictionary pas mide
p1 = Product("Laptop", 1000)

print(vars(p1))




'''
khoroji :
{
    "name": "Laptop",
    "price": 1000
}


'''














