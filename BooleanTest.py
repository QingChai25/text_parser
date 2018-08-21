# from sys improt argv
# BooleanTest.py BooleanTest.txt = argv
# txt = open(BooleanTest.txt)

# for x in txt:
# 	ReadEachLine = readline(txt)
	

def convertFileToList(filePath):
	with open(filePath, "r") as fileObj:
		resultList = fileObj.readlines()

	return resultList

def seperateInputAnswer(resultList):
	listOfInputAnswer = []
	for line in resultList: 
		listOfInputAnswer.append(line.split("\t"))
	return listOfInputAnswer


def test():
	filePath = "test.txt"
	resultList = convertFileToList(filePath)
	# print(resultList)
	listOfInputAnswer = seperateInputAnswer(resultList)
	for smallList in listOfInputAnswer:
		print(smallList[0])
		print(smallList[1])

test()