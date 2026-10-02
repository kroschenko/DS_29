import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

df=pd.read_csv('heart.csv')
# print(df.head())
# print(df.isna().sum()) !Пустых строк не обнаружено!

tgt_counts = df['target'].value_counts()
# построение графика
tgt_counts.plot(kind='bar', figsize=(8, 5), color=['green', 'red'])
plt.xlabel('Наличие болезни')
plt.ylabel('Количество людей')
plt.title('Распределение больных и здоровых')
plt.xticks(ticks=[0, 1], labels=['Здоровые', 'Больные'], rotation=0)
plt.show()

# пункт 3, диаграмма рассеивания
df.plot(kind='scatter', x='age', y='thalach', c='target', colormap='coolwarm', figsize=(9, 6))
plt.xlabel('Возраст')
plt.ylabel('Максимальный пульс')
plt.title('Возраст и пульс (синие — здоровые, красные — больные)')
plt.show()

# замена пола и one hot encoding
df['sex'] = df['sex'].map({0: 'female', 1: 'male'})
df = pd.get_dummies(df, columns=['sex'])
# print(df.head())

# подсчет холестерина
chol_avg = df.groupby('target')['chol'].mean()
print("Средний уровень холестерина:")
print(f'У здоровых пациентов (0): {chol_avg[0]:.2f} мг/дл')
print(f'У больных пациентов (1): {chol_avg[1]:.2f} мг/дл\n')

# нормализация данных
scaler = StandardScaler()
features_to_scale = ['age', 'trestbps', 'chol', 'thalach']
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])
print(df[features_to_scale].head())



# пробы предсказания с помощью регрессии
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# деление данных на признаки (X) и целевую переменную (y)
# убрал из X столбец target
X = df.drop(columns=['target'])
y = df['target']
# разбиение выборки на обучающую(80%) и тестовую(20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# обучение лог-регресии
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)  # Вот тут происходит магия обучения!
# насколько хорошо модель научилась предсказывать
y_pred = model.predict(X_test)
# точность
accuracy = accuracy_score(y_test, y_pred)
print(f'\nТочность модели на тестовых данных: {accuracy * 100:.3f}%')
# отчет о качестве предсказаний
report_dict = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(report_dict).transpose()
print('\nДетальный отчет о метриках:')

print(report_df.round(2))
