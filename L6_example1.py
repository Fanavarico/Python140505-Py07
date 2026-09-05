
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
