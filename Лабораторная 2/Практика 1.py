money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count_months = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

while money_capital >= 0:
    money_capital = money_capital + salary - spend
    if money_capital < 0:
        break
    count_months += 1
    spend = spend + spend * increase
print("Количество месяцев, которое можно протянуть без долгов:", count_months)
