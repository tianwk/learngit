# -*- coding: utf-8 -*-
import math
print('欢迎求解二元一次方程ax^2+bx+c=0')
a = int(input())
b = int(input())
c = int(input())
def quadratic(a,b,c):
  x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
  x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
  return x1,x2
if b*b-4*a*c < 0:
 print('该方程无解')
if b*b-4*a*c == 0:
 print('该方程根为', quadratic(a,b,c))
else:
 print(quadratic(a,b,c))

