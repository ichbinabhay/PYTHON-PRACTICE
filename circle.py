#program to print area or perimeter of circle
radius= float(input("Enter radius of circle:"))
print("1.Calculate Area")
print("2. Calculate Perimeter")
choice= int(input("Enter your Choice(1 or 2 :)"))
if choice==1:
   area=3.14159*radius*radius
   print("Area of circle is", area)
else:
   perimeter=2*3.14159*radius
   print("Perimeter of circle",perimeter)
      
   
