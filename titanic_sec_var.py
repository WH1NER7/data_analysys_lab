import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Шаг 1. Загрузка и предварительная обработка данных
df = pd.read_csv('titanic.csv')

# Удаление ненужных признаков
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)

# Заполнение пропущенных значений возраста медианами
df['Age'].fillna(df['Age'].median(), inplace=True)

# Преобразование категориальных признаков в числовые
df['Sex'] = df['Sex'].map({'female': 0, 'male': 1})

# Создание дамми-переменных для порта посадки
df = pd.get_dummies(df, columns=['Embarked'])

# Шаг 2. Создание модели и обучение
X = df.drop('Survived', axis=1)
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Масштабирование данных
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Шаг 3. Предсказание и оценка модели
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Точность модели на тестовых данных: {:.2%}".format(accuracy))