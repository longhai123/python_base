#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))

	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')

if __name__ == '__main__':
	bart = Student('Bart Simpson', 98)
	print(bart.get_name())
	bart.set_score(-1)
	
