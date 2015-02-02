#!/opt/bin/python3
# Author: Zheng Li, V00796189 

import csv
import sys
import string


class spreadsheet(object):
    def __init__(self):
        self.filename=''
        self.numRows=0
        self.numCols=0
        self.contents=[]
        self.checker=0
    def load(self,fileName):
        #filename=input('Please enter your filename: ')
        if fileName[0]=='"' and fileName[-1]=='"':
            fileName = fileName[1:-1]
        try:
            csvfile=open(fileName, newline='')
            csvreader=csv.reader(csvfile,delimiter=',')
            global numRows
            ss=[]
            countRows = 0
            for row in csvreader:
                ss.append(row)
                countRows=countRows+1
            csvfile.close()
            self.filename=fileName
            self.numRows=countRows
            self.numCols=len(ss[0])
            self.contents=ss
            return self.contents
        except:
            print("Error occurred while accessing file", fileName)
            reason = sys.exc_info()
            print("Reason: ", reason[1])
                
    def deleterow(self,a):
        if a>self.numRows-1:
            print('the input is out of the range')
            return -1
        self.contents.pop(a)
        self.numRows=self.numRows-1

    def printrow(self,a,b):
        if b>self.numRows:
            b=self.numRows-1
        for x in range(a,b+1):
            for y in range(0,self.numCols):
                if(self.contents[x][y].find(',') != -1 or self.contents[x][y].find(' ') != -1):
                    print('\"'+self.contents[x][y]+'\"',end='')
                elif(self.contents[x][y].find('\"') != -1):   #find double quote
                    p = self.contents[x][y].find('\"')
                    print('\"'+self.contents[x][y][:p]+'\"'+self.contents[x][y][p:]+'\"',end='')
                else:
                    print(self.contents[x][y],end='')
                if y!=self.numCols-1:
                    print(',',end='')
            print('\n',end='')

    def evalsum(self,CN):
        if CN > self.numCols:
            print('The column number you entered is out of range')
            return -1
        sum=0
        for row in range(0,self.numRows):
             sum=sum+float(self.contents[row][CN])
        print('the sum of the colums is ',sum)
        return sum

    def evalavg(self,CN):
        if CN > self.numCols:
            print('The column number you entered is out of range')
            return -1
        avg=0
        sum=0
        for row in range(0,self.numRows):
             sum=sum+float(self.contents[row][CN])
             avg=sum/self.numRows
        print('the average of the colums is',avg)
        return avg

    def findrow(self,colNum,text):
        if colNum>self.numCols:
            print('The column number you entered is out of range')
            return -1
        global NumberRow
        NumberRow=0;
        x=0
        for x in range(self.numRows):
            if(text==self.contents[x][colNum]):
                 print(text,'is foud in row',NumberRow)
                 return NumberRow
            NumberRow=NumberRow+1
    def merge(self,fileName):
        if fileName[0]=='"' and fileName[-1]=='"':
            fileName = fileName[1:-1]
        ss2=spreadsheet()
        ss2.load(fileName)
        self.contents.extend(ss2.contents)
        self.numRows=self.numRows+ss2.numRows

    def stats(self):
        print (self.filename)
        print (self.colnum)
        print (self.numRows)

    def save(self,filename):
        csvfile=open(filename,'w',newline='')
        csvwriter=csv.writer(csvfile,delimiter=',')
        for row in self.contents:
            csvwriter.writerow(row)
        csvfile.close()

    def sort(self,colums):
        global k
        k=colums
        self.contents=sorted(self.contents,key=selectColumn)

    def sortnumeric(self,colums):
        global j
        j=colums
        if not self.contents[0][colums].isdigit():
             print('cannot be sorted')
             return -1
        self.contents=sorted(self.contents,key=selectColumn2)

def selectColumn(row):
    return row[k]
def selectColumn2(row):
    return float(row[j])
def conveter(c):
    number=-25
    for l in c:
        if not l in string.ascii_letters:
            return False
        number+=ord(l.upper())-64+25
    return number-1

def subcommand(object):
        command=input('Please enter your subcommand ==>')
        command=command.split(' ')
        e='The command is invalid'
        if command[0]=='load':
            if len(command)!=2:
                print(e)
                return -1
            else:
                object.load(command[1])
            object.checker=1
            return 1
        elif command[0]=='printrow':
            if object.checker==0:
               print('spreadsheet is not loaded')
               return -1
            elif len(command)==2:
                object.printrow(int(command[1]),int(command[1]))
            else:
                object.printrow(int(command[1]),int(command[2]))
                return 1
        if command[0]=='deleterow':
            if object.checker==0:
                print('spreadsheet is not loaded')
                return -1
            object.deleterow(int(command[1]))
            return 1
        if command[0]=='evalsum':
             if object.checker==0:
                print('spreadsheet is not loaded')
                return -1
             object.evalsum(conveter(command[1]))
             return 1
        if command[0]=='evalavg':
             if object.checker==0:
                print('spreadsheet is not loaded')
                return -1
             object.evalavg(conveter(command[1]))
             return 1
        if command[0]=='findrow':
             if object.checker==0:
                print('spreadsheet is not loaded')
                return -1
             object.findrow(conveter(command[1]),command[2])
             return 1
        if command[0]=='merge':
             if object.checker==0:
                print('spreadsheet is not loaded')
                return -1
             object.merge((command[1]))
             return 1
        if command[0]=='sort':
             if object.checker==0:
                print('spreadsheet is not loaded')
                return -1
             object.sort(coveter(command[1]))
             return 1
        if command[0]=='sortnumeric':
             if object.checker==0:
                print('spreadsheet is not loaded')
                return -1
             object.sortnumeric(conveter(command[1]))
             return 1
        if command[0]=='stats':
            if object.checker==0:
                print('spreadsheet is not loaded')
                return -1
            object.stats(int(command[1]))
            return 1
        if command[0]=='save':
            if object.checker==0:
                print('spreadsheet is not loaded')
                return -1
            object.save(command[1])
            return 1
def main():
    ss= spreadsheet()
    x=1
    while (x>0):
        x=subcommand(ss)


#   writeSpreadSheet()

if __name__=="__main__":
    main()



