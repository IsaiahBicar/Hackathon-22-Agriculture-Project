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
        if min < 21:
            TempUnder = min - minTemp
            Prod_2 = 100 - (TempUnder * 5.5)
            ProdTotal = ProdTotal + Prod_2
        elif 21<= min <= 25 and 21<= max <= 25:
            Prod_3 = 100
            return  Prod_3
        return ProdTotal/2
    if seed == "Barley":
        minTemp= 12
        maxTemp= 15
        if max > 15:
            TempOver = max - maxTemp
            Prod1 = 100 - (TempOver * 5.5)
            return "The production is only " + str(Prod) + "%" + " due to high temperature"
        elif min < 12:
            TempUnder = min- minTemp
            Prod2 = 100 - (TempUnder * 5.5)
            return "The production is only " + str(Prod) + "%" + " due to low temperature"
    if seed == "Rice":
        minTemp= 23
        maxTemp= 30
        if min < 18:
            TempUnder = min - minTemp
            Prod1 = 100 - (TempUnder * 10)
            return "The production is only " + str(Prod) + "%" + " due to low temperature"
    if seed == "Maize":
        minTemp= 12
        maxTemp= 15
        if max > 15:
            TempOver = max - maxTemp
            Prod1 = 100 - (TempOver * 8.3)
            return "The production is only " + str(Prod) + "%" + " due to high temperature"
        elif min < 12:
            TempUnder = min - minTemp
            Prod2 = 100 - (TempUnder * 8.3)
            return "The production is only " + str(Prod) + "%" + " due to low temperature"
    if seed == "Soybean":
        minTemp=29.4
        maxTemp=29.4
        if max > 29.4:
            TempOver = max - maxTemp
            Prod = 100 - (TempOver * 20)
            return "The production is only " + str(Prod) + "%" + " due to high temperature"
    if seed == "Cotton":
        minTemp= 21
        maxTemp= 37
        if max > 37:
            TempOver = max - maxTemp
            Prod = 100 - (TempOver * 5)
            return "The production is only " + str(Prod) + "%" + " due to high temperature"
        elif min < 21:
            TempUnder = min - minTemp
            Prod = 100 - (TempUnder * 5)
            return "The production is only " + str(Prod) + "%" + " due to low temperature"
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
        if 37> max  > 30:
            TempOver = max - maxTemp
            Prod_1 = 100 - (TempOver * 5)
            return "The production is only " + str(Prod_1) + "%" + " due to high temperature"
        elif max >= 37:
            return "The production is 0" + "%" + " due to high temperature"

temperature(20,40)