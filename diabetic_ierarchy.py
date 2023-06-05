"""
Иерархическая кластеризация (Hierarchical Clustering) - это метод кластеризации, который строит иерархическую структуру кластеров в виде дерева или дендрограммы. В отличие от метода K-средних или DBSCAN, иерархическая кластеризация не требует заранее заданного числа кластеров.

Основная идея иерархической кластеризации заключается в следующих шагах:

1. Начинается с каждой точки данных рассматриваемой как отдельный кластер.
2. Вычисляется попарное расстояние (или сходство) между кластерами или точками данных.
3. Два ближайших кластера (или точки данных) объединяются в новый кластер, создавая иерархию.
4. Шаги 2-3 повторяются, пока все кластеры не объединятся в один общий кластер или пока не будет достигнуто определенное условие остановки.
5. Полученная иерархия представляется в виде дерева или дендрограммы, где листья представляют собой отдельные точки данных, а внутренние узлы представляют собой объединение кластеров.
6. Иерархическая кластеризация может быть двух типов: агломеративная и дивизивная.

Агломеративная иерархическая кластеризация начинается с каждой точки данных в качестве отдельного кластера и последовательно объединяет ближайшие кластеры, пока не будет достигнуто условие остановки.
Дивизивная иерархическая кластеризация начинается с одного общего кластера и последовательно разделяет его на более мелкие кластеры, пока не будет достигнуто условие остановки.
Преимущества иерархической кластеризации включают возможность обнаружения кластеров произвольной формы, представление иерархической структуры кластеров и отсутствие необходимости заранее задавать число кластеров. Однако иерархическая кластеризация может иметь высокую вычислительную сложность и потреблять большой объем памяти при большом количестве точек данных.

При использовании иерархической кластеризации важно выбирать подходящую метрику расстояния и метод объединения кластеров, а также решать, на каком уровне дендрограммы следует проводить разделение на кластеры.
"""


import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score

# Загрузка датасета
data = pd.read_csv("diabetes.csv")

# Предварительная обработка данных
data.dropna(inplace=True)
data_norm = (data - data.mean()) / data.std()

# Кластеризация методом иерархической кластеризации
agglo = AgglomerativeClustering(n_clusters=3)
agglo.fit(data_norm)

# Оценка результатов
silhouette_avg = silhouette_score(data_norm, agglo.labels_)
print("Средний индекс силуэта:", silhouette_avg)