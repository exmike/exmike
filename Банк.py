import account
def main():
    rate = int(input("Введите ставку: "))
    cash = int(input("\nВведите сумму: "))
    period = int(input("\nВведите период: "))
    result = account.calculate_income(rate, cash, period)
    print (result,rate,cash)
if __name__ == "__main__":
    main ()