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

def booleanize(boolString):
	if boolString == "True":
		result = True
	elif boolString == "False":
		result = False
	else:
		raise ValueError("spell error!")

	return result 

def getType1Expression(expressionList):
	left = booleanize(expressionList[0])
	right = booleanize(expressionList[2])
	operand = expressionList[1]
	if operand == "and":
		return left and right
	elif operand == "or":
		return left or right
	else:
		raise ValueError("logic operand not recognized!!")



def test():
	l1 = ["True", "and", "False"]
	l2 = ["False", "or", "True"]
	l3 = ["True", "==", "True"]
	if not getType1Expression(l1):
		print("l1 works.")
	
test()


