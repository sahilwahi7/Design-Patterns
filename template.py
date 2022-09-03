"""   Template methhod is used to convert a monolithic algorithm to various implementation"""

from abc import abstractclassmethod
import random
#this is main class that handles the mining actvities 
class dataMiner:

    @abstractclassmethod
    def openfile(self,path):
        pass

    @abstractclassmethod
    def extrarctData(self,file):
        pass

    @abstractclassmethod
    def closeFile(self):
        pass

    def analyzeData(self,data):
        analysis=len(data) if data else 0
        print(analysis)
        return analysis
        

    def  sendreport(self,analysis):
        report=f"data has lenght {analysis}"
        print(report)


#now we wil concrete miners like csv,pdf,txt

class csvMiner(dataMiner):

    @classmethod
    def openfile(self,path):
        self.path=path
        print(f"file opened with path:{self.path}")
        return self.path

    @classmethod
    def extractData(self,path):
        self.path=path
        data=[random.randint(0,9) for i in range(random.randint(1,3))]
        return data

    @classmethod
    def closeFile(self):
        print("closinf csv file")



d=csvMiner()
path="csv"
file=d.openfile(path)
data=d.extrarctData(file)
analysis=d.analyzeData(data)
print(analysis)
d.sendreport(analysis)
