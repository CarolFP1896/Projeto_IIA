from read import virus, result, alas, infected
import os

def analysis():
    a = 0
    while a != 5:
        print ("""
            --------------------------MENU---------------------------
            1. Resultado dos exames
            2. Número de pacientes internados por alas
            3. Número de pacientes infectados por variantes do vírus
            4. Total de Infectados
            5. Exit/Quit
            ---------------------------------------------------------
            """)

        a = input('Digite a opção desejada: ')

        if a=="1": 
            os.system('cls' if os.name == 'nt' else 'clear')
            result() 
        elif a=="2":
            os.system('cls' if os.name == 'nt' else 'clear')
            alas()
        elif a=="3":
            os.system('cls' if os.name == 'nt' else 'clear')
            virus()
        elif a=="4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n O total de infectados é: \n', infected())
        elif a=="5":
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
        elif a !="":
            print('\n Opção inválida! Digite novamente...') 

if __name__ == "__main__":
    a = 0
    while a != 5:
        print ("""
            -------------------- MENU PRINCIPAL ---------------------
            1. Análise de dados 
            2. Número de pacientes internados por alas
            3. Número de pacientes infectados por variantes do vírus
            4. Total de Infectados
            5. Exit/Quit
            ---------------------------------------------------------
            """)

        a = input('Digite a opção desejada: ')

        if a=="1": 
            os.system('cls' if os.name == 'nt' else 'clear')
            analysis() 
        elif a=="2":
            os.system('cls' if os.name == 'nt' else 'clear')
            alas()
        elif a=="3":
            os.system('cls' if os.name == 'nt' else 'clear')
            virus()
        elif a=="4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\n O total de infectados é: \n', infected())
        elif a=="5":
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
        elif a !="":
            print('\n Opção inválida! Digite novamente...') 
