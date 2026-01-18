f = open("4.txt")
names = f.readline().split()

# Читаем вторую строку - количество транзакций (записей о расходах)
n = int(f.readline().strip())

# Создаём словарь для хранения суммарных расходов каждого человека
# Изначально у всех расходы равны 0
expenses = {}
for name in names:
    expenses[name] = 0.0

# Обрабатываем каждую транзакцию из файла
for i in range(n):
    # Читаем строку с транзакцией
    line = f.readline().strip()

    # Разбиваем строку на имя и сумму
    name, amount = line.split()

    # Преобразуем сумму в число и добавляем к расходам данного человека
    expenses[name] += float(amount)

# Закрываем файл после чтения
f.close()

# Вычисляем общую сумму всех расходов
total_expenses = sum(expenses.values())

# Вычисляем среднюю сумму расходов на человека
average = total_expenses / len(names)

# Создаём список для хранения балансов каждого человека
# Баланс = потрачено - среднее
# Отрицательный баланс: человек должен получить деньги (потратил меньше среднего)
# Положительный баланс: человек должен отдать деньги (потратил больше среднего)
balances = []
for name in names:
    # Вычисляем баланс
    balance = expenses[name] - average

    # Округляем до 10 знаков для избежания ошибок округления
    balance = round(balance, 10)

    # Добавляем кортеж (имя, баланс) в список
    balances.append((name, balance))

# Сортируем балансы по имени (для стабильной работы алгоритма)
balances.sort()

# Список для хранения результирующих транзакций
transactions = []

# Используем два указателя для эффективного сопоставления должников и кредиторов
# left указывает на должников (отрицательные балансы в начале списка)
# right указывает на кредиторов (положительные балансы в конце списка)
left = 0
right = len(balances) - 1

# Алгоритм минимизации количества транзакций
while left < right:
    # Получаем данные текущего должника
    debtor_name, debtor_balance = balances[left]

    # Получаем данные текущего кредитора
    creditor_name, creditor_balance = balances[right]

    # Если баланс должника близок к нулю (уже рассчитался), переходим к следующему
    if abs(debtor_balance) < 1e-9:  # 1e-9 = 0.000000001
        left += 1
        continue

    # Если баланс кредитора близок к нулю (уже получил всё), переходим к следующему
    if abs(creditor_balance) < 1e-9:
        right -= 1
        continue

    # Вычисляем сумму перевода: минимальное из того, что должен отдать должник
    # и того, что должен получить кредитор
    amount = min(-debtor_balance, creditor_balance)

    # Округляем сумму до копеек (2 знака после запятой)
    amount = round(amount, 2)

    # Если сумма меньше 1 копейки, пропускаем эту пару
    if amount < 0.01:
        # Выбираем, кого пропустить: того, у кого меньший остаток по модулю
        if abs(debtor_balance) < abs(creditor_balance):
            left += 1
        else:
            right -= 1
        continue

    # Добавляем транзакцию в результат
    transactions.append((debtor_name, creditor_name, amount))

    # Обновляем балансы после перевода
    # Должник отдал деньги: его отрицательный баланс уменьшается (становится ближе к 0)
    debtor_balance = round(debtor_balance + amount, 10)

    # Кредитор получил деньги: его положительный баланс уменьшается (становится ближе к 0)
    creditor_balance = round(creditor_balance - amount, 10)

    # Сохраняем обновлённые балансы
    balances[left] = (debtor_name, debtor_balance)
    balances[right] = (creditor_name, creditor_balance)

    # Если должник полностью рассчитался, переходим к следующему
    if abs(debtor_balance) < 1e-9:
        left += 1

    # Если кредитор получил всё причитающееся, переходим к следующему
    if abs(creditor_balance) < 1e-9:
        right -= 1

# Выводим количество транзакций
print(len(transactions))

# Выводим все транзакции
for debtor, creditor, amount in transactions:
    # Форматируем вывод: имя_должника имя_кредитора сумма.две_цифры_после_запятой
    print(f"{debtor} {creditor} {amount:.2f}")