# 1-ое Задание
def Palindrome():
    number = int(input("Введите число для проверки на палиндром \n"))
    number_check = number
    inverted = 0

    while number > 0:
        digit = number % 10
        inverted = inverted * 10 + digit
        number=int(number / 10)

    print(inverted, "- Перевернутое число")
    if(inverted==number_check):
        return True
    else:
        return False

# 2-ое Задание
def IfDivide():
    list = []
    div2 = []
    div3 = []
    div5 = []
    for i in input("Введите числа:").split():
        list.append(int(i))
    for k in list:
        if k%2 == 0:
            div2.append(k)
        if k%3 == 0:
            div3.append(k)
        if k%5 == 0:
            div5.append(k)
    print ("Числа делящиеся на 2: ", div2)
    print ("Числа делящиеся на 3: ", div3)
    print ("Числа делящиеся на 5: ", div5)

# 3-ое Задание
def Reverse():
    number = int(input("Введите число: "))
    reversed = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        reversed = reversed * 10
        reversed = reversed + digit
    print('Обратное число: ', reversed)

# 4-ое Задание
def Sqrt():
    A = float(input("Введите число "))
    n = int(input("Введите степень "))
    x = A/2
    for i in range(1000):
        x = (1/n) * ((n-1)*x + A/x**(n-1))
    print(x)

# 5-ое Задание
def IfSimple(number):
    k = 0
    for i in range(2, number // 2+1):
        if (number % i == 0):
            k = k+1
    if (k <= 0):
        return True
    else:
        return False

#Выбор задания
choose = input("Выберите действие:\n 1. Проверка на палиндром\n 2. Делится ли число на 2/3/5\n 3. Найти обратное число\n 4. Рассчитать квадратный корень n-ой степени методом Ньютона\n 5. Простое ли число\n")
if choose == '1':
    func = Palindrome()
    print(func)
elif choose == '2':
    IfDivide()
elif choose == '3':
    Reverse()
elif choose == '4':
    Sqrt()
elif choose == '5':
    print(IfSimple(int(input("Введите число: "))))