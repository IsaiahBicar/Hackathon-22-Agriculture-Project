def temperature(x):
    seed = input("Enter the seed")
    if seed == "wheat":
        minTemp= 21
        maxTemp= 25
        if x > 25:
            TempOver = x - maxTemp
            Prod = 100 - (TempOver * 5.5)
            return "The production is only " + str(Prod) + "%" + " due to high temperature"
        elif x < 21:
            TempUnder = minTemp - x
            Prod = 100 - (TempUnder * 5.5)
            return "The production is only " + str(Prod) + "%" + " due to low temperature"
    if seed == "Barley":
        minTemp= 12
        maxTemp= 15
        if x > 15:
            TempOver = x - maxTemp
            Prod = 100 - (TempOver * 5.5)
            return "The production is only " + str(Prod) + "%" + " due to high temperature"
        elif x < 12:
            TempUnder = minTemp - x
            Prod = 100 - (TempUnder * 5.5)
            return "The production is only " + str(Prod) + "%" + " due to low temperature"
    if seed == "Rice":
        minTemp= 23
        maxTemp= 30
        if x < 18:
            TempUnder = minTemp - x
            Prod = 100 - (TempUnder * 10)
            return "The production is only " + str(Prod) + "%" + " due to low temperature"
    if seed == "Maize":
        minTemp= 12
        maxTemp= 15
        if x > 15:
            TempOver = x - maxTemp
            Prod = 100 - (TempOver * 8.3)
            return "The production is only " + str(Prod) + "%" + " due to high temperature"
        elif x < 12:
            TempUnder = minTemp - x
            Prod = 100 - (TempUnder * 8.3)
            return "The production is only " + str(Prod) + "%" + " due to low temperature"
    if seed == "Soybean":
        minTemp=29.4
        maxTemp=29.4
        if x > 29.4:
            TempOver = x - maxTemp
            Prod = 100 - (TempOver * 20)
            return "The production is only " + str(Prod) + "%" + " due to high temperature"
    if seed == "Cotton":
        minTemp= 21
        maxTemp= 37
        if x > 37:
            TempOver = x - maxTemp
            Prod = 100 - (TempOver * 5)
            return "The production is only " + str(Prod) + "%" + " due to high temperature"
        elif x < 21:
            TempUnder = minTemp - x
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
        if 37> x > 30:
            TempOver = x - maxTemp
            Prod = 100 - (TempOver * 5)
            return "The production is only " + str(Prod) + "%" + " due to high temperature"
        elif x >= 37:
            return "The production is 0" + "%" + " due to high temperature"

            