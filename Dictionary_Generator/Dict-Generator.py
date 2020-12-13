#!/usr/bin/env python3

from colorama import *

def getmode():
	mode = input("Which type of dictionary would you like to generate? (Quick Generate from template word: " + Fore.YELLOW + Style.BRIGHT + "QG" + Style.RESET_ALL + ") (Append Mode: " + Fore.YELLOW + Style.BRIGHT + "AP" + Style.RESET_ALL + ") (Prepend Mode: " + Fore.YELLOW + Style.BRIGHT + "PP" + Style.RESET_ALL + "): ")
	generate(str(mode))
def generate(mode):
	if str(mode.lower()) == 'qg':
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
		write()
	elif str(mode.lower()) == 'ap':
		filename = input("Input a filename for your dictionary (without a file extension, as this will automatically be set to .txt): ")	
		f = open(str(filename) + ".txt", "a+")
		append = input("Input text to append: ")

		def write():
			phrase = input("Input a phrase to be added: ")
			if phrase == 'q':
				exit()
			else:	
				f.write(phrase + append + "\r\n")
				write()
		write()
	elif str(mode.lower()) == 'pp':
		filename = input("Input a filename for your dictionary (without a file extension, as this will automatically be set to .txt): ")	
		f = open(str(filename) + ".txt", "a+")
		prepend = input("Input text to prepend: ")

		def write():
			phrase = input("Input a phrase to be added: ")
			if phrase == 'q':
				exit()
			else:	
				f.write(prepend + phrase + "\r\n")
				write()
		write()
	else:
		print(Fore.RED + Style.BRIGHT + "Error: Invalid mode" + Style.RESET_ALL)
		getmode()
getmode()
