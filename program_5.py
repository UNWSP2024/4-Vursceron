# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    total = 0.0
    budget = int(input("What is your budget for the month?"))
    while True:
        spent = int(input("What were your expenses?"))
        if spent == 0:
            break
        else:
            total = total + spent
    difference = budget - total
    print(str(round(difference)))
    if difference < 0:
        print("You don't have enough money!")
    else:
        print("You have money!")









if __name__ == '__main__':
    main()