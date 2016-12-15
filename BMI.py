# -*- coding: utf-8 -*-
h = input('height:')
height = float(h)
w = input('weight:')
weight = float(w)
BMI = weight/(height**2)
print('您的结果:',BMI)
if BMI<18.5:
   print('过轻')
elif 18.5<=BMI<25:
   print('正常')
elif 25<=BMI<28:
   print('过重')
elif 28<=BMI<32:
   print('肥胖')
elif BMI>=32:
   print('严重肥胖')
