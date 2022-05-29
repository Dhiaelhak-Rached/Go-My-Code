ch=""
x=-1
while(not(ch)):
   ch=input("Input a non-empty String : ")
while(x<0 or x>len(ch)-1):
   x=int(input("Input a number : "))
ch=ch[0:x]+ch[x+1:]
print(ch)