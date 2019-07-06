#!/usr/bin/env python3

def generate():
	# Quick Generate a list from a baseword...
	filename = input("Input a filename for your dictionary (without a file extension, as this will automatically be set to .txt): ")	
	f = open(str(filename) + ".txt", "a+")		
	baseword = input("Input a baseword for your dictionary: ")
	minimum = int(input("Input a minimum value for your dictionary: "))
	maximum = int(input("Input a maximum value for your dictionary: "))
	maximum = maximum + 1
	hybrid = baseword.replace('a', '4')
	hybrid = hybrid.replace('e', '3')
	hybrid = hybrid.replace('i', '1')
	hybrid = hybrid.replace('o', '0')
	hybrid = hybrid.replace('s', '5')
	hybrid = hybrid.replace('t', '7')
	hybrid = hybrid.replace('A', '4')
	hybrid = hybrid.replace('E', '3')
	hybrid = hybrid.replace('I', '1')
	hybrid = hybrid.replace('O', '0')
	hybrid = hybrid.replace('S', '5')
	hybrid = hybrid.replace('T', '7')
	def write():
		# Simple, yet effective
		for i in range(int(minimum), int(maximum)):
			f.write(baseword + str(i) + "\r\n")
		for i in range(int(minimum), int(maximum)):
			f.write(baseword.lower() + str(i) + "\r\n")
		for i in range(int(minimum), int(maximum)):
			f.write(baseword.upper() + str(i) + "\r\n")
		for i in range(int(minimum), int(maximum)):
			f.write(hybrid + str(i) + "\r\n")
		for i in range(int(minimum), int(maximum)):
			f.write(hybrid.lower() + str(i) + "\r\n")
		for i in range(int(minimum), int(maximum)):
			f.write(hybrid.upper() + str(i) + "\r\n")
	def newdict():
		restart = input("Would you like to create another dictionary? y/N: ")
		if restart.lower() == 'y':
			generate()
		else:
			f.close()
			exit	
	write()
	newdict()
generate()
