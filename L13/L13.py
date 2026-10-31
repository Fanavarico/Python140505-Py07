
"""
In The Name of GOD
Created on Fri Oct 30 15:05:32 2026

@author: Ali Pilehvar Meibody


L13 - Akhar




"""



'''

Human (english) <-----python----> Machine (0,1binary)


Ipython kernel --> Python
IDE/EDITOR --> Spyder , VS code (anaconda) , cursor
Trae.ai  , Z.ai  , 



1- Python built in functions
print() input() len() type() 

https://docs.python.org/3/builtins/functions.html


2- Keywords --> logice barnamaro avaz mikrdim

    2.1. Conditional statement
        2.1.1 Just if --> rahzan, catchign the error
        2.1.2. IF esle --> dorahi 
        2.1.3. Elif --> multiple selection, range
    
    2.2. Loops
        2.2.1. For --> for shoamrande in iterable : dastoor , range()....
                    static repeat, dynamic repeat() 
                    iteration(())
                    
                    for ...:
                        if
                        print) , count , append
    
        2.2.2. While --> ta zamani ke --> sharte payan mikhahim bezarim
        
        
    2.3. Def --> functions -->
    Vorodi --> BOX ---> khoroji
        def name(v1:type_hind,*,/,v2,v3=default):
            docstrin
            .....
            raise 
            return o
            return o1,o2 --->(tuple)
        
        
    2.4. Class --> object Oriented programming (OOP)
    
        gahan shoma chand chize msohtarak darid --> class
        
        harchizi az donayye birone python --> class 
        layer haye -> file manager, writer --> class
        
        class name:
            def __init__(self,.....):
                self. zakhire
                
                
            def method1(self,....):
                
                
                
            def method2(self,....)
            
            
        obj1 = name(.....)
        
    2.5. Error Handling -->
    aksaran too tavabe , raise error bzar
    too file main.py ya oni k roo rune --> 
    try except --> handle koni error
    
    na bayad codet errro bde
    
    
    2.6. File managing--> RAM tamame variable ha
    pas zakhire nemishdo
    
    
    file --> open(,'w')   open(,'r')
    
    
    2.7. Packages 
    
    import kardano yad ddim , fodler chandin .py import konim
    
    ma paxckage haei darim k azona estefade mikonim 
    
    standard library --> math, random, datetime, os , pathlib , json , csv ,....
    
    
    external libraries --> numpy ,... , mysql-python-connector
    
    
    
    
    


3- Variablees --> value in zarf (variable)

    3.1. Numebrs --> int,float,complex
                    ** , * , / , + , -
                    == , != , > , < ,
    3.2. Boolean --> True, False
    
    3.3.  Strings --> reshte haei az character ha
        [index]  0 
        [start:end]
        str.fucntions()
        
        .lower() .upper() ,.....
        khoroji midad emal nemishod
        new_zarf = zarf.function()
        
        
    3.4. Iterables -> mutliple valeus inside one variabel
    
        3.4.1. List --> order(index), changable, allow duploicated
            [a1,a2,a3,]
            a[index]
            a[index]=new_value
            
            a.append()
            a.extend()
            a.clear()
            
            az list --> iteration , elemnti joda koni
            
            list --> bar paye python neevshte shdoe --> konde kheyli jaha
            
            Numpy array --> C++ --> pip install numpy 
            
            
            
            
        3.4.2. Tuple --> order (index) ,. unchangabel, allow duplciated
        
            sql barmigrdond --> tuple brmigrdon 
            dictionary
            
            
        3.4.3. Set --> no order , unchangable, no duplicated
            majmoe haye riazi
            
        3.4.4. Dictionary --> Information
        index value --> key value
        
        a= {'key1':'value1' ,'key2':'value2'}
        a['key1'] #error
        
        a.get('key1') #None
        a.get('key1','default')
        zarf = a.get('phone','0919....')
        
        
        a['key1'] = new_value
        a['new_key'] = new_value
        
        a.update({'key1':new_value})
        
        
        
        





SQL ---> structured query language --> 

mysql , --> server <---> mysql client


client --> bsh (terminal , powershell) 


ROOT 

mysql -u root -p ...








ta alan --> fudnementale python ro baladid -->

edameye masir koja mishe???



fundementale python ro baladim --> ama aya mitonim hamin alan
kari bahash anjam bdim ?


English --> 

---> Backend, website , .. --->[database, ORM] Django 
---> Data analysis and data science --> [Database,orm] Pandas , matplotlib
----> ML , Dl (deeep learning) --> pandas,matplotin, algorithm , RNN , ANN --> sklearn,tensorflow, pytorch --> mahsoelt amade shod 
                                    ---> database, orm , django /fastapi
 
                                    
kolan niaze -> 
Git  --> porozhe --> 
linux --> server kar koni
Docker --> ...

      

                           
1--->  SQL --> zaban

DBM -> database manager --> mysql, sqlite , postgresss

Mysql ---> configure -->

mysql server <----> mysql client



mysql -u root -p    --->
mysql>

SELECT CURRENT_USER(); --> root

user --> 
CREATE DATABASE shop_db;

CREATE USER 'shop_user'@'localhost' IDENTIFIED BY 'strongpassword';

GRANT ALL PREVELEGES  'shop_db.*' to 'shop_user'@'localhost'

exit;


mysql -u shop_user -p 1234

SELECT  


mysql> SELECT CURRENT_USER()
    -> ;
+---------------------+
| CURRENT_USER()      |
+---------------------+
| shop_user@localhost |
+---------------------+
1 row in set (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| performance_schema |
| shop_db            |
+--------------------+
3 rows in set (0.04 sec)

mysql> USE shop_db;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed


mysql> SHOW TABLES;
+-------------------+
| Tables_in_shop_db |
+-------------------+
| products          |
+-------------------+
1 row in set (0.00 sec)



mysql> SELECT * from products;
+----+-----------+---------+-------+
| id | name      | price   | stock |
+----+-----------+---------+-------+
|  1 | Phone     |  100.00 |     5 |
|  2 | iphone    | 1200.00 |    12 |
|  3 | iphone 18 | 1400.00 |    30 |
+----+-----------+---------+-------+
3 rows in set (0.00 sec)




ba root --> User misazi
ye database misazi
b user dastresi hamechizo b database midi

Use database (miri toosh) --> create table (yek jadval)

select * from jadval
insert ........




Create TABLE users (
    column_name column_type constraints ,
    column_name column_type constraints ,
    column_name column_type constraints ,
    column_name column_type constraints )



column_name -> harchizi mitoni --> esme soton 


column_type--->
INT 
BIGINT -> chandsal milyardi

Create TABLE users (
    page INT constraints ,
    column_name column_type constraints ,
    column_name column_type constraints ,
    column_name column_type constraints ,
    DESCRIPTION  TEXT)


VARCHAR(100)

TEXT

DECIMAL(10,2)
2 ragham ashar 
12345678.12


BOOLEAN --> true , false

DATE --> 2026-10-5
TIME  --> 10:23:23

JSONB --> { } --> extra 


Create TABLE users (
    page INT constraints ,
    column_name column_type constraints ,
    column_name column_type constraints ,
    price DECIMAL(10,2) constraints ,
    DESCRIPTION  TEXT,
    meta_data JSONB)



constraints --> mahdoodiat mizarim

NOT NULL 

insert konan --> 


UNIQUE --> ejaxz enadare in soton too kole jadval tekrari bashe

PRIMARY KEY --> kilide avalie --> inde

DEFAULT


id INT PRIMARY KEY AUTO_INCREMENET,




Create TABLE workflow (
    id INT PRIMARY KEY AUTO_INCREMENT,
    workflow_name VARCHAR(20) NOT NULL ,
    .......
    )
    
    
    
    
    
    
    
    page INT constraints ,








type --> haro yad grftm
Constraints --> 

Price DECIMAL(10,2) DEFAULT 0,
price DECIMAL(10,2) CHECK (price>0),



FOREIGN KEY

UNIQUE NOT NULL --> PRIMARY KEY

column_name columnt_type constraintss,





MODEL LAYER
#-----------------
CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100)  UNIQUE,
    phone VARCHAR(100) 
    )


CREATE TABLE orders(
    id INT PRIMARY KEY AUTO_INCREMENT,
    order_name VARCHAR(100) NOT NULL,
    order_tracking_id INT NOT NULL UNIQUE,
    total_price DECIMAL(10,2) ,
    #owner_id INT NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES users(id) ON ..

    )



ON DELETE RESTRICT --> ta vaghty order hast ,ejaze hazfe user nemide

ON DELETE CASCADE --> age user dleete shod -> orderash baahsh hazf mishe

ON DELETE SET NULL --> age usser hazf beshe 




#------mysql in details-------------------

models ----------




mysql server <------> Mysql client(terminal,powweershell)

mysql server <------> python 


pip install mysql-python-connector

import mysql

mysql.conenction(())

cursor.

cursor.execute('dastore sql midadi')




In ravesh yekam sakhte baraye ma k python baladim -->


ORM --> object relational mappers



CREATE TABLE users(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    email VARCHAR(100)  UNIQUE,
    phone VARCHAR(100) 
    )




class User:
    __tablename__ = 'users'
    id : Int
    username : Str
    password : Str
    email : Str
    phone : str
    


1---> sakhjte table
2-->User.id  User.email

select * from users where id ==1


ORM --> SQLalchemy 

L11 , L12 ---> moghadamei -->



mysql --> root

mysql -u root -p

database, user 

CREATE DATABASE FORM_STARTUP;

CREATE USER 'form_user'@'localhost' IDENTIFIED BY 'ddssd';

GRANT ALL PREVELEGES on 'FORM_STARTUP.*' to 'form_user'@'localhost';



yek database , yek user, behesham access dadi

kole app --> Model layer --> 




Frontend 
ENDPOINT LAYER
SERVICE LAYER
REPOSITORY LAYER
MODEL LAYER ----> laye rhastim


model layer --> mysql table besazi , python

models/  users.py  shops.py company.py workflows.py 





ketabkhane ha --> pip

SQLAlchemy
PyMySQL
python-dotenv



aval yek user va database besazim

mysql> CREATE DATABASE FAN_DB;
Query OK, 1 row affected (0.04 sec)

mysql> CREATE USER 'fan_user'@'localhost' IDENTIFIED BY '1234';
Query OK, 0 rows affected (0.03 sec)

mysql> GRANT ALL PRIVILEGES ON FAN_DB.* TO 'fan_user'@'localhost';
Query OK, 0 rows affected (0.00 sec)

mysql> exit;
Bye



mysql -u fan_user -p 1234
mysql> SELECT CURRENT_USER();
+--------------------+
| CURRENT_USER()     |
+--------------------+
| fan_user@localhost |
+--------------------+
1 row in set (0.01 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| FAN_DB             |
| information_schema |
| performance_schema |
+--------------------+
3 rows in set (0.02 sec)

mysql> USE FAN_DB;
Database changed














requirements.txt

SQLAlchemy>=2.0,<3.0
PyMySQL
python-dotenv


pip install  -r requirements.txt



(base) apm@APMs-MacBook-Pro desktop % pwd
/Users/apm/desktop
(base) apm@APMs-MacBook-Pro desktop % mkdir final_project
(base) apm@APMs-MacBook-Pro desktop % cd final_project
(base) apm@APMs-MacBook-Pro final_project % touch requirements.txt
(base) apm@APMs-MacBook-Pro final_project % vim requirements.txt 
(base) apm@APMs-MacBook-Pro final_project % ls
requirements.txt



.env ---> passsword,token
configuration database


(base) apm@APMs-MacBook-Pro final_project % vim .env
(base) apm@APMs-MacBook-Pro final_project % cat .env
DB_HOST=localhost
DB_PORT= 3306
DB_NAME=fan_db
DB_USER=fan_user
DB_PASSWORD=1234


***advance

.gitignore  --> *.env  .env





-->database.py 


(base) apm@APMs-MacBook-Pro final_project % touch database.py
(base) apm@APMs-MacBook-Pro final_project % ls
database.py		requirements.txt



dakheeld atabase.py ro bebinid

omadim dotenv ovordim
ba sqalchemy --. URL --> configurationo gzoashtim tosh (az .env)

create_engine() --> engine() 

class decreatiev =-. Base ers bord



database.py --> engine, Base


models--->table haro misazid

(base) apm@APMs-MacBook-Pro final_project % mkdir models
(base) apm@APMs-MacBook-Pro final_project % ls
database.py		requirements.txt
models



(base) apm@APMs-MacBook-Pro models % touch user.py
(base) apm@APMs-MacBook-Pro models % ls
user.py



mysql       sqlalchemy
INT           Integer
VARCHAR(100)  String(100)
TEXT          Text
DECIMAL      Numeric
nOT NULL   nullabel =
UNIQUE    unique=True
PRIMARY KEY    primary_key =true
AUTO_INCREMENET  autoincrement =true
FOREIGNKEY     Foreignkey



raftim file e users -->

from database import Base

User(Base) --> jadval

users.py --:> yek fiel e structure database e
jadval nemisaze


raftam too models --> __init___ esm yabi rahat 


too main.py --> Base.metadaa.create_all(bind=engine)

misaze



(base) apm@APMs-MacBook-Pro final_project % python main.py




mysql> USE fan_db;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SHOW TABLES;
+------------------+
| Tables_in_fan_db |
+------------------+
| user_profiles    |
| users            |
+------------------+
2 rows in set (0.01 sec)





repository --> mostaghim rooye databsse model taghir bdid


function --> 


add_user(username,password,email)


delete_user(username)


'''












