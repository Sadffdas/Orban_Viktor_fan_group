"""
class sajatosztaly:
    def __new__(self, nev,kor):
        self.nev=nev
        self.kor=kor

nev = input("add meg a neved: ")
kor = int(input("add meg a korod: "))

en=sajatosztaly(nev, kor)
print(sajatosztaly.nev)
print(sajatosztaly.kor)
print(type(en))
"""



list=[3,4,5,6,7,8,9,10,123,2131231231,45,23,34,4,4,5,7,9,33,46]
print(list)
print(type(list))
print(sum(list) /len(list))
nagyszam = 1000
print(nagyszam - sum(list)) 
sum=0
for i in list:
    sum+=i
print("lista elemek összege", sum)

#Maximum keresés
print(max(list))
lista = [-1000,400,-200,-100]
max = index=-1000, 0
for i in lista: 
