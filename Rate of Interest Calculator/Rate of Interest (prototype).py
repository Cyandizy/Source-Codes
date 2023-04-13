import math

global Total
global Current
global Recurring
global Rate
global n
global k

print("Choose Formula [type numbers]")
print("\n1. Current Account Compound Interest")
print("\n2. Recurring Deposite Compound Interest (at the BEGINNING of n)")
print("\n3. Recurring Deposite Compound Interest (at the END of n)\n")

Formula = input(": ")

print("Type ? for an unknown value")


def Input(Type):
    if Type == 1:
        Total = input("Input S: ")
        Current = input("Input P: ")
        Rate = input("Input r in percentage: ")
        n = input("Input n: ")
        k = input("Input k: ")

        if Total == "?":
            # Floatize
            FCurrent = float(Current)
            Fn = float(n)
            Fk = float(k)
            # Rate   
            FRate = float(Rate.replace("%",""))
            # Calculate
            RbyK = FRate/Fk
            rated = math.pow(1+RbyK, Fn*Fk)
            x = FCurrent*rated

            return "Total = " + str(x)

        elif Current == "?":
            # Floatize
            FTotal = float(Total)
            Fn = float(n)
            Fk = float(k)
            # Rate
            FRate = float(Rate.replace("%",""))
            # Calculate
            RbyK = FRate/Fk
            rated = math.pow(1+RbyK, Fn*Fk)
            x = FTotal/rated

            return "Current Money = " + str(x)


        elif Rate == "?":
            # Floatize
            FTotal = float(Total)
            FCurrent = float(Current)
            Fn = float(n)
            Fk = float(k)
            # Calculate \\ SbyP(Total divided by Current) Power(n k times) RootnSbyP(Root of Power SbyP)
            SbyP = FTotal/FCurrent
            Power = Fn*Fk
            RootnSbyP = SbyP**(1/Power)
            x = (RootnSbyP-1)*Fk
            x = x*100
            return "Rate = " + str(x) + "%"
        
        elif n == "?":
            # Floatize
            FTotal = float(Total)
            FCurrent = float(Current)
            Fk = float(k)
            # Rate
            FRate = float(Rate.replace("%",""))
            # Calculate
            SbyP = FTotal/FCurrent
            RbyK = FRate/Fk
            RbyKPlusOne = 1 + RbyK
            x = (math.log(SbyP, RbyKPlusOne))/Fk
            return "n = " + str(round(x))

        elif k == "?":
            return "Due to complications, we cannot calculate k value of this type of formula."


    elif Type == 2:
        Total = input("Input S: ")
        Recurring = input("Input R: ")
        Rate = input("Input r in percentage: ")
        n = input("Input n: ")
        k = input("Input k: ")

        if Total == "?":
            # Floatize
            FRecurring = float(Recurring)
            Fn = float(n)
            Fk = float(k)
            # Rate
            FRate = float(Rate.replace("%",""))
            FRate = FRate/100
            # Calculate
            RbyK = FRate/Fk
            Power = Fn*Fk
            OnePlusRate = 1+RbyK
            PoweredOnePlusRate = OnePlusRate**(Power)
            PoweredOnePlusRateMinusOne = PoweredOnePlusRate-1
            PreDivideSum = FRecurring*OnePlusRate*PoweredOnePlusRateMinusOne
            x = PreDivideSum/RbyK
            return "Total = " + str(x)
        
        elif Recurring == "?":
            # Floatize
            FTotal = float(Total)
            Fn = float(n)
            Fk = float(k)
            # Rate
            FRate = float(Rate.replace("%",""))
            FRate = FRate/100
            # Calculate
            RbyK = FRate/Fk
            Power = Fn*Fk
            OnePlusRate = 1+RbyK
            PoweredOnePlusRate = OnePlusRate**(Power)
            PoweredOnePlusRateMinusOne = PoweredOnePlusRate-1
            PreDivideSum = OnePlusRate*PoweredOnePlusRateMinusOne
            x = FTotal*RbyK/PreDivideSum
            return "Recurring = " + str(x)
        
        elif Rate == "?":
            return "Due to complications, we cannot calculate k value of this type of formula."
        
        elif n == "?":
            # Floatize
            FTotal = float(Total)
            FRecurring = float(Recurring)
            Fk = float(k)
            # Rate
            FRate = float(Rate.replace("%",""))
            FRate = FRate/100
            #Calculate
            RbyK = FRate/Fk
            OnePlusRate = 1+RbyK
            RecurringTimesOnePlusRate = FRecurring*OnePlusRate
            RateTimesTotal = FTotal*RbyK
            RateTimesTotalByRecurringTimesOnePlusRate = RateTimesTotal/RecurringTimesOnePlusRate
            AllPlusOne = RateTimesTotalByRecurringTimesOnePlusRate+1
            x = math.log(AllPlusOne, OnePlusRate)/Fk
            return "n = " + str(round(x))
        
        elif k == "?":
            return "Due to complications, we cannot calculate k value of this type of formula."
        
    elif Type == 3:
        Total = input("Input S: ")
        Recurring = input("Input R: ")
        Rate = input("Input r in percentage: ")
        n = input("Input n: ")
        k = input("Input k: ")

        if Total == "?":
            # Floatize
            FRecurring = float(Recurring)
            Fn = float(n)
            Fk = float(k)
            # Rate
            FRate = float(Rate.replace("%",""))
            FRate = FRate/100
            # Calculate
            RbyK = FRate/Fk
            Power = Fn*Fk
            OnePlusRate = 1+RbyK
            PoweredOnePlusRate = OnePlusRate**(Power)
            PoweredOnePlusRateMinusOne = PoweredOnePlusRate-1
            PreDivideSum = FRecurring*PoweredOnePlusRateMinusOne
            x = PreDivideSum/RbyK
            return "Total = " + str(x)
        
        elif Recurring == "?":
            # Floatize
            FTotal = float(Total)
            Fn = float(n)
            Fk = float(k)
            # Rate
            FRate = float(Rate.replace("%",""))
            FRate = FRate/100
            # Calculate
            RbyK = FRate/Fk
            Power = Fn*Fk
            OnePlusRate = 1+RbyK
            PoweredOnePlusRate = OnePlusRate**(Power)
            PoweredOnePlusRateMinusOne = PoweredOnePlusRate-1
            x = FTotal*RbyK/PoweredOnePlusRateMinusOne
            return "Recurring = " + str(x)
        
        elif Rate == "?":
            return "Due to complications, we cannot calculate k value of this type of formula."
        
        elif n == "?":
            # Floatize
            FTotal = float(Total)
            FRecurring = float(Recurring)
            Fk = float(k)
            # Rate
            FRate = float(Rate.replace("%",""))
            FRate = FRate/100
            #Calculate
            RbyK = FRate/Fk
            OnePlusRate = 1+RbyK
            RateTimesTotal = FTotal*RbyK
            RateTimesTotalByRecurring = RateTimesTotal/FRecurring
            AllPlusOne = RateTimesTotalByRecurring+1
            x = math.log(AllPlusOne, OnePlusRate)/Fk
            return "n = " + str(round(x))
        
        elif k == "?":
            return "Due to complications, we cannot calculate k value of this type of formula."



if Formula == "1":
    x = Input(1)
    print(x)
elif Formula == "2":
    x = Input(2)
    print(x)
elif Formula == "3":
    x = Input(3)
    print(x)