#program sum three numbers while ignoring duplicate numbers for sum 
s1=s2=0
n1=int(input("ENTER NUMBER 1:"))
n2=int(input("ENTER NUMBER 2:"))
n3=int(input("ENTER NUMBER 3:"))
s1=n1+n2+n3
if n1 !=n2 and n1 !=n3:
    s2+=n1
if n2 !=n1 and n2 !=n3:
    s2+=n2
if n3 !=n1 and n3 !=n2:
        s2+=n3
print("Numbers are",n1,n2,n3)
print("Sum of three given numbers is",s1)        
print("Sum of non-duplicate numbers is",s2)

        
