import account
import evro
answer = input('"Вы хотите открыть счёт в иностранной валюте? (y/n)')

if not answer or answer[0].lower() != 'n':
        money = int(input("Введите сумму, которую вы хотите обменять: "))
        currency = int(input("Укажите код валюты (USD - 400, EUR - 401, BGN - 402, HUF - 403): "))
        result = evro.russian_analog(currency)
        count = result
        result = evro.currency_calc(money,currency)
        money = result
        rate = int(input("Введите процентную ставку: "))
        period = int(input("Введите период ведения счета в месяцах: "))
        result = account.calculate_income(rate, money, period)
        count = round(result * count)
        print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n", "Период: ", period, "\n",
              "Сумма на счете в конце периода: ", result, "\n", "В переводе в рубли: ", count)

else:
        rate = int(input("Введите процентную ставку: "))
        money = int(input("Введите сумму: "))
        period = int(input("Введите период ведения счета в месяцах: "))
        result = account.calculate_income(rate, money, period)
        print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n", "Период: ", period, "\n",
          "Сумма на счете в конце периода: ", result)
