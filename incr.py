l=eval(input("enter a list"))
le=len(l)
a=int(input("enter no. to be added"))
for i in range(0,le):
    l[i]+=a
print(l)
