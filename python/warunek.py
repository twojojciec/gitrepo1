#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  


def main(args):
    a = int(input ('podaj liczbę:'))
    b = int(input ('podaj liczbę:'))
    if a < b:
        print('a < b')
    elif b < a:
        print('b < a')
            
    else:
        print('b nie jest większe od a')
        
    
    
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
