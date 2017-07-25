import serial
import time
import read_one
from random import randint
import sys
'''
def func(xcord, ycord, QRcode):
	ser = serial.Serial('/dev/ttyACM0', 9600)
	time.sleep(2)
	count = 0
	prev = ''

	if xcord < ycord:
		short = xcord
	else:
		short = ycord

	for i in range(1, short):
		pass #calldiagfn
		
	xcord -= short
	ycord -= short

	for i in range(0, xcord):
		pass #callhorfn
	for i in range(0, ycord):
		pass #callvertfn

	temp = read_one.funct()
	print temp

	sys.exit()
'''
'''
	while temp != qrc and count <=2:
		count = 0
		flag = 0
		while count <= 2:
			if temp != prev:
				prev = temp
				temp = read_one.funct()
				print(temp)
			ser.write('3')
			if temp != 'empty':
				count += 1
			if temp == qrc:
				sys.exit()

	prev = ''
	#count = randint(0,2)
	count = 0
	time.sleep(1)
	temp = ''
	while temp != qrc and count <= 1:
		count = 0
		flag = 0
		while count <= 1:
			if temp != prev:
				prev = temp
				temp = read_one.funct()
			ser.write('2')
			if temp != 'empty':
				count += 1
			if temp == qrc:
				sys.exit()

	print(randint(0,2))
	count = 0
	time.sleep(2)
	temp = ''
	prev = ''
	while temp != qrc and count <= 2:
		count = 0
		flag = 0
		while count <= 2:
			if temp != prev:
				prev = temp
				temp = read_one.funct()
			ser.write('4')
			if temp != 'empty':
				count += 1
			if temp == qrc:
				sys.exit()
		
		#count = randint(0,2)
	count = 0
	time.sleep(1)
	temp = ''
	prev = ''
	while temp != qrc and count <= 1:
		count = 0
		flag = 0
		while count <= 1:
			if temp != prev:
				prev = temp
				temp = read_one.funct()
			ser.write('2')
			if temp != 'empty':
				count += 1
			if temp == qrc:
				sys.exit()

	count = 0
	time.sleep(1)
	temp = ''
	prev = ''
	while temp != qrc and count <= 2:
		count = 0
		flag = 0
		while count <= 2:
			if temp != prev:
				prev = temp
				temp = read_one.funct()
			ser.write('3')
			if temp != 'empty':
				count += 1
			if temp == qrc:
				sys.exit()

'''