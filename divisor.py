#program to find multiples of a number
print("Enter five number below")
num1=float(input("Enter Number 1:"))
num2=float(input("Enter Number 2:"))
num3=float(input("Enter Number 3:"))
num4=float(input("Enter Number 4:"))
num5=float(input("Enter Number 5:"))
divisor=float(input("Enter Divisor Number:"))
count=0
print("Multiples of",divisor,"are")
remainder= num1%divisor
if remainder==0:
    print(num1)
    count+=1
remainder=num2%divisor    
if remainder==0:
    print(num2)
    count+=1
remainder=num3%divisor    
if remainder==0:
    print(num3)
    count+=1 
remainder=num4%divisor    
if remainder==0:
    print(num4)
    count+=1     
remainder=num5%divisor    
if remainder==0:
    print(num5)
    count+=1    
print()
print(count, "multiples of", divisor, "found ")    
      
    
    

    
