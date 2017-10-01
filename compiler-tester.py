import os
import re

PATH = '/media/savitoj/Windows/Computer Stuff/CS courses/python scripts/Python-Programs-master/file compiler and tester/test'

def findFile():
	
	for root, dirs, files in os.walk(PATH):
		for file in files:
			pos = file.count('.')
			if pos == 1:
				pos = file.index('.')
				lang = file[pos+1:]
				if lang == 'c' or lang == 'java' or lang == 'cpp':
					return (file,pos,lang)


def langCompiler(file,pos,lang):
	
	classfile = ''
	runfile = ''
	
	if lang == 'java':
		classfile = 'javac ' + file
		runfile = 'java ' + file[:pos]   #name of class and file should be same

	if lang == 'cpp':
		classfile = 'g++ -o ' + file[:pos] + ' ' + file   
		runfile = './' + file[:pos]

	if lang == 'c':
		classfile = 'gcc -o ' + file[:pos] + ' ' + file
		runfile = './' + file[:pos]

	return (classfile,runfile)


def compileFile(classfile):
	
	os.system(classfile)

def runFile(runfile):
	
	i = 1
	for file in os.listdir(PATH):
		if file == str(i): 
			os.system(runfile + ' < ' + str(i) + ' > ' + 'output_' + str(i))
			i = i + 1
				
def removeObject(file,lang,pos):
	
	if lang == 'c' or lang == 'cpp':
		for files in os.listdir(PATH):
			if files == file[:pos]:
				os.remove(file[:pos])
	elif lang == 'java':
		for files in os.listdir(PATH):
			if files == file[:pos] + '.class':
				os.remove(file[:pos] + '.class')


def removeWhiteSpaces(data):
	return data.strip()


def compareOutputs():
	
	i = 1 
	passed = 1
	for files in os.listdir(PATH):
		if files == 'output_' + str(i):
			f = open('output_' + str(i) , 'r')
			data = f.read()
			
			os.chdir(PATH + '/outputs')
			g = open(str(i),'r')
			datacmp = g.read()
			
			if removeWhiteSpaces(data) == removeWhiteSpaces(datacmp):
				passed = passed + 1
			
			g.close()
			os.chdir(PATH)
			f.close()
			i = i + 1
	if passed == i :
		print("\nAll Test Cases Passed")
	else:
	    print("\nOops! You failed " + str(i-passed) + " Test Cases")


if __name__ == '__main__':
	
	file, pos, lang = findFile();
	classfile, runfile = langCompiler(file,pos,lang)

	os.chdir(PATH)
	try:
		compileFile(classfile)
	except:
		print("Compilation Error")
		exit(0)
	
	runFile(runfile)
	removeObject(file,lang,pos)
	
	compareOutputs()