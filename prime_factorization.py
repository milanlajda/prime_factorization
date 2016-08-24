
def prime_factorization(x):
    primefactors=[]
    for i in range (2, x):
        blabla = x%i
        if primenum_check(i) == True and blabla == 0:
            primefactors.append(i)
    print primefactors


def primenum_check(x):
    counter=0
    for i in range (1, x):
        remainder = x%i
        if remainder == 0:
            counter=counter+1
    if counter > 1:
        return False
    else:
        return True

prime_factorization(100)