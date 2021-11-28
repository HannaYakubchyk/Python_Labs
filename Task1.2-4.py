years = int(input("Введите количество лет, когда фирма закупала оборудование: "))
YearlyPurchases = [] #стоимость закупки оборудования отдельно по каждому году
amortizationPercent = 0.05 #процент амортизации
ValueOfEquipmentAtFinalPoint = [] #стоимость оборудования по каждому году с учетом амортизации на финальную дату

for eachYear in range(years):
    MoneySpentPerYear = int(input("Введите стоимость закупаемого оборудования в год " + str(eachYear + 1) + ": "))  #стоимость закупаемого обрудования в год
    YearlyPurchases.append(MoneySpentPerYear)

print(f"Годовая норма амортизации составляет {amortizationPercent*100} %. В расчете используется линейный способ начисления амортизации.")

yearsLeft = years
for eachYear in range(years):

    YearlyAmortizationSum = YearlyPurchases[eachYear] * amortizationPercent #годовая сумма амортизации
    ValueInTheEndOfPeriod = YearlyPurchases[eachYear] - (yearsLeft * YearlyAmortizationSum)
    yearsLeft -= 1
    print(f"Стоимость оборудования, купленного в год {eachYear + 1}, с учетом амортизации к году {years}: " + str(
        ValueInTheEndOfPeriod))
    ValueOfEquipmentAtFinalPoint.append(ValueInTheEndOfPeriod)


print("Общая стоимость накопленного оборудования: " + str(sum(ValueOfEquipmentAtFinalPoint)))




