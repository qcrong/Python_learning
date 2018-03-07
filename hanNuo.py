# _*_ coding: utf-8 _*_
#输出汉诺塔搬运方法，a,b,c 表示三根柱子，n表示a柱子上盘子的数量
def move(n,a,b,c):
	if n==1:					#当n==1时，直接从a移动到c
		print(a, '-->', c)		#直接输出a到c
	else:
		move(n-1,a,c,b)			#先将a上除了最大底盘外的所有圆盘(n-1个)移动到b
		move(1,a,b,c)			#再将a上的最大底盘移动到c
		move(n-1,b,a,c)			#最后将b上的所有圆盘(n-1个)移动到c