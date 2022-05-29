x=-1
s=1
while(x<0):
   x=int(input("Input a number : "))
print("Factorial(",x,")=")
while(x>=0):
    if (x==0):
        s=s*1
    else:
        s=s*x
    x=x-1
print(s)


