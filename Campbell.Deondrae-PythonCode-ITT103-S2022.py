'''
Author: Deondrae Campbell
Date Created: April 26, 2022
Course: Programming Techniques - ITT103
Purpose: The purpose of the program is to calculate the commission given to an
        employee in the different classes.
'''


salesp_num = ' '

while (salesp_num != '0'):
    salesp_num  = input("Please enter the salesperson's number or press '0' to exit:\n")
    if salesp_num == '0':
        print("Exiting....")
        break
        
    if len(salesp_num) != 5:
        print("The salesperson's number must be 5 digits\n")

    else:
        salesp_num = int(salesp_num)

        salesamount = float(input("Enter the sales amount:\n"))
        Class = int(input("What is the class of the sales person? 1, 2, or 3?\n"))

        if Class == 1:
            if salesamount <= 1000:
                commission = salesamount * 0.06
            elif salesamount > 1000 and salesamount < 2000:
                commission = salesamount * 0.07
            elif salesamount > 2000:
                commission = salesamount * 0.1
        elif Class ==2:
            if salesamount < 1000:
                commission = salesamount * 0.04
            elif salesamount >= 1000:
                commission = salesamount * 0.06
        elif Class ==3:
            commission = salesamount * 0.045
        else:
            print("Incorrect class")


        print("The employee's ID number is:",salesp_num)
        print("The employee's class is:",Class)
        print("The employee's sales amount is:",salesamount)
        print("The commission made by the employee is:",commission)
        print("\n")
