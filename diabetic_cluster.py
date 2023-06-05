"""
Кластеризация методом DBSCAN (Density-Based Spatial Clustering of Applications with Noise) - это алгоритм кластеризации,
который основывается на плотности распределения объектов в пространстве данных.
 DBSCAN способен обнаруживать кластеры произвольной формы и учитывать шумовые точки, не требуя заранее заданного числа кластеров.

Основная идея метода DBSCAN заключается в следующих шагах:

1. Задается два параметра: eps (epsilon) - радиус окрестности, в пределах которого ищутся соседние точки,
и min_samples - минимальное количество точек в окрестности, чтобы считаться ядром кластера.

2. Выбирается случайная нерассмотренная точка и определяется, является ли она ядром кластера, т.е. имеет достаточное количество соседей в пределах радиуса eps.

3. Если точка является ядром кластера, то все достижимые точки в пределах eps добавляются в кластер.
Достижимые точки - это точки, которые могут быть достигнуты из ядра кластера последовательностью переходов по соседним точкам.
4. Шаги 2 и 3 повторяются для всех нерассмотренных точек, пока не будут обработаны все точки.

5. Повторяются шаги 2-4 для следующего нерассмотренного ядра кластера, если таковые остались.

6. Результатом работы алгоритма является разбиение данных на кластеры и метку "шум" для выбросов, которые не принадлежат ни одному кластеру.
Преимущества DBSCAN включают возможность обнаружения кластеров произвольной формы, робастность к выбросам и отсутствие необходимости заранее задавать число кластеров. Однако DBSCAN может иметь сложность в выборе оптимальных значений eps и min_samples для конкретного набора данных.

DBSCAN также имеет некоторые ограничения, такие как чувствительность к настройкам параметров и проблемы с масштабированием признаков. Поэтому важно тщательно подбирать параметры eps и min_samples и проводить предварительную обработку данных, чтобы достичь оптимальных результатов при использовании DBSCAN.
"""

import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

# Загрузка датасета
data = pd.read_csv("diabetes.csv")

# Предварительная обработка данных
data.dropna(inplace=True)

# Масштабирование данных
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Кластеризация методом DBSCAN
dbscan = DBSCAN(eps=0.7, min_samples=4)
labels = dbscan.fit_predict(data_scaled)

# Проверка наличия нескольких кластеров
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
if n_clusters > 1:
    # Оценка результатов
    silhouette_avg = silhouette_score(data_scaled, labels)
    print("Средний индекс силуэта:", silhouette_avg)
else:
    print("Недостаточно кластеров для оценки")
