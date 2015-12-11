#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用__slots__
from types import MethodType

class Student(object):
	__slots__ = ('name', 'age')

s = Student()
s.name = 'Micheal'
s.age = 25
print(s.name, s.age)
#s.score = 99

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用
class GraduateStudent(Student):
	pass

g = GraduateStudent()
g.score = 9999
print(g.score)

