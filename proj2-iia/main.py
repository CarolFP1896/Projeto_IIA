# importa modulos e pacotes necessarios
from dataAnalysis import virus, result, alas, infected
from randomForest import classifierReport, bestParams
import os

# funcao que imprime o menu da analise de dados e retorna os graficos gerados em cada resultado
def analysis():
    a = 0
    while a != 5:
        print ("""
            -------------------ANÁLISE DOS DADOS---------------------
            1. Resultado dos exames
            2. Número de pacientes internados por alas
            3. Número de pacientes infectados por variantes do vírus
            4. Total de resultados
            5. Exit/Quit
            ---------------------------------------------------------
            """)

        a = input('Digite a opção desejada: ')

        if a=="1": 
            # se opcao for 1, chama a funcao que mostra plot dos resultados dos exames
            os.system('cls' if os.name == 'nt' else 'clear')
            result() 
        elif a=="2":
            # se opcao for 2, chama funcao que mostra plot dos pacientes infectados por alas
            os.system('cls' if os.name == 'nt' else 'clear')
            alas()
        elif a=="3":
            # se opcao for 3, chama funcao que mostra plot dos pacientes infectados por cada variante do virus
            os.system('cls' if os.name == 'nt' else 'clear')
            virus()
        elif a=="4":
            # se for 4, chama a funcao que imprime no terminal o total de resultados de exames
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n O total de resultados é: \n', infected())
        elif a=="5":
            # se opcao for 5, sai do programa
            os.system('cls' if os.name == 'nt' else 'clear')
            main()
        elif a !="":
            print('\n Opção inválida! Digite novamente...') 

# funcao principal que imprime um menu principal
def main():
    a = 0
    while a != 5:
        print ("""
            -------------------- MENU PRINCIPAL ---------------------
            1. Análise de dados 
            2. Relatório de classificação (classifier)
            3. Ajuste de hiperparâmetros (best params)
            4. Exit/Quit
            ---------------------------------------------------------
            """)

        a = input('Digite a opção desejada: ')

        if a=="1": 
            # se opcao for 1, chama a funcao que imprime o menu de analise dos dados
            os.system('cls' if os.name == 'nt' else 'clear')
            analysis() 
        elif a=="2":
            # se opcao for 2, chama a funcao que imprime no terminal o relatorio de classificao da random forest gerada
            os.system('cls' if os.name == 'nt' else 'clear')
            classifierReport()
        elif a=="3":
            # se opcao for 3, chama a funcao que imprime no terminal os resultados dos melhores parametros da random forest gerada
            os.system('cls' if os.name == 'nt' else 'clear')
            bestParams()
        elif a=="4":
            # se opcao for 4, sai do programa
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
        elif a !="":
            print('\n Opção inválida! Digite novamente...') 

main()