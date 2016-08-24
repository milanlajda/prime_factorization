
def prime_factorization(x):
    primefactors=[]
    for i in range (2, x):
        if primenum_check(i) == True and x%i == 0:
            primefactors.append(i)
    print primefactors


def primenum_check(x):
    counter=0
    for i in range (1, x):
        if x%i == 0:
            counter=counter+1
    if counter > 1:
        return False
    else:
        return True

prime_factorization(120)