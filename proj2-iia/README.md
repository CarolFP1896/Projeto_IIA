----------------------------------------------------------------
------------------------ PROJETO 2 - IIA -----------------------
----------------------------------------------------------------
-- Universidade de Brasília ------------------------------------
-- Departamento de Ciência da Computação -----------------------
-- Prof. Díbio -------------------------------------------------
----------------------------------------------------------------
-- Aluna: Caroline Ferreira Pinto ------------------------------
-- Matrícula: 16/0067766 ---------------------------------------
----------------------------------------------------------------

COMENTÁRIOS DO ARQUIVO main.py:

# importa modulos e pacotes necessarios
# funcao que imprime o menu da analise de dados e retorna os graficos gerados em cada resultado
# se opcao for 1, chama a funcao que mostra plot dos resultados dos exames
# se opcao for 2, chama funcao que mostra plot dos pacientes infectados por alas
# se opcao for 3, chama funcao que mostra plot dos pacientes infectados por cada variante do virus
# se opcao for 4, chama a funcao que imprime no terminal o total de resultados de exames
# se opcao for 5, sai do programa
# funcao principal que imprime um menu principal
# se opcao for 1, chama a funcao que imprime o menu de analise dos dados
# se opcao for 2, chama a funcao que imprime no terminal o relatorio de classificao da random forest gerada
# se opcao for 3, chama a funcao que imprime no terminal os resultados dos melhores parametros da random forest gerada
# se opcao for 4, sai do programa

COMENTÁRIOS DO ARQUIVO dataAnalysis.py:
 
# importa modulos e pacotes necessarios
# faz a leitura do arquivo .xlsx e armazena em data
# Substitui os valores negativo/not_detected e positivo/detected para 0 e 1, respectivamente
# seleciona apenas os dados que vamos levar em conta para a análise
# calcula o numero de resultados positivos e negativos e retorna o total de resultados
# calcula o numero de pacientes internados por ala
# calcula o numero de infectados por cada variante do virus 
# Grafico gerado para demonstrar o numero de pacientes com resultados positivos e negativos
# gera o grafico
# Grafico gerado para demonstrar o numero de pacientes infectados por alas
# gera o grafico
# Grafico gerado para demonstrar o numero de pacientes infectados de acordo com cada variante do vírus
# gera o grafico

COMENTÁRIOS DO ARQUIVO randomForest.py:

# importando bibliotecas necessarias
# faz a leitura do arquivo .xlsx e armazena em data
# Substitui os valores negativo/not_detected e positivo/detected para 0 e 1, respectivamente
# seleciona apenas os dados que vamos levar em conta para a análise
# substitui todos os valores Nan por 0
# A coluna 'resultado do exame' sera nossa variavel independente, pois estamos tentando prever se um paciente tem covid
# Implementa train-test-split para dividir os dados em dados de treinamento e dados de teste
# Criando modelo de Random Forest
# Resultados ja conectados ao modelo para ver melhora de desempenho
# predicoes
# Executa a validacao cruzada para obter uma melhor visao geral dos resultados
# Funcao que imprime os resultados de classificacao
# A Confusion Matrix e util para fornecer falsos positivos e falsos negativos
# Ajuste de hiperparametros
# Numero de arvores na Random Forest
# Numero de recursos em cada divisao
# Profundidade maxima
# Cria grade aleatoria
# Pesquisa aleatoria de parametros
# Ajusta o modelo
# Imprime os resultados
