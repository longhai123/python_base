#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from types import MethodType

# 定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
class Student(object):
	pass

s = Student()
s.name = 'Micheal'
print(s.name)

# 可以绑定方法
def set_age(self, age):
	self.age = age

s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)

# 给一个实例绑定的方法，对另一个实例不起作用
s2 = Student()
#s2.set_age(25)
