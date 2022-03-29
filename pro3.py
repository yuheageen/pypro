import math

word = input("케나다에서주문?")
money = int(input("얼마주문?"))

if (word == "y"):
    print("지역에따른세금을부과합니다")
    where = input("어디지역에서주문?")
    if(where == "Alberta"):
        cmon = (money/100*5)
    elif(where == "Ontario" or "NovaScotia"):
        cmon = (money/100*13)
    else :
        cmon = (money/100*6)
    amon = money + cmon
    print("금액은",amon,"입니다")
else :
    print("세금을부과하지않습니다 금액은",money,"입니다")
