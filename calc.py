print("Только целые числа, и символы операции '*', '/', '+','-'")
first_num = int(input("Введите первое число: "))
make = input("Введите символ, для операций над числами: ")
second_num = int(input("Введите второе число: "))

if make == "+":
    result = first_num + second_num
    print(f"Сумма сложения двух чисел: {result}")
elif make == "-":
    result = first_num - second_num
    print(f"Разница вычитания двух чисел: {result}")
elif make == '/':
    try:
        result = first_num/second_num
        print(f"Результат деления двух чисел: {result}")
    except ZeroDivisionError:
        print("На ноль делить нельзя")
elif make == '*':
    result = first_num*second_num
    print(f"Результат умножения двух чисел: {result}")
else:
    print("Введены не верные символы операции, только * / + - ")
