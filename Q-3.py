from math import sqrt


a = float(input("side a: "))
b = float(input("side b: "))
c = float(input("side c: "))

if (a+b) <=c or (a+c) <=b or (b+c) <=a:

 print("given values are invalid ")

else:

#find out semi-perimeter "s"
 s = (a+b+c)/2

r = float(s*(s-a)*(s-b)*(s-c))
area = sqrt(r)
        
print("the area of triangle is: ", area)