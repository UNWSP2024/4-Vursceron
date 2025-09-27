# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ticket_count = 0
    while True:
        input("What movie do you want to see? " )
        ticket = int(input("How many tickets do you want? "))
        ticket_count += ticket
        answer = input("Do you want to see more movies (Y,N)? ")
        if answer != 'Y' or answer != 'y':
            break
    print("The total amount of tickets you want is:", ticket_count)
if __name__ == '__main__':
    main()