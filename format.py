#some methods of formating string
# first method
print("{} is a student.".format("she"))

person="Mary"
print("{} is a student.".format(person))

name="Janny"
occupation="teacher"
print("{} is a {}.".format(name,occupation))
print("{1} is a {0}.".format(occupation,name))

#second method 
print(f"{name} is a {occupation}.")

#number formating

#0：指的是需要格式化的对象
#：后面是格式化信息
#.:指的是小数点后面
#5：指的是小数点后5位
#f：指的是浮点数
print("{0:.5f}".format(3.14))

#another formating example
print("{0:_^11}".format("hello"))
print("{0:_>11}".format("hello"))
print("{0:_<11}".format("hello"))


