import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import math

class correlacao:
    def __init__(self):
        super().__init__()
        self.corrListAll = []
        self.corrListSingle = 0.0
        self.yList = []
        self.xListAll = []
        self.xListSingle = []
        self.listLinha = []
        self.listCoord = []
        self.timeSteps = []
        self.graph = []

    def do(self, file):
        self.file = file
        self.readFile()

    def readFile(self):
        dados = 'start'
        dados_ant = 'start'
        countLinhas = False

        with open(self.file, 'r') as arquivo_binario:
            self.listLinha.clear()
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

        self.timesteps()

        self.getY()

    def cleanLists(self, list):
        for i in range(len(list)):
            list[i] = [valor for valor in list[i] if valor != '']

        if self.listLinha.__len__() > 0:
            self.listLinha.pop()    

    def getUx(self):
        self.clearLists()
        for lista in self.listLinha:
            i = 0
            for Ux in lista[1:]:
                if(i % 3 == 0):
                    self.xListAll.append(float(Ux))
                i += 1
            self.calcCorrelacaoAll()
            self.xListAll.clear()
            

    def findUx(self, timestep, path):
        self.clearLists()
        for lista in self.listLinha:
            if lista[0] == timestep:
                i = 0
                for Ux in lista[1:]:
                    if(i % 3 == 0):
                        self.xListSingle.append(float(Ux))
                    i += 1
                pass

        self.calcCorrelacaoSingle()
                
        basename = str(os.path.basename(self.file))
        file = str(str(path)+'\\'+basename +'_'+ timestep+'.txt')

        with open (file, 'w+') as arquivo:
            arquivo.write(''.join(timestep) +'\t'+str(self.corrListSingle)+'\n')
        
        self.xListSingle.clear()

    def getY(self):
        self.yList.clear()
        self.yCentral = self.listCoord[self.listCoord.__len__()//2][1]

        for y in self.listCoord:
            val = pow(float(y[1]) - float(self.yCentral), 2)
            self.yList.append(val)

    def timesteps(self):
        self.timeSteps.clear()
        for time in self.listLinha: 
            self.timeSteps.append(time[0])

    def calcCorrelacaoAll(self):
        x = pd.Series(self.xListAll)
        y = pd.Series(self.yList)

        z = y.corr(x)
        if(z):
            self.corrListAll.append(abs(z))
        
    def calcCorrelacaoSingle(self):
        x = pd.Series(self.xListSingle)
        y = pd.Series(self.yList)

        z = y.corr(x)
        self.corrListSingle = abs(z)

    def clearLists(self):
        self.xListAll.clear()
        self.corrListAll.clear()

    def writeCorrFile(self, path):
        self.getUx()
        basename = str(os.path.basename(self.file))
        file = str(str(path)+'\\Corr_'+basename)
        with open (file, 'w+') as arquivo:
            for timestep, corr in zip(self.timeSteps, self.corrListAll):
                arquivo.write(''.join(timestep) +'\t'+str(corr)+'\n')


    def generateGraphs(self, paths):
        values = []

        for path in paths:
            self.do(path)
            self.getUx()
            self.timesteps()
            values.append((self.timeSteps, self.corrListAll))

        fig, ax = plt.subplots()

        for i, conjunto in enumerate(values):
            valores_x, valores_y = conjunto
            plt.plot(valores_x, valores_y, marker='o', linestyle='-', label=f'Arquivo: {i+1}')

        plt.xlabel('Eixo X')
        plt.ylabel('Eixo Y')
        plt.title('Correlações')

        # Personalização da grade
        plt.grid(True, which='both', linestyle='--', linewidth=0.5, markersize=4)

        # Personalização das legendas
        plt.legend()

        # Ajuste do layout
        plt.tight_layout()

        # Exibição do gráfico
        plt.show()

    def generateGraph(self):
        self.clearLists()
        self.corrListAll.clear()
        self.getUx()
        self.timesteps()

        # self.graph.append((self.timeSteps, self.corrListAll))
        self.minMaxGraph()
        self.defineX()
        plt.figure(figsize=(12, 7), layout='constrained')
        plt.plot(self.timeSteps, self.corrListAll)
        listOfTicksX = np.arange(0,self.timeSteps.__len__(),self.dividirX)
        plt.xticks(listOfTicksX)
        plt.suptitle("Minimo: "+str(self.minimo)+"\n Maximo: "+str(self.maximo)) 
        plt.autoscale()
        plt.show()

    def minMaxGraph(self):
        self.corrListAll = [x for x in self.corrListAll if not math.isnan(x)]
        self.minimo = min(self.corrListAll)
        self.maximo = max(self.corrListAll)

        if(self.timeSteps[0] == '0'):
            self.timeSteps.remove('0')

    def defineX(self):
        if self.timeSteps.__len__() > 10000:
            self.dividirX = self.timeSteps.__len__()//7.5
        else:
            self.dividirX = self.timeSteps.__len__()//15

