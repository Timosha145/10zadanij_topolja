#t=0
#c=0
#n=0
#while t<15:
#	t+=1
#	a=float(input('введи цифру :'))
#	if a==round(a):
#		c+=1
#	else:
#		n+=1
#print(f'целых {c}, дробных {n}')

#c=0
#n=0
#for t in range(15):
#	a=float(input('введи цифру :'))
#	if a==round(a):
#		c+=1
#	else:
#		n+=1
#print(f'целых {c}, дробных {n}')

#задание 2

#a=int(input('введи число: '))
#for a in range(a):
#	a+=a
#print(f'сумма {a}')

#задание 3

#b=1
#for t in range(8):
#	a=int(input('введи число'))
#	if a>0:
#		b*=a
#print(f'произведение равно {b}')

#задание 4

#for a in range (10,21):
#	print(a**2)
#	print('')

#задание 5

#from random import *
#d=0
#a=randint(1,10)
#for b in range(a):
#	c=int(input('введи число: '))
#	if c<0:
#		d+=c
#print(d)

#задание 6

#from random import *
#minus=0
#plus=0
#nol=0
#a=randint(3,10)
#for b in range(a):
#	c=int(input('введи число: '))
#	if c<0:
#		minus+=1
#	elif c>0:
#		plus+=1
#	elif c==0:
#		nol+=1
#print(f'колво отрицательных {minus}, колво положительных {plus}, колво нулей {nol}')

#задание 7

#K=int(input('введи K: '))
#A=int(input('введи A: '))
#B=int(input('введи B: '))
#for t in range(A,B):
#	if  K%A == 0:
#		print(A)
#		print('')
#		A+=1

#купи слона

#a=input('Купи слона! ')
while a.lower() !='слон':
	a=input(f'все говорят {a}, а ты купи!')
print('слон твой')