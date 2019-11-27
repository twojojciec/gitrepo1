#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# zadanie2py
#
#Zsumuj liczby naturalne w przedziale podanym przez użytkownika



def main(args):
    
    a = b = -1
    while a < 0:
        a = int(input('Podaj pierwszą liczbę:'))
     
    while b <= 0: 
        b = int(input('Podaj drugą liczbę:'))
    
    if a < 0 or b < a : 
        print('błędne dane')
        return
    if a <= b : 
        print('błędne dane')
        return
def sumuj_parzyste(a,b):        
    suma = 0
    for liczba in range(a, b +1):[2,4,6,8,12 , ...]
        if liczba % 2 == 0:
            suma = suma + liczba
    print(suma)
            
def main(args):
    a = b = -1        
    while a < 0:
        a = int(input('podaj 1 liczbe:'))
    while b <= a :
        b = int(input('podaj 2 liczbe:'))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    
    
    
