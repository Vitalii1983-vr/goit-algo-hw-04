import timeit
import random

# Реалізація сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:  # Базовий випадок рекурсії: масив з 0 або 1 елемента вже відсортований
        return arr
    mid = len(arr) // 2  # Знаходження середини масиву для поділу на дві частини
    left = merge_sort(arr[:mid])  # Рекурсивне сортування лівої половини
    right = merge_sort(arr[mid:])  # Рекурсивне сортування правої половини
    return merge(left, right)  # Злиття двох відсортованих половин

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):  # Злиття двох масивів в один відсортований
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])  # Додавання залишків лівої половини (якщо є)
    result.extend(right[j:])  # Додавання залишків правої половини (якщо є)
    return result

# Реалізація сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):  # Прохід по всіх елементах масиву, починаючи з другого
        key = arr[i]  # Поточний елемент, який потрібно вставити в відсортовану частину
        j = i - 1
        while j >= 0 and key < arr[j]:  # Пошук правильного місця для поточного елемента
            arr[j + 1] = arr[j]  # Зсув елементів вправо
            j -= 1
        arr[j + 1] = key  # Вставка поточного елемента на знайдене місце
    return arr

# Функція для використання вбудованої функції sorted (Timsort)
def timsort(arr):
    return sorted(arr)  # Використання вбудованої функції sorted, яка реалізує Timsort

# Генерація випадкових даних для тестування
def generate_data(size):
    return [random.randint(0, size) for _ in range(size)]  # Генерація списку випадкових чисел заданого розміру

# Функція для заміру часу виконання
def measure_time(func, data):
    timer = timeit.Timer(lambda: func(data.copy()))  # Створення таймера для вимірювання часу виконання функції
    n_runs = 3  # Кількість запусків для вимірювання часу
    return min(timer.repeat(repeat=n_runs, number=1))  # Повернення мінімального часу виконання з кількох запусків

# Розміри масивів для тестування (скорочені для прискорення)
sizes = [100, 1000, 5000]

# Результати
results = {
    'Merge Sort': [],  # Збереження результатів для сортування злиттям
    'Insertion Sort': [],  # Збереження результатів для сортування вставками
    'Timsort': []  # Збереження результатів для Timsort
}

# Тестування і замір часу виконання
for size in sizes:
    data = generate_data(size)  # Генерація випадкового масиву даного розміру
    results['Merge Sort'].append(measure_time(merge_sort, data))  # Заміри часу для сортування злиттям
    results['Insertion Sort'].append(measure_time(insertion_sort, data))  # Заміри часу для сортування вставками
    results['Timsort'].append(measure_time(timsort, data))  # Заміри часу для Timsort

import pandas as pd
import matplotlib.pyplot as plt

# Створення DataFrame для результатів
df = pd.DataFrame(results, index=sizes)  # Створення таблиці з результатами замірів часу
print(df)  # Виведення таблиці результатів

# Побудова графіку
plt.figure(figsize=(10, 6))  # Встановлення розміру графіку
plt.plot(df.index, df['Merge Sort'], label='Merge Sort')  # Додавання лінії для сортування злиттям
plt.plot(df.index, df['Insertion Sort'], label='Insertion Sort')  # Додавання лінії для сортування вставками
plt.plot(df.index, df['Timsort'], label='Timsort')  # Додавання лінії для Timsort
plt.xlabel('Input size')  # Підпис осі X
plt.ylabel('Time (seconds)')  # Підпис осі Y
plt.title('Comparison of Sorting Algorithms')  # Заголовок графіку
plt.legend()  # Додавання легенди
plt.grid(True)  # Додавання сітки на графік
plt.show()  # Відображення графіку

