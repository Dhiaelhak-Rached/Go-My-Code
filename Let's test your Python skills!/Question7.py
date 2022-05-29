import math as math
c=50
h=30
ch=""
while(not(ch)):
   ch=input("Input D (seperated by ,) : ")
while (ch.find(",")>=0):
   d=int(ch[0:ch.find(",")])
   q=round(math.sqrt((2*c*d)/h))
   print(q)
   ch=ch[ch.find(",")+1:]
d=int(ch[:])
q=round(math.sqrt((2*c*d)/h))
print(q)