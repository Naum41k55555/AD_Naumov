import requests

# Загружаем файл с почтовыми сообщениями
try:
    response = requests.get('https://www.py4e.com/code3/mbox.txt', timeout=10)
    response.raise_for_status()  # Проверяем успешность запроса
except requests.RequestException as e:
    print(f"Ошибка при загрузке файла: {e}")
    exit(1)

# Получаем содержимое файла в виде текста и разбиваем на строки
mbox = response.text
all_lines = mbox.split('\n')
print(f"Успешно загружено {len(all_lines)} строк")

# Словарь для подсчета количества писем от каждого отправителя
email_counts = {}

# Обрабатываем каждую строку файла
for line in all_lines:
    # Нас интересуют только строки, начинающиеся с 'From '
    if line.startswith('From '):
        parts = line.split()
        # Проверяем, что строка имеет нужный формат (минимум два элемента)
        if len(parts) >= 2:
            email = parts[1]
            # Проверяем, что это валидный email (содержит @ и .)
            if '@' in email and '.' in email:
                # Увеличиваем счетчик для этого отправителя
                email_counts[email] = email_counts.get(email, 0) + 1

# Если письма найдены, находим наиболее активного отправителя
if email_counts:
    # Используем встроенную функцию max для поиска отправителя с наибольшим количеством писем
    max_email = max(email_counts, key=email_counts.get)
    max_count = email_counts[max_email]

    print(f"Найдено уникальных отправителей: {len(email_counts)}")
    print(f"Самый активный отправитель: {max_email}")
    print(f"Количество его писем: {max_count}")
else:
    print("Письма не найдены в файле")
