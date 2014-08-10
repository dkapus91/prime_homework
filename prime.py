'''
Created on 2014.08.10.

@author: David
'''

import sys

#eldonti, hogy egy szam prim-e    
def is_prime(input):
    value = True
    
    if input < 2:
        value = False
    else:
        for i in range(2,input):
            if input % i == 0:
                    value = False
        return value

# az adott szamtol kisebb primszamokat adja vissza (mivel osztokat keresunk, eleg volt a szam feleig vizsgalni) 
def prime_numbers(input):
    prime_list = []
    
    #ha a megadott szam prim, nem kell a tole kisebb szamokat, osztokat vizsgalni, hiszen csak 1-gyel es magaval lehet osztani
    if is_prime(input) == True:
        prime_list.append(input)
    else:
        for n in range(1,(input/2)+1):
            if (is_prime(n)== True):
                prime_list.append(n)
    #egy tuple-ben adom at            
    return prime_list

#a prime_numbers() altal atadott prim szamokat levizsgalja, hogy osztoi-e az input-nak, es az osztokat return-oli
def is_prime_divider(input):
    dividers = []
    
    numbers = prime_numbers(input)
    for n in numbers:
       
        if input % n == 0:
            dividers.append(n)
    #az osztokat tuple-ben adom at
    return dividers

#miutan az is_prime_divider()-bol tudjuk a prim osztokat, ez a fuggveny vegzi el a primtenyezos egyutthatokra valo felbontast 
def prime_factory(input):
    prime_factor_divs = [] 
    
    divs = is_prime_divider(input)
    for number in divs:
        while((input % number) == 0):
                      
            prime_factor_divs.append(number)
            input = input/number#a ciklus vegen be kell allitani az aktualis hanyados erteket
                
    return prime_factor_divs

def main(argv):
    
    x = input("Enter a number: ")
      
    print str(x) + ' -> ' + str(prime_factory(x))
     
if __name__ == "__main__":
        main(sys.argv[1:])