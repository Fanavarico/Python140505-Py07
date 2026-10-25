"""
In The Name of GOD

Created on Fri Oct 23 15:07:51 2026

@author: Ali Pilehvar Meibody

L12

"""

'''

1 python built in function 
2 keywords
3 variables


functions
Class --> object oriented programming (OOP)

function ---> ye boxi bod vorodi -->box -> khoroji
class --> object misakhti
product, .... , service bashe

file management --> open() w r .readline()

class --> file managemen tkone --> l11 , l11_advances
filemanager() 



Python ---->


'''


username = 'ali'


#volatile --> Farrar --> RAM


#moshtari haye banke markazi --> 1 milllion ensan -> ram zakhire koni
#servr khamoshshe, etefaghi --> kolesho az beyn miran




#---> Yejaye Non-volatile --> gheyre farrar --> daemi
#agar serveram khamoshshpd bemone

#HARD --> zakhire 



#raveshe 1 ---> dafr yek file zakhire konim -->
#.txt .json .csv ,.....


#moshkele --> structure dasht??? sakhtar dasht

#baraye sade tarin Query ha --> man sad ha khat bauyad benvise


#Query --> Jostojoo va gashto gozar tooye file


'''

ba function, class --> appeto besazi --> amalkardesho (logic)

DATA --> Zakhire , .txt ,... --> unstructured

matne errora --> .txt  log --> print() log.txt


dataye moshtari , dataha--->
chanta pish niaz :
    - daemi bashe --> HARD
    - Viraysh krd taghir dad
    - Query rahat bshe zad -> structure dashte bashe
    
    
-----------------------------------
DATA BASE --> DB 



Service (abzar , toool) --> database management DBM --> 
yek abzare --> ejaze mide --> 

git -->git abzar --> ejaze mdiad folder manage konid
vim -->  baraye skahte yek file

DBM --> Yek abzarie --> ejaze mide shoma toosh user besazid 
har user , password , access 

mitonid DB besazi -> database --> table ha zakhire mishavad

rooye HARD --> Byte() zakhire mikone . 

in karo direct mostaghim mikone. 



excell? --> DBM , -->Hardet
excell -> narm afzaree tejari -> sakhte soton hast 



mysql , sqlite , postgress --> 3 ta abzaran 
ejaze midan shoma table haei besazid

be goonei structure (sakhtar) --> zabani amade
--> SQL (structured query language)

mysql , sqlite, postgress --> SQL code bzni 
user , database, table , --> disk zakhire mishe


abzar --> laptobam, server, harja bekhay --> nasb koni 
abzar --> .db -->kole data -> structured zakhire mishe


efficient -> query 
jadval passsword --> len > 8 --> bia bede
hazf kon ,



------
sql --> yek zaban hast 
DBM --> yek system(abzar) k ejaze mdie man toosh sql bznmi
user , database (table,table,table)

databae --> user access



1----> DBM --> mysql , sqlite , postgress

mysql--> ghadimie, kh khobe
sqlite --> production sangin nemikhore --> kh rahate
postgress --> behtarine , sakht





SQL --> yad begirim 

dbm --> berizam toosh sql benvisam -> mysql ro entekhab mikonm 



sql --> miriz laptob --> sql server -->abzare run 

sql client 

sql server <---> sql client


harchi tooye sql clien t----> sql server ejra mishe.


sql client ( app ha , python)





SQL , DBM , DB , table, row , columnms


SQL --> yek zaban
DBM --> yek abzar k ejaze mide
DB --> yek majmoei ee az table ha
table --> yek structure az soton va radis
row --> radif /satr / record
columns --> sotoon / vizhegi / feature 

'''

#========================================
#========================================
#========================================


'''
Mysql ---> DBM hast ro brizam 

abzar --> sql , mohiti dare k toosh sql code bzni

raveshe Basic --> 
https://blog.faradars.org/install-mysql-windows/






--> mysql installer
https://dev.mysql.com/downloads/windows/installer/5.7.html

mysql installer --> 7 , 8 ta appe

mysql --> mysql workbench , tejari








Raveshe 2 --> GUI ,..... mikhay CLI bash



Macboook --> terminal

brew install mysql@8.4 

[y/n]  --> y enter y enter --> tamom shod

ejrash

service ro start -->
brew service start mysql@8.4

motmaen shi -->
brew service list


vared shi -->
mysql -u root 


user --> root , passwordam nadare 

aghaye mysql baz sho , -u --> useename : root 
mysql>


mysql -u root -p







-----------WINDOWS-----------------
https://dev.mysql.com/downloads/mysql/

download mikoni --> ejrash mikoni -->
configure peykarbandi 

-> Port 3306 TCP/IP va Root ,passsword gozineye apply/execute 


powershell root --->

Get-Service *mysql*

inja ye listi az mysql miare --> esmesho peyd amikoni
mysql8 mysql83 845 /

Start-Service MYSQL84

in service run mishe

##### stoop koni service
Stop-Service MYSQL84

Get-Command mysql --> age javab dad yes 

--> b code zani
mysql -u root 

-->chizi nayovord
$mysqlPath = "C:\Program Files\MySQL\MySQL Server 8.4\bin"

$userPath = [Environment]::GetEnvironmentVariable("Path", "User")

[Environment]::SetEnvironmentVariable(
    "Path",
    "$userPath;$mysqlPath",
    "User"
)




mysql --> mishnase

windows, mac , linux ,......

nasb beshe --> terminal/powershell

ag jaei ravandet --> password --> 

age nazashti

mysql -u root 




mysql -u root -p enter --> password --> mizani 


'''



'''

mysql server (laptabet app)  | terminal / powersheell -_> mysql client


tooye powershell/terminal -> sql code mizni --> mysql server (laptab) -> run mishe




mysql -u root -p


mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

mysql> SELECT CURRENT_USER()
    -> 
    -> 
    -> 
    -> ;
+----------------+
| CURRENT_USER() |
+----------------+
| root@localhost |
+----------------+
1 row in set (0.00 sec)



mysql> CREATE DATABASE shop_db;



mysql> CREATE DATABASE IF NOT EXISTS shop_db;
Query OK, 1 row affected (0.01 sec)




mysql> USE shop_db;
Database changed



#ye useram besazim

mysql> CREATE USER 'shop_user'@'localhost' IDENTIFIED BY '1234';
Query OK, 0 rows affected (0.02 sec)


baraye dafeye bad bznid

mysql -u shop








'''


#====================================
#====================================
#====================================
#====================================


'''
(base) apm@APMs-MacBook-Pro desktop % mysql -u root -p 
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 32
Server version: 8.4.11 Homebrew

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| shop_db            |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

mysql> SELECT CURRENT_USER();
+----------------+
| CURRENT_USER() |
+----------------+
| root@localhost |
+----------------+
1 row in set (0.01 sec)

mysql> USE shop_db ;
Database changed
mysql> -u shop_user -p
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '-u shop_user -p' at line 1
mysql> exit;
Bye
(base) apm@APMs-MacBook-Pro desktop % mysql -u shop_user -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 33
Server version: 8.4.11 Homebrew

Copyright (c) 2000, 2018, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| performance_schema |
+--------------------+
2 rows in set (0.01 sec)

mysql> USE shop_db;
ERROR 1044 (42000): Access denied for user 'shop_user'@'localhost' to database 'shop_db'
mysql> 




be in useram --> access bdm

ROOT --> USER HA



agar user hato khasti bebini
mysql> SELECT user,host FROM mysql.user;
+------------------+-----------+
| user             | host      |
+------------------+-----------+
| mysql.infoschema | localhost |
| mysql.session    | localhost |
| mysql.sys        | localhost |
| root             | localhost |
| shop_user        | localhost |
+------------------+-----------+
5 rows in set (0.00 sec)





mysql> GRANT ALL PRIVILEGES ON shop_db.* TO 'shop_user'@'localhost';
Query OK, 0 rows affected (0.01 sec)




be shop user --> dastresi b db shop_db fght dadam


-->ALL PREVILEGES
SELECT --> Khandadne data
INSERT --> ezafe krdn
UPDATE -> virayeshe dade
DELETE -- Remove radif
CREATE -> sakhte jadval ashya 
ALTER --> taghire sakhtar jadval
DROP --> hazfe jadval ya sayere ashyaye mojaz
INDEX --> ijad ya hazfe index
ALL PREVELEGES



root -->
SHOW GRANTS FOR 'shop_user'@'localhost';

REVOKE DELETE ON shop_db.* FROM 'shop_user'@'localhost';
yani dastresi delete --> shop_db grftim az shop_user









kole kar (standard)
yekbar miri root, database o misazi,
usero misazi, dasdtresie databseo midi b user miay biron

mysql -u root -p
CREATE DATABASE IF NOT EXISTS esme_db ;
CREATE USER 'esme_user'@'localhost' IDENTIFIED BY 'strongppassword' ;
GRANT ALL PREVILEGES esme_db.* TO 'esme_user'@'localhost';
exit;


miri too useri k sakhti
mysql -u esme_user -p
SHOW DATABASES;
USE shop_db;




jadval --> product ---> db (shop_db)

product --> soton haei dare ???
id , name , price , quantity 

type -->
INT  
DECIMAL
TEXT
VARCHAR




CREATE TABLE products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    
  
    
  
    
CREATE TABLE products(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0
);
    




hichi nazari , not mnull, default bezari
    
    
    
class TABLE:
    id: int
    name : str
    price : float
    
    
    
    
    
mysql> SELECT CURRENT_USER();
+---------------------+
| CURRENT_USER()      |
+---------------------+
| shop_user@localhost |
+---------------------+
1 row in set (0.00 sec)

mysql> USE shop_db;
Database changed
mysql> CREATE TABLE products(
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     name VARCHAR(100) NOT NULL,
    ->     price DECIMAL(10,2) NOT NULL,
    ->     stock INT DEFAULT 0
    -> );
Query OK, 0 rows affected (0.04 sec)

mysql> SHOW TABLES;
+-------------------+
| Tables_in_shop_db |
+-------------------+
| products          |
+-------------------+
1 row in set (0.00 sec)

                 shop_db
         ---------
     product
---------------------
id   name price   stock




ezafe krdn --> INSERT
yekj radif (row) mikahhi ezafe koni



dastoor

INSERT INTO products (name,price,stock)
VALUES ('Phone',100,5);





mysql> INSERT INTO products (name,price,stock)
    -> VALUES ('Phone',100,5);
Query OK, 1 row affected (0.01 sec)




sakhte table , 
ezafe krdne record ,
didanesh



mysql> SELECT * FROM products;
+----+-------+--------+-------+
| id | name  | price  | stock |
+----+-------+--------+-------+
|  1 | Phone | 100.00 |     5 |
+----+-------+--------+-------+
1 row in set (0.00 sec)


dar python, yek file
yek tabel bename --> products
id , name, code , price, quantity , type 
yek ketab varedesh konid
selectesh konid



mysql> CREATE TABLE products(
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     name VARCHAR(100) NOT NULL,
    ->     price DECIMAL(10,2) NOT NULL,
    ->     stock INT DEFAULT 0
    -> );

mysql> INSERT INTO products (name,price,stock)
    -> VALUES ('Phone',100,5);
    
mysql> SELECT * FROM products;






CREATE TABLE product2(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    code VARCHAR(5) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    quantity INT DEFAULT 0,
    type VARCHAR(10) DEFAULT 'Physic'
);


INSERT INTO product2 (name,code,price,quantity,type)
VALUES ('Book1','b12',10.20 , 2 , 'Physic');



select * from product2


harchi hasto bede az product2 




-------------------------------------
L12_ADVANCED_DB_Query.py



DELETE FROM product2 WHERE id = 1



SELECT * from product2 WHERE id=1




in sert multiuple bvalues -->


INSERT INTO product2 (name,code,price,quantity,type)
VALUES ('Book1','b12',10.20 , 2 , 'Physic'),
        ('BOOK2','B13',10.2323,4,'PHYSICS');


SELECT * FROM product2;   #---> HAMARO


SELECT * FROM product2 WHERE ...;

SELECT * FROM product2 WHERE id=1;

#shart

SELECT * FROM product2 WHERE price >100;


SELECT * FROM product2 WHERE price>100 AND quantity>0;

SELECT * FROM product2 WHERE price>100 OR quantity>0;




SELECT * FROM product2;  --> binazm

orderesh koni

SELECT * FROM produc



INSERT INTO product2 (name,code,price,quantity,type)
    VALUES ('Book3' , 'b15' , 20.65 , 6 , 'online'),
          ('Book4' , 'B19' , 80 , 2 , 'online'),
         ('Book5' ,'b10' , 5 , 50 , 'Physic');
         
         
         
         


#------yek example-----
mysql> SELECT CURRENT_USER()
    -> ;
+---------------------+
| CURRENT_USER()      |
+---------------------+
| shop_user@localhost |
+---------------------+
1 row in set (0.00 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| performance_schema |
| shop_db            |
+--------------------+
3 rows in set (0.00 sec)

mysql> USE shop_db;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> SHOW TABLES;
+-------------------+
| Tables_in_shop_db |
+-------------------+
| product2          |
| products          |
+-------------------+
2 rows in set (0.01 sec)

mysql> SELECT * FROM product2;
+----+-------+------+-------+----------+--------+
| id | name  | code | price | quantity | type   |
+----+-------+------+-------+----------+--------+
|  2 | Book1 | b12  | 10.20 |        2 | Physic |
+----+-------+------+-------+----------+--------+
1 row in set (0.00 sec)

mysql> INSERT INTO product2 (name,code,price,quantity,type)
    -> VALUES ('Book3' , 'b15' , 20.65 , 6 , 'online'),
    ->        ('Book4' , 'B19' , 80 , 2 , 'online'),
    ->        ('Book5) ,'b10' , 5 , 50 , 'Physic');
    '> ;
    '> VALUES ('Book3' , 'b15' , 20.65 , 6 , 'online'),^C
mysql> ^C
mysql> INSERT INTO product2 (name,code,price,quantity,type)
    ->     VALUES ('Book3' , 'b15' , 20.65 , 6 , 'online'),
    ->           ('Book4' , 'B19' , 80 , 2 , 'online'),
    ->          ('Book5' ,'b10' , 5 , 50 , 'Physic');
Query OK, 3 rows affected (0.01 sec)
Records: 3  Duplicates: 0  Warnings: 0

mysql> select * from product2;
+----+-------+------+-------+----------+--------+
| id | name  | code | price | quantity | type   |
+----+-------+------+-------+----------+--------+
|  2 | Book1 | b12  | 10.20 |        2 | Physic |
|  3 | Book3 | b15  | 20.65 |        6 | online |
|  4 | Book4 | B19  | 80.00 |        2 | online |
|  5 | Book5 | b10  |  5.00 |       50 | Physic |
+----+-------+------+-------+----------+--------+
4 rows in set (0.00 sec)

mysql> SELECT * FROM product2 WHERE id=4;
+----+-------+------+-------+----------+--------+
| id | name  | code | price | quantity | type   |
+----+-------+------+-------+----------+--------+
|  4 | Book4 | B19  | 80.00 |        2 | online |
+----+-------+------+-------+----------+--------+
1 row in set (0.00 sec)

mysql> SELECT * FROM product2 WHERE type='online';
+----+-------+------+-------+----------+--------+
| id | name  | code | price | quantity | type   |
+----+-------+------+-------+----------+--------+
|  3 | Book3 | b15  | 20.65 |        6 | online |
|  4 | Book4 | B19  | 80.00 |        2 | online |
+----+-------+------+-------+----------+--------+
2 rows in set (0.00 sec)

mysql> SELECT * FROM product2 WHERE price >20;
+----+-------+------+-------+----------+--------+
| id | name  | code | price | quantity | type   |
+----+-------+------+-------+----------+--------+
|  3 | Book3 | b15  | 20.65 |        6 | online |
|  4 | Book4 | B19  | 80.00 |        2 | online |
+----+-------+------+-------+----------+--------+
2 rows in set (0.00 sec)

mysql> SELECT * FROM product2 WHERE price<50 AND quantity>20;
+----+-------+------+-------+----------+--------+
| id | name  | code | price | quantity | type   |
+----+-------+------+-------+----------+--------+
|  5 | Book5 | b10  |  5.00 |       50 | Physic |
+----+-------+------+-------+----------+--------+
1 row in set (0.00 sec)

mysql> SELECT * FROM product2
    -> ORDER BY price DESC 
    -> LIMIT 3;
+----+-------+------+-------+----------+--------+
| id | name  | code | price | quantity | type   |
+----+-------+------+-------+----------+--------+
|  4 | Book4 | B19  | 80.00 |        2 | online |
|  3 | Book3 | b15  | 20.65 |        6 | online |
|  2 | Book1 | b12  | 10.20 |        2 | Physic |
+----+-------+------+-------+----------+--------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM product2 WHERE name LIKE 'B%';
+----+-------+------+-------+----------+--------+
| id | name  | code | price | quantity | type   |
+----+-------+------+-------+----------+--------+
|  2 | Book1 | b12  | 10.20 |        2 | Physic |
|  3 | Book3 | b15  | 20.65 |        6 | online |
|  4 | Book4 | B19  | 80.00 |        2 | online |
|  5 | Book5 | b10  |  5.00 |       50 | Physic |
+----+-------+------+-------+----------+--------+
4 rows in set (0.01 sec)

mysql> select * from product2;
+----+-------+------+-------+----------+--------+
| id | name  | code | price | quantity | type   |
+----+-------+------+-------+----------+--------+
|  2 | Book1 | b12  | 10.20 |        2 | Physic |
|  3 | Book3 | b15  | 20.65 |        6 | online |
|  4 | Book4 | B19  | 80.00 |        2 | online |
|  5 | Book5 | b10  |  5.00 |       50 | Physic |
+----+-------+------+-------+----------+--------+
4 rows in set (0.00 sec)

mysql> UPDATE product2 
    -> SET quantity = 1 , price =60.00
    -> WHERE id=4;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from product2;
+----+-------+------+-------+----------+--------+
| id | name  | code | price | quantity | type   |
+----+-------+------+-------+----------+--------+
|  2 | Book1 | b12  | 10.20 |        2 | Physic |
|  3 | Book3 | b15  | 20.65 |        6 | online |
|  4 | Book4 | B19  | 60.00 |        1 | online |
|  5 | Book5 | b10  |  5.00 |       50 | Physic |
+----+-------+------+-------+----------+--------+
4 rows in set (0.00 sec)








mysql> DELETE FROM product2 WHERE id=3;
Query OK, 1 row affected (0.00 sec)

mysql> select * from product2;
+----+-------+------+-------+----------+--------+
| id | name  | code | price | quantity | type   |
+----+-------+------+-------+----------+--------+
|  2 | Book1 | b12  | 10.20 |        2 | Physic |
|  4 | Book4 | B19  | 60.00 |        1 | online |
|  5 | Book5 | b10  |  5.00 |       50 | Physic |
+----+-------+------+-------+----------+--------+
3 rows in set (0.00 sec)

mysql> DELETE FROM product2 WHERE code='b10';
Query OK, 1 row affected (0.00 sec)

mysql> select * from product2;
+----+-------+------+-------+----------+--------+
| id | name  | code | price | quantity | type   |
+----+-------+------+-------+----------+--------+
|  2 | Book1 | b12  | 10.20 |        2 | Physic |
|  4 | Book4 | B19  | 60.00 |        1 | online |
+----+-------+------+-------+----------+--------+
2 rows in set (0.00 sec)

mysql> DROP TABLE product2;
Query OK, 0 rows affected (0.01 sec)

mysql> SHOW TABLES;
+-------------------+
| Tables_in_shop_db |
+-------------------+
| products          |
+-------------------+
1 row in set (0.01 sec)






-->advance

tavabe amri --> count, average, bishtarin kamtarin

taghire sakhtar jadval ,......









SQL 


sql client (terminal,powershell) ------(sql)-----> sql server(srvice aslimon)

select * from product2; --> terminal  | python bznm 


python --> sql client





MYSQL ---> berizi hatman 
root user besazid -->
mysql -u root -p


klefayat mikone --> python beshid

bejaye terminal/powershell --> python inkaro bokonid



pip install mysql-connector-python




(base) apm@APMs-MacBook-Pro desktop % pip install mysql-connector-python
Collecting mysql-connector-python
  Downloading mysql_connector_python-26.10.0-cp312-cp312-macosx_14_0_arm64.whl.metadata (11 kB)
Downloading mysql_connector_python-26.10.0-cp312-cp312-macosx_14_0_arm64.whl (20.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 20.0/20.0 MB 4.3 MB/s eta 0:00:00
Installing collected packages: mysql-connector-python
Successfully installed mysql-connector-python-26.10.0





'''

import mysql.connector




#mysql esme package
#connector --> .py esh
#connect -->Class




connection = mysql.connector.connect(host = '127.0.0.1',
                        port =3306,
                        user='shop_user',
                        password ='1234',
                        database='shop_db')

#mysql -u shop_user -p 1234
#USE shop_db

#bejaye inke az terminal koni , az python mikoni

#client ---(sql)--->server (localhost)


#supabase --> dipa 


print(type(connection))
#<class 'mysql.connector.connection_cext.CMySQLConnection'>

connection.close()


#baraye har kar roshan kon close --> tabe konish ->
#connect_db()



#--------------
import mysql.connector

connection = mysql.connector.connect(host = '127.0.0.1',
                        port =3306,
                        user='shop_user',
                        password ='1234',
                        database='shop_db')



cursor = connection.cursor()

#sakhte user --> age ba rooot bashi 
#sakhte table , hazfe tabel va va va ....

cursor.execute('SELECT * FROM products;')

results = cursor.fetchall()

print(results)
#[(1, 'Phone', Decimal('100.00'), 5)]

print(type(results)) #<class 'list'>
results[0] #Out[173]: (1, 'Phone', Decimal('100.00'), 5)

print(type(results[0])) #<class 'tuple'>


'''
[ ()  , ()  ,()  ]

'''
connection.close()









import mysql.connector
connection = mysql.connector.connect(host = '127.0.0.1',
                        port =3306,
                        user='shop_user',
                        password ='1234',
                        database='shop_db')

cursor = connection.cursor(dictionary=True)

#etelaat begiri --> cursor.execute().   cursore.fetchall()
cursor.execute('SELECT * FROM products;')

results = cursor.fetchall()

print(results)

#[{'id': 1, 'name': 'Phone', 'price': Decimal('100.00'), 'stock': 5}]


#in karie k mikhahi anjam bedi
#cursor.execute() --> connection.commit()

cursor.execute("""INSERT INTO products (name,price,stock)
                   VALUES ('iphone',1200 ,12);
               """)


connection.commit()





cursor.execute('SELECT * from products;')
results = cursor.fetchall()

print(results)
'''
[{'id': 1, 'name': 'Phone', 'price': Decimal('100.00'), 'stock': 5}, 
 {'id': 2, 'name': 'iphone', 'price': Decimal('1200.00'), 'stock': 12}]
'''



cursor.execute("""INSERT INTO products (name,price,stock)
                   VALUES (%s , %s , %s);
               """   , ('iphone 18' ,1400 , 30))


connection.commit()





cursor.execute('SELECT * from products;')
results = cursor.fetchall()

print(results)

'''
[{'id': 1, 'name': 'Phone', 'price': Decimal('100.00'), 'stock': 5},
 {'id': 2, 'name': 'iphone', 'price': Decimal('1200.00'), 'stock': 12},
 {'id': 3, 'name': 'iphone 18', 'price': Decimal('1400.00'), 'stock': 30}]
'''







'''
Mysql --> abzar TOOL 

mysql server <----> mysql client 





taklif -->


users --> db users besazid


uswr baraye


user_manager --> useram




terminal / poweshell

mysql -u root -p
CREATE USER 'user_manager'@'localhost' IDENTIFIEND BY 'stongpassword' ;
CREATE DATABASE IF NOT EXISTS users;
GRANT ALL PREVILEGES  users.* TO 'user_manager'@'localhost';





tooye python --> table ro besaz --> id,username,password,status
esme table --> user_information
in ro too python besaz  (powershell)





models --> table haye database e


USERS ---> table users --> username, password, email 
userprofile --> username, fullname,..........
shops --> shop_name , shop_photo ,shop_address ,...
FORM --> form_name, form_id, created_date , ......




table ha mitonan beham vasl beshan


form --> element


table --> forms  -_>form1 (element a , b)  , form2  (element c)
table --> elements  -->  element a , element b , element c 

jalsate ayande yad migirim 

'''
import os
import mysql.connector 


#def connect_db():
    #connection = mysql.connector.connect(host = '127.0.0.1',
                        #    port =3306,
                         #   user='shop_user',
                          #  password ='1234',
                          #  database='shop_db')
    #return connection


#def add_user(username,password,status):
    #connection = connect_db()
    #insert ....
    
#def read_users():
    #connection = connect_db()
    #connect.cursor()
    #.exceute ('select * from user_information)
    
    
#def delete_user()


#def user_is_available():
    

    


# O R M

#products = (.....)
#products.prices
#class object --> pythonic 


'''
IN taklif hal mikonim


python sql --> python ORM 


models / crud (repository) / service / endpoint 


endpoint --> flask


'''




