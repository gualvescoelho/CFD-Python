import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class correlacao:
    def __init__(self):
        self.corrList = []
        self.yList = []
        self.xList = []
        self.listLinha = []
        self.listCoord = []
        self.timeSteps = []

    def readFile(self, file = ''):
        dados = 'start'
        dados_ant = 'start'
        countLinhas = False

        with open('U-1.txt', 'r') as arquivo_binario:
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

# Atribuir aqui o calculo da correlação completo, para quando for necessário fazer o de todos, lera linha, e fazer
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
            

    def findUx(self, timestep):
        self.clearLists()
        for lista in self.listLinha:
            if lista[0] == timestep:
                i = 0
                for Ux in lista[1:]:
                    if(i % 3 == 0):
                        self.xList.append(float(Ux))
                    i += 1
                self.calcCorrelacao()
                break

    def getY(self):
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

def main():
    # Crie uma instância da classe
    objeto = correlacao()

    objeto.readFile()
    objeto.getUx()

    # objeto.findUx('0.001')
    # print(objeto.corrList)

    minimo = min(objeto.corrList)
    maximo = max(objeto.corrList)

    plt.plot(objeto.timeSteps, objeto.corrList)
    listOfTicksX = np.arange(0,objeto.timeSteps.__len__(),2000)
    plt.xticks(listOfTicksX)
    plt.suptitle("Minimo: "+str(minimo)+"\n Maximo: "+str(maximo)) 
    plt.autoscale()
    plt.show()

if __name__ == "__main__":
    main()
