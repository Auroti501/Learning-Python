#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('This programm will determine your BMI Index','\n')
w=float(input('Please input your weight in KGs ：'))
h=float(input('Please input your height in M ：'))
bmi=w/(h*h)
n1=23*h*h
n='%.2f'%n1
if bmi<18.5:
    print('过轻','建议增重至',n,'kg')
elif bmi<=25:
    print('正常','但是最正常的是',n,'kg')
elif bmi<=28:
    print('过重','建议减重至',n,'kg')
elif bmi<=32:
    print('肥胖','建议减重至',n,'kg')
else:
    print('严重肥胖','建议减重至',n,'kg')
