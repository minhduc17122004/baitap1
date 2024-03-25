a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
S=float((a+b+c)/2)
import math
kq=math.sqrt(S*(S-a)*(S-b)*(S-c))
print(f"Dien tich={kq}")