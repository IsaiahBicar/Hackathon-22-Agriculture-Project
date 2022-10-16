def temperature(min, max):
    seed = str(input("Enter the seed value: "))
    if seed == 'Wheat':
        minTemp= 21
        maxTemp= 25
        ProdTotal = 0
        if max > 25:
            TempOver = max - maxTemp
            Prod_1 = 100 - (TempOver * 5.5)
            ProdTotal = ProdTotal + Prod_1
        if max ==25:
            ProdTotal = ProdTotal + 100
        if min < 21:
            TempUnder = min - minTemp
            Prod_2 = 100 - (TempUnder * 5.5)
            ProdTotal = ProdTotal + Prod_2
        if min == 21:
            ProdTotal = ProdTotal + 100
        elif 21<= min <= 25 and 21<= max <= 25:
            Prod_3 = 100
            return  Prod_3
        return ProdTotal/2
    if seed == "Barley":
        minTemp= 12
        maxTemp= 15
        ProdTotal = 0
        if max > 15:
            TempOver = max - maxTemp
            Prod1 = 100 - (TempOver * 5.5)
            ProdTotal = ProdTotal + Prod1
        if max ==25:
            ProdTotal = ProdTotal + 100
        if min < 12:
            TempUnder = min - minTemp
            Prod2 = 100 - (TempUnder * 5.5)
            ProdTotal = ProdTotal + Prod2
        if min == 12:
            ProdTotal = ProdTotal + 100
        elif 12<= min <= 15 and 12<= max <= 15:
            Prod3 = 100
            return  Prod3
        return ProdTotal/2
    if seed == "Rice":
        minTemp= 23
        maxTemp= 30
        ProdTotal = 0
        if min < 23:
            TempUnder = min - minTemp
            Prod1 = 100 - (TempUnder * 10)
            ProdTotal = ProdTotal + Prod1
        if max > 30:
            TempOver = max - maxTemp
            Prod2 = 100 - (TempOver * 10)
            ProdTotal = ProdTotal + Prod2
        if min == 23:
            ProdTotal = ProdTotal + 100
        if max == 30:
            ProdTotal = ProdTotal + 100
        elif 23<= min <= 30 and 23<= max <= 30:
            Prod3 = 100
            return  Prod3
        return ProdTotal/2
    if seed == "Maize":
        minTemp= 12
        maxTemp= 15
        ProdTotal = 0
        if max > 15:
            TempOver = max - maxTemp
            Prod1 = 100 - (TempOver * 8.3)
            ProdTotal = ProdTotal + Prod1
        if min < 12:
            TempUnder = min - minTemp
            Prod2 = 100 - (TempUnder * 8.3)
            ProdTotal = ProdTotal + Prod2
        if min == 12:
            ProdTotal = ProdTotal + 100
        if max == 15:
            ProdTotal = ProdTotal + 100
        elif 12<= min <= 15 and 12<= max <= 15:
            Prod3 = 100
            return  Prod3
        return ProdTotal/2
    if seed == "Soybean":
        minTemp=29.4
        maxTemp=29.4
        ProdTotal = 0
        if max > 29.4:
            TempOver = max - maxTemp
            Prod1 = 100 - (TempOver * 20)
            ProdTotal = ProdTotal + Prod1
        if min < 29.4:
            TempUnder = min - minTemp
            Prod2 = 100 - (TempUnder * 20)
            ProdTotal = ProdTotal + Prod2
        if min == 29.4:
            ProdTotal = ProdTotal + 100
        if max == 29.4:
            ProdTotal = ProdTotal + 100
        elif 29.4<= min <= 29.4 and 29.4<= max <= 29.4:
            Prod = 100
            return  Prod
        return ProdTotal/2
    if seed == "Cotton":
        minTemp= 21
        maxTemp= 37
        ProdTotal = 0
        if max > 37:
            TempOver = max - maxTemp
            Prod1 = 100 - (TempOver * 5)
            ProdTotal = ProdTotal + Prod1
        if min < 21:
            TempUnder = min - minTemp
            Prod2 = 100 - (TempUnder * 5)
            ProdTotal = ProdTotal + Prod2
        if min == 21:
            ProdTotal = ProdTotal + 100
        if max == 37:
            ProdTotal = ProdTotal + 100
        elif 21<= min <= 37 and 21<= max <= 37:
            Prod = 100
            return  Prod
        return ProdTotal/2

    #if seed == "Sunflower":
        #minTemp= 21
        #maxTemp= 35
       # if x > 35:
            #TempOver = x - maxTemp
            #Prod = 100 - (TempOver * 5)
            #return "The production is only " + str(Prod) + "%" + " due to high temperature"
        #elif x < 21:
            #TempUnder = minTemp - x
            #Prod = 100 - (TempUnder * 5)
            #return "The production is only " + str(Prod) + "%" + " due to low temperature"
    if seed == "Sorghum":
        minTemp= 26 
        maxTemp= 34
        ProdTotal = 0
        if 37> max  > 30:
            TempOver = max - maxTemp
            Prod_1 = 100 - (TempOver * 5)
            ProdTotal = ProdTotal + Prod_1
        if min < 26:
            TempUnder = min - minTemp
            Prod_2 = 100 - (TempUnder * 5)
            ProdTotal = ProdTotal + Prod_2
        elif max >= 37:
            return "The production is only 0% due to high temperature"
        return ProdTotal/2
            
