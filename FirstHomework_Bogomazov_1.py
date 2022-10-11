#1. Вывод на экран максимального числа из трех введенных с клавиатуры
first = int(input("введите первое число "))
second = int(input("введите второе число "))
third = int(input("введите третье число "))
if (first > second):
    if (first > third):
        print("Наибольшее число первое", first)
    else:
        print("Наибольшее число третье", third)
elif (second > third):
    print("Наибольшее число второе", second)
else:
    print("Наибольшее число третье", third)



#2. Расчет факториала числа, введенного с клавиатуры
num = int(input("введите  число "))
if num == 0:
    print("Факториал числа равен ", 0)
else:
    factor = 1
    for i in range (1, num+1):
        factor = factor*i
    print("Факториал числа равен ", factor)