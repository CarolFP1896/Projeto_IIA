# importando bibliotecas necessarias
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import RandomizedSearchCV

# faz a leitura do arquivo .xlsx e armazena em data
dataset = pd.read_excel ('dataset.xlsx')
dataset.head()

# Substitui os valores negativo/not_detected e positivo/detected para 0 e 1, respectivamente
dataset['resultado do exame'] = dataset['resultado do exame'].replace({"negative": 0, "positive": 1})
dataset['CoronavirusNL63'] = dataset['CoronavirusNL63'].replace({"not_detected": 0, "detected": 1})
dataset['Coronavirus HKU1'] = dataset['Coronavirus HKU1'].replace({"not_detected": 0, "detected": 1})
dataset['Coronavirus229E'] = dataset['Coronavirus229E'].replace({"not_detected": 0, "detected": 1})
dataset['CoronavirusOC43'] = dataset['CoronavirusOC43'].replace({"not_detected": 0, "detected": 1})

# seleciona apenas os dados que vamos levar em conta para a análise
dataset = dataset[['resultado do exame', 'Patient addmited to regular ward (1=yes, 0=no)', 'Patient addmited to semi-intensive unit (1=yes, 0=no)', 
            'Patient addmited to intensive care unit (1=yes, 0=no)', 'CoronavirusNL63', 'Coronavirus HKU1', 'Coronavirus229E', 'CoronavirusOC43']]

# substitui todos os valores Nan por 0
dataset = dataset.replace(np.nan, 0)

# Estamos tentando prever se um paciente tem covid. Isso coincide com a coluna 'resultado do exame', que sera nossa variavel independente
X = dataset.drop('resultado do exame', axis=1)
y = dataset['resultado do exame']

# Implementa train-test-split para dividir os dados em dados de treinamento e dados de teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=66)

# Criando modelo de Random Forest
# Resultados ja conectados ao modelo para ver melhora de desempenho
rfc = RandomForestClassifier(n_estimators=1000, max_depth=140, max_features='auto') 
rfc.fit(X_train,y_train)
# predicoes
rfc_predict = rfc.predict(X_test)
# Executa a validacao cruzada para obter uma melhor visao geral dos resultados
rfc_cv_score = cross_val_score(rfc, X, y, cv=10, scoring='roc_auc')

# Funcao que imprime os resultados de classificacao
def classifierReport():
    # A Confusion Matrix e util para fornecer falsos positivos e falsos negativos
    print("=== Confusion Matrix ===")
    print(confusion_matrix(y_test, rfc_predict))
    print('\n')
    print("=== Classification Report ===")
    print(classification_report(y_test, rfc_predict))
    print('\n')
    print("=== All AUC Scores ===")
    print(rfc_cv_score)
    print('\n')
    print("=== Mean AUC Score ===")
    print("Mean AUC Score - Random Forest: ", rfc_cv_score.mean())

# Ajuste de hiperparametros
def bestParams():
    # Numero de arvores na Random Forest
    n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
    # Numero de recursos em cada divisao
    max_features = ['auto', 'sqrt']

    # Profundidade maxima
    max_depth = [int(x) for x in np.linspace(100, 500, num = 11)]
    max_depth.append(None)

    # Cria grade aleatoria
    random_grid = {
     'n_estimators': n_estimators,
     'max_features': max_features,
     'max_depth': max_depth
     }

    # Pesquisa aleatoria de parametros
    rfc_random = RandomizedSearchCV(estimator = rfc, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)

    # Ajusta o modelo
    rfc_random.fit(X_train, y_train)

    # Imprime os resultados
    print(rfc_random.best_params_)