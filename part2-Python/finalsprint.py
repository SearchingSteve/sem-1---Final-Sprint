# Description: This is the HAB Taxi Services program to enter the driver information and the other business data and generate reports.
# Author(s): Artem Hanzha, Asif Lakhani, Donovan Head, Michelle Anderson, Sara Woodford, Stephen Crocker
# Date(s): 1 Apr 2024 - 



# Define required libraries.
import datetime
import FormatValues as FV
import ImpFunctions as ImF
import time
import sys



# Define program constants.
global CUR_DATE

CUR_DATE = datetime.datetime.now()


 
# Main Program
def func1():
    # Define program constants
    global CUR_DATE, Today

    # Open the defaults file and read the values into variables
    defaults = open('Defaults.dat', 'r')
    NEXT_TRANS_NUM = int(defaults.readline())
    NEXT_DRIVER_NUM = int(defaults.readline())
    MONTHLY_STAND_FEE = float(defaults.readline())
    DAILY_RENTAL_FEE = float(defaults.readline())
    WEEKLY_RENTAL_FEE = float(defaults.readline())
    HST_RATE = float(defaults.readline())
    defaults.close()


    

    while True:
        # Gather user inputs
        print()
        print("\033[0;36m------------------------------------------------------------------------\033[0m")   
        print("                   \033[0;36mEmployee Personal Information\033[0m")
        print("\033[0;36m------------------------------------------------------------------------\033[0m")   
        print()

        EmpFirstName = ImF.fName("First Name")
        EmpLastName = ImF.lName("Last Name")
        EmpFullName = EmpFirstName + " " + EmpLastName
        
        StAddress = ImF.strAddress("Address")
        City = ImF.city("City")
        Prov = ImF.provList("Province")
        PostalCode = ImF.postalCode("X9X9X9")
        Address2 = City + ", " + Prov + ", " + PostalCode

        PhoneNum = ImF.cellNumber("9999999999")
            
        print()
        print("\033[0;36m------------------------------------------------------------------------\033[0m")   
        print("                        \033[0;36mCar Rental Information\033[0m")
        print("\033[0;36m------------------------------------------------------------------------\033[0m")   
        print()


        while True:
            DriversLicNum = input("Enter the employee driver license number (X99999)       : ").upper()
            if DriversLicNum == "":
                print("\033[0;31mData Entry Error - Driver License number cannot be blank, please try again.\033[0m")
                print()
            elif len(DriversLicNum) != 6: 
                print("\033[0;31mData Entry Error - Driver License number must be 6 digits only, please try again.\033[0m")
                print()
            elif (DriversLicNum[0].isalpha()) == False:
                print("\033[0;31mData Entry Error - First character must be a letter, please try again.\033[0m")
                print()
            elif (DriversLicNum[1].isnumeric()) == False:
                print("\033[0;31mData Entry Error - Second character must be a number, please try again.\033[0m")
                print()
            elif (DriversLicNum[2].isnumeric()) == False:
                print("\033[0;31mData Entry Error - Third character must be a number, please try again.\033[0m")
                print()
            elif (DriversLicNum[3].isnumeric()) == False:
                print("\033[0;31mData Entry Error - Fourth character must be a number, please try again.\033[0m")
                print()
            elif (DriversLicNum[4].isnumeric()) == False:
                print("\033[0;31mData Entry Error - Fifth character must be a number, please try again.\033[0m")
                print()
            elif (DriversLicNum[5].isnumeric()) == False:
                print("\033[0;31mData Entry Error - Sixth character must be a number, please try again.\033[0m")
                print()
            else:
                break
        
        
        while True:
            try:
                ExpDate = input("Enter the date of expiry (YYYY-MM-DD)                   : ")
                ExpDate = datetime.datetime.strptime(ExpDate, "%Y-%m-%d")
            except:
                print("\033[0;31mData Entry Error - Date of expiry is not in a valid format, please try again.\033[0m")
                print()
            else:
                break
        
            
        while True:
            InsPolicyName = input("Enter the driver's insurance policy company name        : ").title()
            if InsPolicyName == "":
                print("\033[0;31mData Entry error - Insurance policy company name cannot be blank.\033[0m")
                print()
            else:
                break
    
        
        while True:
            InsPolicyNum = input("Enter the employee driver license number (XX99)         : ").upper()
            if InsPolicyNum == "":
                print("\033[0;31mData Entry Error - Driver License number cannot be blank, please try again.\033[0m")
                print()
            elif len(InsPolicyNum) != 4: 
                print("\033[0;31mData Entry Error - Driver License number must be 6 digits only, please try again.\033[0m")
                print()
            elif (InsPolicyNum[0].isalpha()) == False:
                print("\033[0;31mData Entry Error - First character must be a letter, please try again.\033[0m")
                print()
            elif (InsPolicyNum[1].isalpha()) == False:
                print("\033[0;31mData Entry Error - Second character must be a letter, please try again.\033[0m")
                print()
            elif (InsPolicyNum[2].isnumeric()) == False:
                print("\033[0;31mData Entry Error - Third character must be a number, please try again.\033[0m")
                print()
            elif (InsPolicyNum[3].isnumeric()) == False:
                print("\033[0;31mData Entry Error - Fourth character must be a number, please try again.\033[0m")
                print()
            else:
                break
        
             
        while True:
            EmpCarDesc = input("Enter the type of car, own or rental as (O / R)         : ").upper()
            if EmpCarDesc == "":
                print("\033[0;31mData Entry Error - Type of car cannot be blank.\033[0m")
                print()
            elif EmpCarDesc == "O":
                EmpCarDesc = "Own Car"
                CarRentalHST = MONTHLY_STAND_FEE * HST_RATE
                EmpBalDue = MONTHLY_STAND_FEE + CarRentalHST
                CarRentalDays = 0
                CarRentalAmount = 0 
                StandFees = MONTHLY_STAND_FEE
                break
            elif EmpCarDesc == "R":
                EmpCarDesc = "Rental Car"
                StandFees = 0.00
                while True:
                    CarRental = input("Enter the type of car rental, weekly or daily as (W / D): ").upper()
                    if CarRental == "":
                        print("\033[0;31mData Entry Error - Type of car rental cannot be blank.\033[0m")
                        print()
                    elif CarRental == "W":
                        EmpCarDesc = "Weekly Rental"
                        StandFees = 0.00
                        while True:
                            try:
                                CarRentalWeeks = int(input("Enter the number of weeks for car rental                : "))
                                CarRentalDays = CarRentalWeeks * 7
                                CarRentalAmount = CarRentalWeeks * WEEKLY_RENTAL_FEE
                                CarRentalHST = CarRentalAmount * HST_RATE
                                EmpBalDue = CarRentalAmount + CarRentalHST
                                break
                            except ValueError:
                                print("\033[0;31mData Entry Error - Number of weeks is not a valid number, please try again.\033[0m")
                                print()
                        break
                    elif CarRental == "D":
                        EmpCarDesc = "Daily Rental"
                        StandFees = 0.00
                        while True:
                            try:
                                CarRentalDays = int(input("Enter the number of days for car rental: "))
                                CarRentalAmount = CarRentalDays * DAILY_RENTAL_FEE
                                CarRentalHST = CarRentalAmount * HST_RATE
                                EmpBalDue = CarRentalAmount + CarRentalHST
                                break
                            except ValueError:
                                print("\033[0;31mData Entry Error - Number of days is not a valid number, please try again.\033[0m")
                                print()
                        break
                    else:
                        print("\033[0;31mData Entry Error - Please enter either 'W' for weekly or 'D' for daily rental type.\033[0m")
                        print()
                break
            else:
                print("\033[0;31mData Entry Error - Please enter either 'O' for Own or 'R' for Rental.\033[0m")
                print()
        
        
           
        # Display results
        print()
        print("\033[0;36m------------------------------------------------------------------------\033[0m")   
        print("                        \033[0;36mBalance Due Calculation\033[0m")
        print("\033[0;36m------------------------------------------------------------------------\033[0m")   
        print()
        print(f"Car Type          : {EmpCarDesc:<10s}")
        print(f"Standard Fees     : {FV.FDollar2(StandFees):<10s}")
        print()
        print(f"Car Rental Days   : {int(CarRentalDays):<10d}")
        print(f"Car Rental Amount : {FV.FDollar2(CarRentalAmount):<10s}")
        print()
        print(f"HST Amount        : {FV.FDollar2(CarRentalHST):<10s}")
        print(f"Balance Due       : {FV.FDollar2(EmpBalDue):<10s}")
        print()
        
            
    
        # Write the employee values to a data file called Employee.dat.
        emp = open("Employee.dat", "a")
        emp.write("{}, ".format(str(NEXT_DRIVER_NUM)))
        emp.write("{}, ".format(str(EmpFirstName)))
        emp.write("{}, ".format(str(EmpLastName)))
        emp.write("{}, ".format(str(StAddress)))
        emp.write("{}, ".format(City))
        emp.write("{}, ".format(Prov))
        emp.write("{}, ".format(str(PostalCode)))
        emp.write("{}, ".format(str(PhoneNum)))
        emp.write("{}, ".format(DriversLicNum))
        emp.write("{}, ".format(FV.FDateS(ExpDate)))
        emp.write("{}, ".format(InsPolicyName))
        emp.write("{}, ".format(InsPolicyNum))
        emp.write("{}, ".format(EmpCarDesc))
        emp.write("{}\n".format(str(EmpBalDue)))
        emp.close ()
    
        print()
        print("Employee data successfully saved ...", end='\r')
        time.sleep(1)  # To create the blinking effect
        sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns



        REV_TRANS_DATE = CUR_DATE
        REV_DECRP = EmpCarDesc
        EMP_ID = NEXT_DRIVER_NUM
        TRANS_AMOUNT = 175.00
        HST_AMOUNT = 26.25
        TOTAL_AMOUNT = 201.25
        
        if EmpCarDesc == "Own Car":
            TRANS_AMOUNT = 175.00
            HST_AMOUNT = 26.25
            TOTAL_AMOUNT = 201.25
        else:
            TRANS_AMOUNT = CarRentalAmount
            HST_AMOUNT = CarRentalHST
            TOTAL_AMOUNT = EmpBalDue               
        
        

        # Write the employee values to a data file called Revenue.dat.
        rev = open("Revenue.dat", "a")
        rev.write("{}, ".format(str(NEXT_TRANS_NUM)))
        rev.write("{}, ".format(FV.FDateS(REV_TRANS_DATE)))
        rev.write("{}, ".format(REV_DECRP))
        rev.write("{}, ".format(str(EMP_ID)))
        rev.write("{}, ".format(str(TRANS_AMOUNT)))
        rev.write("{}, ".format(str(HST_AMOUNT)))
        rev.write("{}\n".format(str(TOTAL_AMOUNT)))
        rev.close ()
    
        
        
        
        print("\033[0;33mEmployee and Revenue data successfully saved...\033[0m", end='\r')
        time.sleep(1)  # To create the blinking effect
        sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
        time.sleep(1)  # To create the blinking effect
        print("\033[0;33mBalance Due updated now\033[0m", end='\r')
        sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
        time.sleep(1)  # To create the blinking effect
        
        
       

    
        NEXT_DRIVER_NUM += 1
        NEXT_TRANS_NUM += 1
        
        
    
    
        # Any housekeeping duties at the end of the program.
    
        # Write the default values back to the Defaults.dat file
        defaults = open('Defaults.dat', 'w')
        defaults.write("{}\n".format(str(NEXT_TRANS_NUM)))
        defaults.write("{}\n".format(str(NEXT_DRIVER_NUM)))
        defaults.write("{}\n".format(str(MONTHLY_STAND_FEE)))
        defaults.write("{}\n".format(str(DAILY_RENTAL_FEE)))
        defaults.write("{}\n".format(str(WEEKLY_RENTAL_FEE)))
        defaults.write("{}\n".format(str(HST_RATE)))
        defaults.close()

        while True:
            program_continue = input("Would you like to enter new employee record? (Y/N): ").upper()
            if program_continue != "Y" and program_continue != "N":
                print("\033[0;31mData Entry Error - Must enter either Y or N, please try again.\033[0m")
                print()
            else:
                break
        if program_continue == "N":
            break



def report6():
    
    # Define program constants
    global CUR_DATE, Today

    # Initialize counters and accumulators.
    RevTotalAcc = 0
    StandFeesAcc = 0

    SuppliesAcc = 0
    RepairAcc = 0
    FuelAcc = 0
    InsuranceAcc = 0
    OtherExpAcc = 0

    # Open the data file.
    r = open("Revenue.dat", "r")

    # Process each line (record) in the file in a loop.
    for RevRecord in r:

        # Read the records from Revenue.
        RevLst = RevRecord.split(",")
        RevID = RevLst[0].strip()
        RevDate = RevLst[1].strip()
        RevDate = datetime.datetime.strptime(RevDate, "%Y-%m-%d")
        RevDesc = RevLst[2].strip()
        EmpID = RevLst[3].strip()
        RevAmount = RevLst[4].strip()
        RevAmount = float(RevAmount)
        RevHST = RevLst[5].strip()
        RevHST = float(RevHST)
        RevTotal = RevLst[6].strip()
        RevTotal = float(RevTotal)


        if RevDesc == "Weekly Rental" or RevDesc == "Daily Rental":
            RevTotalAcc += RevTotal
        elif RevDesc == "Own Car":
            StandFeesAcc += RevTotal

    r.close()

    # Open the data file.
    rd = open("Revenue.dat", "r")

    # Read all lines into a list
    lines = rd.readlines()   
    FirstLine = lines[0].strip().split(",")
    LastLine = lines[-1].strip().split(",")
    FirstRevDate = FirstLine[1].strip()
    FirstRevDate = datetime.datetime.strptime(FirstRevDate, "%Y-%m-%d")
    LastRevDate = LastLine[1].strip()
    LastRevDate = datetime.datetime.strptime(LastRevDate, "%Y-%m-%d")
    rd.close()


    #Open the data file.
    e = open("Expenses.dat", "r")
    
    # Process each line (record) in the file in a loop.
    for ExpRecord in e:

        # Read the records from Revenue.
        ExpLst = ExpRecord.split(",")
        ExpID = ExpLst[0].strip()
        InvNo = ExpLst[1].strip()
        ExpDate = ExpLst[2].strip()
        ExpDate = datetime.datetime.strptime(ExpDate, "%Y-%m-%d")
        EmpID = ExpLst[3].strip()
        ItemNo = ExpLst[4].strip()
        ItemDesc = ExpLst[5].strip()
        ItemCost = ExpLst[6].strip()
        ItemCost = float(ItemCost)
        ItemQty = ExpLst[7].strip()
        ItemQty = int(ItemQty)
        ItemTotal = ExpLst[8].strip()
        ItemTotal = float(ItemTotal)
        TotalHST = ExpLst[9].strip()
        TotalHST = float(TotalHST)
        TotalAmount = ExpLst[10].strip()
        TotalAmount = float(TotalAmount)


        if ItemDesc == "Supplies":
            SuppliesAcc += TotalAmount
        elif ItemDesc == "Repair":
            RepairAcc += TotalAmount
        elif ItemDesc == "Fuel":
            FuelAcc += TotalAmount
        elif ItemDesc == "Insurance":
            InsuranceAcc += TotalAmount
        elif ItemDesc == "Other":
            OtherExpAcc += TotalAmount     
    
    e.close()
        

    TotalIncome = RevTotalAcc + StandFeesAcc
    TotalExpense = SuppliesAcc + RepairAcc + FuelAcc + InsuranceAcc + OtherExpAcc
    ProfitLoss = TotalIncome - TotalExpense

    if ProfitLoss > 0:
        Profit = ProfitLoss
        Loss = 0
    elif ProfitLoss < 0:
        Loss = ProfitLoss
        Profit = 0


    print()
    print(f"\033[1;34mHAB TAXI SERVICES\033[0m")
    print(f"\033[0;34mPROFIT / LOSS LISTING                      {FV.FDateL(CUR_DATE)}\033[0m")
    print(f"_________________________________________________________________")
    print()
    print(f"Report Date                       From: {FV.FDateM(FirstRevDate):<9s}   To: {FV.FDateM(LastRevDate):<9s}")
    print(f"_________________________________________________________________")
    print()

    print("\033[1;32mRevenue\033[0m                                \033[1;31mExpenses\033[0m")
    # print(f"__________________________")
    print(f"_________________________________________________________________")
    print(f"Rentals       : {FV.FDollar2(RevTotalAcc):>10s}             Supplies      : {FV.FDollar2(SuppliesAcc):>10s}")
    print(f"Standard Fees : {FV.FDollar2(StandFeesAcc):>10s}             Repairs       : {FV.FDollar2(RepairAcc):>10s}")
    print(f"                                       Fuel          : {FV.FDollar2(FuelAcc):>10s}")
    print(f"                                       Insurance     : {FV.FDollar2(InsuranceAcc):>10s}")
    print(f"                                       Others        : {FV.FDollar2(OtherExpAcc):>10s}")        
    print(f"_________________________________________________________________")
    print(f"Total Revenue : {FV.FDollar2(TotalIncome):>10s}             Total Expenses: {FV.FDollar2(TotalExpense):>10s}")
    print()
    print(f"Profit: {FV.FDollar2(Profit):>10s}")
    print(f"Loss  : {FV.FDollar2(Loss):>10s}")
    print()
    print(f"Authorized By: HAB Taxi Services")
    print(f"_________________________________________________________________")




def report8():
    # Define program constants
    global CUR_DATE, Today


    print()
    print(f"\033[1;34mHAB TAXI SERVICES\033[0m")
    print(f"\033[0;34mEMPLOYEE DETAIL INFORMATION                                                                               {FV.FDateL(CUR_DATE)}\033[0m")
    print(f"_________________________________________________________________________________________________________________________________")
    print()
    print(f" Driver  Employee              Phone            License    License        Insurance      Insurance    Car               Balance")
    print(f" No      Name                  No               No         Expiry Date    Company        Policy No    Status            Due")
    print(f"_________________________________________________________________________________________________________________________________")
    print()


    # Initialize counters and accumulators.
    EmpCtr = 0
    BalDueAcc = 0

    # Open the data file.
    f = open("Employee.dat", "r")

    # Process each line (record) in the file in a loop.
    for EmpRecord in f:

        # Read the record.  Grab values from the list.
        EmpLst = EmpRecord.split(",")
        EmpID = EmpLst[0].strip()
        EmpNameFir = EmpLst[1].strip()
        EmpNameLas = EmpLst[2].strip()
        EmpName = EmpNameFir + " " + EmpNameLas
        EmpPhoneNum = EmpLst[7].strip()
        EmpLiscNum = EmpLst[8].strip()
        EmpLiscExp = EmpLst[9].strip()
        EmpLiscExp = datetime.datetime.strptime(EmpLiscExp, "%Y-%m-%d")
        InsCom = EmpLst[10].strip()
        InsPolNum = EmpLst[11].strip()
        CarStatus = EmpLst[12].strip()
        BalDue = EmpLst[13].strip()
        BalDue = float(BalDue)
        

        # Format Phone No.
        EmpPhoneNum = "(" + EmpPhoneNum[0:3] + ") " + EmpPhoneNum[3:6] + " " + EmpPhoneNum[6:]

        # Display the detail line.
        print(f" {EmpID:<4s}    {EmpName:<20s}  {EmpPhoneNum:<12s}   {EmpLiscNum:<6s}     {FV.FDateS(EmpLiscExp):<12s}   {InsCom:<11s}    {InsPolNum:<4s}         {CarStatus:<13s}   {FV.FDollar2(BalDue):>10s}")

        # Update counters and accumulators.
        EmpCtr += 1
        BalDueAcc += BalDue


    # Close the file.
    f.close()

    # Print summary data - counters and accumulators.
    print(f"_________________________________________________________________________________________________________________________________")
    print(f"\033[0;36mTotal Employee: {EmpCtr:>3d}                                                                                Total Balance Due: {FV.FDollar2(BalDueAcc):>10s}\033[0m")
    print()







# Program - Main program starts here.
while True:
    print()
    print()
    print("                 \033[1;34mHAB Taxi Services\033[0m")

    print("\033[1;34m----------------------------------------------------\033[0m")
    print("                      \033[0;34mMain Menu\033[0m")
    print("\033[1;34m----------------------------------------------------\033[0m")
    print()

    print("1. Enter a New Employee (driver).")
    print("2. Enter Company Revenues.")
    print("3. Enter Company Expenses.")
    print("4. Track Car Rentals.")
    print("5. Record Employee Payment.")
    print("6. Print Company Profit Listing.")
    print("7. Print Driver Financial Listing.")
    print("8. Print Employee Detail Information.")
    print("9. Quit Program")
    print()
    print("\033[1;34m----------------------------------------------------\033[0m")
   

    while True:
        try:
            Choice = int(input("\033[0;36mEnter choice (1 - 6): \033[0m"))
            print()
        except:
            print("\033[0;31mData Entry Error - must be a valid number between 1 and 9.\033[0m")
            print()
        else:
            if Choice < 1 or Choice > 9:
                print("\033[0;31mData Entry Error - must be a valid number between 1 and 6.\033[0m")
                print()
            else:
                break
       
    if Choice == 1:
        func1()
    elif Choice == 2:
        print("\033[0;33m**This option is not developed, kindly choose option 1.**\033[0m")
        print()
    elif Choice == 3:
        print("\033[0;33m**This option is not developed, kindly choose option 1.**\033[0m")
        print()
    elif Choice == 4:
        print("\033[0;33m**This option only have the Data Files.**\033[0m")
        print()
    elif Choice == 5:
        print("\033[0;33m**This option only have the Data Files.**\033[0m")
        print()
    elif Choice == 6:
        report6()
    elif Choice == 7:
        print("\033[0;33m**This option is not developed, kindly choose option 6.**\033[0m")
        print()
    elif Choice == 8:
        report8()
        # print("\033[0;33m**Program is in Developing Mode.**\033[0m")
        print()
    else:
        break
   


# Any housekeeping duties at the end of the program.
    
print()
print("\033[1;34m----------------------------------------------------\033[0m")
print("   \033[1;34mThank you for using HAB Taxi Service Program!\033[0m")
print("\033[1;34m----------------------------------------------------\033[0m")
print()