def calculate_income(rate,period,money):
    if money<=0:
        return (0)
    for i in range(1,period+1):
        money = round(money + money * rate / 100 / 12, 2)
        return (money)
def main():
    rate = 10
    money = 100000
    period = 12
    result = calculate_income(rate,money,period)
    print(result,money,period,rate)
if __name__ =='__main__':
    main()