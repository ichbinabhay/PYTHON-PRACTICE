a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
if (a>b) and (a>c):
    largest=a
if (b>a) and (b>c):
    largest=b
if (c>a) and (c>b):
    largest=c        
print("largest number is",largest)