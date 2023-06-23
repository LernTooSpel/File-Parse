import os
#Class definition
class Student:
    def __init__(self,id="Unknown",firstName="Unknown",lastName="Unknown",birthday="Unknown",
                 education="Unknown",degree="Unknown",hobby="Unknown"):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.birthday = birthday
        self.education = education
        self.degree = degree
        self.hobby = hobby
    
    def __str__(self):
        return f"{self.id}, {self.firstName} {self.lastName}, {self.birthday}, {self.education}, {self.degree}, {self.hobby}"


#First Function
def firstFileParse():
    textFilePath = os.path.join('File-Parse','3students_separate_fields.txt') #Open File
    outFile = open(textFilePath,"r")
    textData = outFile.readlines()
    rawData = []
    for line in textData:
        temp = line.split('=') # Filter out '=', '\n', and '"'
        temp = temp[1].split('\n')
        temp = temp[0].split('"')
        rawData.append(temp[1]) # Append filtered data
    for i in range(int(len(rawData)/6)): # Print out new student every 6 elements
        j = i*6
        print(Student(i,rawData[j],rawData[j+1],rawData[j+2],rawData[j+3],rawData[j+4],rawData[j+5]))
    outFile.close()

def thirdFileParse():
    textFilePath = os.path.join('File-Parse','3students_human_readable.txt') #Open File
    outFile = open(textFilePath,"r")
    textData = outFile.readlines()
    rawData = []
    LABELLINES = 2 #Number of lines that need to be skipped
    counter = 0
    for line in textData:
        counter = counter+1
        if counter <= LABELLINES:
            continue
        temp = line.split(' ') # Filter out ' '
        for element in temp:
            if (element != "") & (element != "\n"):
                rawData.append(element) # Append filtered data
    for element in rawData:
        if "\n" in element:  # If element contains \n, remove it
            temp = element.split('\n')[0]
            print(temp)
            location = rawData.index(element)
            rawData.insert(location, temp)
            rawData.pop(location+1)
    print(rawData)
    for i in range(int(len(rawData)/6)): # Print out new student every 6 elements
        j = i*6
        print(Student(i,rawData[j],rawData[j+1],rawData[j+2],rawData[j+3],rawData[j+4],rawData[j+5]))
    outFile.close()

thirdFileParse()