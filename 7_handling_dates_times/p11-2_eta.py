#!/usr/bin/env python3

from datetime import datetime, timedelta

def main():
    print("Arrival Time Estimator")
    print()

    while True:
        # get departure date/time
        dep_date_str = input("Estimated date of departure (YYYY-MM-DD): ")    
        dep_time_str = input("Estimated time of departure (HH:MM AM/PM): ")

        # convert str to datetime
        dep_str = dep_date_str + " " + dep_time_str
        dep_datetime = datetime.strptime(dep_str, "%Y-%m-%d %I:%M %p")

        # get miles / mph
        miles = int(input("Enter miles: "))
        miles_per_hour = int(input("Enter miles per hour: "))
        print()

        # perform the calculations
        hours = miles // miles_per_hour
        minutes = miles % miles_per_hour
        travel_time = timedelta(hours=hours, minutes=minutes)
        arr_datetime = dep_datetime + travel_time

        # display travel time and eta
        print("Estimated travel time")
        print("Hours:", hours)
        print("Minutes:", minutes)
        print("Estimated date of arrival: " + arr_datetime.strftime("%Y-%m-%d"))
        print("Estimated time of arrival: " + arr_datetime.strftime("%I:%M %p"))
        print()
        
        # ask if user wants to continue
        result = input("Continue? (y/n): ")
        print()
        if result.lower() != "y":
            print("Bye!")
            break      

if __name__ == "__main__":
    main()
