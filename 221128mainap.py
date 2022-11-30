
def sorozatszamitas(x, func, s=0):
    s=0
    for i in range(len(x)):
        s=func(s, x[i])
    return s
def szorzas(a,b):
    return a*b
x=[1,2,3,4,5,]
print(sorozatszamitas(x, szorzas, 1))

def osszead(a,b):
    return a+b
print(sorozatszamitas(x, osszead))
def megszamlalas(x, func):
    c=0
    for i in range(len(x)):
        c+=1
    return c
def paros_e(a):
    return a%2==0
print(megszamlalas(x, paros_e))

def ptlan_e(a):
    return a%2==1
print(megszamlalas(x, ptlan_e))

def maxkivalasztas(x):
    maxIndex=0
    maxErtek=x[0]
    for i in range(1, len(x)):
        if (x[i]>maxErtek):
            maxErtek=x[i]
            maxIndex=i
    return (maxIndex,maxErtek)
print()
def Szelsoertekkivalasztas(x):
    Index=0
    Ertek=x[0]
    for i in range(1, len(x)):
        if (x[i]<Ertek):
            Ertek=x[i]
            Index=i
    return (Index,Ertek)
print()
def maximum(a,b):
    return a>b 
def minimum(a,b):
    return a<b
print(Szelsoertekkivalasztas([4,3,5,2,6,1],minimum))
print(Szelsoertekkivalasztas([4,3,5,2,6,1],maximum)) 