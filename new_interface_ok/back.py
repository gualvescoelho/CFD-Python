import sys as op
import os as op
import matplotlib.pyplot as plt

class new_interface_back():
    def __init__(self):
         super().__init__()

    def processSerieTemporal(self, url, diretorio_saida, pontos):
        if self.verificarDigito(pontos):
            return
        
        self.read_file(url)
        basename = op.path.basename(url)
        url = self.get_path_from_file(url)
        url = '"' + ''.join(url)+'/'+ basename + '"'
        saida = diretorio_saida+ '/' + basename
        comando = 'start new_c '+ url +' '+ self.qnt_coord +' -1 '+ self.lines +' ' + pontos + ' "' + saida + '"'
        op.system(
            comando
        )
        
        # print(comando)

    def countPontos(self, pontos):
        countSpace = 0
        for ponto in pontos:
            if ponto.isspace():
                countSpace+=1
        
        if countSpace > 10:
            return True

        return False

    def verificarDigito(self, pontos):
        # Check if the string is empty or contains only whitespace
        if not pontos.strip():
            return True

        # Check if any character in the string is not a digit
        for ponto in pontos:
            if not ponto.isdigit() and not ponto.isspace():
                return True

        return False
    
    def process(self, itmin, path, checkbox_values, dirout):
        self.itmin = itmin if itmin.__len__() > 0 else '0'
        self.checkbox_values = checkbox_values
        self.diretorio_saida = dirout

        # criar regra de negocio para criar apenas se for selecionado o diretorio respectivo
        self.read_file(path)

        # criação dessa regra de negocio
        if self.first != '#':
            self.create_diretorios()
            self.processing(path, self.qnt_coord, self.itmin, self.checkbox_values, self.diretorio_saida)
        else:
            return 0
        
    def process_limpeza(self, url, diretorio_saida):
        self.read_file(url)

        if self.first == '#':
            file = diretorio_saida +"\\"+ op.path.basename(url) + '"'
            path = '"' + url + '" '+ '"' + file
            op.system(
                "start limpeza_1.exe " + path
            )

    def gerar_grafico(self, paths):
        conjuntos_de_valores = []

        for path in paths:
            with open(path, 'r') as f:
                dados = f.read()
                dados_ = dados[1:].split('/')
                is_y = False
                dados_y = [1.1]
                dados_x = [1.1]

                for d in dados_:
                    if d != 'y':
                        if is_y and d != 'y':
                            dados_y.append(float(d))
                        else:
                            dados_x.append(float(d))
                    else:
                        is_y = True

            conjuntos_de_valores.append((dados_x[1:], dados_y[1:]))

        # Criação do gráfico
        fig, ax = plt.subplots()

        # Itere por cada conjunto de valores e plote os pontos usando scatter
        for i, conjunto in enumerate(conjuntos_de_valores):
            valores_x, valores_y = conjunto
            plt.plot(valores_x, valores_y, marker='o', linestyle='-', label=f'Arquivo: {i+1}')

        # Personalização dos eixos
        plt.xlabel('Eixo X')
        plt.ylabel('Eixo Y')
        plt.title('Velocidades na Simulação de Fluido')

        # Personalização da grade
        plt.grid(True, which='both', linestyle='--', linewidth=0.5, markersize=4)

        # Personalização das legendas
        plt.legend()

        # Ajuste do layout
        plt.tight_layout()

        # Exibição do gráfico
        plt.show()

# comando para realizar limpeza
    def limpeza(self, url, qtd_coord, itmin, checkbox_values, diretorio_saida):
        # Sair com nome do arquivo na pasta selecionada
        file = diretorio_saida +"\\"+ op.path.basename(url) + '"'
        path = '"' + url + '" '+ '"' + file
        # op.system(
        #     "start limpeza_1.exe " + path
        # )
        # await asyncio.sleep(5)
        # print("Path no limpeza: ")
        # print(path)
        # ao terminar chamar o processing no arquivo novo
        self.processing(file, qtd_coord, itmin, checkbox_values, diretorio_saida)


    # chamada para o processamento
    def processing(self, url, qtd_coord, itmin, checkbox_values, diretorio_saida):
            basename = op.path.basename(url)
            url = self.get_path_from_file(url)
            url = '"' + ''.join(url)+'/'+ basename + '"'
            comando = 'start new_c '+ url +' '+ qtd_coord +' '+ itmin +' '+ self.lines +' '+ ' '.join(map(str,checkbox_values)) + ' "' + diretorio_saida + '"'
            op.system(
                comando
            )

            # print("Comando no processing: ")
            # print(comando)

    # comando para organizar parametros
    def create_calling_string(url, itmin, checkbox_values):
        calling_string = ""

        # Unir a URL e os outros valores na string final
        calling_string += f"{url}\n"
        calling_string += f"{itmin}\n"

        for value in checkbox_values.values():
            calling_string += f"{value}\n"

        return calling_string


    # verifica se o arquivo está limpo e retorna a quantidade de coordenadas e linhas
    def read_file(self, url):
            with open(url, 'r') as arquivo:
                # informa o primeiro caracter do arquivo e volta ao inicio com fim de verificar as linhas
                first = arquivo.read(1)
                arquivo.seek(0)
                read = arquivo.read()
                qtd_coord = self.getting_qtd_coord(read, first)
                arquivo.seek(0)

                
                # retornar a quantidade de iterações e subtrair pela quantidade de coordenadas
                len = arquivo.readlines()
            
            size = int(len.__len__()) - int(qtd_coord) - 2

            # Imprimir os caracteres lidos
            self.qnt_coord = str(qtd_coord)
            self.first = str(first)
            self.lines = str(size)

    # conta as coordenadas
    def getting_qtd_coord(self, file, first):
        if first != '#':
            i = 0
            for x in file:
                if x == '\n':
                    a += 1
                    i += 1
                else:
                    a = 0
                if(a == 2):
                    return i - 1
        else:
            qtd_coord = file.count('#')
            return qtd_coord - 1
        
    def get_path_from_file(self, url):
            url = list(url)
            url.reverse()
            i = 0
            for char in url:
                i += 1
                if char == '/':
                    url = url[i:]
                    url.reverse()
                    return url

    def create_diretorios(self):
        op.system('mkdir "' + self.diretorio_saida + '/vel_media"')
        op.system('mkdir "' + self.diretorio_saida + '/coordenadas"')
        op.system('mkdir "' + self.diretorio_saida + '/vel_media_grafico"')
        op.system('mkdir "' + self.diretorio_saida + '/desvio_padrao"')