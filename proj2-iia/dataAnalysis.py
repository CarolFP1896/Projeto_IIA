# importa modulos e pacotes necessarios
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# faz a leitura do arquivo .xlsx e armazena em data
data = pd.read_excel ('dataset.xlsx')

# Substitui os valores negativo/not_detected e positivo/detected para 0 e 1, respectivamente
data['resultado do exame'] = data['resultado do exame'].replace({"negative": 0, "positive": 1})
data['CoronavirusNL63'] = data['CoronavirusNL63'].replace({"not_detected": 0, "detected": 1})
data['Coronavirus HKU1'] = data['Coronavirus HKU1'].replace({"not_detected": 0, "detected": 1})
data['Coronavirus229E'] = data['Coronavirus229E'].replace({"not_detected": 0, "detected": 1})
data['CoronavirusOC43'] = data['CoronavirusOC43'].replace({"not_detected": 0, "detected": 1})

# seleciona apenas os dados que vamos levar em conta para a análise
data = data[['resultado do exame', 'Patient addmited to regular ward (1=yes, 0=no)', 'Patient addmited to semi-intensive unit (1=yes, 0=no)', 
            'Patient addmited to intensive care unit (1=yes, 0=no)', 'CoronavirusNL63', 'Coronavirus HKU1', 'Coronavirus229E', 'CoronavirusOC43']]

# calcula o numero de resultados positivos e negativos e retorna o total de resultados
def infected():
    positive = (data['resultado do exame'] == 1).sum(axis = 0)
    negative = (data['resultado do exame'] == 0).sum(axis = 0)
    total = (positive + negative)
    
    return total

# calcula o numero de pacientes internados por ala
regular = (data['Patient addmited to regular ward (1=yes, 0=no)'] == 1).sum(axis = 0)
semi = (data['Patient addmited to semi-intensive unit (1=yes, 0=no)'] == 1).sum(axis = 0)
intensive = (data['Patient addmited to intensive care unit (1=yes, 0=no)'] == 1).sum(axis = 0)

# calcula o numero de infectados por cada variante do virus 
coronaNL63 = (data['CoronavirusNL63'] == 1).sum(axis = 0)
coronaHKU1 = (data['Coronavirus HKU1'] == 1).sum(axis = 0)
corona229E = (data['Coronavirus229E'] == 1).sum(axis = 0)
coronaOC43 = (data['CoronavirusOC43'] == 1).sum(axis = 0)

# Grafico gerado para demonstrar o numero de pacientes com resultados positivos e negativos
def result():
    count_result = data['resultado do exame'].value_counts().values
    result = data['resultado do exame'].value_counts().index

    plt.figure(figsize = (10, 5))
    plt.pie(count_result, 
            labels = list(result),  
            colors = ["#20257c", "#424ad1", "#6a8ee8", "#66bbe2", "#66dee2", "#6ce2cb", "#6ad187", "#3b7f5b"],
            labeldistance = 1.1,
            explode = [0, 0],
            wedgeprops = {"ec": "k"}, 
            textprops = {"fontsize": 15}, 
            )
    plt.axis("equal")
    plt.title("Resultados dos exames")
    plt.legend(['Negative', 'Positive'])
    # gera o grafico
    plt.show()

# Grafico gerado para demonstrar o numero de pacientes infectados por alas
def alas():
    plt.figure(figsize = (10, 5))
    x = ['Regular', 'Semi-intensive', 'Intensive']
    y = [regular, semi, intensive]
    plt.barh(x, y)

    for index, value in enumerate(y):
        plt.text(value, index, str(value))
    # gera o grafico
    plt.show()

# Grafico gerado para demonstrar o numero de pacientes infectados de acordo com cada variante do vírus
def virus():
    unit =[["Virus variants", coronaNL63, coronaHKU1, corona229E, coronaOC43]]
    data = pd.DataFrame(unit, columns=["Infected patients","NL63","HKU1","229E", "OC43"])
    data.plot(kind="barh", figsize = (10, 5))
    plt.xlabel('Virus variants')
    plt.ylabel('Infected patients')
    # gera o grafico
    plt.show()