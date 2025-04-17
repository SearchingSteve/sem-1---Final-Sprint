import datetime

# First Name
def fName(firstName):
    allowed_char = set ("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-.,'")
    while True:
        firstName = input("Enter the first name                : ").title()
        if firstName == "":
            print("\033[0;31mData Entry Error - First name cannot be blank, please try again.\033[0m")
            print()
        elif set (firstName) .issubset (allowed_char) == False:
            print("\033[0;31mData Entry Error - First name contains invalid characters, please try again.\033[0m")
            print()
        else:
            break
    return firstName

    
# Last Name
def lName(lastName):
    allowed_char = set ("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-.,'")
    while True:
        lastName = input("Enter the last name                 : ").title()
        if lastName == "":
            print("\033[0;31mData Entry Error - Last name cannot be blank, please try again.\033[0m")
            print()
        elif set (lastName) .issubset (allowed_char) == False:
            print("\033[0;31mData Entry Error - Last name contains invalid characters, please try again.\033[0m")
            print()
        else:
            break
    return lastName


# Date of Birth
def doBirth(dateBirth):
    while True:
        try:
            dateBirth = input("Enter the date of birth (YYYY-MM-DD) : ")
            dateBirth = datetime.datetime.strptime(dateBirth, "%Y-%m-%d")
        except:
            print("\033[0;31mData Entry Error - Date of birth is not in a valid format, please try again.\033[0m")
            print()
        else:
            break
    return dateBirth


# Cell Number
def cellNumber(cellNum):
    while True:
        cellNum = input("Enter the phone number (9999999999) : ")
        if cellNum == "":
            print("\033[0;31mData Entry Error - Phone number cannot be blank, please try again.\033[0m")
            print()
        elif len(cellNum) != 10: 
            print("\033[0;31mData Entry Error - Phone number must be 10 digits only, please try again.\033[0m")
            print()
        elif cellNum.isdigit() == False:
            print("\033[0;31mData Entry Error - Phone number must be digits only, please try again.\033[0m")
            print()
        else:
            break
    # cellNumberFormat = "(" + cellNum[0:3] + ") " + cellNum[3:6] + " " + cellNum[6:]
    # return cellNumberFormat
    return cellNum




# Street Address
def strAddress(strAdd):
    while True:
        strAdd = input("Enter the street address            : ").title()
        if strAdd == "":
            print("\033[0;31mData Entry Error - Street Address cannot be blank, please try again.\033[0m")
            print()
        elif len(strAdd) > 20:
            print("\033[0;31mData Entry Error - Street address cannot be more than 20 characters, please try again.\033[0m")
            print()
        else:
            break
    return strAdd

    
# City
def city(city):
    allowed_char = set ("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-.,'")
    while True:
        city = input("Enter the city                      : ").title()
        if city == "":
            print("\033[0;31mData Entry Error - City cannot be blank, please try again.\033[0m")
            print()
        elif set (city) .issubset (allowed_char) == False:
            print("\033[0;31mData Entry Error - City contains invalid characters, please try again.\033[0m")
            print()
        elif len(city) > 15:
            print("\033[0;31mData Entry Error - City cannot be more than 15 characters, please try again.\033[0m")
        else:
            break
    return city




def provList(province):
    provinceList = ["NL", "NS", "NB", "PE", "PQ", "ON", "MB", "AB", "BC", "NT", "YT", "NV"]
    while True:
        province = input("Enter the province code (XX)        : ").upper()
        if province == "":
            print("\033[0;31mData Entry Error - Province cannot be blank, please try again.\033[0m")
            print()
        elif len(province) != 2:
            print("\033[0;31mData Entry Error - Province must be 2 characters only, please try again.\033[0m")
            print()
        elif province not in provinceList:
            print("\033[0;31mData Entry Error - Invalid province code, please try again.\033[0m")
            print()
        else:
            break
    return province


# Postal Code Validations
def postalCode(pc):
    while True:
        pc = input("Enter the postal code (X9X9X9)      : ").upper()
        if pc == "":
            print("\033[0;31mData Entry Error - Postal Code cannot be blank, please try again.\033[0m")
            print()
        elif len(pc) != 6: 
            print("\033[0;31mData Entry Error - Postal Code must be 6 digits only, please try again.\033[0m")
            print()
        elif (pc[0].isalpha()) == False:
            print("\033[0;31mData Entry Error - First character must be a letter, please try again.\033[0m")
            print()
        elif (pc[1].isnumeric()) == False:
            print("\033[0;31mData Entry Error - Second character must be a number, please try again.\033[0m")
            print()
        elif (pc[2].isalpha()) == False:
            print("\033[0;31mData Entry Error - Third character must be a letter, please try again.\033[0m")
            print()
        elif (pc[3].isnumeric()) == False:
            print("\033[0;31mData Entry Error - Fourth character must be a number, please try again.\033[0m")
            print()
        elif (pc[4].isalpha()) == False:
            print("\033[0;31mData Entry Error - Fifth character must be a letter, please try again.\033[0m")
            print()
        elif (pc[5].isnumeric()) == False:
            print("\033[0;31mData Entry Error - Sixth character must be a number, please try again.\033[0m")
            print()
        else:
            break
    return pc


# Date of Birth
def expDate(expiryDate):
    while True:
        try:
            dateExpiry = input("Enter the date of expiry (YYYY-MM-DD) : ")
            dateExpiry = datetime.datetime.strptime(dateExpiry, "%Y-%m-%d")
        except:
            print("\033[0;31mData Entry Error - Date of expiry is not in a valid format, please try again.\033[0m")
            print()
        else:
            break
    return dateExpiry