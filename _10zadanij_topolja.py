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
#while a.lower() !='слон':
#	a=input(f'все говорят {a}, а ты купи!')
#print('слон твой')

#задание 8

#a=0
#b=0
#for d in range(20):
#	a+=1
#	b+=1
#	a*=2.5
#	print(f'{b} дьюм это {a}см')
#	a/=2.5

#задание 17

#N=int(input('На какую цифру желаете таблицу умножения? - '))
#for i in range(9):
#	print(N,'*',i,'=',N*i)

#задание 15

#for b in range(1,10):
#	for i in range(1,10):
#		print(f'{(i*b):5}',end=' ')
#	print()

#задание 16

#for b in range(1,10):	
#	for i in range(1,10):
#		if b==i:
#			print((i), end=' ')
#		else:
#			print(0, end=' ')
#	print()

#задание 18

#for i in range(20,50):
#	if i%3==0 and i%5!=0:
#		print(i)

#задание 28

#from random import *
#a=randint(1,20)
#n=0
#U=int(input('Угадайка число от 1 до 20 - '))
#if U==a:
#	print(f'Угадал! не верных попыток было {n}')
#else:
#	n+=1
#while U!=a:
#	U=int(input('Не угадал, заново! - '))
#	if U==a:
#		print(f'Угадал! не верных попыток было {n}')
#	else:
#		n+=1

#Задание