#vertup 1 vertdown 2 horright 3 horleft 4

import serial
import time
import read_one
from random import randint
import sys

def go_to_origin(ixcord, iycord):
	ser = serial.Serial('/dev/ttyACM0', 9600)
	time.sleep(2)

	while ixcord != 0:
			ser.write('4')
			time.sleep(1)
			ixcord -= 1

	while iycord != 0:
			ser.write('1')
			time.sleep(1)
			to_move_vert -= 1


def go_to_product(ixcord, iycord, xcord, ycord):
	ser = serial.Serial('/dev/ttyACM0', 9600)
	time.sleep(2)

	to_move_vert = ycord - iycord
	to_move_horz = xcord - ixcord

	if to_move_horz > 0:
		while to_move_horz != 0:
			ser.write('3')
			time.sleep(1)
			to_move_horz -= 1
	elif to_move_horz < 0:
		while to_move_horz != 0:
			ser.write('4')
			time.sleep(1)
			to_move_horz += 1

	if to_move_vert > 0:
		while to_move_vert != 0:
			ser.write('2')
			time.sleep(1)
			to_move_vert -= 1
	elif to_move_vert < 0:
		while to_move_vert != 0:
			ser.write('1')
			time.sleep(1)
			to_move_vert += 1

	qr = Read_qr.funct()

	return qr
