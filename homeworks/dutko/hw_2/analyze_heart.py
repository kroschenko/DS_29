"""
Анализ датасета Heart Disease (UCI Cleveland)
Выполнение 6 заданий по обработке и визуализации медицинских данных.

Задания:
1. Загрузка и информация о данных
2. Столбчатая диаграмма распределения пациентов
3. Диаграмма рассеяния thalach от age
4. One-Hot Encoding признака 'sex'
5. Средний уровень холестерина по группам
6. Нормализация признаков (StandardScaler)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import os


# ==========================================
# ВСПОМОГАТЕЛЬНАЯ ФУНКЦИЯ ДЛЯ ГРАФИКОВ
# ==========================================
def add_value_labels(ax, bars, fmt="{:.0f}"):
    """Добавляет текстовые подписи значений на столбцах графика."""
    for bar in bars:
        height = bar.get_height()
        ax.annotate(
            fmt.format(height),
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 5),  # смещение вверх на 5 пикселей
            textcoords="offset points",
            ha="center",
            va="bottom",
            fontsize=11,
            fontweight="bold",
            color="black",
        )


# ==========================================
# 1. ЗАГРУЗКА ДАННЫХ
# ==========================================
# Автоматически определяем путь к файлу рядом со скриптом
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_NAME = os.path.join(SCRIPT_DIR, "heart.csv")

print("=" * 60)
print("1. ИНФОРМАЦИЯ О ДАННЫХ")
print("=" * 60)

try:
    # na_values="?" на случай, если в данных есть пропуски, обозначенные знаком вопроса
    df = pd.read_csv(FILE_NAME, na_values="?")
    print(f"✅ Файл '{FILE_NAME}' успешно загружен!\n")
except FileNotFoundError:
    print(f"❌ Ошибка: файл '{FILE_NAME}' не найден.")
    print(f"💡 Убедитесь, что файл лежит в той же папке: {SCRIPT_DIR}")
    exit()
except Exception as e:
    print(f"❌ Произошла ошибка при чтении файла: {e}")
    exit()

print(f"Размер датасета: {df.shape[0]} строк, {df.shape[1]} столбцов")
print("\nПервые 5 строк:")
print(df.head())
print("\nОсновная информация:")
print(df.info())
print("\nСтатистическое описание:")
print(df.describe().round(2))
print("\nПропуски в данных:")
print(df.isnull().sum())

# Удаляем пропуски, если они есть
df = df.dropna().reset_index(drop=True)
print(f"\nРазмер после очистки от пропусков: {df.shape[0]} строк")


# ==========================================
# 2. СТОЛБЧАТАЯ ДИАГРАММА (Здоровые vs Больные)
# ==========================================
print("\n" + "=" * 60)
print("2. РАСПРЕДЕЛЕНИЕ ПАЦИЕНТОВ")
print("=" * 60)

# Используем numpy для быстрой бинаризации и подсчета
target_array = df["target"].values
df["target_binary"] = np.where(target_array == 0, 0, 1)

healthy_count = np.sum(df["target_binary"].values == 0)
sick_count = np.sum(df["target_binary"].values == 1)

print(f"Здоровых пациентов (target=0): {healthy_count}")
print(f"Больных пациентов (target=1): {sick_count}")

plt.figure(figsize=(8, 6))
bars_2 = plt.bar(
    ["Здоровые", "Больные"],
    [healthy_count, sick_count],
    color=["#4CAF50", "#F44336"],
    alpha=0.8,
    edgecolor="black",
)
add_value_labels(plt.gca(), bars_2)
plt.title("Распределение пациентов по наличию заболевания сердца")
plt.ylabel("Количество пациентов")
plt.grid(axis="y", alpha=0.3, linestyle="--")
plt.tight_layout()
plt.show()


# ==========================================
# 3. ДИАГРАММА РАССЕЯНИЯ (thalach от age)
# ==========================================
print("\n" + "=" * 60)
print("3. ДИАГРАММА РАССЕЯНИЯ: Максимальный пульс от возраста")
print("=" * 60)

# Извлекаем numpy-массивы для эффективной передачи в matplotlib
age_arr = df["age"].values
thalach_arr = df["thalach"].values
target_arr = df["target_binary"].values

plt.figure(figsize=(10, 6))
plt.scatter(
    age_arr,
    thalach_arr,
    c=target_arr,
    cmap="RdYlGn",  # Красный (1=болен) - Зеленый (0=здоров)
    alpha=0.7,
    edgecolors="black",
    linewidth=0.5,
)
plt.xlabel("Возраст (age)")
plt.ylabel("Максимальный пульс (thalach)")
plt.title("Зависимость максимального пульса от возраста")
cbar = plt.colorbar()
cbar.set_label("Статус: 0 = Здоров, 1 = Болен")
plt.grid(alpha=0.3, linestyle="--")
plt.tight_layout()
plt.show()


# ==========================================
# 4. ONE-HOT ENCODING ДЛЯ ПРИЗНАКА 'sex'
# ==========================================
print("\n" + "=" * 60)
print("4. ПРЕОБРАЗОВАНИЕ ПРИЗНАКА 'sex' (One-Hot Encoding)")
print("=" * 60)

# Преобразуем 0 и 1 в строки для наглядности
df["sex"] = df["sex"].map({0: "female", 1: "male"})
print("Распределение пола:")
print(df["sex"].value_counts())

# Применяем One-Hot Encoding через sklearn (drop="first" избегает мультиколлинеарности)
encoder = OneHotEncoder(sparse_output=False, drop="first")
sex_encoded = encoder.fit_transform(df[["sex"]])

# Создаем DataFrame с новым признаком и объединяем
sex_df = pd.DataFrame(sex_encoded, columns=["sex_male"], index=df.index, dtype=int)
df = pd.concat([df.drop("sex", axis=1), sex_df], axis=1)

print("\nРезультат One-Hot Encoding (первые 5 строк столбца 'sex_male'):")
print(sex_df.head())
print("\nИтоговые столбцы датасета:", df.columns.tolist())


# ==========================================
# 5. СРЕДНИЙ УРОВЕНЬ ХОЛЕСТЕРИНА
# ==========================================
print("\n" + "=" * 60)
print("5. СРЕДНИЙ УРОВЕНЬ ХОЛЕСТЕРИНА (chol)")
print("=" * 60)

# Используем numpy-маски для быстрой фильтрации
chol_arr = df["chol"].values
target_bin_arr = df["target_binary"].values

healthy_mask = target_bin_arr == 0
sick_mask = target_bin_arr == 1

avg_chol_healthy = np.mean(chol_arr[healthy_mask])
avg_chol_sick = np.mean(chol_arr[sick_mask])

print(f"Средний холестерин у здоровых: {avg_chol_healthy:.2f} мг/дл")
print(f"Средний холестерин у больных:  {avg_chol_sick:.2f} мг/дл")
print(f"Разница: {np.abs(avg_chol_sick - avg_chol_healthy):.2f} мг/дл")

plt.figure(figsize=(8, 6))
bars_5 = plt.bar(
    ["Здоровые", "Больные"],
    [avg_chol_healthy, avg_chol_sick],
    color=["#4CAF50", "#F44336"],
    alpha=0.8,
    edgecolor="black",
)
add_value_labels(plt.gca(), bars_5, fmt="{:.1f}")
plt.title("Средний уровень холестерина по группам")
plt.ylabel("Холестерин (мг/дл)")
plt.grid(axis="y", alpha=0.3, linestyle="--")
plt.tight_layout()
plt.show()


# ==========================================
# 6. НОРМАЛИЗАЦИЯ ПРИЗНАКОВ (StandardScaler)
# ==========================================
print("\n" + "=" * 60)
print("6. НОРМАЛИЗАЦИЯ ПРИЗНАКОВ (StandardScaler)")
print("=" * 60)

features_to_normalize = ["age", "trestbps", "chol", "thalach"]
scaler = StandardScaler()

df_normalized = df.copy()
df_normalized[features_to_normalize] = scaler.fit_transform(df[features_to_normalize])

print("\nОригинальные данные (первые 3 строки):")
print(df[features_to_normalize].head(3))
print("\nНормализованные данные (первые 3 строки):")
print(df_normalized[features_to_normalize].head(3).round(4))
print("\nСтатистика нормализованных данных (среднее ≈ 0, станд. отклонение ≈ 1):")
print(df_normalized[features_to_normalize].describe().round(4))


# ==========================================
# ЗАВЕРШЕНИЕ
# ==========================================
print("\n" + "=" * 60)
print("✅ ВСЕ 6 ЗАДАНИЙ ВЫПОЛНЕНЫ УСПЕШНО!")
print("=" * 60)
