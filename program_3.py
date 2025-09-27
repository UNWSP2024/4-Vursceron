# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    month_count = 0
    rain_falls = []
    year_count = int(input("How many years do you want?"))
    for i in range(1,year_count+1):
        print ("Year ", i)
        for current_month in range(1,13):
            month_count = month_count + 1
            rain_falls.append(float(input("How many inches of rain in month "+str(current_month)+": ")))
    total_rainfall= sum(rain_falls)
    print("Total rainfall: ", total_rainfall)
    print("Total months: ", month_count)
    average_of_rainfall = total_rainfall/month_count
    print("Average rainfall: ", average_of_rainfall)







if __name__ == '__main__':
    main()