import math

print("Привет, выбери, что ты хочешь сделать")

def cc():
            while True:
                print()
                print("1. Перевод в десятичную степень")
                print("2. Смена режима на целые числа")
                print("3. Смена режима на дробные числа")
                print("q. Выход")

                choice2 = input("Выбор: ")
                if choice2 == '1':
                    def f(x, i):
                        x = int(str(x), i)
                        return x
                    num1 = int(input("Введи число: "))
                    num2 = int(input("Введи систему счисления: "))
                    print(f"Ответ: {f(num1, num2)}")
                elif choice2 == '2':
                    inter()
                    break
                elif choice2 == '3':
                    fl()
                    break
                elif choice2 == 'q':
                    break
                else:
                    print("Неправильно выбран режим")

def fl():
                while True:
                    print()
                    print("1. Сложение")
                    print("2. Вычитание")
                    print("3. Умножение")
                    print("4. Деление")
                    print("5. Остаток деления")
                    print("6. Возведение в степень")
                    print("7. Квадратный корень")
                    print("8. Смена режима на целые числа")
                    print("9. Смена режима на системы счисления")
                    print("q. Выход")

                    choice = input("Выбор: ")

                    if choice == '1':
                        num1 = float(input("Введи первое число: "))
                        num2 = float(input("Введи второе число: "))
                        print(f"Ответ: {num1 + num2}")
                    elif choice == '2':
                        num1 = float(input("Введи первое число: "))
                        num2 = float(input("Введи второе число: "))
                        print(f"Ответ: {num1 - num2}")
                    elif choice == '3':
                        num1 = float(input("Введи первое число: "))
                        num2 = float(input("Введи второе число: "))
                        print(f"Ответ: {num1 * num2}")
                    elif choice == '4':
                        num1 = float(input("Введи делимое: "))
                        num2 = float(input("Введи делитель: "))
                        if num2 != 0:
                            print(f"Ответ: {num1 / num2}")
                        else:
                            print("Ошибка: деление на ноль")
                    elif choice == '5':
                        num1 = float(input("Введи делимое: "))
                        num2 = float(input("Введи делитель: "))
                        if num2 != 0:
                            print(f"Ответ: {num1 % num2}")
                        else:
                            print("Ошибка: деление на ноль")
                    elif choice == '6':
                        num1 = float(input("Введи число: "))
                        num2 = float(input("Введи степень: "))
                        print(f"Ответ: {num1 ** num2}")
                    elif choice == '7':
                        num = float(input("Введи сюда корень: "))
                        if num >= 0:
                            sqrt = math.sqrt(num)
                            print(f"Ответ: {sqrt}")
                        else:
                            print("Ошибка: квадратный корень из отрицательного числа")
                    elif choice == '8':
                        inter()
                        break
                    elif choice == '9':
                        cc()
                        break
                    elif choice == 'q':
                        break
                    else:
                        print("Неправильно выбран режим")

def inter():
    while True:
        print()
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Целочисленное деление")
        print("6. Остаток деления")
        print("7. Возведение в степень")
        print("8. Квадратный корень")
        print("9. Смена режима на дробные числа")
        print("10. Смена режима на системы счисления")
        print("q. Выход")

        choice = input("Выбор: ")

        if choice == '1':
            num1 = int(input("Введи первое число: "))
            num2 = int(input("Введи второе число: "))
            print(f"Ответ: {num1 + num2}")
        elif choice == '2':
            num1 = int(input("Введи первое число: "))
            num2 = int(input("Введи второе число: "))
            print(f"Ответ: {num1 - num2}")
        elif choice == '3':
            num1 = int(input("Введи первое число: "))
            num2 = int(input("Введи второе число: "))
            print(f"Ответ: {num1 * num2}")
        elif choice == '4':
            num1 = int(input("Введи делимое: "))
            num2 = int(input("Введи делитель: "))
            if num2 != 0:
                print(f"Ответ: {num1 / num2}")
            else:
                print("Ошибка: деление на ноль")
        elif choice == '5':
            num1 = int(input("Введи делимое: "))
            num2 = int(input("Введи делитель: "))
            if num2 != 0:
                print(f"Ответ: {num1 // num2}")
            else:
                print("Ошибка: деление на ноль")
        elif choice == '6':
            num1 = int(input("Введи делимое: "))
            num2 = int(input("Введи делитель: "))
            if num2 != 0:
                print(f"Ответ: {num1 % num2}")
            else:
                print("Ошибка: деление на ноль")
        elif choice == '7':
            num1 = int(input("Введи число: "))
            num2 = int(input("Введи степень: "))
            print(f"Ответ: {num1 ** num2}")
        elif choice == '8':
            num = int(input("Введи сюда корень: "))
            if num >= 0:
                sqrt = math.sqrt(num)
                print(f"Ответ: {sqrt}")
            else:
                print("Ошибка: квадратный корень из отрицательного числа")
        elif choice == '9':
            fl()
            break
        elif choice == '10':
            cc()
            break
        elif choice == 'q':
            break
        else:
            print("Неправильно выбран режим")

inter()
