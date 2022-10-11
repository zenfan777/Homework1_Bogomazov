#1. Вывод на экран максимального числа из трех введенных с клавиатуры
first = int(input("введите первое число"))
second = int(input("введите второе число"))
third = int(input("введите третье число"))
min = first
if (min - second > 0):
    if (first - third > 0):
        print("Наибольшее число первое", first)
    else: print("Наибольшее число третье", third)
if (second - third > 0):
    print("Наибольшее число второе", second)
else:print("Наибольшее число третье", third)



#2. Расчет факториала числа, введенного с клавиатуры