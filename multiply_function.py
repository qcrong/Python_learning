# _*_ coding: utf-8 _*_

#计算输入数据的乘积
def product(*numbers):
	if not isinstance(numbers,(int, float)):
		raise TypeError('错误参数')
	#if len(numbers)==0:
	if numbers==():
		raise TypeError('至少需要一个数据')
	else:
		result=1
		for n in numbers:
			result=result*n
		return result