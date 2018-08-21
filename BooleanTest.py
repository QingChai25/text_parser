def convertFileToList(filePath):
	with open(filePath, "r") as fileObj:
		resultList = fileObj.readlines()

	return resultList

def seperateInputAnswer(resultList):
	listOfInputAnswer = []
	for line in resultList:
		smallList = line.split("\t")
		inputList = smallList[0].split(" ")
		singleLine = [inputList, smallList[1].strip()]
		listOfInputAnswer.append(singleLine)
	return listOfInputAnswer

def fileReadAndConvert(filePath):
	lineList = convertFileToList(filePath)
	return seperateInputAnswer(lineList)


def test():
	filePath = "test.txt"
	print(fileReadAndConvert(filePath))

test()

