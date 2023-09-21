import pandas as pd

#Falta organizar coordenadas, para pegar os valores 
#Procurar a coluna desejada, ja é possivel encontrar
listLinha = [[float]]
listCoord = []

yList = []
xList = []
corrList = []

dados = 'a'
dados_ant = 'a'
countLinhas = False

yCentral = ''
y = ''

with open('U-1.txt', 'r') as arquivo_binario:
    while dados:
        dados = arquivo_binario.readline()

        if(dados and dados_ant == '\n'):
            countLinhas = True

        if(dados != '\n'):
            if countLinhas == True:
                linha = dados[:-2].rsplit(' ')
                listLinha.append(linha)
            else:
                coord = dados[:-2].rsplit(' ')
                listCoord.append(coord)
            
        dados_ant = dados

i = 0

for i in range(len(listLinha)):
    listLinha[i] = [valor for valor in listLinha[i] if valor != '']

for lista in listLinha:
    # Verifique se o valor na primeira posição da lista é igual ao valor procurado
    if lista[0] == '0.001':
        i = 0
        for Ux in lista[1:]:
            if(i % 3 == 0):
                xList.append(float(Ux))
            i += 1
        break  # Saia do loop se encontrar o valor

yCentral = listCoord[listCoord.__len__()//2][1]
for y in listCoord:
    val = pow(float(y[1]) - float(yCentral), 2)
    yList.append(val)

print(yList)
print(xList)

# dataset = { 
#     'Y' : xList, 
#     'X' : yList 
# }

dataset = {
    'Y' : [pow((0- 0.05), 2),
           pow((0.005- 0.05), 2),
           pow((0.01- 0.05), 2),
           pow((0.015- 0.05), 2),
           pow((0.02- 0.05), 2),
           pow((0.025- 0.05), 2),
           pow((0.03- 0.05), 2),
           pow((0.035- 0.05), 2),
           pow((0.04- 0.05), 2),
           pow((0.045- 0.05), 2),
           pow((0.05- 0.05), 2),
           pow((0.055- 0.05), 2),
           pow((0.06- 0.05), 2),
           pow((0.065- 0.05), 2),
           pow((0.07- 0.05), 2),
           pow((0.075- 0.05), 2),
           pow((0.08- 0.05), 2),
           pow((0.085- 0.05), 2),
           pow((0.09- 0.05), 2),
           pow((0.095- 0.05), 2),
           pow((0.1- 0.05), 2),],
    'X' : [0.999202, 0.999202, 0.999999, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.999999, 0.999202]
}

valores = pd.DataFrame(dataset)

print(valores.corr())
