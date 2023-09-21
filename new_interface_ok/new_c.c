#include<stdio.h>
#include<stdlib.h>
#include<math.h>

struct _DADOS_ 
{
	int coluna;
	double soma_x, soma_y, soma_z;
	float x, y, z;
	struct _DADOS_ * proxima;
	struct _DADOS_ * anterior;
};
typedef struct _DADOS_ * dados;

struct _DADOS_ *inicio_colunas, *fim_colunas;
void dividir(double x);
void leitura_arquivo(char  nome_in[250], int qtd_coord, int itmin, int qtd_linhas);
dados add_dados(int coluna, float x, float y,float z,double soma_x,double soma_y,double soma_z,dados anterior);
dados procurar_coluna(int coluna);
void adc_valor(double valor_x, double valor_y,double valor_z, int coluna);
void exibir_coordenadas();
void exibir_somas();
void limpar_dados();
void arq_saida(int coord, int linhas, int itmin, char  nome_in[250]);
void ler_coluna(char  nome_in[250], int colunas, int linhas, char nome_out[250], int coluna_desejada);
void desvio_padrao(int qtd_colunas, int linhas, int itmin, int escolha, char  nome_in[250], char nome_out[250], int l, int desejado); 
double media_ponto(int ponto, int escolha);

void arq_saida_vel_media_x(char nome_out[250]);
void arq_saida_vel_media_y(char nome_out[250]);
void arq_saida_vel_media_z(char nome_out[250]);
void arq_saida_vel_media_todas(char nome_out[250]);
void arq_saida_coordenadas(char nome_out[250]);
void arq_saida_grafico_x();
void arq_saida_grafico_y();
void arq_saida_grafico_z();

//desvio padrao l = 0, desejado define se � x = 1, y = 2 ou z = 3
void arq_saida_desvio_padrao(int qtd_coord, int linhas, int itmin, char nome_in[200], char nome_out_desvio_padrao[250], int l, int desejado);

void main(int argc, char *argv[])
{
	int qtd_coord, itmin, qtd_linhas,ok_vel_x, ok_vel_y, ok_vel_z, ok_vel_gerais, ok_coordenadas, ok_serie_temporal;
    int ok_grafico_x, ok_grafico_y, ok_grafico_z;
    int ok_desvio_padrao_x, ok_desvio_padrao_y, ok_desvio_padrao_z;
	int coluna_desejada;
	char nome_out[300];
	
	qtd_coord = atoi(argv[2]);
	itmin = atoi(argv[3]);
	qtd_linhas = atoi(argv[4]);

	if(itmin == -1)
	{
		int st1, st2, st3, st4, st5, st6, st7, st8, st9, st10;

		st1 = atoi(argv[5]);
		st2 = atoi(argv[6]);
		st3 = atoi(argv[7]);
		st4 = atoi(argv[8]);
		st5 = atoi(argv[9]);
		st6 = atoi(argv[10]);
		st7 = atoi(argv[11]);
		st8 = atoi(argv[12]);
		st9 = atoi(argv[13]);
		st10 = atoi(argv[14]);

		if(st1 > 0)
		{
			sprintf(nome_out,"%s_st1.txt", argv[15]);
			ler_coluna(argv[1], qtd_coord, qtd_linhas,nome_out,st1);
		}

		if(st2 > 0)
		{
			sprintf(nome_out,"%s_st2.txt", argv[15]);
			ler_coluna(argv[1], qtd_coord, qtd_linhas,nome_out,st2);
		}

		if(st3 > 0)
		{
			sprintf(nome_out,"%s_st3.txt", argv[15]);
			ler_coluna(argv[1], qtd_coord, qtd_linhas,nome_out,st3);
		}

		if(st4 > 0)
		{
			sprintf(nome_out,"%s_st4.txt", argv[15]);
			ler_coluna(argv[1], qtd_coord, qtd_linhas,nome_out,st4);
		}

		if(st5 > 0)
		{
			sprintf(nome_out,"%s_st5.txt", argv[15]);
			ler_coluna(argv[1], qtd_coord, qtd_linhas,nome_out,st5);
		}

		if(st6 > 0)
		{
			sprintf(nome_out,"%s_st6.txt", argv[15]);
			ler_coluna(argv[1], qtd_coord, qtd_linhas,nome_out,st6);
		}

		if(st7 > 0)
		{
			sprintf(nome_out,"%s_st7.txt", argv[15]);
			ler_coluna(argv[1], qtd_coord, qtd_linhas,nome_out,st7);
		}

		if(st8 > 0)
		{
			sprintf(nome_out,"%s_st8.txt", argv[15]);
			ler_coluna(argv[1], qtd_coord, qtd_linhas,nome_out,st8);
		}

		if(st9 > 0)
		{
			sprintf(nome_out,"%s_st9.txt", argv[15]);
			ler_coluna(argv[1], qtd_coord, qtd_linhas,nome_out,st9);
		}

		if(st10 > 0)
		{
			sprintf(nome_out,"%s_st10.txt", argv[15]);
			ler_coluna(argv[1], qtd_coord, qtd_linhas,nome_out,st10);
		}

		return;
	}
	
    ok_coordenadas = atoi(argv[5]);
	ok_vel_x = atoi(argv[6]);
	ok_vel_y = atoi(argv[7]);
	ok_vel_z = atoi(argv[8]);
	ok_vel_gerais = atoi(argv[9]);
    ok_desvio_padrao_x = atoi(argv[10]);
    ok_desvio_padrao_y = atoi(argv[11]);
    ok_desvio_padrao_z = atoi(argv[12]);
	ok_grafico_x = atoi(argv[13]);
	ok_grafico_y = atoi(argv[14]);
	ok_grafico_z = atoi(argv[15]);

    leitura_arquivo(argv[1], qtd_coord, itmin, qtd_linhas);
	
    if(ok_coordenadas == 1)
    {
        sprintf(nome_out,"%s/coordenadas/coordenadas", argv[16]);
        arq_saida_coordenadas(nome_out);
    }

    if(ok_vel_x == 1)
    {
        sprintf(nome_out,"%s/vel_media/vel_media_x", argv[16]);
	    arq_saida_vel_media_x(nome_out);
	}
    
    if(ok_vel_y == 1)
    {
        sprintf(nome_out,"%s/vel_media/vel_media_y", argv[16]);
	    arq_saida_vel_media_y(nome_out);
    }

    if(ok_vel_z == 1)
    {
        sprintf(nome_out,"%s/vel_media/vel_media_z", argv[16]);
        arq_saida_vel_media_z(nome_out);
    }
	    
    if(ok_vel_gerais == 1)
    {
        sprintf(nome_out,"%s/vel_media/vel_media", argv[16]);
        arq_saida_vel_media_todas(nome_out);
    }
	
	if(ok_desvio_padrao_x == 1) 
    {
        sprintf(nome_out, "%s/desvio_padrao/desvio_padrao_x", argv[16]);
        arq_saida_desvio_padrao(qtd_coord, qtd_linhas, itmin, argv[1], nome_out, 0, 1);
    }
		
	if(ok_desvio_padrao_y == 1)
    {
        sprintf(nome_out, "%s/desvio_padrao/desvio_padrao_y", argv[16]);
        arq_saida_desvio_padrao(qtd_coord, qtd_linhas, itmin, argv[1], nome_out, 0, 2);
    }
			
	if(ok_desvio_padrao_z == 1)
    {
        sprintf(nome_out, "%s/desvio_padrao/desvio_padrao_z", argv[16]);
        arq_saida_desvio_padrao(qtd_coord, qtd_linhas, itmin, argv[1], nome_out, 0, 3);
	}
	
	if(ok_grafico_x == 1)
    {
        sprintf(nome_out,"%s/vel_media_grafico/geracao_grafico_x", argv[16]);
        arq_saida_grafico_x(nome_out);
    }
	    

	if(ok_grafico_y == 1)
    {
        sprintf(nome_out,"%s/vel_media_grafico/geracao_grafico_y", argv[16]);
        arq_saida_grafico_y(nome_out);
    }
	    
	
	if(ok_grafico_z == 1)
    {
        sprintf(nome_out,"%s/vel_media_grafico/geracao_grafico_z", argv[16]);
        arq_saida_grafico_z(nome_out);
    }
	
	limpar_dados(inicio_colunas); //fazer limpeza ao final automaticameente
}

void arq_saida_coordenadas(char nome_out[250])
{
	struct _DADOS_ *aux;
	aux = inicio_colunas;
	FILE *arq;
	int i = 0;
	
	arq = fopen(nome_out,"w+b");	
	fprintf(arq,"x\ty\tz\t\n"); 
	while(aux != NULL)
	{
		fprintf(arq,"%d\t%f\t%f\t%f \n",i, aux->x, aux->y, aux->z);
		aux = aux->proxima;
		i++;
	}
	fclose(arq);
}

void arq_saida_vel_media_x(char nome_out[250]) //parametro passado para verificar se vai ou n�o ser chamado
{
	struct _DADOS_ *aux;
	aux = inicio_colunas;
	FILE *arq;
	
	arq = fopen(nome_out,"w+b");
	
	fprintf(arq,"Ux\n"); 
	while(aux != NULL)
	{
		fprintf(arq,"%.30lf \n",aux->soma_x);
		aux = aux->proxima;
	}
	fclose(arq);
}

void arq_saida_vel_media_y(char nome_out[250]) //parametro passado para verificar se vai ou n�o ser chamado
{
	struct _DADOS_ *aux;
	aux = inicio_colunas;
	FILE *arq;
	
	arq = fopen(nome_out,"w+b");
	
	fprintf(arq,"Uy\n"); 
	while(aux != NULL)
	{
		fprintf(arq,"%.30lf \n",aux->soma_y);
		aux = aux->proxima;
	}
	fclose(arq);
}

void arq_saida_vel_media_z(char nome_out[250]) //parametro passado para verificar se vai ou n�o ser chamado
{
	struct _DADOS_ *aux;
	aux = inicio_colunas;
	FILE *arq;
	
	arq = fopen(nome_out,"w+b");
	
	fprintf(arq,"Uz\n"); 
	while(aux != NULL)
	{
		fprintf(arq,"%.30lf \n",aux->soma_z);
		aux = aux->proxima;
	}
	fclose(arq);
}

void arq_saida_vel_media_todas(char nome_out[250])
{
	struct _DADOS_ *aux;
	aux = inicio_colunas;
	FILE *arq;
	
	arq = fopen(nome_out,"w+b");
	
	fprintf(arq,"Ux\tUy\tUz\t\n"); 
	while(aux != NULL)
	{
		fprintf(arq,"%.30lf\t%.30lf\t%.30lf\n",aux->soma_x,aux->soma_y,aux->soma_z);
		
		aux = aux->proxima;
	}
	fclose(arq);	
}

void arq_saida_desvio_padrao(int qtd_coord, int linhas, int itmin, char  nome_in[250], char nome_out[250], int l, int desejado)
{
	int escolha;
	
	for(escolha = 0; escolha < qtd_coord; escolha++)
	{
	desvio_padrao(qtd_coord, linhas, itmin, escolha, nome_in, nome_out, l, desejado);
	l++;
	}
}


void arq_saida_grafico_x(char nome_out[250])
{
	struct _DADOS_ *aux;
	aux = inicio_colunas;
	FILE *arq;
	int contador_y = 0, aux_cont_y = 0;
	
	arq = fopen(nome_out,"w+b");		
				
	while(aux != NULL)
		{
			fprintf(arq,"/%.30lf",aux->soma_x);
			aux = aux->proxima;
			contador_y++;
		}
		
		fprintf(arq,"/y");
		while(aux_cont_y < contador_y)
		{
			fprintf(arq,"/%d",aux_cont_y);
			aux_cont_y++;	
		}
		
		fclose(arq);
}

void arq_saida_grafico_y(char nome_out[250])
{
	struct _DADOS_ *aux;
	aux = inicio_colunas;
	FILE *arq;
	int contador_y = 0, aux_cont_y = 0;
	
	arq = fopen(nome_out,"w+b");		
				
	while(aux != NULL)
		{
			fprintf(arq,"/%.30lf",aux->soma_y);
			aux = aux->proxima;
			contador_y++;
		}
		
		fprintf(arq,"/y");
		while(aux_cont_y < contador_y)
		{
			fprintf(arq,"/%d",aux_cont_y);
			aux_cont_y++;	
		}
		
		fclose(arq);
}

void arq_saida_grafico_z(char nome_out[250])
{
	struct _DADOS_ *aux;
	aux = inicio_colunas;
	FILE *arq;
	int contador_y = 0, aux_cont_y = 0;
	
	arq = fopen(nome_out,"w+b");		
				
	while(aux != NULL)
		{
			fprintf(arq,"/%.30lf",aux->soma_z);
			aux = aux->proxima;
			contador_y++;
		}
		
		fprintf(arq,"/y");
		while(aux_cont_y < contador_y)
		{
			fprintf(arq,"/%d",aux_cont_y);
			aux_cont_y++;	
		}
		
		fclose(arq);
}

void ler_coluna(char  nome_in[250], int colunas, int linhas, char nome_out[250], int coluna_desejada)
{
	int i = 0, qtd_colunas = 0;
	FILE *arq, *arq_out;
	float x,y,z,tempo;
	double c_x, c_z, c_y;	
	
	arq = fopen(nome_in,"r+b");
	
	for( i = 0; i < colunas; i++) //passando quantas coordenadas tem
	{
		fscanf(arq,"%f %f %f", &x, &y, &z);
		printf("%d.\t%f\t%f\t%f \n",i, x, y, z);
	}
	
	arq_out = fopen(nome_out,"w+b");
	
	fprintf(arq_out,"Time\tUx\tUy\tUz\n"); 
	for(i = 0; i < linhas; i++) //le as linhas com os valores
	{
	fscanf(arq,"%f",&tempo); //le o tempo inicial

	fprintf(arq_out,"%f\t",tempo);	
	
		for(qtd_colunas = 0; qtd_colunas < colunas;  qtd_colunas++) //leitura das colunas
		{	
			fscanf(arq,"%lf %lf %lf",&c_x, &c_y, &c_z);	
			
			if(qtd_colunas == coluna_desejada)
			{		
				fprintf(arq_out,"%.30lf\t%.30lf\t%.30lf \n",c_x, c_y, c_z);
			}		
		}
	}
	
	fclose(arq);
	fclose(arq_out);
}

void desvio_padrao(int colunas, int linhas, int itmin, int escolha, char  nome_in[250], char nome_out[250], int l, int desejado)
{
	FILE *arq_out, *arq;
	double soma = 0, media = 0, c_x = 0, c_y = 0, c_z = 0, aux = 0;
	float sub = 0, tempo = 0, x = 0, y = 0, z = 0;
	int i = 0, qtd_colunas = 0;
	
	sub = linhas - itmin + 1; //n no desvio padr�o	
	
	arq = fopen(nome_in,"r+b");
	arq_out = fopen(nome_out,"a+b");
	
	if(l == 0)
	fprintf(arq_out,"Pontos\tDesvios\n");
	
	media = media_ponto(escolha,desejado);
	
	for(i = 0; i < colunas; i++) //LENDO AS COORDENADAS
	{
	fscanf(arq,"%f %f %f", &x, &y, &z);
	}
	
	switch(desejado)
	{
		case 1: //x
			
			for(i = 2; i < linhas + 2; i++) //le as linhas com os valores
			{
			fscanf(arq,"%f",&tempo); //le o tempo inicial			
			
				for(qtd_colunas = 0; qtd_colunas < colunas;  qtd_colunas++) //leitura das colunas
				{	
					if(i > itmin) //pular endere�os indesejados
					{
						fscanf(arq,"%lf %lf %lf",&c_x, &c_y, &c_z);	
						
						if(qtd_colunas == escolha) //entrega a coluna desejada
						{	
							aux = c_x - media;
							soma = soma + pow(aux, 2);
						}
						
					}else
					{
						fscanf(arq,"%lf %lf %lf",&c_x, &c_y, &c_z);	
					}		
				}
			}			
		break; 
		
		case 2: //y
			
			for(i = 2; i < linhas + 2; i++) //le as linhas com os valores
			{
			fscanf(arq,"%f",&tempo); //le o tempo inicial
			
			
				for(qtd_colunas = 0; qtd_colunas < colunas;  qtd_colunas++) //leitura das colunas
				{	
					if(i > itmin) //pular endere�os indesejados
					{
						fscanf(arq,"%lf %lf %lf",&c_x, &c_y, &c_z);	
						
						if(qtd_colunas == escolha) //entrega a coluna desejada
						{	
							aux = c_y - media;
							soma = soma + pow(aux, 2);
						}
						
					}else
					{
						fscanf(arq,"%lf %lf %lf",&c_x, &c_y, &c_z);	
					}		
				}
			}
		break;
		
		case 3: //z
			
			for(i = 2; i < linhas + 2; i++) //le as linhas com os valores
			{
			fscanf(arq,"%f",&tempo); //le o tempo inicial
			
			
				for(qtd_colunas = 0; qtd_colunas < colunas;  qtd_colunas++) //leitura das colunas
				{	
					if(i > itmin) //pular endere�os indesejados
					{
						fscanf(arq,"%lf %lf %lf",&c_x, &c_y, &c_z);	
						
						if(qtd_colunas == escolha) //entrega a coluna desejada
						{	
							aux = c_z - media;
							soma = soma + pow(aux, 2);
						}
						
					}else
					{
						fscanf(arq,"%lf %lf %lf",&c_x, &c_y, &c_z);	
					}		
				}
			}
		break;
	}
	
	soma = sqrt(soma / sub);
	
	fprintf(arq_out,"%d\t",escolha);
	fprintf(arq_out,"%.30lf\n",soma);
	
	fclose(arq);
	fclose(arq_out);
}

double media_ponto(int ponto, int decisao)
{
	struct _DADOS_ *aux;
	double resultado;
	
	aux = procurar_coluna(ponto);
	
	switch(decisao)
	{
		case 1:			
			resultado = aux->soma_x;
		break;
		
		case 2:
			resultado = aux->soma_y;
		break;
		
		case 3:
			resultado = aux->soma_z;
		break;
	}
	
	return resultado;
}


void leitura_arquivo(char nome_in[200], int qtd_coord, int itmin, int qtd_linhas) 
{
	FILE *arq;
	float x, y, z, tempo;
	int i, qtd_colunas, j = 0, inicio;
	double c_x, c_z, c_y, sub;
	struct _DADOS_ *aux;
	char teste = 'c';
	
	arq = fopen(nome_in,"r+b");
	
	inicio = ftell(arq);
	fread(&teste,8,1,arq);
	
	if(teste == '#')
	{
		printf("\nTEXTO SUJO, LIMPE O TEXTO!!\n");	
	}else
	{
	
		fseek(arq,inicio,SEEK_SET);
		
		while(!arq)
		{
			printf("\nArquivo vazio, tente novamente: ");
			
			printf("\nInforme o nome do arquivo a ser lido: ");
			scanf("%s",nome_in);
			arq = fopen(nome_in,"r+b");
		}
			
		for( i = 0; i < qtd_coord; i++) //passando quantas coordenadas tem
		{
		fscanf(arq,"%f %f %f", &x, &y, &z);
		
			if(j != 0)
			{
				aux->proxima = add_dados(i,x,y,z,0,0,0,aux); //adicionando as coordenadas na lista
				aux = aux->proxima;
			}else
			{
				inicio_colunas = add_dados(i,x,y,z,0,0,0,NULL); //criando lista inicial
				aux = inicio_colunas;
				j++;
			}
		}
		
		for(i = 2; i < qtd_linhas + 2; i++) //le as linhas com os valores
		{
			fscanf(arq,"%f",&tempo); //le o tempo inicial
			printf("Timestep: %f %c", tempo,13); //exibicao do tempo durante o processo
			
			for(qtd_colunas = 0; qtd_colunas < qtd_coord;  qtd_colunas++) //leitura das colunas
			{	
				if(i > itmin)
				{
					fscanf(arq,"%lf %lf %lf",&c_x, &c_y, &c_z);	
					adc_valor(c_x,c_y,c_z,qtd_colunas);				
				}
				else
				{				
					fscanf(arq,"%lf %lf %lf",&c_x, &c_y, &c_z);	
				}
				
			}
		}
		fclose(arq);
		
		fim_colunas = aux;
		
		sub = (qtd_linhas - itmin + 1);
	
		dividir(sub);
	}
	
	system("cls || clear");
}

void dividir(double x)
{
	struct _DADOS_ *aux;
	
	aux = inicio_colunas;
	
	while(aux != NULL)
	{
		aux->soma_x = aux->soma_x / x;
		aux->soma_y = aux->soma_y / x;
		aux->soma_z = aux->soma_z / x;	
		
		aux = aux->proxima;
	}
}

void adc_valor(double valor_x, double valor_y,double valor_z, int coluna) //funcao responsavel por realizar a soma dos valores
{
	struct _DADOS_ *aux;
	aux = inicio_colunas;
	
	aux = procurar_coluna(coluna);
	aux->soma_x += valor_x;
	aux->soma_y += valor_y;
	aux->soma_z += valor_z;
}

dados procurar_coluna(int coluna) //responsavel por direcionar para a coluna certa
{
	struct _DADOS_ *aux;
	aux = inicio_colunas;
	
	while(aux->coluna != coluna)
	{
		aux = aux->proxima;
	}
	
	return aux;
}

void limpar_dados(struct _DADOS_ *colunas)
{
	struct _DADOS_ *atual, *prox;
	
	if(colunas == NULL)
	{
		return;
	}
	
	atual = colunas->proxima;
	
	while(atual != NULL)
	{
		prox = atual->proxima;
		free(atual);
		atual = prox;
	}
}

dados add_dados(int coluna, float x, float y,float z,double soma_x,double soma_y,double soma_z,dados anterior)
{
	dados M = malloc(sizeof(struct _DADOS_));
	M->coluna = coluna;
	M->x = x;
	M->y = y;
	M->z = z;
	M->soma_x = soma_x;
	M->soma_y = soma_y;
	M->soma_z = soma_z;
	M->proxima = NULL;
	M->anterior = anterior;
	
	return M;
}
//FIM

