"""
В коде было добавлено два сверточных слоя (Conv2D) для обработки изображений.

Сверточные слои являются ключевым элементом сверточных нейронных сетей (Convolutional Neural Networks, CNN) и позволяют модели извлекать локальные особенности изображений. Вот как они работают:

Первый сверточный слой:

model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
32 означает, что в слое будет 32 фильтра. Каждый фильтр будет выделять различные локальные особенности в изображении.
(3, 3) определяет размер окна свертки, которое перемещается по изображению для выделения признаков.
activation='relu' указывает на использование функции активации ReLU после операции свертки.
input_shape=(28, 28, 1) задает форму входных данных. Здесь (28, 28, 1) означает изображение размером 28x28 пикселей с одним каналом (оттенки серого).


Второй сверточный слой:

model.add(Conv2D(64, (3, 3), activation='relu'))
64 указывает на использование 64 фильтров во втором сверточном слое.
Остальные параметры остаются такими же, как и в первом сверточном слое.
Сверточные слои применяют операцию свертки к входным данным с помощью фильтров, что позволяет выявить локальные особенности, такие как границы, текстуры или шаблоны в изображении. Функция активации ReLU активирует нейроны, сохраняя только положительные значения и игнорируя отрицательные, что помогает в обеспечении нелинейности и усиливает способность модели выявлять сложные признаки.

Увеличение количества сверточных слоев, фильтров или изменение их параметров может дополнительно повысить способность модели распознавать сложные признаки и улучшить точность классификации.
"""


import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
from keras.utils import np_utils

# Устанавливаем seed для повторяемости результатов
np.random.seed(42)

# Загружаем данные
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Преобразование размерности изображений и нормализация данных
X_train = X_train.reshape(60000, 28, 28, 1).astype('float32') / 255
X_test = X_test.reshape(10000, 28, 28, 1).astype('float32') / 255

# Преобразуем метки в категории
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

# Создаем последовательную модель
model = Sequential()

# Добавляем сверточные слои
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

# Преобразование в одномерный вектор
model.add(Flatten())

# Добавляем полносвязные слои
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

# Компилируем модель
optimizer = Adam(learning_rate=0.001)
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

print(model.summary())

# Добавляем раннюю остановку (Early Stopping)
early_stopping = EarlyStopping(monitor='val_accuracy', patience=5)

# Обучаем сеть
model.fit(X_train, Y_train, batch_size=128, epochs=30, validation_split=0.2, verbose=2, callbacks=[early_stopping])

# Оцениваем качество обучения сети на тестовых данных
scores = model.evaluate(X_test, Y_test, verbose=0)
print("Точность работы на тестовых данных: %.2f%%" % (scores[1] * 100)) # 99.17% точность