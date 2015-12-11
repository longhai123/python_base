#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用@property

class Student(object):

	# Python内置的@property装饰器就是负责把一个方法变成属性调用
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value ,int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100!')
		self._score = value

s = Student()
s.score = 100
print(s.score)
#s.score = 9999

# birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来
class Student(object):
	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self, value):
		self._birth = value

	@property
	def age(self):
		return 2015 - self._birth
