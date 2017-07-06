#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
#低于18.5：过轻
#18.5-25：正常
#25-28：过重
#28-32：肥胖
#高于32：严重肥胖
#用if-elif判断并打印结果：

#_*_ coding:utf-8 _*_

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
