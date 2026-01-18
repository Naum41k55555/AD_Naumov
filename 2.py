# Открываем файл '2.txt' для чтения
f = open("2.txt")

# Читаем первую строку файла - количество паролей для проверки
N = int(f.readline())

# Создаём пустую строку для накопления результатов проверки
s_out = ""

# Списки допустимых символов по категориям:
upperCaseLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                    "U", "V", "W", "X", "Y", "Z"]
lowerCaseLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
specialSymbols = ["!", "@", "#", "$", "%", "&", "*", "+"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


# Функция для проверки пароля на соответствие критериям
def checkPassword(password):
    # Критерий 1: длина пароля должна быть не менее 12 символов
    if len(password) < 12:
        return "Invalid\n"

    # Флаги наличия различных типов символов
    hasUpperLetter = False
    hasLowerLetter = False
    hasSpecialSymbol = False
    hasNumber = False

    # Проверяем каждый символ пароля
    for symbol in password:
        # Проверяем, является ли символ заглавной буквой
        if symbol in upperCaseLetters:
            hasUpperLetter = True
        # Проверяем, является ли символ строчной буквой
        elif symbol in lowerCaseLetters:
            hasLowerLetter = True
        # Проверяем, является ли символ специальным символом
        elif symbol in specialSymbols:
            hasSpecialSymbol = True
        # Проверяем, является ли символ цифрой
        elif symbol in numbers:
            hasNumber = True
        else:
            # Если символ не принадлежит ни к одной из разрешённых категорий
            return "Invalid\n"

    # Проверяем, что пароль содержит все необходимые типы символов
    if (hasNumber == True and hasSpecialSymbol == True and hasLowerLetter == True and hasUpperLetter == True):
        return "Valid\n"
    else:
        return "Invalid\n"


# Читаем и проверяем N паролей из файла
for i in range(N):
    # Читаем пароль и удаляем символы перевода строки и пробелы по краям
    password = f.readline().strip()
    # Добавляем результат проверки в строку вывода
    s_out += checkPassword(password)

# Выводим все результаты проверки
print(s_out)

# Закрываем файл
f.close()