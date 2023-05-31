# def check_affordability(s, p, m):
#     return s + p <= m
#
# s = int(input("Введите стоимость подписки на онлайн-кинотеатр: "))
# p = int(input("Введите стоимость пиццы: "))
# m = int(input("Введите зарплату Пети: "))
#
# result = check_affordability(s, p, m)
# if result:
#     print("Да")
# else:
#     print("Нет")
# input("press any key to close window")
def check_affordability(s, p, m):
    if s + p <= m:
        return "Да"
    else:
        return "Нет"

s = int(input("Введите стоимость подписки на онлайн-кинотеатр: "))
p = int(input("Введите стоимость пиццы: "))
m = int(input("Введите зарплату Пети: "))

result = check_affordability(s, p, m)
print(result)
input("press any key to close window")
