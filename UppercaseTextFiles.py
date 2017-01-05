import os
import codecs

def test():
	os.chdir("D:/TEXT")
	files = os.listdir(".")
	for x in files:
		if os.path.isdir(x) == False:
			print("Processing file... ",x)
			inputFile = codecs.open(x,"r",'utf-8')
			content = inputFile.read()
			with codecs.open(os.path.join('D:/TEXT/UPPER',x),"wb",'utf-8') as outputFile:
					outputFile.write(content.upper())
		
test()