#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。
# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。

# __str__
class Student(object):
	def __init__(self, name):
		self.name = name
	# 自定义__str__()
	def __str__(self):
		return 'Student object (name:%s)' % self.name
	__repr__ = __str__
print(Student('Micheal'))

# __iter__ + __next__()
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法
# 拿到循环的下一个值，直到遇到StopIteration错误时退出循环
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1

	def __iter__(self):
		return self #实例本身就是迭代对象

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 10000: # 退出循环的条件
			raise StopIteration()
		return self.a # 返回下一个值
	
	# 支持切片
	def __getitem__(self, n):
		if isinstance(n, int): # n是索引
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice): # n是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L

for n in Fib():
	print(n)

# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
# 定义在上面
f = Fib()
print(f[0], f[1], f[100])
print(f[0:5])
print(f[:10])
