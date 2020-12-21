
"""
Task 2

The valid phone number program.

Make a program that checks if a string is in the right format for a phone number. T
he program should check that the string contains only numerical characters and is only 10 characters long.
Print a suitable message depending on the outcome of the string evaluation.

Задание (із зірочкой):
Получить от пользователя его номер телефона, проверить подходит ли номер под форматы
+380_________ (прочерки - любая цифра)
0_________ (например 0931233232)
0__ ___ __ __ (пробелы именно пробелы и телефон например 095 321 12 21)
Если номер введен верно - похвалите человека. Если нет - поругайте.

"""
# Первый вариант

phone = input("Напиши свой номер телефона коректно:")

phone_checking = phone.strip()
#проверяю наличие табуляции и +38
if phone_checking.isalnum():
    # проверяю наличие букв
    if phone_checking.isdigit():
        # проверка дляины
        if len(phone_checking) == 10:
            print("Спасибо")
        else:
            print('Посчитай цифры!!!')
    else:
        print('Пиши цифрами!!!')
else:
    #проверяю наличие +38
    if phone_checking.find("+38") == 0:
        phone_checking_less = phone_checking[3:]
        # проверяю на наличие табуляции
        if phone_checking_less.isalnum():
            #проверяю наличие букв
            if phone_checking_less.isdigit():
                #проверяю длину
                if len(phone_checking_less) == 10:
                    print("Спасибо")
                else:
                    print('Посчитай цифры!!!')
            else:
                print("Пиши цифрами!!!")
        else:
            phone_checking_less_glued = phone_checking_less.replace(" ", "")
            # проверяю наличие букв
            if phone_checking_less_glued.isdigit():
                # проверяю длину
                if len(phone_checking_less_glued) == 10:
                    print("Спасибо")
                else:
                    print('Посчитай цифры!!!')
            else:
                print("Пиши цифрами!!!")
    else:
        # проверяю на наличие табуляции
        if phone_checking.isalnum():
            # проверяю наличие букв
            if phone_checking.isdigit():
                # проверяю длину
                if len(phone_checking) == 10:
                    print("Спасибо")
                else:
                    print('Посчитай цифры!!!')
            else:
                print("Пиши цифрами!!!")
        else:
            phone_checking_glued = phone_checking.replace(" ", "")
            # проверяю наличие букв
            if phone_checking_glued.isdigit():
                # проверяю длину
                if len(phone_checking_glued) == 10:
                    print("Спасибо")
                else:
                    print('Посчитай цифры!!!')
            else:
                print("Пиши цифрами!!!")


# Второй вариант

phone = input("Напиши свой номер телефона коректно:")

phone = phone.strip()
phone = phone.replace(" ", "")

print(phone)

if phone.find("+") == 0:
    phone = phone[3:]
    if phone.isdigit():
        if len(phone) == 10:
            print ("Спасибо")
        else:
            print("Считай цифры!!!")
    else:
        print("Пиши цифрами!!!")
else:
    if phone.isdigit():
        if len(phone) == 10:
            print ("Спасибо")
        else:
            print("Считай цифры!!!")
    else:
        print("Пиши цифрами!!!")




