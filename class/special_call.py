#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

	def __init__(self, name):
		self.name = name
	
	def __call__(self):
		print('My name is %s.' % self.name)

s = Student('Micheal')
s()
print(callable(Student('NB')))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))
