import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

class correlacao:
    def __init__(self):
        super().__init__()
        self.corrList = []
        self.yList = []
        self.xList = []
        self.listLinha = []
        self.listCoord = []
        self.timeSteps = []

    def do(self, file):
        self.file = file
        self.readFile()

    def readFile(self):
        dados = 'start'
        dados_ant = 'start'
        countLinhas = False

        with open(self.file, 'r') as arquivo_binario:
            while dados:
                dados = arquivo_binario.readline()

                if(dados and dados_ant == '\n'):
                    countLinhas = True

                if(dados != '\n'):
                    if countLinhas == True:
                        self.listLinha.append(dados[:-2].rsplit(' '))
                    else:
                        self.listCoord.append(dados[:-2].rsplit(' '))
                    
                dados_ant = dados
        
        self.cleanLists(self.listLinha)
        self.cleanLists(self.timeSteps)

        self.timesteps()
        self.getY()

    def cleanLists(self, list):
        for i in range(len(list)):
            list[i] = [valor for valor in list[i] if valor != '']

    def getUx(self):
        self.clearLists()
        for lista in self.listLinha:
            i = 0
            for Ux in lista[1:]:
                if(i % 3 == 0):
                    self.xList.append(float(Ux))
                i += 1
            self.calcCorrelacao()
            self.xList.clear()
            

    def findUx(self, timestep, path):
        self.clearLists()
        self.xList.clear()
        self.corrList.clear()
        for lista in self.listLinha:
            if lista[0] == timestep:
                i = 0
                for Ux in lista[1:]:
                    if(i % 3 == 0):
                        self.xList.append(float(Ux))
                    i += 1
                self.calcCorrelacao()
                
        basename = str(os.path.basename(self.file))
        file = str(str(path)+'\\'+basename +'_'+ timestep)
        with open (file, 'w+') as arquivo:
            for timestep, corr in zip(self.timeSteps, self.corrList):
                arquivo.write(str(timestep) +'\t'+str(corr)+'\n')
        
        self.xList.clear()

    def getY(self):
        self.yList.clear()
        self.yCentral = self.listCoord[self.listCoord.__len__()//2][1]

        for y in self.listCoord:
            val = pow(float(y[1]) - float(self.yCentral), 2)
            self.yList.append(val)

    def timesteps(self):
        self.listLinha.pop()
        for time in self.listLinha:
            self.timeSteps.append(time[0])


    def calcCorrelacao(self):
        x = pd.Series(self.xList)
        y = pd.Series(self.yList)

        z = y.corr(x)
        self.corrList.append(z)

    def clearLists(self):
        self.xList.clear()
        self.corrList.clear()

    def writeCorrFile(self, path):
        self.getUx()
        basename = str(os.path.basename(self.file))
        file = str(str(path)+'\\'+basename)
        with open (file, 'w+') as arquivo:
            for timestep, corr in zip(self.timeSteps, self.corrList):
                arquivo.write(str(timestep) +'\t'+str(corr)+'\n')

    def generateGraph(self):
        self.corrList.clear()
        self.getUx()
        minimo = min(self.corrList)
        maximo = max(self.corrList)

        plt.plot(self.timeSteps, self.corrList)
        listOfTicksX = np.arange(0,self.timeSteps.__len__(),2000)
        plt.xticks(listOfTicksX)
        plt.suptitle("Minimo: "+str(minimo)+"\n Maximo: "+str(maximo)) 
        plt.autoscale()
        plt.show()