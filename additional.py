import random  # Імпорт модуля для генерації випадкових чисел

# Крок 1: Читання тексту з файлу
with open('J. K. Rowling - Harry Potter 1.txt', 'r') as file:
    text = file.read()  # Прочитати весь файл

# Крок 2: Обробка тексту
text = text.lower()  # Перетворити весь текст на маленькі літери
words = text.split()  # Розділити текст на слова

# Крок 3: Створення словника слів
word_dict = {}  # Створити порожній словник
for i in range(len(words) - 1):  # Проходимо по всіх словах, окрім останнього
    current_word = words[i]  # Поточне слово
    next_word = words[i + 1]  # Наступне слово
    if current_word not in word_dict:  # Якщо поточного слова ще немає в словнику
        word_dict[current_word] = []  # Додаємо його зі значенням порожнього списку
    word_dict[current_word].append(next_word)  # Додаємо наступне слово до списку

# Крок 4: Генерація тексту
generated_text = []  # Список для збереження згенерованих слів
first_word = random.choice(list(word_dict.keys()))  # Випадковий вибір першого слова
generated_text.append(first_word)  # Додаємо перше слово до згенерованого тексту

current_word = first_word  # Починаємо з першого слова
for word in range(199):  # Генеруємо ще 199 слів
    if current_word in word_dict:  # Якщо поточне слово є в словнику
        next_word = random.choice(word_dict[current_word])  # Вибираємо випадкове наступне слово
        generated_text.append(next_word)  # Додаємо наступне слово до згенерованого тексту
        current_word = next_word  # Переходимо до наступного слова
    else:  # Якщо поточного слова немає в словнику
        break  # Зупиняємо генерацію слів

# Крок 5: Виведення згенерованого тексту
print(' '.join(generated_text))  # Об'єднуємо список слів у рядок та виводимо його
