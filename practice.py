# _*_ coding: utf-8 _*_

#-----------------【函数findMinAndMax】----------------
#迭代查找list中最大和最小值，返回一个tuple
#------------------------------------------------------
def findMinAndMax(L):
	max=None;
	min=None;
	if L!=[]:
		max=L[0]
		min=L[0]
		for data in L:
			if data > max:
				max=data
			elif data < min:
				min=data
	return (min, max)