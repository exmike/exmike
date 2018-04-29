def procedure_perevod(money, currency):
    usd = 57
    euro = 60
    jpy = 0.5
    cny = 8.9
    gbr = 78.3


    if currency == 1:
        money = round(money / usd, 2)
        print("Валюта: доллары США")
    elif currency == 2:
        money = round(money / euro, 2)
        print("Валюта: евро")
    elif currency == 3:
        money = round(money / jpy, 2)
        print("Валюта: йена")
    elif currency == 4:
        money = round(money / cny, 2)
        print("Валюта: юань")
    elif currency == 5:
        money = round(money / gbr, 2)
        print("Валюта: фунт стерлингов")
    return money

def main():
    money = int(input("Введите сумму, которую вы хотите обменять: "))
    currency = int(input("Укажите код валюты: доллары - 1, евро - 2, йена - 3, юань - 4, фунт стерлингов - 5: "))
    result = procedure_perevod(money, currency)
    print("К получению:", result)

if __name__ == "__main__":
    main()