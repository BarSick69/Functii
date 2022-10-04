import random
from re import M


def is_correct(number,base):
    greatest_cif=0
    while number!=0:
        cifra=number%10
        number//=10
        if cifra>greatest_cif:
            greatest_cif=cifra
    if greatest_cif>=base:
        print(greatest_cif)
        return False
    return True

def make_decimal(number,base):
    num_in_10=0
    i=0
    while number!=0:
        cifra=number%10
        number//=10
        num_in_10+=cifra*(base**i)
        i+=1
    return num_in_10

def adunarea(n,m,b):
    n=make_decimal(n,b)
    m=make_decimal(m,b)
    suma = n+m
    return from_decimal_to_base(suma,b)
def scaderea(n,m,b):
    n=make_decimal(n,b)
    m=make_decimal(m,b)
    if(n>m):
        diff=n-m 
        return from_decimal_to_base(diff,b)
    diff=m-n 
    return from_decimal_to_base(diff,b)
def from_decimal_to_base(number,b):
    numarul_final=""
    while number!=0:
        cifra=number%b
        number//=b
        numarul_final+=str(cifra)
    numarul_final=numarul_final[::-1]
    return(int(numarul_final))

def inmultire(n,m,b):
    n=make_decimal(n,b)
    m=make_decimal(m,b)
    prod=n*m
    return from_decimal_to_base(prod,b)

n = random.randint(0,999)
b = random.randint(2,9)
m = random.randint(0,999)
print("Baza:",b)
print("Numarul_1: ",n)
print("Numarul_2: ",m)

este_corect_n=is_correct(n,b)
este_corect_m=is_correct(m,b)

if(este_corect_n and este_corect_m):
    print("Aceste numere sunt scrise corect")
    print("Numarul",n,"in zecimal:",make_decimal(n,b))
    print("Numarul",m,"in zecimal:",make_decimal(m,b))
    print("Suma:",adunarea(n,m,b))
    print("Diferenta:",scaderea(n,m,b))
    print("Produsul:",inmultire(n,m,b))
else:
    print("Numarul nu este scris corect")



    


