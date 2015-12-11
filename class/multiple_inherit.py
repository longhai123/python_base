#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多重继承使一个子类可以同时获得多个父类的所有功能

class Animal(object):
	pass

class Mammal(Animal):
	pass

class Bird(Animal):
	pass

class Runnable(object):
	def run(self):
		print('Running...')

class Flyable(object):
	def fly(self):
		print('Flying...')

class Dog(Mammal, Runnable):
	pass

class Bat(Mammal, Flyable):
	pass



if __name__ == '__main__':
	dog = Dog()
	dog.run() 
	
	bat = Bat()
	bat.fly()

# MixIn
# 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
# 只允许单一继承的语言（如Java）不能使用MixIn的设计。
